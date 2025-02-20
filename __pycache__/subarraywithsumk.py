def subarraySum(nums,k):
        sub_num = {0:1}
        total = count = 0

        for n in nums:
            total += n
            
            if total - k in sub_num:
                count += sub_num[total-k]
            print(count,(sub_num),total)
            sub_num[total] = 1 + sub_num.get(total, 0)
        return count,sub_num
print(subarraySum([2,4,1,2,7],7))