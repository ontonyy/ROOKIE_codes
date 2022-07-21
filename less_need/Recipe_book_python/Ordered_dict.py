from collections import OrderedDict
import json

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['grok'] = 4
d['got'] = 5
d['spam'] = 3

print(json.dumps(d))