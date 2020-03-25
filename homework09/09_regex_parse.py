import re

filename = 'ParseData.txt'
pattern = r'\[(.*) .*\] DEBUG \[(.*)\] (.*)'

with open(filename) as f:
    for line in f.readlines():
        match = re.match(pattern, line)
        if match is not None:
            result = re.findall(pattern, line)
            print(f'Date: {result[0][0]}')
            print(f'File and string number: {result[0][1]}')
            print(f'Requiest: {result[0][2]}')
            print()
