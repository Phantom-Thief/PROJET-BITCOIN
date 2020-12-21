def resQ(a,mod):
    tab = []
    N=int((mod-1)/2)
    M=int((mod+1)/4)
    if(pow(a,N,mod)!=1 or mod%4!=3):
        return
    else:
        tab.append(pow(a,M,mod))
        tab.append(mod-pow(a,M,mod))
                

    print("les racines de",a,"dans Z",mod,"sont:",tab)

def main(a,mod):
    resQ(a,mod)

if __name__ == '__main__':
    main(52,103)