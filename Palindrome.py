def Pali(word):
    reverse  = ""
    for x in range(len(word)-1, -1, -1):
        reverse += word[x]
    if reverse.lower() == word.lower():
        print('This is a palindrome')
    else:
        print('This is not a palindrome')
    return reverse



user = input('Give me a word:')
Pali(user)

