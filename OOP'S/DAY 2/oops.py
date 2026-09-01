





'''a=[1,2,3,4,5]
for i in reversed(a):
    print(i,end=" ")
print()
print(a[::-1])
a.reverse()
print(a)
x="man"
print(''.join(reversed(x)))

for i in range(5,-1,-1):
    print(i,end="")
   
print() 
rev=""
for char in x:
    rev=char+rev
print(rev)'''

'''a=[1,2,3,4,5]
def reverse_array():
    for i in a:
        reversed(i)
        return i
s=reverse_array()
print(s)'''
'''
def two_sum(nums: list[int], target: int) -> list[int]:
    # Store value -> index mapping
    num_map = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        
        # Check if the complement already exists in the dictionary
        if complement in num_map:
            return [num_map[complement], i]
            
        # Store the current number and its index
        num_map[num] = i
        
    return [-1, -1]
# Example Input
nums = [2, 7, 11, 15]
target = 9

# Function Call
print(two_sum(nums, target))
'''

