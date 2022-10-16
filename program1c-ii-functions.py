def geometric_series(n):
    if n<0:
        return 0
    else:
        return 1/(pow(2,n)+geometric_series(n-1))
print(geometric_series(2))