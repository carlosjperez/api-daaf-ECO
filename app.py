from flask import Flask, jsonify
from flasgger import Swagger
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Set up Swagger UI with the OpenAPI documentation
swagger = Swagger(app, template_file='openapi.yaml')

@app.route('/')
def index():
    """Check API Status
    Returns a message indicating that the API is running.
    ---
    responses:
      200:
        description: A message confirming that the API is working
        schema:
          type: object
          properties:
            message:
              type: string
              example: "API running successfully"
    """
    return jsonify({"message": "API running successfully"})

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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
  