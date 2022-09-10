#Hola, Bienvenido!
#Primero que todo vamos a importar la libreria de python math, esta nos ayudará para hacer algunas operaciones matemáticas.

def funmat(a,v):
    m = len(a)
    n = len(a[0])
    print(m)
    print(n)
    fila = [(0, 0)] * n
    r = [fila] * m
    for j in range(m):

        fila = [(0, 0)] * n
        r[j] = fila
        for k in range(n):
            r[j][k] = lc.cplxsum(lc.cplxmult(a[j][k],v[k]),lc.cplxmult(v[k],[j][k]))

    return r

#1. Adición de vectores complejos.

def suvectores(v,w) :
    n = len(v)
    print(n)
    r = [(0,0)] *n
    for k in range(n):
        r[k]=lc.cplxsum(v[k],w[k])
    return r
#2. Inverso (aditivo) de un vector complejo.

def invector(a):
    n = len(v)
    print(n)
    r = [(0,0)] * n
    for k in range(n):
        r[k] = lc.cplxmult((-1,0),v[k])
    return r
#3. Multiplicación de un escalar por un vector complejo.

def multesc(c,v):
    n = len(v)
    print(n)
    r = [(0, 0)] * n
    for k in range(n):
        r[k] = lc.cplxmult(c, v[k])
    return r
#4. Adición de matrices complejas.

def summa(a,b):
    m = len(a)
    n = len(a[0])
    print(m)
    print(n)
    fila = [(0,0)] * n
    r = [fila] * m
    for j in range (m):

        fila = [(0,0)] * n
        r[j] = fila
        for k in range(n):
            r[j][k] = lc.cplxsum(a[j][k],b[j][k])
    return r
#5. Inversa (aditiva) de una matriz compleja.
def inverso(a,b):
    imaginario = a[0] + b[0]
    inverso_imaginario =  -a[0] - b[0]
    return (inverso_imaginario)

#6. Multiplicación de un escalar por una matriz compleja.

def escalar(a,b):
    vector = a[0] , b[0] 
    escalar = d[0]
    escalar_mult = d[0]*a[0] + d[0]*b[0] 
    return ( escalar_mult)


#10. Producto de dos matrices (de tamaños compatibles)

def multmat(a,b):
    m = len(a)
    n = len(a[0])
    print(m)
    print(n)
    fila = [(0,0)] * n
    r = [fila] * m
    for j in range (m):

        fila = [(0,0)] * n
        r[j] = fila
        for k in range(n):
            r[j][k] = lc.cplxsum(lc.cplxmult(a[j][0], b[0][k]), lc.cplxmult(a[0][k],b[j][0]))
    return r
#11. Función para calcular la "acción" de una matriz sobre un vector.

#12. Producto interno de dos vectores

def productointernov(a,b):
    n = len(a)
    print(n)
    r = [(0, 0)] * n
    for k in range(n):
            r[k] = lc.cplxmult(a[k], b[k])
    return r

#13. Norma de un vector

def norma(a,b):
    vector1 = a[0] , b[0] 
    norma =   (a[0]**2 + b[0]**2)**(1/2)
    return (norma)


#16. Revisar si una matriz es Hermitiana

def hermitanio(a):
    m = len(a)
    n = len(a[0])
    print(m)
    print(n)
    fila = [(0, 0)] * n
    r = [fila] * m
    for j in range(m):

        fila = [(0, 0)] * n
        r[j] = fila
        for k in range(n):
            r[j][k] = lc.cplxcon(a[k][j])
    resultado = (a == r)
    print(resultado)
    return r

    
#17. Producto tensor de dos matrices/vectores

def vectensor(A,B):
    na = len(A)
    nb = len(B)
    nr = nb * na
    print(nr)
    R = [(0,0)] * nr
    index = 0
    for j in range(na):
        for k in range(nb):
            R[index] = lc.cplxmult(A[j], B[k])
            index = index + 1
    return R


print("Bienvenido a su libreria de computación cuántica")
print("Realizado por Thomas Feris Riaño")