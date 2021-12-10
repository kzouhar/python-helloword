import json
import logging

from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"

@app.route("/status")
def status():
    app.logger.info('Status request successfull')
    return app.response_class(response=json.dumps("{'OK':'Healthy'}"),
                              status=200,
                              mimetype='application/json'
                              )

@app.route("/metrics")
def metrics():
    app.logger.info('metrics request successfull')
    return app.response_class(response=json.dumps("{'UserCount': 140, 'UserCountActive': 23}"),
                              status=200,
                              mimetype='application/json'
                              )

logging.basicConfig(filename='app.log',level=logging.INFO)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
