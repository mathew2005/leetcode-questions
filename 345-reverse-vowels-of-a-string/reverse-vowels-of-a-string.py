class Solution:
    def reverseVowels(self, s: str) -> str:

        """
        """
        # if vowel -> reverse it
        # if consonant -> don't touch it
        # lower and upper cases, more than once
# [a,e,i,o,u,A,E,I,O,U]
        # solution 1:
        # loop through the list
        # push the vowels in to a temp array
        # reverse the temp array

        # loop through the list again
        # when we encounter a vowel, replace it with the value of temp array
        # T(n+ nlogn+ n.n)
        # S(n)

        # solution 2:
        # two pointers, l and r, l = 0 and r = len(s) - 1
        l = 0
        r = len(s) - 1
        vSet = {'a', 'e', 'i','o', 'u', 'A', 'E', 'I', 'O', 'U'}
        # keep looping while l < r
        s = list(s)
        while l < r:
            left = s[l]
            right = s[r]
            # case 1: l is vowel and r is not
            if s[l] in vSet and s[r] not in vSet:
                # r keeps moving s[l]
                r -= 1
            # case 2: l isn't vowel and r is
            elif s[l] not in vSet and s[r] in vSet:
                # l keeps moving  
                l += 1 
            # case 3: l and r isn't vowel
            elif s[l] not in vSet and s[r] not in vSet:
                # l moves s[r] and r moves s[l]
                l += 1
                r -= 1
            
            # case 4: l and r vowel
            else:
                temp = s[l]
                s[l] = s[r]
                s[r] = temp
                # swap l and r, using temp
                l +=1
                r -= 1
                # l moves s[r] and r moves s[l]
        return "".join(s)