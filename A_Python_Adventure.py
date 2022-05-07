# This is an adaptation of the Scrimba Python Course Dictionaries Exercise.
# Made it repeatably playable using a while loop, a function, and a sub-function.

def python_adventure():
    # Set starting purse amount
    purse = 1000
    # Create shops with inventory and prices
    freelancers = {'name': 'Freelancing Shop', 'brian': 70, 'black knight': 20, 'biggus diccus': 100,
                   'grim reaper': 500, 'minstrel': -15}
    antiques = {'name': 'Antique Shop', 'french castle': 400, 'german joke': 5, 'wooden grail': 3, 'scythe': 150,
                'catapult': 75}
    pet_shop = {'name': 'Pet Shop', 'blue parrot': 10, 'white rabbit': 5, 'newt': 2, 'eric the half-a-bee': 8,
                'fish': 20}

    # Print game instructions for the users.
    print('Your village is being attacked by "a germanic tribe" and you need to run to each of the three stores and ')
    print('get the right thing from each to save your village, and probably some good-looking girl or boy you want ')
    print('to marry. All prices are in gold pieces excl. VAT... chop chop!! ze germanz are coming!')
    print(f'You have {purse} Gp to make your purchases.')
    shopping_cart, items_purchased = _shopping(freelancers, antiques, pet_shop)
    sum_purchases = sum(shopping_cart.values())
    final_purse = purse - sum_purchases
    # TODO try to figure out why purse -= sum_purchases doesn't calculate correctly.
    # Print list of items purchased.
    # Ver 1.2 update - Add information about how much coin was spent and how much is left in user's purse.
    print(f'You purchased{items_purchased}. You spent {sum_purchases} Gp and have {final_purse} Gp remaining.')
    print('Have a nice day of mayhem!')
    # Added message if the user found the best possible solution where they make money but easily defeat the enemy.
    if shopping_cart == {'minstrel': -15, 'german joke': 5, 'white rabbit': 5}:
        print("Congratulations! You found the best possible solution. You made money and defeated the enemy with ease!")
        try_again = input('Would you like to play again, anyway? type Y or N: ').upper()
    else:
        print("You didn't find the best possible solution, but hopefully you had some fun.")
        try_again = input('Would you like to play again to try to find the best solution? type Y or N: ').upper()
    return try_again


def _shopping(shop1, shop2, shop3):
    # Create cart to keep track of items purchased from each shop and string format list of items for final report.
    cart = {}
    bought_items = ''
    # Loop through each shop, asking user input of items they want to purchase.
    for shop in (shop1, shop2, shop3):
        print(f"Welcome to {shop['name']}!  Type \"exit\" if you do not want to purchase anything.")
        # Print list of all items available in the shop with costs.
        print(f"Today we have: ")
        for key, value in shop.items():
            if key == 'name':
                # Excludes the name of the shop from the list of items available in the shop.
                continue
            else:
                print(f"{key} costs {value}", end=", ")
        # Request input from user forcing it to lower case
        buy_item = input(f"What do you want to buy?: ").lower()
        if buy_item == "exit":
            # Allow user to type exit if they don't want to buy from this shop.
            continue
        elif buy_item not in shop:
            # Exit shop without purchase if user types something that isn't in the shop.
            print(f"The {shop['name']} does not have any {buy_item}. Please come again.")
            continue
        else:
            # Modify string format list of items purchased with costs.
            bought_items = bought_items + f': {buy_item} at {shop[buy_item]} Gp'
            # Modify cart to add item purchased and remove the item from shop inventory.
            cart.update({buy_item: shop.pop(buy_item)})
    return cart, bought_items


play_again = 'Y'
while play_again == 'Y':
    play_again = python_adventure()
