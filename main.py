#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
'''Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].'''

#Code

# Collecting the target value.
target=int(input("Enter Target Number: "))
# Collecting the inputs in the array using map function in one line seperating with space.
arr=list(map(int,input("Enter Data in the Array: ").strip(" ").split(" ")))

'''You can use this example for checking the output instantly
target=5
arr=[1,2,3,4,5,0]'''

#print the header.
print("|| Output || \n------------\nIndex 1 | value 1 + Index 2 | Value 2 = Result")
#for loop
for i in range(len(arr)):
  #capture the first index as front value.
  set=arr[i]
  #inner for loop for calculating the values between the front index and rare indexes. 
  for j in range(i+1,len(arr)):
    if set+arr[j]==target:
      print("\n   {}    |    {}    +    {}    |    {}    =   {}".format(arr.index(arr[i]),arr[i],arr.index(arr[j]),arr[j],(arr[i]+arr[j])))
print("-----------------------------------------------")
