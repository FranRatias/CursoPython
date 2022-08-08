import numpy

def areatriangulo(base, altura):
    area = (base * altura) / 2
    return area


pi = numpy.pi

def areacirculo(radio):
    area = pi * (radio * radio)
    return round(area, 2)



print(areatriangulo(8, 10))
print(areacirculo(10))