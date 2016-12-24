# oblonski 24.12.16
my_pizzas = ['margaritta', 'hawai', 'salami']
friend_pizzas = my_pizzas[:]

my_pizzas.append('super supreme')
friend_pizzas.append('tanuri')

print("My favorite pizzas are: ", end = "")
for pizza in my_pizzas:
	print(pizza +" ", end = "")
	
print("\nMy friends favorite pizzas are: ", end = "")
for pizza in friend_pizzas:
	print(pizza +" ", end = "")
