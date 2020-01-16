import re

def add(number_str): 
    if len(number_str) == 0:
        return 0
                 
    elif len(number_str) == 1:
        return int(number_str)
   
    elif number_str[0] == "/":
         result = 0
         delim = number_str[3]

    else:
        result = 0
        delim = ","
        if number_str[1] != ",":
            delim = "\n"
        numbers = number_str.split(delim)
        for num in numbers:
            result += int(num)
        return result
