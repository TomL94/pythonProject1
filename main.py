# Code for team A's points
a_team_goals = int(input())

a_team_scoring_time = []
for i in range(a_team_goals):
    a_team_scoring_time.append(int(input()))


# code for team B's points
b_team_goals = int(input())

b_team_scoring_time = []
for i in range(b_team_goals):
    b_team_scoring_time.append(int(input()))


# code for output 1: goals scored in first half

a_plus_b_lst = a_team_scoring_time + b_team_scoring_time

first_half_goals = 0
for i in a_plus_b_lst:
    if i <= 1440:
        first_half_goals += 1


print(first_half_goals)

# create lists for both A team and B team, run lists parallel to create how many times they came from behind calc

length_a = []
length_b = []
comebacks = 0
previous_difference = 0

a_team_winning = False
b_team_winning = False

for i in range(2880):
    if i in a_team_scoring_time:
        length_a.append(i)
    if i in b_team_scoring_time:
        length_b.append(i)

    score_difference = len(length_a) - len(length_b)

    if i == 0:
        if score_difference > 0:
            a_team_winning = True
            previous_difference = score_difference
        if score_difference < 0:
            b_team_winning = True
            previous_difference = score_difference
        else:
            continue

    if i > 0:
        if score_difference > 0:
            if a_team_winning == True:
                if previous_difference <= 0:
                    comebacks += 1
        if score_difference < 0:
            if b_team_winning == True:
                if previous_difference >= 0:
                    comebacks += 1


print(comebacks)
