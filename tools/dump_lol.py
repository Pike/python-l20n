import argparse

from l20n.format.lol.parser import Parser
import pyast.dump.raw, pyast.dump.js

def read_file(filename, charset='utf-8', errors='strict'):
    with open(filename, 'rb') as f:
        return f.read().decode(charset, errors)

def dump_lol(path, t):
    source = read_file(path)
    p = Parser()
    lol = p.parse(source)
    if t == 'raw':
        print(pyast.dump.raw.dump(lol))
    else:
        print(pyast.dump.js.dump(lol))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Dump LOL\'s AST.',
        prog="dump_lol")
    parser.add_argument('path', type=str,
                        help='path to lol file')
    parser.add_argument('--type', '-t',
                        type=str,
                        choices=('json', 'raw'),
                        default='raw',
                        help='path to lol file')
    args = parser.parse_args()
    dump_lol(args.path, args.type)
