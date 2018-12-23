"""
A palindrome is a word, number, phrase, or other sequence of characters which reads the same backward as forward,
such as madam or racecar or the number 10201.
Sentence-length palindromes may be written when allowances are made for adjustments to capital letters,
punctuation, and word dividers, such as "A man, a plan, a canal, Panama!",
"Was it a car or a cat I saw?" or "No 'x' in Nixon".
"""
import argparse


def is_palindrome(phrase):
    cleaned_str = ''.join(x.lower() for x in phrase if x.isalpha() or x.isdigit())
    if cleaned_str and (cleaned_str == cleaned_str[::-1]):
        return True
    return False


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--phrase',
        dest='phrase',
        required=True,
        help='String which to check'
    )
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_arguments()
    print(is_palindrome(args.phrase))
