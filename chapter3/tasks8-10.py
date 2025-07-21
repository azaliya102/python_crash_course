locations = ['china', 'usa', 'ireland', 'iceland', 'arctic']
print("original order:")
print(locations)

print("\nnow alphabetical order:")
print(sorted(locations))

print("\noriginal again:")
print(sorted(locations, reverse=True))

print("\nalphabetical:")
locations.reverse()
print(locations)

print("\noriginal again:")
locations.reverse()
print(locations)

print("\nalphabetical but with sort(): ")
locations.sort()
print(locations)

print("\nreverse-alphabetical but with sort(): ")
locations.sort(reverse=True)
print(locations)