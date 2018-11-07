s = 'abcd efgh ijklm'
s = s.split(' ')
print (s[1])
print (s[0][0:4:2] + ' ' + s[1][1:4:2] + s[2][0:5:2])
print (s[2][-1::-1])

s = 'abc def ghi jkl'
s = s.split(' ')
print ( s[len(s)-1] )

