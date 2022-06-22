import random

random.seed()

people = []
luck_coef = 1  # Success is 1% luck
hard_work_coef = 99  # and 99% hard work
population = 10000  # Sample size

for i in range(0, population):
    luck = random.randint(0, luck_coef)
    hard_work = random.randint(0, hard_work_coef)
    person = [i, hard_work, luck, luck + hard_work]
    people.append(person)

hardworking = []
hardworking.append(people[0])
ti = 1

for i in range(1, population):
    for j in range(0, len(hardworking)):
        if j + 1 == len(hardworking):
            if people[i][ti] > hardworking[j][ti]:
                hardworking.insert(j, people[i])
                break
            else:
                hardworking.append(people[i])
                break
        else:
            if j == 0 and people[i][ti] >= hardworking[j][ti]:
                hardworking.insert(0, people[i])
                break
            elif hardworking[j][ti] > people[i][ti] >= hardworking[j + 1][ti]:
                hardworking.insert(j + 1, people[i])
                break
            else:
                pass

successful = []
successful.append(people[0])
ti = 3
for i in range(1, population):
    for j in range(0, len(successful)):
        if j + 1 == len(successful):
            if people[i][ti] > successful[j][ti]:
                successful.insert(j, people[i])
                break
            else:
                successful.append(people[i])
                break
        else:
            if j == 0 and people[i][ti] >= successful[j][ti]:
                successful.insert(0, people[i])
                break
            elif successful[j][ti] > people[i][ti] >= successful[j + 1][ti]:
                successful.insert(j + 1, people[i])
                break
            else:
                pass

for i in range(0, len(hardworking)):
    print("Rank ", i + 1, " Hardworking: ", hardworking[i][0], hardworking[i][2], " VS Successful: ", successful[i][0],
          successful[i][2])
