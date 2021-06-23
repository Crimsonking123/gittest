def recursive(n):
    if n<2:
        return n
    else:
        return n*recursive(n-1)
print(recursive(4))