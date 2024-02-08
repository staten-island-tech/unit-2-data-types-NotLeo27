#Let's create a function to accept a "bill" value and offer a tip of 0%, 15%, 20% or 25% depending on if the service was "bad, okay, good , or great ".


subtotal = float(input("> $"))
print('How was our services?')

def ratings():
    services = input()
    if services == "Bad":
        print("I'm sorry to hear that, you won't need to tip at all!")
    elif services == "Okay":
        print("Thank you! We recommend a tip of", subtotal*0.15)
    elif services == "Good":
        print("Thank you! We recommend a tip of", subtotal*0.20)
    elif services == "Great":
        print("Thank you! We recommend a tip of", subtotal*0.25)

ratings()
