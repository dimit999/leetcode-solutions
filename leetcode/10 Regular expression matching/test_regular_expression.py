import re

import pytest


class TestRegularExpression:
    """
    Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

    '.' Matches any single character.​​​​
    '*' Matches zero or more of the preceding element.
    The matching should cover the entire input string (not partial).



    Example 1:

    Input: s = "aa", p = "a"
    Output: false
    Explanation: "a" does not match the entire string "aa".
    """

    data = [
        ("aa", "a*", True),
        ("aa", "a", False)
    ]

    @pytest.mark.parametrize("string, pattern, expected_result", data)
    def test_regular_expression(self, string, pattern, expected_result):
        match = re.search(pattern, string)
        match_value = string in match.group()
        assert match_value == expected_result, "Not correct expression value"
