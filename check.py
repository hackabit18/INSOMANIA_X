import zulip


zulip_client = zulip.Client(email="detect-bot@tougx.zulipchat.com", client="MyTestClient/0.1")

message = {
  "type": "stream",
  "to": ["general"],
  "subject": "your subject",
  "content": "This is amit singh",
}
print(zulip_client.send_message(message))
