# time O(N), space O(1)
def missing_number(self, nums: List[int]) -> int:
    n = len(nums)
    missing = n * (n +1) // 2 - sum(nums)
    return missing
