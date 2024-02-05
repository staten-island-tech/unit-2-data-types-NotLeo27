print('what is your subtotal?')
subtotal=int(input())
print('What is your tip percent?')
tip_percent = int(input())

def Tip_calculator():
    print(subtotal)
    tip=tip_percent*subtotal/100
    Total=tip+subtotal
    print(Total)

Tip_calculator()