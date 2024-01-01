
#this is shopping cart calculator - my 1st project in python - date 01.01.2024


bread_price = 2
bread_amount = int(input('How much breads do you want to buy? '))

onion_price = 3
onion_amount = int(input('How much onions do you want to buy? '))

cola_price = 5
cola_amount = int(input('How much coca colas do you want to buy? '))

# price for all products
totalprice = (bread_price * bread_amount) + (onion_price * onion_amount) + (cola_price * cola_amount)

print(f'For all of items you are gonna pay {totalprice} USD')