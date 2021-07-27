* This is a markdown file
# I'm not sure how a markdown works

> the script can be used inside the terminal
> or imported in your script
---
Title: Build Software Robots with Python
Date: 2017-12-06 09:00
Status: draft
Author: tester
Date: July 27
---

> output to a file like so

~~~bash
mkparse path/to/markdown/file > mkdata.json
~~~

> use in a python script like so
~~~python
from mkparse import mk_to_dict

data = mk_to_dict(path)
print(data)
~~~

---
Text: another data set
Project: simple markdown data extraction
---

---
hedjj
---
