print "Welcome to restaurant program !"

menu = {}

while True :
    new_dish = raw_input("Please enter name of dish: ")
    total_price = raw_input("Please enter the price of dish: ")
    menu[new_dish] = total_price

    new = raw_input("would you like to enter new dish ? (y/n) ")
    if new == 'n':
        break


menu_file = ("menu.txt" , "w+ ")

print "Your menu : %s " % menu

with open("menu.txt", "w+") as menu_file:
    for dish in menu:
        menu_file.write("%s, %s eur\n" % (dish, menu[dish]))

print " goodbye!"