S, P = map(int, input().split())   

 
D = S**2 - 4*P

 
if D < 0:
    print("NO")
else:
    
    X = (S + D**0.5) / 2
    Y = (S - D**0.5) / 2
     
    print(int(X), int(Y))

