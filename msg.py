import os
import sys
import zulip
from twilio.rest import Client
v=sys.argv[1]
zulip_client = zulip.Client(email="detect-bot@tougx.zulipchat.com", client="MyTestClient/0.1")
msg="QR code was tried to be generated at Toll Tax "+v+" of Your Car"
account_sid = "AC5adda6db593a0f369a427283c8436959"
auth_token = "fc647306d1cd37646ac0f1f23c55e612"
client = Client(account_sid, auth_token)
client.api.account.messages.create(to="+13153538299",from_="+13153229683",body=msg)
message = {
  "type": "stream",
  "to": ["general"],
  "subject": "your subject",
  "content": msg,
}
print(zulip_client.send_message(message))
print("Message Sent")
                






