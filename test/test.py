import re

'''
* 多次匹配任意值
^a 以a开始
3$ 以3结束

? 变成非贪婪匹配(从左至右匹配)
+ 至少出现一次

{m,n} 最小m次 最多n 次
{m,} 大于等于m次
{m} 出现m次
|  或者

[] 里面的任意字符或者区间
[^1] 不等于1

\s 空格
\S 不是空格都行
\w  = [A-Za-z0-9_]
\W  != [A-Za-z0-9_]
\d 数字

'''

line1 = "bryant123"
line2 = "boooobooooobaabbryant123"
line3 = "bryakntasdfkobe"
line4 = "18616396821"
line5 = "hoo"
line6 = "dddd遇见她如春水映梨花"
line7 = "出生2018"
regex_str = "^b.*3$"
regex_str2 = ".*(b.{2,5}b).*"
regex_str3 = "(.*(kobe| f))"
regex_str4 = "(1[86123][0-9]{9})"
regex_str5 = "(h\wo)"
regex_str6 = ".*?([\u4E00-\u9FA5]+花)"
regex_str7 = ".*?(\d+)"

line8 = ""
regex_str8 = ""

match_obj = re.match(regex_str8, line8)

if match_obj:
    print(match_obj.group(1))
