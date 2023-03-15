age = int(input("Enter your age :"))

if age < 10:
    print('You are young, strange one')

elif age == 10:
    print('You have the right age to play in our level')

else:
    print('You\'re too old, strange one')


meaty = input('Do you eat meat? (y/n):')

if meaty == 'y':
    print('Here is the meaty menu...')
else:
    print('Here is the veggie menu...')
