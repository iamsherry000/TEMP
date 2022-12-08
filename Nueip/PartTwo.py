# :改全形 OK
# - 兩側保留空白 OK
# :到-之間的字元 OK
def main():
    input_a = "人易科技:上 機 測 驗 - 演算法"
    arrayAns = []
    for i in input_a:
        if i == ' ':
            continue
        elif i == ':': 
            k = HalftoFull(i) 
            arrayAns.append(k)
        elif i =='-':
            m = " "        
            arrayAns.append(m)
            break
        else:
             arrayAns.append(i)
    strAns = "".join(arrayAns)    
    n = strAns.index(k)
    print(strAns[n+1:])

def HalftoFull(c:str): ## 轉全形+65248
   return chr(ord(c)+65248)

if __name__ == "__main__":
    main()