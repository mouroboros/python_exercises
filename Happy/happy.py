
def happy (x) :
    seen = []
    while x != 1:
        y = 0
        for n in range(len(str(x))):
            y += int(str(x)[n])**2
        if y in seen : return False
        seen.append(y)

        x = y
    return True
                    
                    
for x in range (1, 100) :
     if happy(x) : print (x, end = " ")


