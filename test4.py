## So if you run this code, the response can be seen if u run "http://localhost:5000" on your web browser
## we now need to expose this to a server to allow twilio to see this...
## https://www.twilio.com/docs/quickstart/python/sms/hello-monkey


from flask import Flask, request, redirect
import twilio.twiml

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond to incoming calls with a simple text message."""

    resp = twilio.twiml.Response()
    resp.message("Hello, Mobile Monkey")
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
