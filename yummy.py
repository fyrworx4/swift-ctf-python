print("Fill in the blank: This year is SWIFT'S _______. ")

fries = None

try:
    fries = input()

    cheeseburger = fries.split()[0]
    pizza = fries.split()[-1]
    rice = []
    pepperoni = 0

    if len(cheeseburger) == 4:
        for lettuce in cheeseburger:
                rice.append(str(hex(ord(lettuce))))
          
    for pineapple in pizza[::-1]:
        pepperoni += 1
        rice.append(ord(pineapple))

    if rice[::-1] == [65, 78, 78, 73, 86, 69, 82, 83, 65, 82, 89, '0x48', '0x54', '0x30', '0x33'] and pepperoni == 11:
        print(f"Correct! The flag is in the format of 'flag[{cheeseburger} {pizza}]'.")
    else:
        print("Sorry, wrong answer, try again!")
except:
    print("You need to put in something, try again!")
