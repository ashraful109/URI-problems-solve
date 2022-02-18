age = int(input())

print("{} ano(s)".format(int(age/365)))
aux = (age%365)
print("{} mes(es)".format(int(aux/30)))
aux = (aux%30)
print("{} dia(s)".format(int(aux%30)))


