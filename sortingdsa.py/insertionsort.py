def insertionsort(nums):
    for i in range(1,len(nums)):
        temp=nums[i]
        j=i-1
        while j>=0 and temp<nums[j]:
            nums[j+1]=nums[j]
            j-=1
        nums[j+1]=nums[j]
    return nums
nums=list(map(int, input().split()))
print(insertionsort(nums))

#tc=o(n) bestcase,worst case = o(n2),space complexity=o(1)
