def add_everything_up(a,b):
    try:
        print(a+b)
    except(TypeError):
        print(str(a)+str(b))



add_everything_up("string", 2)
add_everything_up(1234, "apple")
add_everything_up(1,1)