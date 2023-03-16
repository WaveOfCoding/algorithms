"""https://leetcode.com/problems/single-number/"""
import pytest
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        mask = 0
        for num in nums:
            mask ^= num
        return mask


s = Solution()


@pytest.mark.parametrize("int, answer", [
    ([2, 2, 1], 1),
    ([4, 1, 2, 1, 2], 4),
    ([1], 1)
])
def test_solution(int, answer):
    assert s.singleNumber(int) == answer
