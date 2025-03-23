def sum2(nums):
  sum = 0
  l = len(nums)
  if l >= 2:
    sum = nums[0] + nums[1]
  elif l == 1:
    sum = nums[0]
  else:
    sum = 0
  return sum  
