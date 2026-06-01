def calculate_tax(price,tax_rate=0.05):
    return price*tax_rate



def calculate_tip(price,tip_amount=0.10):
    return price*tip_amount

def calculate_total(price):
    return price + calculate_tax(price) + calculate_tip(price)


def print_bill(item,price):
    print(f"{'Item':<12}:{item}")
    print(f"{'Base price':<12}:{price:.2f}")
    print(f"{'Tax(5%)':<12}:{calculate_tax(price):.2f}")
    print(f"{'Tip(10%)':<12}:{calculate_tip(price):.2f}")
    print(f"{'Total':<12}:{calculate_total(price):.2f}")



print_bill("Chicken Biriyani",250)


