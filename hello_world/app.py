from flask import Flask, jsonify
from flask import request
from flasgger import Swagger
import os
import jwt

app = Flask(__name__)
swagger = Swagger(app)

@app.route("/")
def home():
  """
  Welcome home!
  ---
  responses:
    200:
      description: goes to home page
  """
  return "welcome home"


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

@app.route("/headers")
def headers():
  """
  This will return the headers sent in the request
  ---
  responses:
    200:
      description: return the headers
  """
  return dict(request.headers)

@app.route("/decodejwt", methods = ['POST'])
def decode_jwt():
  """
  This will return decoded jwt [WIP]
  ---
  responses:
    200:
      description: return the headers
  """
  encoded = request.headers["X-Introspect-Id-Token"]
  decoded = jwt.decode(encoded, verify=False)
  return decoded

@app.route("/patient", methods = ['POST'])
def patient():
  """
  This will return reponse depending on the user role [WIP]
  ---
  responses:
    200:
      description: return the headers
  """
  encoded = request.headers["X-Introspect-Id-Token"]
  decoded = jwt.decode(encoded, verify=False)
  roles = decoded['resource_access']['api-connect']["roles"]
  if "patient" in roles:
    return "you are a valid user"

  return "invalid user"
  

@app.route("/provider", methods = ['POST'])
def provider():
  """
  This will return reponse depending on the user role [WIP]
  ---
  responses:
    200:
      description: return the headers
  """
  encoded = request.headers["X-Introspect-Id-Token"]
  decoded = jwt.decode(encoded, verify=False)
  roles = decoded['resource_access']['api-connect']["roles"]
  if "provider" in roles:
    return "you are a valid user"

  return "invalid user"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(debug=True,host='0.0.0.0',port=port)