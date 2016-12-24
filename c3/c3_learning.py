my_list = [1,2,3,1,2,3,1,2,3]
n = 0
m = 0
while True:
	try:
		my_list.remove(1)
		n+=1
		print("n: "+ str(n))
	except:
		#m+=1
		#print("m: "+ str(m))
		break
		
print(my_list)