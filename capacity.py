




def print_triangle(w):
    o = 0
    i = 0
    c = 1

    while w > 0:

        if w > c:
            print("1" *c)
            w -= c

        elif w == c:
            print("1" * c)
            w -= c

        else:
            i = (w / ((c - 1) * 2)) * 2
            o = w / ((c - 1) * 2)
            print(o, f"{i} " * (c - 2), o)
            w = 0

        c += 1


print_triangle(5)
