def is_palindrome(s):
    return s == "" or s[0].casefold() == s[-1].casefold() and is_palindrome(s[1:-1])
