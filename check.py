import zulip


zulip_client = zulip.Client(email="detect-bot@tougx.zulipchat.com", client="MyTestClient/0.1")
work="work"
msg="do your "+work
message = {
  "type": "stream",
  "to": ["general"],
  "subject": "your subject",
  "content": msg
}
print(zulip_client.send_message(message))
