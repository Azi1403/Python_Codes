def zarb(*args): # n number we can enter by *arg and arg is a list
    m = 1
    for num in args:
        m = m* num
    print(m)
    
zarb(10,2)
zarb(100,46,7,23)
zarb(5,4,3,-1,-2)