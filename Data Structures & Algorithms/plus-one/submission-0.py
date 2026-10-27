class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        l=[]
        s=""
        for i in digits:
            s+=str(i)
        s=int(s)
        s+=1
        for i in str(s):
            l.append(i)
        return l
        