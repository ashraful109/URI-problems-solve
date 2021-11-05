
# X1,Y1 = input().split()
# X2,Y2 = input().split()
# #Distence = (((X2-X1)*(X2-X1)) + ((Y2-Y1)(Y2-Y1)))* 0.5
# Distence = ((float(int(X2)-int(X1)))**2 + (float(int(Y2)-int(Y1)))**2) 
# Distence = float
# #Distence = ((float(X2)-(X1))**2 + (float((Y2)-(Y1)))**2) * 0.5
# print("%.4f"%Distence)

#A = math.sqrt(float(int(X2)-int(X1)**2) + (float(int(Y2)-int(Y1)**2)))
#Distence = ((float(int(X2)-int(X1)))** 2 + (float(int(Y2)-int(Y1))** 2)) * 0.5


import math
X1,Y1 = list(map(float,input().split()))
X2,Y2 = list(map(float,input().split()))
Distance = math.sqrt((X2-X1)**2+(Y2- Y1)**2)

print("%.4f"%Distance)
