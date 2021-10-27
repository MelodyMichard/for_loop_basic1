print('Numbers from 1 to 150:')
for n in range(1, 151):
    print(n)

print('Numbers from 1 to 1000 multiples of 5:')
for n in range(5, 1001, 5):
    print(n)

print('Numbers 1 to 100. Divisible by 5 print coding. Divisible by 10 print coding dojo:')
for n in range(1, 101):
    if n % 10 == 0:
        print('Coding Dojo')
    elif n % 5 == 0:
        print('Coding')
    else:
        print(n)

print('add odd integers from 0 to 500,000 and print sum')
sum = 0
for n in range(1, 500001, 2):
    sum += n
print(sum)

print('positive numbers starting at 2018 counting down by fours')
for n in range(2018, 0, -4):
    print(n)

lowNum = 2
highNum = 9
mult = 3  

for n in range(lowNum, highNum + 1):
    if n % mult == 0:
        print(n)    

