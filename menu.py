# Create new dictionary
# Ask user for menu name
# Ask user for meal name
# Ask user for meal price
# Ask user to add a new meal
# Print final menu card
# Log added menu-card to menu.txt file


menu_card = {}
menu_name = input('Set menu type: Spanish / Italian / Balkan... ')
while True:
    print('Pleas name your meal: ')
    meal = input('> ...  ')
    print('Set price for this meal: ')
    price = input('> ... €')
    menu_card[meal] = price

    new = input('Do you need to add a new meal? y/n')
    if new == 'no':
        break

with open('menu.txt', 'w+') as menu_file:
    print('Menu name: {}'.format(menu_name))
    menu_file.write('Menu name: {}\n'.format(menu_name))
    for item in menu_card:
        print('- ' + item + ': ' + menu_card[item] + '€ \n')
        menu_file.write('- ' + item + ': ' + menu_card[item] + '€ \n')
