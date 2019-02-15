import os
import logging
from flask import Flask, jsonify, request, render_template
from flask_httpauth import HTTPBasicAuth
import dialog
import kayako
import settings


app = Flask(__name__)
auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(username, password):
    valid = (username == settings.API_USER and password ==
             settings.API_TOKEN)
    return valid


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/messagehook', methods=['GET', 'POST'])
@auth.login_required
def login():
    message = request.json['message']
    case_id = request.json['id']
    reply = dialog.detect_intent_texts(case_id, message)
    kayako.send_message(case_id, reply)

    print("="*20)
    print("New income message")
    print("Case ID:{}\tMessage: {}".format(case_id, message))
    print("Bot reply:\t{}".format(reply))
    print("="*20)
    return ''


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, threaded=True)
