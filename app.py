from flask import Flask, jsonify, redirect
from flasgger import Swagger
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Configuración de Swagger
swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": 'apispec_1',
            "route": '/apidocs/apispec_1.json',
            "rule_filter": lambda rule: True,  # todos los endpoints
            "model_filter": lambda tag: True,  # todos los modelos
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/apidocs/"
}
swagger = Swagger(app, config=swagger_config)

# Redirección a la documentación Swagger
@app.route('/')
def index():
    return redirect("/apidocs")

@app.route('/status', methods=['GET'])
def status():
    """Estado de la API
    Retorna un mensaje simple de estado.
    ---
    responses:
      200:
        description: Mensaje de estado simple
        schema:
          type: object
          properties:
            status:
              type: string
              example: "API is accessible"
    """
    return jsonify({"status": "API is accessible"})

@app.route('/api/hello', methods=['GET'])
def hello():
    """Endpoint Hello World
    Retorna un mensaje de saludo simple.
    ---
    responses:
      200:
        description: Mensaje de saludo
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
    """Obtener mensaje de estado
    Retorna un mensaje de estado detallado.
    ---
    responses:
      200:
        description: Mensaje de estado detallado
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