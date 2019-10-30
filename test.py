
items = {'apple': 1, 'banana': 2, 'orange': 4}

while True:
    
    money = int(input('Please enter your budgeds to purchase fruits: $'))
    for item_name in items:
    #print('--------------------------------------------------')
    print('You have $' + str(money) + ' to purchase products')
    print(item_name + ' costs $' + str(items[item_name]) )
    
    input_count = input('Please enter how many ' + item_name + ' you would like to purchase：')
    print('You will purchase' + input_count + "of" + item_name)
    
    count = int(input_count)
    total_price = items[item_name] * count
    print('Total will be $' + str(total_price) )
    
    if money >= total_price:
        print("you purchased "+ input_count + "of " + item_name)
        money -= total_price
        
        if money == 0:
            print("It's out of budges!")
    else:
        print('There is no enough money to purchase products')
        print("I'm sorry, you could not buy "+ item_name)
    print('You have $' + str(money) + ' Left')
    
play_again = money("If you'd like to purchase again, plese type 'yes' ")
if play_again == 'yes':
    continue
else:
    break