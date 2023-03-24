
f = open("text.txt","r")
# f.write("hello\nworld")
con = f.readlines()
# print(con)
i = 1
for temp in con:
    print("%d:%s"%(i,temp),end="")
    i+=1