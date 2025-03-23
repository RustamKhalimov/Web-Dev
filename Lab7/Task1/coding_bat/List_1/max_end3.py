def max_end3(nums):
  maxi = 0
  if nums[0] > nums[2]:
    maxi = nums[0]
  else:
    maxi = nums[2]
  arr = [maxi,maxi,maxi]
  return arr
