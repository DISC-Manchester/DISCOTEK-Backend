from flask import Flask, request
from controller import controller

app = Flask("discoAPI")


@app.route('/items', methods=["GET"])
def read_all_items():
  result = controller.find_all()
  return result, 200


if __name__ == "__main__":
  app.run()
