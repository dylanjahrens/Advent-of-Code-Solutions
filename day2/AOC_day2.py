f = open('day2input.txt', 'r')
inputs = f.read()

#PART 1
f = open('day2input.txt', 'r')
valid_passwords = 0
for line in f:
    counter = 0
    split1 = line.split(': ')
    password = split1[-1]#password
    split2 = split1[0].split(' ')
    letter = split2[-1] #letter
    split3 = split2[0].split('-')
    min_range = split3[0] #min range
    max_range = split3[1] #max range
    for l in password:
        if l == letter:
            counter +=1
    if counter in range(int(min_range), int(max_range)+1):
        valid_passwords += 1

print(valid_passwords)

#PART 2
f = open('day2input.txt', 'r')
valid_passwords = 0
for line in f:
    split1 = line.split(': ')
    password = split1[-1]#password
    split2 = split1[0].split(' ')
    letter = split2[-1] #letter
    split3 = split2[0].split('-')
    first_index = int(split3[0]) -1 #they are not counting index 0
    second_index = int(split3[1]) -1
    if letter == password[first_index] and letter == password[second_index]:
        valid_passwords += 0
    elif letter == password[first_index] or letter == password[second_index]:
        valid_passwords +=1
    else:
        valid_passwords +=0
        
print(valid_passwords)





