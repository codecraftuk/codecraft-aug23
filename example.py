# Processing the Aisles
import json



def list_products(warehouse):
    for product in warehouse['products']:
        print('%(id)s\t%(name)s\t%(size)s' % product)

warehouse = json.load(open('example.json'))

list_products(warehouse)

# print(warehouse)

