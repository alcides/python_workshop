cores = {
    'Benfica': 'Vermelho',
    'Porto': 'Azul',
    'Sporting': 'Verde'
}

print cores['Benfica']

cores['Academica'] = 'Preto'

del cores['Sporting']

for clube in cores:
    print "O %s joga de %s" % (clube, cores[clube])