guest_list = ['Papa', 'Mama', 'Albert Einstein', 'Thomas Edison', 'James Clark Maxwell']
print("Hi dear " + guest_list[0].title() + ", I would love to invite you to my dinner :)")
print("Hi dear " + guest_list[1].title() + ", I would love to invite you to my dinner :)")
print("Hi dear " + guest_list[2].title() + ", I would love to invite you to my dinner :)")
print("Hi dear " + guest_list[3].title() + ", I would love to invite you to my dinner :)")
print("Hi dear " + guest_list[4].title() + ", I would love to invite you to my dinner :)")

print("-" * 10)
print("Hi people, unfortunately " + guest_list[-1] + " won't make it to the dinner!") 
guest_list[-1] = "Alizee"

print('-' * 10)
print("Dear " + guest_list[0].title() + ", You are invited to my dinner!")
print("Dear " + guest_list[1].title() + ", You are invited to my dinner!")
print("Dear " + guest_list[2].title() + ", You are invited to my dinner!")
print("Dear " + guest_list[3].title() + ", You are invited to my dinner!")
print("Dear " + guest_list[4].title() + ", You are invited to my dinner!")

print("-" * 10)
print("Hi people again! I found a bigger dinner table!")
guest_list.insert(3, 'Eric Matthes')
guest_list.insert(3, 'Hasan Kachal')
guest_list.append('Gorbe Nare')


print('-' * 10)
print("Dear " + guest_list[0].title() + ", You are invited to my dinner!")
print("Dear " + guest_list[1].title() + ", You are invited to my dinner!")
print("Dear " + guest_list[2].title() + ", You are invited to my dinner!")
print("Dear " + guest_list[3].title() + ", You are invited to my dinner!")
print("Dear " + guest_list[4].title() + ", You are invited to my dinner!")
print("Dear " + guest_list[5].title() + ", You are invited to my dinner!")
print("Dear " + guest_list[6].title() + ", You are invited to my dinner!")
print("Dear " + guest_list[7].title() + ", You are invited to my dinner!")


print("Shockingly I can only invite 2 people.")
while len(guest_list) > 2:
	next = guest_list.pop()
	print("Dear " + next + ", I am sorry to tell you that this time I can't invite you to dinner!")

print(guest_list)
for person in guest_list[:]:
	print ("Dear "+ person + ", you are so dear to me! And you are invited to my dinner!")
	guest_list.remove(person)

print(guest_list)
