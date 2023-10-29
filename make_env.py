#!/usr/bin/env python
import os, sys, base64
import platform
import secrets
import string



FILENAME='.env'

def lower(s): return s.lower()
def _bool(s):
    return {'t':'true',
            'y':'true',
            'n':'false',
            'f': 'false'}.get(s.lower(), s.lower())

VARS = (
        ('MYSQL_DB_NAME', 'mysql db name', lower),
        ('MYSQL_USERNAME', 'mysql user name e.g(root)', lower),
        )


def random_pw(length=12):
    if platform.system() == "Windows":
        characters = string.ascii_letters + string.digits
        password = ''.join(secrets.choice(characters) for _ in range(length))
    else:  # Assume Unix-like system (including Linux)
        with open('/dev/urandom', 'rb') as f:
            password = base64.urlsafe_b64encode(f.read(12))[:length].decode('utf-8')
    
    return password

print ("""
Making the ENV file...
""")

if os.path.exists(FILENAME):
    print (".env file exists, either remove or edit directly")
    sys.exit(0)

vars = dict((var,_filter(input(prompt + "? ").strip())) for var, prompt, _filter in VARS)

for pw in (
           'MYSQL_ROOT_PASSWORD',
           'ADMIN_PASSWORD',
           'POSTGRES_PASSWORD'):
    vars[pw] = random_pw()

with open (FILENAME, 'w') as f:
    for k,v in sorted(vars.items()):
        strVal = v
        if isinstance(v, bytes):
            strVal=v.decode('ascii')
        f.write("%s=%s\n" % (k,strVal))
    print ("\n\nAdmin Password: %s\n" % vars['ADMIN_PASSWORD'])

sys.exit(0)