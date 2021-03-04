f_line = int(input())
s_line = int(input())
if f_line == s_line:
    print(f_line)
    print(s_line)
    exit()
if f_line < s_line:
    print(s_line)
    print(f_line)
else:
    print(f_line)
    print(s_line)
