coins = input().split()   
heads = 0   
tails = 0   
i = 0   
while i < len(coins):
    if coins[i] == '1':
        heads += 1
    else:
        tails += 1
    i += 1
print(min(heads, tails))   
