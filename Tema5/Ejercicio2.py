

def primo(num):
    
    for i in range(2, num-1):
        if num % i == 0:
            return False
    return True

print(primo(11))