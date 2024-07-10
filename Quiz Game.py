
print('Welcome to my computer quiz!')
count = 0
playing = input('Do you want to play? ')
if playing.lower() != 'yes':
    quit()

print("Okay! Let's play :)")

answer = input("Q: What does CPU stand for?\nA: ").lower()
if answer == 'central processing unit':
    count += 1
    print("You are correct ")
    print("Your points : ",str(count))
else:
    print("You are wrong :( ")

answer = input("Q: What does GPU stand for?\nA: ").lower()
if answer == 'graphics processing unit':
    count += 1
    print("You are correct ")
    print("Your points : ",str(count))
else:
    print("You are wrong :( ")

answer = input("Q: What does RAM stand for?\nA: ").lower()
if answer == 'random access memory':
    count += 1
    print("You are correct ")
    print("Your points : ",str(count))
else:
    print("You are wrong :( ")

answer = input("Q: What does PSU stand for?\nA: ").lower()
if answer == 'power supply unit':
    count += 1
    print("You are correct ")
    print("Your points : ",str(count))
else:
    print("You are wrong :( ")

print("Your score card : "+str(count)+" / 4")
print("Your score card : "+str((count/4)*100)+" %")