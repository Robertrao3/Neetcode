class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s
        
        rows = [''] * numRows

        curr_row = 0
        down = False

        for char in s:
            rows[curr_row] += char

            if curr_row == 0 or curr_row == numRows - 1:
                down = not down
            
            if down:
                curr_row += 1
            else:
                curr_row -= 1
        return ''.join(rows)