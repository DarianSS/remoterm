from flask import Flask, request, redirect
from twilio import twiml
import IO

app = Flask(__name__)

@app.route("/", methods=['POST'])
def sms_reply():
    command = request.values.get('Body', None);

    shell = IO.ShellManager('/bin/bash')
    output = shell.getOutput(command)

    if len(output) > 160:
        output = getLink(output)

    resp = twiml.Response()
    resp.message(output)

    return str(resp)

def getLink(message):
    link = "" #@TODO: Post the output to pastebin
    return link

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
