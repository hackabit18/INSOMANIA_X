import zulip
def caller(msg):
    print("I am calleder")
    try:
        zulip_client = zulip.Client(email="detect-bot@tougx.zulipchat.com", client="http://localhost:8000/Hack_a_bit/Report.php",config_file="C:\\Users\\tusha\\.zuliprc")
        message = {"type": "stream","to": ["general"],"subject": "your subject","content": msg}
        print(zulip_client.send_message(message))
    except Exception as e:
        print(e)
        


