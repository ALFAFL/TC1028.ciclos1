def main():
  #escribe tu código abajo de esta línea
    def num(n):
        list=[]
        s=0
        for i in range(0,n+1):
            list.append(i)
        for i in list:
            s=s+i
        return (s)
    print(num(int(input())))

if __name__ == '__main__':
    main()
