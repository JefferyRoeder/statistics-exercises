#1. How likely is it that you roll doubles when rolling two dice?

import numpy as np
import pandas as pd
np.random.seed(123)

# roll doubles with dice
n_trials = 1000000
n_dice = 2

#16%
rolls = pd.DataFrame(np.random.choice([1,2,3,4,5,6],(n_trials,n_dice)))
rolls.head(2)

rolls['roll_doubles'] = np.where(rolls[0] == rolls[1],True,False)

rolls['roll_doubles'].mean()


#2 If you flip 8 coins, what is the probability of getting exactly 3 heads? What is the probability of getting more than 3 heads?
n_trials = 100000
n_flips = 8
coin_flips = pd.DataFrame(np.random.randint(1,3,(n_trials,n_flips)).astype(str))
coin_flips['heads'] = coin_flips.count(1)
coin_flips.head(2)

#2.a exactly 3 heads is 21%
coin_flips = pd.DataFrame(np.random.choice([True,False],(n_trials,n_flips)))
coin_flips
coin_flips['heads'] = coin_flips[coin_flips==True].count(axis=1)
coin_flips.head()

#2.b more than 3 is 63%

exactly_three = coin_flips['heads'] > 3
exactly_three.mean()



#3 There are approximitely 3 web development cohorts for every 1 data science cohort at Codeup. Assuming that Codeup randomly selects an alumni to put on a billboard, what are the odds that the two billboards I drive past both have data science students on them?
n_trials = 1000
p_ds = .25
signs = 2

#3.a 6.8% chance both are DS students
data = pd.DataFrame(np.random.random((n_trials,signs)))
data['both_ds'] = data[data<=.25].count(axis=1)
both_ds = data['both_ds'] == 2
both_ds.mean()


#4 Codeup students buy, on average, 3 poptart packages (+- 1.5) a day from the snack vending machine. If on monday the machine is restocked with 17 poptart packages, how likely is it that I will be able to buy some poptarts on Friday afternoon?
days = 5
days = 5
n_trials = 10000
tarts_per_day = pd.DataFrame(np.random.normal(3,1.5,(n_trials,days)))
tarts_per_day = tarts_per_day.round(0)
#4.a 67% chance there wiill be a poptart left (if you are ok with possibly eating .1 parts of a poptart)
tarts_per_day['week_total'] = tarts_per_day.sum(axis=1) < 17
tarts_per_day['week_total'].mean()

#5
#Compare Heights

#Men have an average height of 178 cm and standard deviation of 8cm.
#Women have a mean of 170, sd = 6cm.
#If a man and woman are chosen at random, P(woman taller than man)?

n_trials = 100000
man_height = np.random.normal(178,8,n_trials)
woman_height = np.random.normal(170,6,n_trials)
# 21% chance a woman is taller
df = list(zip(man_height,woman_height))
df = pd.DataFrame(df,columns=['Men','Women'])
df['woman_taller'] = df['Women'] > df['Men']
df['woman_taller'].mean()

#6 When installing anaconda on a student's computer, there's a 1 in 250 chance that the download is corrupted and the installation fails. What are the odds that after having 50 students download anaconda, no one has an installation issue? 100 students?
n_trials = 100000
p_fail = .996
installs = 100

#6.a    81% chance no failure with 50 installs
#       67% chance there is no failure after 100 installs
#       45% chance there is a failure in first 150
#       16% chance no issues with 450 installs

install_pass = pd.DataFrame(np.random.random((n_trials,installs)))
install_pass['num_of_failure'] = install_pass[install_pass>.996].count(axis=1)
no_fail = install_pass['num_of_failure'] == 0
no_fail.mean()


#7 There's a 70% chance on any given day that there will be at least one food truck at Travis Park. However, you haven't seen a food truck there in 3 days. How unlikely is this?

n_trials = 10000
p_success = .7
days = 3
# 97% chance a truck will show up at least once
truck_in_park = pd.DataFrame(np.random.random((n_trials,days)))
truck_in_park
no_truck = truck_in_park <p_success
(no_truck.sum(axis=1) > 0).mean()

#how likely a food truck will show up this week

n_trials = 10000
p_success = .7
days = 7
#
truck_in_park = pd.DataFrame(np.random.random((n_trials,days)))

truck_in_park['num_for_week'] = (truck_in_park <p_success).sum(axis=1)
(truck_in_park['num_for_week']>0).mean()
truck_in_park.head()


#8 If 23 people are in the same room, what are the odds that two of them share a birthday? What if it's 20 people? 40?
birthdays['unique'] = birthdays.count(axis=1) - birthdays.nunique(axis=1)
1-(birthdays['unique']==0).mean()
#50% chance