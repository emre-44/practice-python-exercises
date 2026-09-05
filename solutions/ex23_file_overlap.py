with open('ex23_primes.txt','r') as f:
    primes = set(line.strip() for line in f)  #Generator Expression

with open ('ex23_happy.txt','r') as f:
    happies = set(line.strip() for line in f) #line.strip() for delete \n

overlaps = primes.intersection(happies)
print(overlaps)