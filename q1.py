
nums = [3,2,3]
dic = {}
for ii in nums:
    if ii in dic:
        val = dic.get(ii)
        dic[ii] = val + 1
    else:
        dic[ii] = 1
length = len(nums) / 2
print(dic)
output = 0
for jj in list(dic.keys()):
    if dic.get(jj) > length:
        output = jj
print(output)