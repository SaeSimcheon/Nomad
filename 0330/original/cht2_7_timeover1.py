import sys
sys.stdin = open("cht2_7_input.txt","rt")

n=int(input())


def remain_counter(element):
    if element == 1:
        return 1
    for i in range(2,element+1):
        if i == element:
            return 0
        if element % i ==0:
            return 1
        
list_below_n=list(range(1,n+1))
print([remain_counter(x) for x in list_below_n ].count(0))


#list_below_n=list(range(1,n+1))
#count_list=list(map(remain_counter,list_below_n))

#print(count_list.count(2))
