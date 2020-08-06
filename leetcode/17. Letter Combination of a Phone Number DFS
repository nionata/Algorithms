class Solution:
    def __init__(self):
        self.letters = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        self.combos = []
        self.digits = ""
        
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        self.digits = len(digits)
        self.helper(digits, "")
        return self.combos if self.combos != [""] else []
    
    def helper(self, todo, path):
        if len(path) == self.digits:
            self.combos.append(path)
            return
        for letter in self.letters[int(todo[0])]:
            self.helper(todo[1:], path + letter)
