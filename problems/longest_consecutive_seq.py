def longest_conecutive_seq(nums):
    nums_set = set(nums)
    longest = 0
    for n in nums:
        # check if previous consecutive val present in set. if yes then move on
        # if no then thats the start of the sequence
        if (n-1) not in nums_set:
            length = 0

            # keep checking if next val is present in set and increment length
            while (n+length) in nums_set:
                length += 1
        
            # update longest
            longest = max(longest, length)
    
    return longest

nums = [100,4,200,1,3,2]
nums2 = [0,3,7,2,5,8,4,6,0,1]
nums3 = [1,0,1,2]

print(longest_conecutive_seq(nums))
print(longest_conecutive_seq(nums2))
print(longest_conecutive_seq(nums3))
