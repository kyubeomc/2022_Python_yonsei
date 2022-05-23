number = 1
ssum = 0
while 1:
    
    ssum = ssum + number*3
    number = number + 1
    if number*3 >1000:
        break

print(ssum)

add = 0
average = 0
a = [70, 60, 55,75,95,90,80,80,85,100]

for score in a:
    add = add + score

average = add / len(a)
print(average)

numbers = [1,2,3,4,5]

result = [i*2 for i in numbers if i%2==1]
print(result)


z = ['dog', 'cat', 'parrot']
x = []
for word in z:
    x.append(word[0].upper())

print(x)