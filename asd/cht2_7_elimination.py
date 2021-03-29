import sys
sys.stdin = open("cht2_7_input.txt","rt")

n=int(input())
list_below_n=list(range(1,n+1))
i= 0
#print(len(list_below_n))
while i < len(list_below_n):
    #print(len(list_below_n))
    if i == 0:
        i+=1
    else:
        
        j=list_below_n[i]
        #print("j",j)
        list_below_n= [k for k in list_below_n if (( k != 1)&(k <= j))|(( k % j != 0)&( k != 1))]
        i+=1

print(list_below_n)