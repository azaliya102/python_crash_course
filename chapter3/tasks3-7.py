#3-4 guest list
my_guests = ['tesla', 'einstein', 'mendeleev']
print(f"i'm inviting {my_guests[0].title()} to dinner")
print(f"i'm inviting {my_guests[1].title()} to dinner")
print(f"i'm inviting {my_guests[2].title()} to dinner")

#3-5 changing the list
print(f"\nunfortunately {my_guests[1].title()} won't make it(((")
my_guests.remove('einstein')
my_guests.insert(1, 'ford')
print(f"\ni got a new guest and it's {my_guests[1].title()}!!")
print(f"\nAttention!!! i have got a bigger table!!!")
#3-6 more guests
my_guests.insert(0, 'newton')
my_guests.insert(1, 'Curie')
my_guests.append('edison')
print(f"\ni'm inviting {my_guests[0].title()} to dinner")
print(f"i'm inviting {my_guests[1].title()} to dinner")
print(f"i'm inviting {my_guests[2].title()} to dinner")
print(f"i'm inviting {my_guests[3].title()} to dinner")
print(f"i'm inviting {my_guests[4].title()} to dinner")
print(f"i'm inviting {my_guests[5].title()} to dinner")
#3-7 shrinking my guest list
for i in range(1, 5):
    my_guests.pop()
print(my_guests)

print(f"hey {my_guests[0].title()} you're still invited")
print(f"hey {my_guests[1].title()} you're also invited")

del my_guests[0]
del my_guests[0]
print(my_guests)