import sys
if len(sys.argv) < 1:
    print("Too few arguments, aborting.")
    quit()
f = open(sys.argv[1], 'r', encoding="utf-8")
content = f.read()
parsed = ""
flag = False
for c in content:
    if c == " " and flag:
        continue
    elif c == " ":
        flag = True
    else:
        flag = False
    parsed += c
f.close()
f_w = open(sys.argv[1], 'w')
f_w.write(parsed)