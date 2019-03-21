if __name__ == '__main__':

    a = ((1,2,3),(4,5,6,),(7,8,9))
    b = list(a)
    for c in b:
        b[b.index(c)] = list(c)
        print(c)
    print (b)