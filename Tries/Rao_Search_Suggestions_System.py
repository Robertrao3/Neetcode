class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        if not products:
            return []
        
        n = len(searchWord)
        res = []
        products.sort()

        for i in range(1, n + 1):
            prefix = searchWord[:i]
            suggestions = []
            for p in products:
                if p.startswith(prefix):
                    suggestions.append(p)
                    if len(suggestions) == 3:
                        break
            res.append(suggestions)
        return res