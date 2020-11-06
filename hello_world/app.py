from flask import Flask, jsonify
from flask import request
from flasgger import Swagger
import os

app = Flask(__name__)
swagger = Swagger(app)

@app.route("/helloworld")
def helloworld():
    """
    This hello world api prints hello world
    ---
    responses:
      200:
        description: print hello world
    """
    return "hello world"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(debug=True,host='0.0.0.0',port=port)