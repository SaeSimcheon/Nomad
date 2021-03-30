import sys
sys.stdin = open("cht2_7_input.txt","rt")

n=int(input())

def remain_counter(element):
    num_list=list(range(1,element+1))
    check_zero=list(map(lambda x : element % x, num_list))
    return check_zero.count(0)

list_below_n=list(range(1,n+1))
count_list=list(map(remain_counter,list_below_n))

print(count_list.count(2))
#20 점