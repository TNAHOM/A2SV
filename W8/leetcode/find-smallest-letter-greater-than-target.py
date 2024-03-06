class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        for x in letters:
            if target < x:
                return x
        return letters[0]