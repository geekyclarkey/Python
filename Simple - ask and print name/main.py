name = ""
again = "yes"

def test():
    name = input("what is your name? ")
    print("So your name is " + name)


while again == "yes":
    test()