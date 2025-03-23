def has23(nums):
  count = 0
  for i in range(len(nums)):
    if nums[i] == 2 or nums[i] == 3:
      count += 1
      
  return count >= 1  
