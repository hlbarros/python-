
usuario = {'nome' : 'Belphegor', 'idade' : 65000, 'username': 'bel'}

print (usuario.items ())

del usuario ['username']

for k in usuario:
    print ('{0} -> {1}'.format (k, usuario[k]))

