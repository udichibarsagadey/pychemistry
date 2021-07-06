f = open("E://udichi/mydoc.txt",'a')

f.writelines("\nthis is wretten by udichi");

f.close()

f = open("E://udichi/mydoc.txt",'r')
for x in f:
    print(x)

f.close()