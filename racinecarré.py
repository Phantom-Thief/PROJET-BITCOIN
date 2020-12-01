def resQ(a,mod):
    tab = []
    N=int((mod-1)/2)
    if(pow(a,N,mod)!=1):
        return
    else:
        for i in range(1,N+1):
            if(pow(i,2)%mod==a):
                tab.append(i)

                if(mod%2 == a%2):
                    tab.append(mod-i)
                else:
                    tab.append(mod-i-1)

    print("les racines de",a,"dans Z",mod,"sont:",tab)

def main(a,mod):
    resQ(a,mod)

if __name__ == '__main__':
    main(52,103)
