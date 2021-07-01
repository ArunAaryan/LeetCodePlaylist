#day 6
#approach 1
def nextGreatestLetter(self, letters: List[str], target: str) -> str:
    ltx = '{'
    mtx = '{'
    for letter in letters:
        if letter > target and letter <= 'z':
            mtx = min(mtx, letter)
        ltx = min(ltx, letter)
    if mtx == '{':
        return ltx
    else:
        return mtx

#approach 2 by user

def nextGreatestLetter(self, letters, target):
        for letter in letters:
            if letter > target:#This will scan till z
                return letter
        return letters[0] # If not found the first element only will be the least element in cyclic wrap.