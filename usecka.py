#mame dva body a pixel po pixli vykresli medzi nimi usecku
#([a,b], [c,d])
#du doplnit tak aby to fungovalo vzdy, ak ked prvy bod bude mat vacsie suradnice ako druhy bod
from PIL import Image
pic = Image.new("RGB", (250,250), "white")
pixels = pic.load()


a = int(input("Zadaj x-ovu suradnicu bodu A: "))
b = int(input("Zadaj y-ovu suradnicu bodu A: "))
c = int(input("Zadaj x-ovu suradnicu bodu B: "))
d = int(input("Zadaj y-ovu suradnicu bodu B: "))

if a>c and b>d or (a>c or b>d):
    a, c = c, a
    b, d = d, b

A = (a, b)
B = (c, d)

if a != c:
    k = (B[1]-A[1])/(B[0]-A[0])
    q = A[1] - k*A[0]

if a == c:
    for y in range(A[1], B[1]):
        x = a
        pixels[x,y] = (0,0,0)
elif c-a > d-b:
    for x in range(A[0], B[0]):
        y = int(k*x + q)
        pixels[x,y] = (0,0,0)
elif c-a < d-b:
    for y in range(A[1], B[1]):
        x = int((y-q)/k)
        pixels[x,y] = (0,0,0)

pic.show()
