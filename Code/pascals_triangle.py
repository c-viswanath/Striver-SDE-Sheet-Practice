class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        def nCr(n, r):
            return (fact(n) / (fact(r) * fact(n - r)))
        def fact(n):
            if n == 0 or n==1:
                return 1
            res = 1
            for i in range(2, n+1):
                res = res * i  
            return res    
        result=[]
        for i in range(1,numRows+1):
            if i==1:
                result.append([1])
            elif i==2:
                result.append([1,1])
            elif i>=3:
                arr=[]
                for j in range(1,i+1):
                    ele=int(nCr(i-1,j-1))
                    arr=arr+[int(ele)]
                result.append(arr)
        return result                    
            
