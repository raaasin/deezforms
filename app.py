
from flask import Flask, jsonify, request
from models.roberta import pipe
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.route('/', methods=['GET'])
def index():    
    return jsonify({'message': 'Check the URL, also try POST method to /api/custom with a JSON body'})

@app.route('/api/newuser', methods=['POST'])
def newuser():
    data = request.get_json()
    #enter details of the user to mongodb
    pass

@app.route('/api/fetchuser', methods=['POST'])
def fetchuser():
    data = request.get_json()
    #fetch details of the user from mongodb
    pass

@app.route('/api/edituser', methods=['POST'])
def edituser():
    data = request.get_json()
    #edit details of the user to mongodb
    pass
 
# Define a route for handling POST requests at the '/api/custom' URL
@app.route('/api/fillme', methods=['POST'])
def custom():
    # Retrieve JSON data from the request body
    data = request.get_json()

    # Check if JSON data is provided; if not, return an error response
    if data is None:
        return jsonify(error='No JSON data provided'), 400

    # Initialize an empty dictionary to store responses
    response = {}

    # Loop through the keys in the JSON data
    for key in data:
        # Get the question from the JSON data
        label = key

        # Run the RoBERTa model with specific parameters
        output = pipe.run(query=label, params={"Retriever": {"top_k": 10}, "Reader": {"top_k": 5}})
        
        # Extract the answer from the model's output
        out = output["answers"][0].answer
        answer = out

        # Store the answer for the question in the response dictionary
        response[key] = answer

    # Return the response dictionary as a JSON response
    return jsonify(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
