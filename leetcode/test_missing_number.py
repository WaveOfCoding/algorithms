"""https://leetcode.com/problems/missing-number/description/"""
import pytest
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return n * (n + 1) // 2 - sum(nums)


s = Solution()


@pytest.mark.parametrize("int, answer", [
    ([3, 0, 1], 2),
    ([0, 1], 2),
    ([9, 6, 4, 2, 3, 5, 7, 0, 1], 8)
])
def test_solution(int, answer):
    assert s.missingNumber(int) == answer