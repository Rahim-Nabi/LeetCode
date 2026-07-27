class Solution:
    from typing import List

    def sortedSquares(self, nums: List[int]) -> List[int]:
        siz=len(nums)
        neg=[]
        pos=[]

        #Seperation of +ve and -ve elements
        for num in nums:
            if num<0:
                neg.append(num)
            else:
                pos.append(num)
            
        #Case1 : no -ve elements
        if len(neg) == 0:
            return[x*x for x in pos]

        #case2 : no +ve elements
        if len(pos) == 0:
            res=[x*x for x in neg]
            res.reverse()
            return res

        #Case3: Both +ve and -ve elements
        neg=[x*x for x in neg][::-1]
        pos=[x*x for x in pos]
        n,m = len(neg),len(pos)
        res = []

        i = j = 0
        while i < n and j < m:
            if neg[i] <= pos[j]:
                res.append(neg[i])
                i += 1
            else:
                res.append(pos[j])
                j += 1
        while i<n:
            res.append(neg[i])
            i += 1
        while j<m:
            res.append(pos[j])
            j += 1
         
        return res
        