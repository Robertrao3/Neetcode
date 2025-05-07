class Solution:
    def compress(self, chars: List[str]) -> int:
        index = 0
        i = 0
        n = len(chars)

        while i < n:
            character = chars[i]
            count = 0

            while i < n and chars[i] == character:
                i += 1
                count += 1
            
            chars[index] = character
            index += 1

            if count > 1:
                for j in str(count):
                    chars[index] = j
                    index += 1
        return index