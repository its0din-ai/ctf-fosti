

def konpertDesimal(desim):
    desimList = desim.split(" ")
    for xzx in desimList:
        print(chr(int(xzx)), end="")


javas = "88 74 97 118 97 95 68 101 99 111 109 112 105 108 101"
desimeeex = "70 111 115 116 105 67 84 70 123 84 101 120 116 95 116 111 95 68 101 99 105 109 97 108 125"
print(konpertDesimal(javas))