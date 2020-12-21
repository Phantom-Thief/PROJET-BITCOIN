
def legendre(a, mod):
    return pow(a, (mod - 1) // 2, mod)


def resQ(a, mod):
                                                            #Algorithme de Tonelli
    if(legendre(a,mod)==1):                                 #On teste s'il s'agit d'un résidus quadratique
            q = mod - 1
            s = 0
            while q % 2 == 0:
                q //= 2
                s += 1
            if s == 1:
                return pow(a, (mod + 1) // 4, mod)
            for z in range(2, mod):
                if mod - 1 == legendre(z, mod):
                    break
            c = pow(z, q, mod)
            r = pow(a, (q + 1) // 2, mod)
            t = pow(a, q, mod)
            m = s
            t2 = 0
            while (t - 1) % mod != 0:
                t2 = (t * t) % mod
                for i in range(1, m):
                    if (t2 - 1) % mod == 0:
                        break
                    t2 = (t2 * t2) % mod
                b = pow(c, 1 << (m - i - 1), mod)
                r = (r * b) % mod
                c = (b * b) % mod
                t = (t * c) % mod
                m = i
            return r


def main(a,mod):
    resQ(a, mod)
    r = resQ(a, mod)
    assert (r * r - a) % mod == 0
    print("a = %d || modulo = %d" % (a, mod))
    print("\t  roots : [%d ; %d]" % (r, mod - r))

if __name__ == '__main__':
    main(52, 103)                                           #A modifier
