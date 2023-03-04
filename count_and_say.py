class Solution:
    def countAndSay(self, n: int) -> str:
        # base case or initial value of ans when n=1
        prev="1"
        # calculating and updating prev value remaining n-1 times
        for i in range(n-1):
            prev=self.fun(prev)
        return prev
    
    # main logic to find count and say of a given number as string
    def fun(self, num):
        n=len(num)
        count=1
        ans=""
        # loop until n-1, as for nth digit we dont know num[i+1] 
        for i in range(n-1):
            # grouping same digits
            if num[i]==num[i+1]:
                count+=1
            # if one group is over, update ans, like we say that group
            else:
                ans+=str(count)+num[i]
                count=1
        # update ans for the last digit
        ans+=str(count)+num[n-1]
        return ans
