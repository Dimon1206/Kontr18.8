def check_palindrome(string):
    reversed_string = string[::-1]
    if string == reversed_string:
        print(string, 'это слово полиндром')
    else:
        print(string, 'это слово не полиндром')


check_palindrome('мадам')
check_palindrome('world')