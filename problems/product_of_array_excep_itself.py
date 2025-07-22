# taking prefix and postfix approach
# using 2 arrs for pre and post for better understanding --> requires extra space
nums = [1, 2, 3, 4]
def productExceptSelf(nums):
    pre, post = 1, 1
    prefix, postfix = [1]*len(nums), [1]*len(nums)
    for i in range(len(nums)):
        prefix[i] = pre
        pre *= nums[i]

    for i in range(len(nums)-1, -1, -1):
        postfix[i] = post
        post *= nums[i]
    
    print(prefix)
    print(postfix)

    res = []
    i = 0
    while i < len(nums):
        res.append(prefix[i] * postfix[i])
        i += 1
    print(res)
    return res

productExceptSelf(nums)

# can be optimized for space
# dont need 2 arrs seperate
#   - just create 1 arr and do prefix calculations
#   - then directly mulitply the postfix values in reverse

def product1(nums):
    res = [1] * len(nums)

    pre = 1
    for i in range(len(nums)):
        res[i] = pre
        pre *= nums[i]

    post = 1
    for i in range(len(nums)-1, -1, -1):
        res[i] *= post
        post *= nums[i]

    print('optimized', res)
    return res

product1(nums)
    
