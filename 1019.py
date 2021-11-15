N = int(input())

M = int(N/60)
S = (N % 60)
H = int(M/60)
M = M % 60

print(f'{H}:{M}:{S}')


   
# seconds = int(input());

# minutes = int(seconds/60);
# seconds %= 60;
# hours = int(minutes/60);
# minutes %= 60;

# print(f'{hours}:{minutes}:{seconds}')