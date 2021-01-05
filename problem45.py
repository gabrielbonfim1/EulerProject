def tri_test(x):
    return ((((8*x+1)**(0.5))-1)/2).is_integer()

def pen_test(x):
    return (((24 * x + 1) ** (0.5) + 1) / 6).is_integer()

def hex_test(x):
    return (((8 * x + 1) ** (0.5) + 1) / 4).is_integer()

def gen_next_triangle(x):
    if tri_test(x):
        i = int(((((8*x+1)**(0.5))-1)/2))+1
        return int((i*(i+1)/2))


print(gen_next_triangle(10))
x=gen_next_triangle(40755)
while not (tri_test(x) and pen_test(x) and hex_test(x)):
    x = gen_next_triangle(x)

print(x)

