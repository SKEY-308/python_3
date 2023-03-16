# -----------------Function greet()
def greet():
    print('hello, dear!!')


greet()

# Greet Severus


def greetsev(name, time):
    print(f"Good {time} {name}, happy to see you again")


name = input('Enter your name : ')
time = input('Enter the time of the day :')

greetsev(name, time)


# -----------------Function circle area()

def area(ray):
    return 3.142 * ray ** 2


ray = int(input('Enter the rayon of your circle: '))


def vol(area, length):
    return area*length


length = int(input('Enter the length: '))

print('The area of your circle is: ', area(ray))
print('The vol of your circle is: ', vol(area(ray), length))
