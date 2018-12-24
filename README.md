# This script checks whether the sentence is a palindrome

A palindrome is a word, number, phrase, or other sequence of characters which reads the same backward as forward,
such as madam or racecar or the number 10201.
Sentence-length palindromes may be written when allowances are made for adjustments to capital letters,
punctuation, and word dividers, such as "A man, a plan, a canal, Panama!",
"Was it a car or a cat I saw?" or "No 'x' in Nixon". (Wikipedia)


This function works corretly only for sentence-length palindomes. Function "is_palindrome" drops spaces, punctuations and sets lowercase for all characters.
Example:
```
"No 'x' in Nixon" will be "noxinnixon".
```
If reading from the end is equal direct reading, then function returns True, otherwise function returns False.

# How to run on linux
```
$ python3 palindrome.py --phrase "No 'x' in Nixon"
```

# How to run unit tests
```
$ python3 -m unittest unit_tests.py
```
Also you can run direct tests
```
$ python3 -m unittest unit_tests.TestPalindromeStringMethod.test_is_palindrome
```
# Project Goals

The code is written for educational purposes only.
