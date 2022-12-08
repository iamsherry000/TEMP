def twosum(nums, target):
    dic = {}
    ans = []
    for i in range(len(nums)):
        if (target - nums[i]) not in dic:
            dic[nums[i]] = i
        else:
            ans.append(dic[target - nums[i]])
            ans.append(i)
            return ans

if __name__ == "__main__":
    print('輸入: nums =', end='  ')
    nums = eval(input()) #不能用list
    print('target =', end='  ')
    target = int(input())
    ans = twosum(nums, target)
    print(ans)