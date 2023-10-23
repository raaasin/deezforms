from flask import Flask, jsonify,request
from models.roberta import pipe
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
@app.route('/api/custom', methods=['POST'])
def custom():
    data = request.get_json()  # Retrieve JSON data from the request body
    if data is None:
        return jsonify(error='No JSON data provided'), 400
    print(data)
    response = {}

    for key in data:
        print(key)
        label = key  # Get the key from the JSON data
        output = pipe.run(
            query=label, params={"Retriever": {"top_k": 10}, "Reader": {"top_k": 5}}
        )
        out = output["answers"][0].answer
        answer = out

        response[key] = answer  # Store the answer for the key in the response
    print(response)
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)