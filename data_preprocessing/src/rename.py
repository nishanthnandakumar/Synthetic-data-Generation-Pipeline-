import random, os

l = os.listdir('./testB/')
n = random.sample(l, len(l))

#print('files:', n)

i = 400

for file in n:

    curr_file = './testB/' + str(file)
    new_file = './testB1/000' + str(i) + '.jpg'
    i = i + 1

    os.rename(curr_file, new_file)

    