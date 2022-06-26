# Here we use a window sliding across the array to find minimum score for the cards not picked, giving us maximum score for cards picked.
# Run time will be O(n) where n is length of the cardPoints array. Space complexity is O(1) as we are not using more memory while sliding window.
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        s=sum(cardPoints)
        N=len(cardPoints)
        w=N-k
        tot=m=sum(cardPoints[0:w]) # Makes a window sum which we will move and update m when tot is smaller than m
        for i in range(0,k):
            tot-=cardPoints[i]
            tot+=cardPoints[i+w]
            if tot<m: # Update
                m=tot
        return s-m # Return the maximum score which is sum- sum(smallest window)
