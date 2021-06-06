#!/usr/bin/env python
# coding: utf-8

# In[15]:



#name = Kishan Dongare

#topic = Adaline in soft computing

class Adaline :
    def __init__(self) :
        pass


#Adaline training with AND logic
    def AdalAND(self) :

        w1 = float(input('Enter w1 :'))
        w2 = float(input('Enter w2 :'))
        b = float(input('Enter bias :'))
        eta = float(input('Enter learning rate :'))
        
        iters = int(input('Enter the number of iterations :'))

        x1 = [1, 1, -1, -1]
        x2 = [1, -1, 1, -1]
        y = [1, -1, -1, -1] #target


        w1n=0
        w2n=0
        w3n=0
        bn=0
        error=0

        for i in range(0, iters) :
            print ("\n Epoch "+str(i))
            for j in range(0, 4) :
                yin = x1[j]*w1 + x2[j]*w2 + b

                w1n = w1 + eta * x1[j] * (y[j] - yin)
                w2n = w2 + eta * x2[j] * (y[j] - yin)
                bn = b + eta * (y[j] - yin)
                error = (y[j]-yin)**2

                print ("\t[+] Weights and bias after iteration "+str(j)+" :")
                print ("\n\t\tW1 :" +str(w1n))
                print ("\t\tW2 :" +str(w2n))
                print ("\t\tb  :" +str(bn))
                print ("\t\terror :"+str(error))

                w1 = w1n
                w2 = w2n
                b = bn

            print ("\n\n[+] After epoch " +str(i)+ " :")
            print (w1, w2, b,error)

        print ("\n")
        print ("Final Weights :")
        print (w1, w2, b,error)



#Adaline training with OR logic.
    def AdalOR(self) :
        w1 = float(input('Enter w1 :'))
        w2 = float(input('Enter w2 :'))
        b = float(input('Enter bias :'))
        eta = float(input('Enter learning rate :'))

        iters = int(input('Enter the number of iterations :'))

        x1 = [1, 1, -1, -1]
        x2 = [1, -1, 1, -1]
        y = [1, 1, 1, -1]


        w1n=0
        w2n=0
        w3n=0
        bn=0
        error=0

        for i in range(0, iters) :
            print ("\n Epoch "+str(i))
            for j in range(0, 4) :
                yin = x1[j]*w1 + x2[j]*w2 + b

                w1n = w1 + eta * x1[j] * (y[j] - yin)
                w2n = w2 + eta * x2[j] * (y[j] - yin)
                bn = b + eta * (y[j] - yin)
                error = (y[j]-yin)**2

                print ("\t[+] Weights and bias after iteration "+str(j)+" :")
                print ("\n\t\tW1 :" +str(w1n))
                print ("\t\tW2 :" +str(w2n))
                print ("\t\tb  :" +str(bn))
                print ("\t\terror :"+str(error))

                w1 = w1n
                w2 = w2n
                b = bn

            print ("\n\n[+] After epoch " +str(i)+ " :")
            print (w1, w2, b,error)

        print ("\n")
        print ("Final Weights :")
        print (w1, w2, b, error)



def main() :
    adal = Adaline()

    print ("[+] Choose :")
    print ("\t1. AND")
    print ("\t2. OR")

    ch = int(input())

    if ch == 1 :
        adal.AdalAND()

    if ch == 2 :
        adal.AdalOR()

if __name__ == '__main__' :
    main()


# In[ ]:




