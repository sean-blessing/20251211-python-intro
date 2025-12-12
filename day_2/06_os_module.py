import os

print('hello')

cwd = os.getcwd()
print(f"cwd = {cwd}")
os.chdir('./day_2')
cwd = os.getcwd()
print(f"cwd = {cwd}")
keystone_file = open("./keystone.common.wsgi","r")


print('bye')