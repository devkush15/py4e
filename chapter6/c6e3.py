# Encapsulate this code in a function named count, and generalize 
# it so that it accepts the string and the letter as arguments.

def countlet(string, letter):
    count = 0
    for str in string:
        if str == letter:
            count += 1
    return count

word = input('Enter a String: ')
alphabet = input('Enter Letter: ')
print('Count: ', countlet(word, alphabet))