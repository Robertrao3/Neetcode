class Solution:
    def decodeString(self, s: str) -> str:
        if not s:
            return ""
        
        stack = []
        currString = ""
        currCount = 0

        for char in s:
            if '0' <= char <= '9':
                currCount = currCount * 10 + int(char)
            elif char == "[":
                stack.append((currString, currCount))
                currString = ""
                currCount = 0
            elif char == "]":
                prev_String, repeat_count = stack.pop()
                currString = prev_String + (currString * repeat_count)
            else:
                currString += char
        return currString