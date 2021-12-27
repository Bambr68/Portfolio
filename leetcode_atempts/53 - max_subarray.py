# spis = [-2,1,-3,4,-1,2,1,-5,4]
spis = [5,4,-1,7,8]
def maxSubArray(nums):
    rez=[]
    rez.append(nums[0])

    for i in range(1,len(nums)):

        rez.append(max(nums[i],nums[i]+rez[i-1]))

    return max(rez)




print(maxSubArray(spis))