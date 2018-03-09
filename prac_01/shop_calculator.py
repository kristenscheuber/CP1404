"""
A shop requires a small program that would allow them to quickly work out total price for a number of items,
each with different prices.
The program allows the user to enter the number of items and the price of each different item.
Then the program computes and displays the total price of those items.
If the total price is over $100, then a 10% discount is applied to that total before the amount is displayed on the
screen.
The output should look something like (green text represents user input):
Number of items: 3
Price of item: 100
Price of item: 21.56
Price of item: 3
Total price for 3 items is $112.10
"""

number_items = int(input("Number of Items: "))
item_price = []
total_price = 0
if number_items < 0:
    print("Invalid number of items!")
    number_items = int(input("Number of Items: "))
for i in range(number_items):
    item_price = float(input("Price of Item: "))
    if item_price < 0:
        print("Invalid please, please enter the correct price")
        item_price = input("Price of Item: ")
    total_price += item_price
if total_price > 100:
    total_price = total_price / 1.1
print("The price of ",number_items," items is $",total_price)


