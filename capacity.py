




def print_triangle(water_poured):
    outer_water = 0
    inner_water = 0
    containers = 1

    while water_poured > 0:

        if water_poured > containers:
            print("1" *containers)
            water_poured -= containers

        elif water_poured == containers:
            print("1" * containers)
            water_poured -= containers

        else:
            inner_water = (water_poured / ((containers - 1) * 2)) * 2
            outer_water = water_poured / ((containers - 1) * 2)
            print(outer_water, f"{inner_water} " * (containers - 2), outer_water)
            water_poured = 0

        containers += 1


print_triangle(13)

