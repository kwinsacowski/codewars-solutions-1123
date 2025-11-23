# Solution: Even or Odd
def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
# Solution Converty a Number to a String
def number_to_string(num):
    return str(num)

# Solution: Remove String Spaces
def no_space(x):
    return x.replace(" ", "")

#Solution: Vowel Count
def get_count(sentence):
    vowels = "aeiou"
    count = 0
    for char in sentence:
        if char in vowels:
            count += 1
    return count