x = int(input('First number'))
y = int(input('Second number'))


def skibidi(x,y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, x+1):
        if (x % i == 0) and (y % i == 0):
            hcf = i
    return(hcf)

print(skibidi(x,y))
