def calculate_floor(string):
    floor = 0
    for char in string:
        if char == 'u':
            floor+=1
        else:
            floor-=1
    print(floor)
calculate_floor("dddd")
calculate_floor('uudu')