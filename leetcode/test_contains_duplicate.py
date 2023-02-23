"""https://leetcode.com/problems/contains-duplicate/description/"""
import pytest


class Solution(object):
    def containsDuplicate(self, nums):
        seen = set([])

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


s = Solution()


@pytest.mark.parametrize("int, answer", [
    ([1, 2, 3, 1], True),
    ([1, 2, 3, 4], False),
    ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
    ([], False)

])
def test_solution(int, answer):
    assert s.containsDuplicate(int) == answer