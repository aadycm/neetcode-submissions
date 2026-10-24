class Solution:
    def countBits(self, n: int) -> List[int]:
        list = []
        for i in range(n+1):
            num = i
            c = 0 
            while num >0 :
                if num % 2 == 1:
                    c+=1
                num = num//2
            list.append(c)

        return list
            

            
            



        