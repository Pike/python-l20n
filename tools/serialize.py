#!/usr/bin/python 

import sys, os

sys.path.append('./lib')
import codecs
import l20n.format.parser
import l20n.format.serializer
import json

def read_file(path):
    with codecs.open(path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

def print_l20n(fileType, data):
    l20nSerializer = l20n.format.serializer.Serializer()
    if fileType == 'json':
        result = l20nSerializer.serialize(json.loads(data))
    elif fileType == 'l20n':
        print('----- ORIGINAL -----')
        print(data)
        l20nParser = l20n.format.parser.Parser()
        print('----- AST -----')
        ast = l20nParser.parse(data)
        print(json.dumps(ast, indent=2))
        print('--------------------')
        result = l20nSerializer.serialize(ast)
    
    print(result)

if __name__ == "__main__":
    fileName, fileExtension = os.path.splitext(sys.argv[1])
    f = read_file(sys.argv[1])
    print_l20n(fileExtension[1:], f)

