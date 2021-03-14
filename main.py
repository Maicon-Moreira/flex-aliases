import json
import os


flex_aliases = ''

a = '{'
b = '}'

for ai, aia in [['', '0'], ['center', 'c'], ['flex-end', 'e'], ['flex-start', 's']]:
    for jc, jca in [['', '0'], ['space-around', 'a'], ['space-between', 'b'], ['space-evenly', 'e'], ['center', 'c'],  ['flex-end', 'e'], ['flex-start', 's']]:
        for fd, fda in [['', '0'], ['column', 'c'], ['column-reverse', 'cr'], ['row', 'r'], ['row-reverse', 'rr']]:
            flex_aliases += f'.f{aia}{jca}{fda} {a} display: flex;'

            if ai:
                flex_aliases += f'align-items: {ai};'

            if jc:
                flex_aliases += f'justify-content: {jc};'

            if fd:
                flex_aliases += f'flex-direction: {fd};'

            flex_aliases += f'{b}'


with open('flexAliases.css', 'w') as f:
    f.write(flex_aliases)

os.system('prettier flexAliases.css --write')
