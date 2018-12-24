class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        if digits == "":
            return []
        combos = [""]
        for dig in list(digits):
            temp = []
            for c in list(mapping[dig]):
                for combo in combos:
                    temp.append(combo + c)
            combos = temp
        return combos
