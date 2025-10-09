precio = input ("Di el precio del producto con dos decimales: ")
a = precio.split (".")
euros = a[0]
centimos = a[1]
print ("El producto cuesta "+euros + " euros con " + centimos + " céntimos" )
