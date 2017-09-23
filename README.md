# scale
An SMS interface for a Google sheet, specifically for tracking current body weight

# Setup

1. Start the app:
`pipenv run  python main.py`

2. Start ngrok: 
`./ ngrok http 5000`

3. Make sure you add the correct Inbound Request URL setup on your Twilio app. Mine was: http://2a8a609f.ngrok.io/sms 

4. Text your Twilio number, you should see a response!
