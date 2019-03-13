#!/usr/bin/python3

import subprocess
import getpass
import os

user = getpass.getuser()

if user == 'root':
    pass

else:
    print("Must run script as root")
    exit()

subprocess.call("pip install -r requirements.txt", shell=True)

os.system('clear')

text = "#!/bin/bash \n cd $HOME/wiki/ && python3 ./wiki.py"

with open("/usr/local/bin/wiki", "w+") as f:
    f.write(text)

files = ["/usr/local/bin/wiki", "wiki.py"]

for i in files:
    subprocess.call(["sudo", "chmod", "+x", i])

print('DONE')
exit()
