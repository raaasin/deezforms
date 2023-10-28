import logging
import os
from haystack.document_stores import InMemoryDocumentStore
from haystack.telemetry import tutorial_running
from haystack.pipelines.standard_pipelines import TextIndexingPipeline
from haystack.nodes import BM25Retriever
from haystack.nodes import FARMReader
from haystack.pipelines import ExtractiveQAPipeline
from flask import jsonify
tutorial_running(1)

logging.basicConfig(format="%(levelname)s - %(name)s -  %(message)s", level=logging.WARNING)
logging.getLogger("haystack").setLevel(logging.INFO)


def writing_files(data):
    with open("data/data.txt", "w") as f:
        f.write(data)

def get_answers(data, text):
    writing_files(text)
    document_store = InMemoryDocumentStore(use_bm25=True)
    doc_dir = "data"
    files_to_index = [doc_dir + "/" + f for f in os.listdir(doc_dir)]
    indexing_pipeline = TextIndexingPipeline(document_store)
    indexing_pipeline.run_batch(file_paths=files_to_index)
    retriever = BM25Retriever(document_store=document_store)
    reader = FARMReader(model_name_or_path="deepset/roberta-base-squad2", use_gpu=True)
    pipe = ExtractiveQAPipeline(reader, retriever)
    response={}
    for key in data:
        if key =="emailid":
            continue
        toans=data.get(key)


        # Run the RoBERTa model with specific parameters
        output = pipe.run(query=toans, params={"Retriever": {"top_k": 10}, "Reader": {"top_k": 5}})
        
        # Extract the answer from the model's output
        try:
            out = output["answers"][0].answer
        except:
            out = "Sorry, I could not find an answer to the question."

        # Store the answer for the question in the response dictionary
        response[key] = out

    # Return the response dictionary as a JSON response
    print(response)
    return jsonify(response)