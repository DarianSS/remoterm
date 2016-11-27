# remoterm

## Full unattended and unrestricted access to your computer

### Configuration

config.py:
* EMAIL = Gmail address that the daemon will listen to
* EMAIL\_PASSWORD
* APP\_PASSWORD = choose the password that will be used to verify emails

### What to run

* remoterm.py - Email daemon
* twilio\_server.py - Twilio endpoint and flask server

### Limitations

* The phone number can only be changed by pointing your phone number's Twilio dashboard to the machine's address. Alternatively ngrok can be used to tunnel the localhost.
* Configuration has no GUI.

