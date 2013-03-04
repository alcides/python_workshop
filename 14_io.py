fi = open('14_apache.txt', 'r')
fo = open('14_apache_uppercase.txt', 'w')

with fi:
    with fo:
        for line in fi:
            fo.write(line.upper())
