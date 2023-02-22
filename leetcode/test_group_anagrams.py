"""https://leetcode.com/problems/group-anagrams/"""
import pytest
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        def key_by_word(strs):
            return ''.join(sorted(strs))

        groups = {}

        for word in strs:
            group_key = key_by_word(word)
            if group_key not in groups:
                groups[group_key] = []
            groups[group_key].append(word)

        result = []
        for group_key in groups:
            result.append(groups[group_key])
        return result


s = Solution()


@pytest.mark.parametrize("strs, answer", [
    (["eat", "tea", "tan", "ate", "nat", "bat"]), ([["bat"], ["nat", "tan"], ["ate", "eat", "tea"]])
])
def test_solution(strs, answer):
    assert s.groupAnagrams(strs) == answer