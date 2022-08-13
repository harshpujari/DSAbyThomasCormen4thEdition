def horner(poly, n, x):
    result = poly[0] 
    for i in range(1, n):
        result = result*x + poly[i] 
    return result
  
#poly is coefficient of polymonials 
#n in len of poly 
#x is highest degree of polymonial 
