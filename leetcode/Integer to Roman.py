class Solution(object):
    def intToRoman(self, num):
        hash_digitals = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX', 10: 'X', 11: 'XI', 12: 'XII', 13: 'XIII', 14: 'XIV', 15: 'XV', 16: 'XVI', 17: 'XVII', 18: 'XVIII', 19: 'XIX', 20: 'XX', 30: 'XXX', 40: 'XL', 50: 'L', 60: 'LX', 70: 'LXX', 80: 'LXXX', 90: 'XC', 100: 'C', 200: 'CC', 300: 'CCC', 400: 'CD', 500: 'D', 600: 'DC', 700: 'DCC', 800: 'DCCC', 900: 'CM', 1000: 'M', 2000: 'MM', 3000: 'MMM'}
        #hash_digitals я спарсил с википедии :D
        res = str()
        if num <= 20:
            res = (hash_digitals[num])
        elif num < 100:
            s_n = str(num)
            res += (hash_digitals[int(s_n[0] + '0')])
            if int(s_n[1]) != 0:
                res += hash_digitals[int(s_n[1])]
        elif num < 1000:
            s_n = str(num)
            res += (hash_digitals[int(s_n[0] + '00')])
            if int(s_n[1]) != 0:
                res += (hash_digitals[int(s_n[1] + '0')])
            if int(s_n[2]) != 0:
                res += hash_digitals[int(s_n[2])]
        else:
            s_n = str(num)
            res += hash_digitals[int(s_n[0] + '000')]
            if int(s_n[1]) != 0:
                res += (hash_digitals[int(s_n[1] + '00')])
            if int(s_n[2]) != 0:
                res += (hash_digitals[int(s_n[2] + '0')])
            if int(s_n[3]) != 0:
                res += hash_digitals[int(s_n[3])]
        return res
