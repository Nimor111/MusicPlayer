import json
from collections import OrderedDict


d = OrderedDict([['first-name', 'Pesho'],
                 ['second-name', 'Vaskov'],
                 ['age', 17],
                 ['likes', ['GW2', 'Money']]])
d['cake'] = 'cake'

with open('test-json.json', 'w') as f:
    json.dump(d, f, indent=4)
