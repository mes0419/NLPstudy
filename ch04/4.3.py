# 4.3 정제 
# 파이썬에서 정규 표현식 사용
# re.sub('패턴', '바꿀문자열', '문자열', 바꿀횟수)
import re
regex = r"([\w]+\s*:?\s*)?\(?\+?([0-9]{1,3})?\-?[0-9]{2,3}(\)|\-)?[0-9]{3,4}\-?[0-9]{4}"
x = "ke: +82-10-1234-5678"
x = re.sub(regex, "REMOVED", x)
print(x)

y = "CONTENT jiu 02)1234-5678"
y = re.sub(regex, "REMOVED", y)
print(y)

z = '''abcdefg
12345
ab12
a1bc2d
12ab
a1b
1a2
a1
1a
hijklmnop'''
regex2 = r'([a-z])[0-9]+([a-z])'
to = r'\1\2'

z2 = '\n'.join([re.sub(regex2, to, z_i) for z_i in z.split('\n')])
print(z2)