class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        res = 40
        while res >= 40:
            res = 7 * (rand7() - 1) + rand7() - 1
        return res % 10 + 1

        