# Scopes: global variable // une variable local peu devenir global à condition que nous declarions que cette variabl était global
my_name = 'Key'


def print_name():
    global my_name
    my_name = 'Severus'
    print('The name inside is: ', my_name)


print_name()

print('The name outside is: ', my_name)
