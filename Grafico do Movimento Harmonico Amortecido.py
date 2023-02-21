import math
from matplotlib import pyplot as plt

def main():
    b=float(input("Escreva a constante 'b' (Constamte de Amortecimento) em (kg/s): "))
    m=float(input("Escreva a massa do corpo oscilante no sistema massa mola em (kg): "))
    k=float(input("Escreva a constante 'k' (Constante de Proporcionalidade) da mola trabalhada em (N/m): "))
    A=float(input("Escreva a distenção máxima da mola em (m): "))
    gama=b/(2*m)
    w0=(k/m)**(1/2)
    delta=gama**2-w0**2
    if delta>0:
        s=1
    elif delta==0:
        s=2
    elif delta<0:
        s=3
    if s==1:
        c1=(((gama)*A)/(2*(delta**(1/2))))+(A/2)
        c2=(A/2)-((gama*A)/(2*(delta**(1/2))))
        def x(t):
            x=c1*(math.e**(t*((delta**(1/2))-gama)))+c2*(math.e**(-t*(gama+(delta**(1/2)))))
            return x
    elif s==2:
        c1=A
        c2=A*gama
        def x(t):
            x=(c1+t*c2)*math.e**(-gama*t)
            return x
    elif s==3:
        w=(-delta)**(1/2)
        c1=(A*gama)/w
        c2=A
        def x(t):
            x=(math.e**(-gama*t))*(c1*math.sin(w*t)+c2*math.cos(w*t))
            return x
    t=0
    while t<=100:
        xp=[x(t) for i in range(0,100)]
        yp=[]
        while len(yp)<=len(xp):
            if len(yp)==len(xp):
                break
            else:
                yp.append(0)
        plt.scatter(xp,yp)
        plt.xlim(-A,A)
        plt.ylim(-1,1)
        #plt.savefig("{}".format(t))
        t+=1
        plt.close()
    xp2=[i for i in range(0,100)]
    yp2=[x(xp2) for xp2 in range(0,100)]
    plt.plot(xp2,yp2)
    plt.show()
main()