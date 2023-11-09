import algo
import sys

"""
encrypt fern key using algo
fern_key_value+8digitalg
write in a file 
main function fern_key_converter(), fern_value_writer()

bug will found:
    if hacker know the function he will attempt to copy these files to his machine and 
    decrypt.

Solution:
    before decrypt ask the passwd from the user and check the passwd is matching with 
    the file content.

"""

def value_sep(fern_key_, pass_location):
    with open(pass_location, "r") as f:
        controller = int(f.readline())

    fern_key = fern_key_
    fern_key_list = list(fern_key)

    list_of_value=[]

    for fern_key in fern_key_list:
        balance = controller % int(fern_key)
        multipilication = controller// int(fern_key)
        value = str(multipilication) + "*"  + str(balance)
        list_of_value.append(value)
    return list_of_value

def fern_value_writer(fern_key, pass_location, key_location):
    list_ = value_sep(fern_key, pass_location)
    with open(key_location, "w") as fern:
        fern.write("")
    for value in list_:
        fern_ = value + '\n'
        with open(key_location, "a+") as fern:
            fern.write(fern_)

def fern_value(location, passwd):

    with open(location, "r") as key:
        values=key.readlines()
    controller = passwd
    list_value=[]
    for line in values:
        value = line.split("*")
        multipilication = int(value[0])
        balance = int(value[1])
        value = (controller- balance)/multipilication
        list_value.append(value)
    return list_value

def fern_key_decoder(location, passwd):
    numbers = fern_value(location, passwd)
    fern_list = []
    for number in numbers:
        value = chr(int(number))
        fern_list.append(value)
    key=""
    for charactor in fern_list:
        key += charactor
    return key

