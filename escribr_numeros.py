outfile = open('lista.txt', 'w')
for i in range(1, 1000001):
    outfile.write(str(i)+"\tProducto_"+str(i)+"\n")