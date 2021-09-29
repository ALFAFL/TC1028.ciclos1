def main():
    #escribe tu código abajo de esta línea
    p=int(0)
    y=int(0)

    n=int(input())

    while(n>=0):
        if(n%2==0):
            p=p+1
        else:
            y=y+1
        n=int(input())    
    print("total de pares=",p)


if __name__=='__main__':
    main()
