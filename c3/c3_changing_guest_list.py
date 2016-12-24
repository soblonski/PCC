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
