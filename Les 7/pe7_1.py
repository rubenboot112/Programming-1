def convert(celsius):
    fahrenheit = celsius * 1.8 + 32
    return fahrenheit
def table():
    print("{:>3} {:>6}".format("F", "C"))
    for i in range(-30, 41, 10):
        print ("{:5.1f} {:6.1f}".format(convert(i), i))

table()