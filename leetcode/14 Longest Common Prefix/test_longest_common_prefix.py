import pytest


class TestLongestCommonPrefix:
    """
    Write a function to find the longest common prefix string amongst an array of strings.

    If there is no common prefix, return an empty string "".



    Example 1:

    Input: strs = ["flower","flow","flight"]
    Output: "fl"
    Example 2:

    Input: strs = ["dog","racecar","car"]
    Output: ""
    Explanation: There is no common prefix among the input strings.
    """

    data = [
        (["flower", "flow", "flight"], "fl"),
        (["aca", "ica"], "")
    ]

    @pytest.mark.parametrize("received_list, expected_str", data)
    def test_longest_common_prefix(self, received_list, expected_str):
        max_length_items_list = []
        for item in received_list:
            max_length_items_list.append(len(item))

        max_value_from_list = max(max_length_items_list)
        value_from_original_list = received_list[max_length_items_list.index(max_value_from_list)]
        pre_expected_str = ""
        final_expected_str = ""
        for str_item in value_from_original_list:
            pre_expected_str += str_item
            if len([item for item in received_list if item.startswith(pre_expected_str)]) == len(received_list):
                final_expected_str += str_item
        assert final_expected_str == expected_str, "OIncorrect expected result"


