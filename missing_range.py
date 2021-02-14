def findMissingRanges(nums, lower, upper):
    def getRange(lower, upper):
        if lower == upper:
            return "{}".format(lower)
        else:
            return "{}->{}".format(lower, upper)
    ranges = []
    prev = lower-1
        
    for i in range(len(nums) + 1):
        if i==len(nums):
            curr=upper+1
        else:
            curr=nums[i]
        if curr-prev>=2:
            ranges.append(getRange(prev+1, curr-1))
        prev=curr
            
    return ranges


print(findMissingRanges([3, 6, 50, 75], 0, 99))

