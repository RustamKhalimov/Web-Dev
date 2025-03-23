def same_first_last(nums):
  i = len(nums)
  return i >= 1 and nums[0] == nums[i-1]
