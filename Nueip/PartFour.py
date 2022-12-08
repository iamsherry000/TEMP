# 正序: 小到大

def bubblesort(a):
    temp = True
    while temp:
        for i in range(1,len(a)):
            if a[i-1] > a[i]:
                a[i-1],a[i] = a[i],a[i-1]
                temp = False
        if not temp:
            temp = True
        else:
            break
    return a


if __name__ == "__main__":
    input_a = [77,5,5,22,13,55,97,4,796,1,0,9]
    ans = bubblesort(input_a)
    print(ans)