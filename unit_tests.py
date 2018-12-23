import unittest
from palindrome import is_palindrome
from palindrome_list import palindromes, not_palindromes


class TestPalindromeStringMethod(unittest.TestCase):

    def test_is_palindrome(self):
        for pal in palindromes:
            print(pal)
            self.assertEqual(is_palindrome(pal), True)

    def test_numeric_palindromes(self):
        str_num = '1'
        while str_num != '1111111111':
            self.assertEqual(is_palindrome(str(int(str_num) * int(str_num))), True)
            str_num +='1'

    def test_is_not_palindrome(self):
        for pal in not_palindromes:
            self.assertEqual(is_palindrome(not_palindromes), False)


if __name__ == '__main__':
    unittest.main()
