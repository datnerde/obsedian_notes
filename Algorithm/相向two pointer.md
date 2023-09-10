# Reverse型
- 反转字符
- 反转回文串
## 经典例题
- 125. Valid Palindrome![[Pasted image 20230910162250.png]]
```python
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return False
        
        left, right = 0, len(s) - 1
        
        if left >= right:
            return True
        
        while left < right:
            while left < right and not self.is_valid(s[left]):
                left += 1
            while left < right and not self.is_valid(s[right]):
                right -= 1
            if left < right and s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True
    
    def is_valid(self, char):
        return char.isdigit() or char.isalpha()
```
- 680. Valid Palindrome II
