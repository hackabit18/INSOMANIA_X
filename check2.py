import time
from sinchsms import SinchSMS
number = '+yourmobilenumber'
message = 'I love SMS!'
client = SinchSMS("b678ad78-caf2-48ba-8bcf-50a98d838f62","znUho8vKrEa1g69V06El3Q==")
print("Sending '%s' to %s" % (message, number))
response = client.send_message(number, message)
message_id = response['messageId']
response = client.check_status(message_id)
while response['status'] != 'Successful':
    print(response['status'])
    time.sleep(1)
response = client.check_status(message_id)
print(response['status'])
