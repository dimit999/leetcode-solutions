class TestPalindrome:
    def test_palindrome(self):
        x = 121
        assert validate_palindrome(x), "Received item is NOT palindrome"


def validate_palindrome(x):
    final_value = []
    if x < 0:
        return False
    else:
        for item in str(x):
            final_value.append(item)
        final_value.reverse()
        if x == int(''.join(final_value)):
            return True
        else:
            return False
