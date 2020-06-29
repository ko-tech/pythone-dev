# exercise 3-4: Guest List
guests = ["Joe", "Ray", "John", "Harry"]
print(len(guests))
invitation_message = ", you are invited to the biggest orgy of the year"

print("Hey " + guests[0] + invitation_message)
print("Hey " + guests[1] + invitation_message)
print("Hey " + guests[2] + invitation_message)
print("Hey " + guests[3] + invitation_message + "\n")


# exercise 3-5: Changing Guest List

cant_make_it = "John"


guests.remove(cant_make_it)
print(guests)
guests.insert(2, "Derek")
print(guests)
print("\n")

print("Hey " + guests[0] + invitation_message)
print("Hey " + guests[1] + invitation_message)
print("Hey " + guests[2] + invitation_message)
print("Hey " + guests[3] + invitation_message + "\n")

# exercise 3-6: More Guests
announcement = "We have found more room for the party"
print(announcement)

guests.insert(0, "Jake")
guests.insert(2, "Tommy")
guests.append("Faroukh")
print(guests)

print("Hey " + guests[0] + invitation_message)
print("Hey " + guests[1] + invitation_message)
print("Hey " + guests[2] + invitation_message)
print("Hey " + guests[3] + invitation_message)
print("Hey " + guests[4] + invitation_message)
print("Hey " + guests[5] + invitation_message)
print("Hey " + guests[6] + invitation_message)

# exercise 3-7: Shrinking Guest List
announcement_2 = "Unfortunately I'll only be able to have 2 guests"
print(announcement_2)

print(guests)
print(guests)
uninvited1 = guests.pop(0)
print("Unfortunately, you're uninvited " + uninvited1) 

uninvited2 = guests.pop(0)
print("Unfortunately, you're uninvited " + uninvited2)

uninvited3 = guests.pop(0)
print("Unfortunately, you're uninvited " + uninvited3)

uninvited4 = guests.pop(0)
print("Unfortunately, you're uninvited " + uninvited4)

uninvited5 = guests.pop(0)
print("Unfortunately, you're uninvited " + uninvited5)

print(guests)
final_announcement = ", you're still invited to the biggest orgy of the year"

print("Congratulations " + guests[0] + final_announcement)
print("Congratulations " + guests[1] + final_announcement)

del guests[0:2]


print(guests)