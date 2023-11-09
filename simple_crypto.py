from cryptography.fernet import Fernet
import os

'''
This is Written By Cracker Vp Insan.

#This is created for simply encrypt or decrypt your files using 
 Python cryptogaphy module

#You can use it in your programmes

'''



def get_key(key_location, prn=False):
	try:
		with open(key_location, 'rb') as key:
			key = key.read()
	except FileNotFoundError:
		key = Fernet.generate_key()
				
		if prn:
			print("Your Personal Key Has Been Genrated.")
			print("""
WARNIG !!!!!!
If You Lost Your Personal Key You Will Never recover Your Encrypted Data.
{I'm Not Responsible. by:> Cracker Vp Insan}

# 				""")
			time.sleep(2)
		with open(key_location, 'wb') as k:
			k.write(key)

	return key

def encrypt(key, data_file, prn=False):

	fn = Fernet(key)
	with open(data_file, 'rb') as d:
		data = d.read()

	enc = fn.encrypt(data)
	with open(data_file, 'wb') as f:
		f.write(enc)
	if prn==True:
		print("\n\n\t\t<<<Your Data Succesfully Encrypted.>>>")

def decrypt(key, data_file, prn = False):

	fn = Fernet(key)
	with open(data_file, 'rb') as d:
		data = d.read()

	dec = fn.decrypt(data)
	with open(data_file, 'wb') as f:
		f.write(dec)
	if prn==True:
		print("\n\n\t\t<<<Your Data Succesfully Decrypted>>>")

