from flask import Flask, request
from twilio import twiml

app = Flask(__name__)


@app.route("/bot", methods=['POST'])
def bot():
    number=request.form['From']
    message_body=request.form['Body']

    resp=twiml.Response()
    resp.message('Hello {}, you said:{}'.format(number, message_body))
    return str(resp)


if __name__ == '__main__':
    app.run()



