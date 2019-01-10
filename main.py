import logging
import json
import flask
from flask import Flask, render_template
from flask import request
import seo
import gunicorn

# TM_PORT_NO = 3000

app = flask.Flask(__name__)
# print("http://localhost:" + str(TM_PORT_NO))

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500

# @app.route('/', methods=['GET'])
# def index():
#     with open("index.html", "rb") as f:
#         return f.read()
    
@app.route('/api', methods=['GET'])
def api():
    q = request.args.get('q')
#     c = seo.get_word(q)
    list_keywords = seo.get_word(q)
#     return ({"list_keywords": list_keywords})
    return json.dumps({
        "list_keywords": list_keywords})

if __name__ == '__main__':
    app.run()