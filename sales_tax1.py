class Product:
	def __init__(self, details, price):
		
		self.price = float(price)
		self.description = ' '.join(details)

		if 'book' in self.description:
			self.category = 'education'
		elif 'pill' in self.description:
			self.category = 'medicine'
		elif 'chocolate' in self.description:
			self.category = 'food'
		else:
			self.category = 'others'

		if 'imported' in self.description:
			self.origin = 'imported'
		else:
			self.origin = 'india'

def calculate_tax(product):
	
	sales_tax = 10
	import_duty = 5
	
	if product.category == 'others' and product.origin == 'imported':
		tax = product.price * (sales_tax + import_duty) /100
	elif product.category == 'others' and product.origin == 'india':
		tax = product.price * sales_tax/100
	elif product.origin == 'imported':
		tax = product.price * import_duty/100
	else:
		tax = 0.00

	return round_off(tax)

def round_off(x, prec=2, base=.05):
  	return round(base * round(float(x)/base),prec)

def billing():

	item = ''
	cart = []

	while item != str(0):
		item = input('enter the item, enter 0 if done ')
		if item != '0':
			cart.append(item)

	sales_taxes = 0.00
	total = 0.00
	for item in cart:
		item = item.replace(" at ", " ")
		temp = item.split()
		count =int(temp[0])

		product = Product(temp[1:-1], temp[-1])
		tax = calculate_tax(product)
		amount = count * (product.price + tax)

		print ('{count} {details}: {amount:.2f}'.format(count=count, details= product.description, amount= amount))

		sales_taxes += tax
		total += amount

	print('Sales Taxes :{sales_taxes:.2f}'.format(sales_taxes=sales_taxes))
	print('Total :{total:.2f}'.format(total=total))


billing()