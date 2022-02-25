#User function Template for python3

from sys import maxsize
from bisect import bisect_right as upper_bound

class Solution:
    def median(self, matrix, r, c):
        mi=maxsize
        ma=-maxsize
        #find max and min element in the whole matrix
        for arr in matrix:
            if(mi>arr[0]):
                mi=arr[0]
            if(ma<arr[-1]):
                ma=arr[-1]
                
        desired=(r*c)//2 #if m is median, it'll have n//2 elements on both sides 
        
        while(mi<ma):
            mid=mi+(ma-mi)//2
            cnt=0
            for arr in matrix:
                cnt+=upper_bound(arr, mid)  #the rightmost index where mid can be inserted so that it's always sorted
            cnt=cnt-1   #bisect gives index to insert, so to count elements before this index, - by 1
            if(cnt<desired):
                mi=mid+1    #if cnt<desired, median must be greater than the present value, so increase mi
            else:
                ma=mid      #if cnt>desired, median must be less than the present value, so decrease ma
        return mi   #at last, mi stores our median
                
            
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        r,c = map(int,input().strip().split())
        matrix = [[0 for j in range(c)] for i in range(r)]
        line1 = [int(x) for x in input().strip().split()]       
        k = 0
        for i in range(r):
            for j in range (c):
                matrix[i][j]=line1[k]
                k+=1
        ans = ob.median(matrix, r, c);
        print(ans)
# } Driver Code Ends


"""
Input:
R = 3, C = 3
M = [[1, 3, 5], 
     [2, 6, 9], 
     [3, 6, 9]]

Output: 5

"""
