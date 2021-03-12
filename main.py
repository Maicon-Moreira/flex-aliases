import json
import os


flex_aliases = ''

a = '{'
b = '}'

for ai, aia in [['center', 'c'], ['flex-end', 'e'], ['flex-start', 's']]:
    for jc, jca in [['space-around', 'a'], ['space-between', 'b'], ['space-evenly', 'e'], ['center', 'c']]:
        for fd, fda in [['column', 'c'], ['column-reverse', 'cr'], ['row', 'r'], ['row-reverse', 'rr']]:
            flex_aliases += f'.f{aia}{jca}{fda} {a} display: flex ; align-items: {ai} ; justify-content: {jc} ; flex-direction: {fd} {b}'


with open('flexAliases.css', 'w') as f:
    f.write(flex_aliases)

os.system('prettier flexAliases.css --write')
