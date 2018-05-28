import sys

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Invalid number of parameters!")
        sys.exit(1)
    else:
        print("sys.argv[0]: ", sys.argv[0])
        print("sys.argv[1]: ", sys.argv[1])

    l=[]
    for i in range(1,10,2):
        l.append((i, i+1))
    print("l: ", l )

    d = {}
    d[sys.argv[1]] = l
    print("d: ", d)
    print("d[sys.argv[1]]: ", d[sys.argv[1]])