class Solution:
    def isValid(self, s: str) -> bool:
        
        closetoopen = {')':'(', '}':'{',']':'['}
        res = []

        for st in s:
            if st in closetoopen:
                if res and res[-1]==closetoopen[st]:
                    res.pop()
                else:
                    return False
            else:
                res.append(st)
        
        return True if not res else False



        