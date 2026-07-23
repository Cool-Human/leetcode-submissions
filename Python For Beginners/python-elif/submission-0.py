def check_range(num: int) -> str:
    return "negative" if num < 0 else "zero" if num == 0 else "positive single digit" if num < 10 else "positive multi digit"







  
# don't modify code below this line
print(check_range(-10))
print(check_range(0))
print(check_range(9))
print(check_range(1000))
