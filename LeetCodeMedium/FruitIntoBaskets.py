from collections import Counter
class Solution:
    # below solution will work for 'atmost k ' unique elements
    # space complexity will depend on k
    def totalFruit(self, tree):
        left = 0
        right = 0
        res = 0
        current_window = Counter()
        while right < len(tree):
            current_window[tree[right]] += 1
            while len(current_window) > 2:
                current_window[left] -= 1
                if not current_window[tree[left]]:
                    current_window.pop(tree[left])
                left += 1
            res = max(res, right - left + 1)
            right += 1
        print(tree[left : right + 1])
        print(current_window)
        return res

    def totalFruit1(self, fruits):
        firstFruit = secondFruit = 0 #first fruit is the lastsecond fruit we encountered, second is the last fruit we encountered
        secondFruitCount = 0 # store the value of the secondFruitCount to check continuity
        curMax = totalMax = 0
        for fruit in fruits:
            if fruit == firstFruit or fruit == secondFruit: # if the current fruit type already in basket then increase curMax
                curMax += 1 # either it is apple or mango increase the count by 1 because count(apple + mango) + (new apple) / (new mango)
            else:
                curMax = secondFruitCount + 1 # if the current fruit is new to basket or same as first or second then count of last fruit + this new fruit will be curMax
                #ex if apple, mango were in basket now new fruit is pineapple so remove apple from basket and add pineapple , so count(mango) + 1 
            if fruit == secondFruit: 
                secondFruitCount += 1
            else: # means fruit is new  then remove first fruit
                secondFruitCount = 1
                firstFruit = secondFruit
                secondFruit = fruit
                
                
            totalMax = max(curMax, totalMax)
        return totalMax
                




s = Solution()
res = s.totalFruit([0,1,2,2])
print(res)

        



        