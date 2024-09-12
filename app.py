from flask import Flask, jsonify, redirect
from flasgger import Swagger
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Set up Swagger UI with the OpenAPI documentation at /apidocs
swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": 'apispec_1',
            "route": '/apidocs/apispec_1.json',
            "rule_filter": lambda rule: True,  # all in
            "model_filter": lambda tag: True,  # all in
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/apidocs/"
}
swagger = Swagger(app, config=swagger_config)

# Redirect the root endpoint to the Swagger UI documentation
@app.route('/')
def index():
    """Redirects to API documentation
    ---
    responses:
      302:
        description: A redirection to API documentation
    """
    return redirect("/apidocs")

@app.route('/status')
def status():
    """Get API status
    Returns a status message.
    ---
    responses:
      200:
        description: Returns a simple status message
        schema:
          type: object
          properties:
            status:
              type: string
              example: "API is accessible"
    """
    return jsonify({"status": "API is accessible"})

@app.route('/api/hello')
def hello():
    """Hello World endpoint
    Returns a simple greeting message.
    ---
    responses:
      200:
        description: A simple greeting message
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Hello, World!"
    """
    return jsonify({"message": "Hello, World!"})

@app.route('/getStatusMessage', methods=['GET'])
def get_status_message():
    """Get Status Message endpoint
    Returns a detailed status message.
    ---
    responses:
      200:
        description: A detailed status message
        schema:
          type: object
          properties:
            statusMessage:
              type: string
              example: "API is running smoothly"
    """
    return jsonify({"statusMessage": "API is running smoothly"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)