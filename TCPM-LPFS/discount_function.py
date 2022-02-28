# Author: Tracy Vierra
# Date Created: 2/28/2022
# Date Modified: 2/28/2022

# Description:

# Usage:

def student_discount(price):
    price = price - (price * 10) / 100
    return price

def additional_discount(newprice):
    newprice = newprice - (newprice * 5) / 100
    return newprice

selling_price = 100

#applying both discounts simultaneously

print(additional_discount(student_discount(selling_price)))

