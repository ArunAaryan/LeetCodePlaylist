#Both are same methods of solving but different intuitions in array.
nums = [4,5,2,3,9,1,2,9]

prefix1 = [0] * (len(nums) + 1)

for i in range(len(nums)):
    prefix1[i+1] = prefix1[i] + nums[i]

def solution1(l, r):
    print(prefix1[r+1]- prefix1[l])
    print('first prefix',prefix1[r+1], prefix1[l])

solution1(2,3)

prefix = [nums[0]]
for i in range(1, len(nums)):
    prefix.append(prefix[i-1]+ nums[i])

def solution(l, r):
    print(prefix[r] - prefix[l-1])
    print('second prefix',prefix[r] , prefix[l-1])
print(prefix1)
print(prefix)
solution(2,3)
