def main():
    input_a = [0,1,2,3,4,5,6,7,8,9]
    Odd = []
    Even = []
    SumOdd = 0 
    SumEven = 0
    for i in input_a:
        if i%2==0:
            Even.append(i)
            SumEven+=i
        else:
            Odd.append(i)
            SumOdd+=i
    print(SumOdd - SumEven)


if __name__ == "__main__":
    main()