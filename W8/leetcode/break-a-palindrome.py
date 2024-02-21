class Solution:
    def breakPalindrome(self, palindrome: str) -> str:

        palindrome_ = list(palindrome)
        if len(palindrome_) == 1:
            return ''
        for x in range(len(palindrome_)//2):
            if palindrome_[x] > "a":
                palindrome_[x] = 'a'
                break
        if palindrome_ == list(palindrome):
            palindrome_[len(palindrome)-1] = 'b'
        

        return ''.join(palindrome_)