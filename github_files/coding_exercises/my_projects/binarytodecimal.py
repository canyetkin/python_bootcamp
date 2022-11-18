#this function converts binary to decimal 

def binarytodecimal():
    sayi=int(input("ikili sistem degerini giriniz:"))
    sonuc=0
    binary= [int(x) for x in str(sayi)]
    binary.reverse()
    for a,b in zip(range(len(binary)),binary):
        sonuc=sonuc +(2**a)*b
    binary.reverse()
    print("{} binary value equals to ---> {} as decimal".format(binary,sonuc))
    



binarytodecimal()