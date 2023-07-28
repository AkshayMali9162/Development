amount =  5
items = [1,2,3,4,5]

inital_amt = 0
inital_item = 0
a = 0
for item in items:
    if inital_amt + item <= amount:
        a = a+item
        inital_amt  = inital_amt + item
    else:
        break

print(a)
