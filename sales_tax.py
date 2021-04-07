def round_off(val):
	val = round(val, 2)
	last_digit = str(val)[-1]
	if last_digit in ['0','1','2']:
		last_digit = '0'
		return float(str(val)[:-1]+last_digit)

	elif last_digit in ['3','4','5','6','7']:
		last_digit = '5'
		return float(str(val)[:-1]+last_digit)

	else:
		return float(str(val)[:-2]+str(int(val[-2])+1) + '0')


item = ''
items_in_cart = []

while item != str(0):
	item = input('enter the item, enter 0 if none')
	if item != '0':
		items_in_cart.append(item)

books = ['book','books']
food = ['chocolate','chocolates']
medicine = ['pill','pills']
exemption = books + food + medicine
items_in_cart =[x.split(' ') for x in items_in_cart]

sales_tax = 0
amount = 0
applied_sales_tax = 0
for item in items_in_cart:
	if not (set(item)).intersection(set(exemption)):
		sales_tax = 10
	if 'imported' in item:
		sales_tax += 5

	price = float(item[-1])
	sales_tax = round_off(sales_tax * price/100)
	net_price = sales_tax + price
	applied_sales_tax += sales_tax 
	item = [': ' if x == 'at' else x for x in item]
	amount += net_price 
	print(' '.join(item[:-1]) + str(round(net_price,2)))
	sales_tax = 0

print('SALES TAX: '+str(applied_sales_tax))
print('TOTAL: '+str(round(amount,2)))

