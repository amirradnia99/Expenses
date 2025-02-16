from docopt import docopt
from api import *
from tabulate import tabulate

usage = '''
Usage:
    spent_app.py --init
    spent_app.py --show [<category>]
    spent_app.py --add  <amount> <category> [<message>]
'''

args = docopt(usage)

if args['--init']:
    init()
    print('Table was created successfully')

if args['--show']:
    category = args['<category>']
    amount, results = show(category)
    print('Total expense: ', amount)
    print(tabulate(results))

if args['--add']:
    try:
        amount = float(args['<amount>'])
        add(amount, args['<category>'], args['<message>'])
        print('Item added')
    except:
        print(usage)