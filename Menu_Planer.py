# Your friend was so happy with your program that he told everyone how great programmer you are.
# A nearby restaurant owner heard about this and immediately contacted you.
# He'd like to have a program where he'd enter their daily menu and it would get saved into a menu.txt file.
# The menu would consist of a dish (like "Beef steak with potatoes" and a price of the dish (e.g. 5.40).

# Menu genarator for the Chinese Restaurant of Vienna

print "Welcome to the menu generator of the Chinese Restaurant of Vienna!"

menu_file = open("menu.txt", "w+")      # open the TXT file (or create a new one)
menu = {}

while True:
    dish = raw_input("Please enter some kind of dish: ")
    price = raw_input("Please enter the price in EUR for '%s': " % dish)
    price = "   for   EUR " + price
    menu = dish + price
    print "Your new dish is:  " + menu


    answer = raw_input("Would you like to enter a futher dish? (yes/no): ")

    if answer == "no" or answer == "n" or answer == "N" or answer == "No":
        break

print "Your menu"
for i in range (len(menu)):     # Hier duerfte irg ein Fehler passiert sein !!!
    print i + 1, menu

"\n"    # Zeilenumbruch funktioniert nicht




print "Thank you for your visit!"


