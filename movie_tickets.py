print('Welcome to the movies!')
movies_out_now = 'TopGun Maverick', 'Nope', 'Bullet Train'
child_ticket = 5
adult_ticket = 8
ticket_tax = 1.07
popcorn_bucket = 5

buy_more = str(input('Would you like to buy movie tickets? Yes/No: '))
while buy_more == 'Yes':
    print(movies_out_now)
    movie_choice = str(input('Select a movie to view: '))
    number_adult_tickets = int(input('How many adult tickets would you like to purchase?: '))
    number_child_tickets = int(input('How many child tickets would you like to purchase?: '))
    food_purchase = str(input('Would you like to purchase some popcorn? Yes/No: '))
    if food_purchase == 'Yes':
        food_purchase=int(input('How many popcorn buckets would you like to purchase? :'))
    else:
        food_purchase = int(0)
        print('No popcorn purchase today. Sad!')

    total_price = ((child_ticket*number_child_tickets)+(adult_ticket*number_adult_tickets)+(food_purchase*popcorn_bucket))*ticket_tax
    print('Your total price for the movie will be $' + str(round(total_price, 2)) + '!')
    print('Enjoy your movie: ' + movie_choice)
    buy_more = str(input('Would you like to buy more tickets? Yes/No: '))
print('See you next time at the movies!')