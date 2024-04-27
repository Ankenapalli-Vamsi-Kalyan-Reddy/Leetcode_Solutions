'''
1356. Sort Integers by The Number of 1 Bits


You are given an integer array arr.
Sort the integers in the array in ascending order by the number of 1's in their binary representation
and in case of two or more integers have the same number of 1's you have to sort them in ascending order.

Return the array after sorting it.

 

Example 1:

Input: arr = [0,1,2,3,4,5,6,7,8]
Output: [0,1,2,4,8,3,5,6,7]
Explantion: [0] is the only integer with 0 bits.
[1,2,4,8] all have 1 bit.
[3,5,6] have 2 bits.
[7] has 3 bits.
The sorted array by bits is [0,1,2,4,8,3,5,6,7]
Example 2:

Input: arr = [1024,512,256,128,64,32,16,8,4,2,1]
Output: [1,2,4,8,16,32,64,128,256,512,1024]
Explantion: All integers have 1 bit in the binary representation, you should just sort them in ascending order.

'''


#Here's a breakdown of the steps:

#Iterate through each integer in the input list arr.
#For each integer, convert it to its binary representation using bin(i), remove the '0b' prefix from the binary string using slicing [2:], and count the number of '1's in the binary representation using count('1').
#Store this count in the list an.
#Create a list vi to store tuples where each tuple contains the count of set bits and the corresponding integer from the input list.
#Sort the list of tuples vi based on the count of set bits.
#Extract the sorted integers from the sorted list of tuples and store them in the list ka.
#Return the sorted list ka.


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        an = []
        vi = []
        for i in arr:
            an.append(bin(i)[2:].count('1'))
        for i in range(len(arr)):
            vi.append((an[i], arr[i]))
        nextt = sorted(vi)
        ka = [ker for output, ker in nextt]
        return(ka)
