class Solution(object):
    def intToRoman(self, num):
        digitals = [
            ('M', 1000), ('CM', 900), ('D', 500), 
            ('CD', 400), ('C', 100), ('XC', 90), 
            ('L', 50), ('XL', 40), ('X', 10), 
            ('IX', 9), ('V', 5), ('IV', 4), 
            ('I', 1)
        ]
        
        result = ''

        for digital in digitals:
            if num // digital[1]:
                cnt_add = num // digital[1]
                result += (digital[0] * cnt_add)
                num = num % digital[1]
        
        return result
                
