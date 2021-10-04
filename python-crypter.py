import base64
import uuid
import string
from random import randrange
import random

def random_char(y):
       return ''.join(random.choice(string.ascii_letters) for x in range(y))

code=input('Python code to be encrypt : ')

randomuuid=uuid.uuid4()
randomuuid=str(randomuuid).replace('-','')

code=code+'#'+randomuuid

encoded=base64.b64encode(code.encode('ascii'))

encoded=str(encoded, 'utf-8')

print(encoded)

shelter="import base64;exec(base64.b64decode('"+encoded+"'))"

encoded=base64.b64encode(shelter.encode('ascii'))

encoded=str(encoded, 'utf-8')

random_index = randrange(0,len(encoded))

replace=encoded[random_index]

print('replaced :'+replace)

encoded=encoded.replace(encoded[random_index],'*')

rand = random_char(10)

composition="import base64;"+rand+"='"+encoded+"';"+rand+"="+rand+".replace('*','"+replace+"');exec(base64.b64decode("+rand+"))"

print(composition)