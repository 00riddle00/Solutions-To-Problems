def count_sheep(n):
    return ('{} sheep...'*n).format(*[*(range(1,n+1))])
