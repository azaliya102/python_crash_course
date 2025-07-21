bicycles = ['trek', 'canondale', 'redline', 'specialized']
print(bicycles[-1].title())

message = f'my favorite bike is {bicycles[1].title()}'
print(message)

my_birds = ['patrick', 'sean', 'steven', 'jesse', 'bobby']
print(my_birds[0].title())
print(my_birds[-1].title())
print(my_birds[2].title())

message1 = f'hello, {my_birds[0].title()}\n'
message2 = f'hello, {my_birds[-1].title()}\n'
message3 = f'hello, {my_birds[2].title()}\n'

print(message1 + message2 + message3)

motorcycles = ['honda', 'bmw', 'java', 'kawasaki']
print(motorcycles)
message = f'i would like to own a {motorcycles[0].title()} motorcycle'
print(message)
motorcycles[0] = 'suzuki'
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)
birds = []
birds.append('bird_one')
birds.append('bird_two')
birds.append('bird_three')
print(birds)

birds.insert(2, 'unexpected_bird_four')
print(birds)

del birds[2]
print(birds)
popped_bird = birds.pop()
print(popped_bird)

birds.remove('bird_two')
print(birds)

last_owned_moto = motorcycles.pop()
print(f'the last moto i owned was {last_owned_moto}')

print(motorcycles)
too_old = 'java'
motorcycles.remove(too_old)
print(motorcycles)
print(f'\nA {too_old.title()} is too old for me!!!')

cars = ['bwm', 'audi', 'volvo', 'suzuki']
cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

print("\nhere's the original list:")
cars = ['bwm', 'audi', 'volvo', 'suzuki']
print(cars)
print("\nhere's the sorted list:")
print(sorted(cars))
print("\nhere's the original list again")
print(cars)
print("now reversed one")
cars.reverse()
print(cars)
print(len(cars))