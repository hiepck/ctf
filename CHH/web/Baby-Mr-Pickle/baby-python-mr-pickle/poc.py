import pickle, base64

a = {'name': 'hiepck'}

print(base64.b64encode(pickle.dumps(a)))