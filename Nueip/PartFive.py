def main():
    input_a = (77,5,5,22,13,55,97,4,796,1,0,9)
    input_b = (0,1,2,3,4,5,6,7,8,9)
    a = set(input_a)
    b = set(input_b)
    c = set()
    d = set(input_a)
    e = set(input_a)
    for i in b:
        if i in a:
            c.add(i)
            d.remove(i)
        else:
            e.add(i)    
    print(c)
    print(d)
    print(e)

if __name__ == "__main__":
    main()