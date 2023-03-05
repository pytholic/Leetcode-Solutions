class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = "".join(c for c in s if c.isalnum())

        if not s:
            return True

        s = s.lower()

        first = 0
        last = len(s) - 1
        mid = len(s) // 2

        while first <= mid <= last:
            if s[first] != s[last]:
                return False

            first += 1
            last -= 1

        return True


s1 = "A man, a plan, a canal: Panama"
s2 = "race a car"
s3 = " "

solution = Solution()
res = solution.isPalindrome(s3)
print(res)
