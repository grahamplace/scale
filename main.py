from flask import Flask, request
from twilio import twiml
import os
import re
from twilio.twiml.messaging_response import MessagingResponse
from update_sheets import *

app = Flask(__name__)


@app.route('/sms', methods=['POST'])
def sms():
    number = request.form['From']
    message_body = request.form['Body']

    if (number != os.environ['MY_PHONE'] ):
        resp = MessagingResponse()
        resp.message('Sorry, this service is only for Graham to use. ¯\_(ツ)_/¯')
        return str(resp)

    if ('w' not in message_body.lower()):
        resp = MessagingResponse()
        resp.message('Did you mean to add a new input? If so, use the correct input key.')
        return str(resp)
    else:
        parsed_weight = re.sub(r'[^0-9.]', '', message_body)
        add_weight(parsed_weight)
        resp = MessagingResponse()
        resp.message('Added {} to the scale-weight spreadsheet!'.format(parsed_weight))
        return str(resp)

if __name__ == '__main__':
    app.run()
