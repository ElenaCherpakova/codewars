def give_change(amount): 
    hundred, remainder = divmod(amount, 100)
    fifty, remainder = divmod(remainder, 50)
    twenty, remainder = divmod(remainder, 20) 
    ten, remainder = divmod(remainder, 10)
    five, remainder = divmod(remainder, 5)
    one, remainder = divmod(remainder, 1)
    return (one, five, ten, twenty, fifty, hundred)