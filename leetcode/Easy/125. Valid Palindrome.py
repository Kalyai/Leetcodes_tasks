class Solution(object):
    def isPalindrome(self, s):
        def check_symbol(symbol):
            if (48 <= ord(symbol) <= 57) or (65 <= ord(symbol) <= 90) or (97 <= ord(symbol) <= 122):
                string = symbol
                if 65 <= ord(symbol) <= 90:
                    string = chr(ord(symbol) + 32)
                return string, 1
            return False

        left, right = 0, len(s) - 1
        left_flag, right_flag = 0, 0
        left_string, right_string = s[left], s[right]

        while left < right:
            if check_symbol(s[left]):
                left_string, left_flag = check_symbol(s[left])

            else: left += 1

            if check_symbol(s[right]):
                right_string, right_flag = check_symbol(s[right])

            else: right -= 1

            if left_flag and right_flag:
                if left_string != right_string:
                    return False

                left += 1
                right -= 1
                left_flag, right_flag = 0, 0

        return True
