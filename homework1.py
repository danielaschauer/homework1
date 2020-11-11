# Aufgabe 1 - Prüfung Primzahl

def is_prime(n):
    if n < 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Aufgabe 2 - Bruch Addierer

def add_frac(z1,n1,z2,n2):

    gn=int(n1*n2)    #gn = gemeinsamer Nenner
    z1_neu=z1*n2
    z2_neu=z2*n1
    gz=int(z1_neu+z2_neu)   #gz = gemeinsamer Zähler

    print("Ergebnis ungekürzt: ",z1,"/",n1,"+",z2,"/",n2,"=",gz,"/",gn) #Ergebnis ungekürzt

    if gz/2 % gn/2 != 0: #kürzen versucht (nicht optimal!), besser Schleife?
        gz2=int(gz/2)
        gn2=int(gn/2)
    
    print("Ergebnis gekürzt: ",z1,"/",n1,"+",z2,"/",n2,"=",gz2,"/",gn2) #Ergebnis kürzen versucht
