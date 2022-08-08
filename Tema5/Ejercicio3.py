def bisiesto(num):
    if (num % 4 ) & (num % 100) & (num %400) == 0:
        return True
    else:
        return False

print(bisiesto(2000))