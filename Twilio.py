from flask import Flask, request, redirect
from twilio import twiml

app = Flask(__name__)

@app.route("/+447481338028", methods=['GET', 'POST'])
def sms_reply():
    body = request.values.get('Body', None)
    
    output = manager.getOutput(body) #ShellManager class
    link = getLink(output)
    
    resp = twilm.Response()
    if output == "ERROR":
        resp.message("Error")
    else:
        resp.message("Success" + link)
    return str(resp)

def getLink(message)
    link = "" #@TODO: Post the output to pastebin
    return link
