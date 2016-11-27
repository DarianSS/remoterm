# remoterm

## Full unattended and unrestricted access to your computer

In a nutshell, remoTerm is a daemon that runs on our home computer. It listens for emails or text messages that we send to it, executes the commands that are in them, and replies with the terminal output. It is platform agnostic, meaning that it does not need an app on the commanding device, just a mail or messaging client.

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
* No GUI for configuration.
* State is not preserved across queries. (i.e. cd followed by ls will return the contents of the current directory; use && instead)

