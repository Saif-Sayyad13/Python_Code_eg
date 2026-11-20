
"""
# generate random 2 alpha 2 numeric 2 and 2 lower case char
from random import *
def OTP():
    otp=' ' 
    for i in range(2):
        otp=otp+str(randint(0,9))
    
    for j in range(2):
        otp=otp+chr(randint(65,90))
    
    for k in range(2):
        otp=otp+chr(randint(97,122))
    print(otp)
OTP()



# from random import *
# def OTP():
#     otp=[] 
#     for i in range(2):
#         otp.append(str(randint(0,9)))
    
#     for j in range(2):
#         otp.append(chr(randint(65,90)))
    
#     for k in range(2):
#         otp.append(chr(randint(97,122)))
#     shuffle(otp)
#     result=''.join(otp)
#     print(result)
    
# OTP()
"""

'''
# gtenerate random password or opt
import random as r
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(r.choice(characters) for _ in range(length))
    return password

print(generate_password(12))
# VvFqy=+C5HG; kuch bi aa sakta random
# u&M-dV@>54y>'''