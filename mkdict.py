#!/usr/bin/env python3
from sys import argv, stdout
from os.path import exists, isfile, abspath

def parser():
    from argparse import ArgumentParser
    p = ArgumentParser(prog="Markdown Data Extractor")

    p.add_argument('-p', '--path', required=True, type=str)
    p.add_argument('-o', '--output', required=False, default=stdout)
    p.add_argument('-j', '--json', required=False, default=False, action='store_true')
    p.add_argument('-t', '--terminal', required=False, default=True, action='store_true')

    args = p.parse_args(argv[1:])
    return args

def output(data, term=False):
    if term:
        print(data, file=stdout)

def __createLineGen(path):
    for line in open(path, 'r').readlines():
        yield line.strip()
        
def __parse_data(path):
    path = abspath(path)
    if not exists(path):
        print(f"ReadError: {path} does not exist")
        return
    if not isfile(path):
        print(f'ReadError: {path} is not a file')
        return

    gen = __createLineGen(path)
    data = {}
    start = False
    # generator
    while True:
        try:
            d = next(gen)
            
            if not start:
                if d == "---":
                    start = True
                    pass
                pass
            elif start:
                if d != '---':
                    delim = int(d.find(':'))
                    data[d[0:delim].strip()] = d[delim + 1:].strip()
                if d == '---':
                    start = False
                    pass
                
        except StopIteration:
            return data
    
    
def getMkDict(path, json=False, term=False, output=stdout):
    data = __parse_data(path)
    if json:
        import json as js
        data = js.dumps(data, indent=4)
    if output != stdout:
        output = open(output, 'w')
        print(data, file=output)
    if not term:
        return data
    print(data, file=stdout)
    
if __name__ == '__main__':
    args = parser()
    getMkDict(args.path, args.json, args.terminal, args.output)
    
