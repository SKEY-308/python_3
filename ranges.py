# --------------- Previously for loops
# items = [1, 2, 3, 4, 5]
# for item in items:
# do Something


# ------------------- ranges
# for n in range(5):
#     print(n)

# for m in range(2, 10):
#     print(m)

# for m in range(0, 20, 4):
#     print(m)

burgers = ['beef', 'chicken', 'veg', 'supreme', 'double']

# for n in range(len(burgers)):
#     print(n, burgers[n])

for n in range(len(burgers) - 1, - 1, - 1):
    print(n, burgers[n])
