from collections import defaultdict

class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        strnum = str(num)
        n = len(strnum)
        vocab_digit = {1: "One", 2: "Two", 3:"Three", 4: "Four", 5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine",0:""}
        vocab_teen = {1: "Eleven", 2: "Twelve", 3: "Thirteen", 4:"Fourteen",5:"Fifteen",6:"Sixteen" ,7:"Seventeen",8:"Eighteen",9:"Nineteen",}
        vocab_ten = {0: "", 1: "Ten", 2: "Twenty", 3:"Thirty", 4: "Fourty", 5:"Fifty",6:"Sixty",7:"Seventy",8:"Eighty",9:"Ninety",0:""}
        units = {0: "", 1: "Ten", 2: "Hundred", 3: "Thousand", 6: "Million", 9: "Billion"}

        result = ""
        for i in range(0, n):
            pos = n - i - 1
            number = int(strnum[i])
            unit = units[pos]
            lead = vocab_ten[number] if (pos % 3) == 1 else vocab_digit[number]
            number = lead + " " + unit if pos > 1 else lead

            result += number + " "
            print(i, pos, unit, lead, number)

        return result.strip()

sln = Solution()
ans = sln.numberToWords(12)
print(ans)