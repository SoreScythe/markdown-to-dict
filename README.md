# markdown-to-dict
A simple Python script to extract data inside markdown files.

> Simple to use script for easy data extraction

~~~Bash
$ mkdict.py --help
usage: Markdown Data Extractor [-h] -p PATH [-o OUTPUT] [-j] [-t]

optional arguments:
  -h, --help            show this help message and exit
  -p PATH, --path PATH  path to the markdown file
  -o OUTPUT, --output OUTPUT
                        path to output file
  -j, --json            output json format
  -t, --terminal        output to stdout
~~~

> or use in your python script like so

~~~Python
from mkdict import getMkDict

path = 'path/to/file
# getMkDict(path, json=False, Terminal=False)
data = getMkDict(path, json=True)
print(data)
~~~
