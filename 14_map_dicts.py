import copy

items = [
  {
    'producto': 'camisa',
    'price': 100
  },
  {
    'producto': 'pantalones',
    'price': 300
  }
]

prices = list(map(lambda item: item['price'], items)) #l oque hace es tomar el diccionario y solo tomar el valor de la key price
print(prices)

def add_taxes(item):
  items_copy = item.copy()
  items_copy['taxes'] = items_copy['price'] * .19
  return items_copy

new_items = list(map(add_taxes,items))
print(new_items)
print(items)