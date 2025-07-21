message = "Hello Python world!"
print(message)

message = "Hello Python crash course world!"
print(message)

def greet():
    message = "hello from the def scope"
    print(message)
greet()

name = 'ada lovelace'
print(name.title())

first_name = 'ada'
last_name = 'lovelace'
full_name = f'{first_name} {last_name}'
print(full_name.title())

message = f'Hello, {full_name.title()}'
print(message)

name = 'eric cartman'
message =  f'Hello, {name}, would you like to learn some Python today?'
print(message)

print(name.lower())
print(name.upper())
print(name.title())

author = 'Albert Einstein'
message = f'{author} once said, “A person who never made a mistake never tried anything new.”'
print(message)

filename = 'python_test.py'
new_filename = filename.removesuffix('.py')
print(new_filename)