from twilio.rest import Client
from other_files.constants import *

client = Client(twilio_sid, twilio_token)

message = client.messages.create(
                              body='This will be the body of the new message!',
                              from_='numberFrom',
                              to='numberTo'
                          )

print(message.body)
