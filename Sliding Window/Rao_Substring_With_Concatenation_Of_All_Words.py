class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words:
            return []
        
        word_len = len(words[0])
        num_words = len(words)
        sub_len = word_len * num_words
        
        word_counts = Counter(words)
        result = []
        
        s_len = len(s)
        if s_len < sub_len:
            return []

        for i in range(word_len):

            left = i
            window_counts = Counter()
            words_seen = 0
            
            for right in range(i, s_len - word_len + 1, word_len):
                current_word = s[right : right + word_len]
                if current_word not in word_counts:
                    left = right + word_len
                    window_counts.clear()
                    words_seen = 0
                    continue

                window_counts[current_word] += 1
                words_seen += 1
                
                while window_counts[current_word] > word_counts[current_word]:
                    left_word = s[left : left + word_len]
                    window_counts[left_word] -= 1
                    words_seen -= 1
                    left += word_len
                
                if words_seen == num_words:
                    result.append(left)
                    left_word = s[left : left + word_len]
                    window_counts[left_word] -= 1
                    words_seen -= 1
                    left += word_len

        return result