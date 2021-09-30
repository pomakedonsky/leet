# space O(N), time O(N)
def two_sum(self, nums: List[int], target: int) -> List[int]:
    matches = {}
    for x in range(len(nums)):
        potential = target - nums[x]
        if potential in matches:
            return [matches[potential], x]
        else:
            matches[nums[x]] = x
    return []
