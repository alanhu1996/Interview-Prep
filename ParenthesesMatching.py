# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dict = {"}":"{", ")": "(", "]": "["}
        stack = []
        for i in s:
            if(i in dict.values()):
                stack.append(str(i))
            elif(i not in dict.keys() or stack == [] or dict[i] != stack.pop()):
                return False
            
            
        return stack == []