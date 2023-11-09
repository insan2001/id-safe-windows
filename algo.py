import sys
# main function write()

def generate_list(passwd):
	password = bytes(passwd, 'ascii')
	return list(password), len(password)	

def create_alg(passwd_list, len_password):
	lenth = range(1, len_password+1)
	values=[]
	for i , num in zip(lenth, passwd_list):
		result=num*i
		values.append(result)
	value_=0
	for value in values:
		value_+= value
	return value_

def write(password, location='a', write=False):
	passwd_list, len_password = generate_list(password)
	password=create_alg(passwd_list, len_password)
	if write:
		with open(location, "w") as passwd:
			file = str(password) + "\n" + str(len_password)
			passwd.write(file)

	else:
		return password
