from flask import Flask, request, jsonify
from controller import controller

app = Flask("discoAPI")


@app.route('/items', methods=["GET"])
def read_all_items():
  result = controller.find_all()
  response = jsonify(result)
  response.headers.add('Access-Control-Allow-Origin', '*')
  return response, 200


if __name__ == "__main__":
  app.run()
