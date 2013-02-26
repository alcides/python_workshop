a = ['Joaquim', 'Maria', 'Serafim']

print a[0]
print a[-1]

print a.pop(), a

a.append('Josefina')


for pessoa in a:
    print "Hello, %s" % pessoa
    
    
b = [ "Sra %s" % nome for nome in a if nome.endswith("a")  ]
print b