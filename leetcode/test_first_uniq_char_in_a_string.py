"""https://leetcode.com/problems/first-unique-character-in-a-string/"""
import pytest


class Solution:
    def firstUniqChar(self, s: str) -> int:
        symbol_hash = {}

        for symbol in s:
            if symbol in symbol_hash:
                symbol_hash[symbol] += 1
            else:
                symbol_hash[symbol] = 1

        for pos in range(len(s)):
            if symbol_hash[s[pos]] == 1:
                return pos

        return -1


s = Solution()


@pytest.mark.parametrize("string, answer", [
    ('leetcode', 0),
    ('loveleetcode', 2),
    ('aabb', -1)
])
def test_solution(string, answer):
    assert s.firstUniqChar(string) == answer