# Design an algorithm that generates the first n numbers in the following sequence:; 1, 2, 3, 6, 11, 20, 37, ___, ___, ___, …
n = int(input("Enter the length of the sequence: ")) # Do not change this line
nums = [1,2,3]

for number in nums:
    print(number)
    if number == n:
        break

for i in range(n):
    num = nums[-1] + nums[-2] + nums[-3]
    nums.append(num)
    print(num)
    if n == len(nums):
        break