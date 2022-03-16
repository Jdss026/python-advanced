"""
Se precisamos de argumentos em um script python. Ex:
python3 myscript.py -o test.txt -l DEBUG
"""
"""
def myfunction(*args, **kwargs):
    print(args[0])
    print(args[1])
    print(args[2])
    print(args[3])
    print(kwargs['KEYONE'])
    print(kwargs['KEYTWO'])

myfunction('hey', True, 19, 'wow', KEYONE = "Test", KEYTWO=7)
"""
"""
import sys

filename = sys.argv[1] # recebe o nome do arquivo
message = sys.argv[2] #recebe a mensagem

with open(filename,'w+') as f:
    f.write(message) #escreve a mensagem e grava no arquivo

"""

import sys
import getopt

#default opts
filename = "test.txt"
message = "Hello"

opts, args = getopt.getopt(sys.argv[1:], "f:m:", ['filename','message'])

for opt, arg in opts:
    if opt == '-f':
        filename = arg
    if opt == '-m':
        message = arg

with open(filename, 'w+') as f:
    f.write(message)

