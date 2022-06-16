class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        l=[[] for i in range(numRows)]
        N=len(s)
        k=0
        state=1 # Tracks direction of zigzag
        for j in range(N):
            l[k].append(s[j])
            if k<numRows and state==1:
                k+=1
            if k>=0 and state==-1:
                k-=1
            if k==numRows:
                state*=-1
                k-=2
            if k==-1:
                state*=-1
                k+=2
        return ''.join([''.join(h) for h in l])
