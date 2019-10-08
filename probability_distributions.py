#1

# 1.a what is the probability that no cars drive up in the noon hour?
# 13.5% chance
stats.poisson(2).pmf(0)

#1.a simulation

np.random.seed(123)
cars = pd.DataFrame(np.random.poisson(2,10000))
cars[0].value_counts().loc[0]/cars[0].size


#1.b probability 3 or more cars drive up?
# 32% chance
stats.poisson(2).sf(0)

#1.b simulation

cars[cars[0]>=3].count()/cars[0].size

#1.c at least 1 car?
# 83%
stats.poisson(2).sf(0)

#1.c simulation

cars[cars[0]>=1].count()/cars[0].size



#2 Grades of State University graduates are normally distributed with a mean of 3.0 and a standard deviation of .3. Calculate the following:
n_trials = 10000

grades = pd.DataFrame(np.random.normal(3,.3,n_trials))
grades_mean = 3
grades_std = .3
grades.head()

#2a What grade point average is required to be in the top 5% of the graduating class?
# simulation
grades[0].quantile(.95)
#theoretical
grades = stats.norm(3,.3)
grades.isf(.05)

#2.b 2.69gpa
#theoretical
grades.ppf(.15)
#simulation
grades[0].quantile(.15)


#2c. An eccentric alumnus left scholarship money for students in the third decile from the bottom of their class. Determine the range of the third decile. Would a student with a 2.8 grade point average qualify for this scholarship?

# theoretical gpa 2.74 is lower and 2.84 is upper of third decile
grades.ppf(.2)
grades.ppf(.299)
#simlation
grades[0].quantile(.20)
grades[0].quantile(.299)

#3 A marketing website has an average click-through rate of 2%. One day they observe 4326 visitors and 97 click-throughs. How likely is it that this many people or more click through?

#theoretical
n = 4326
success = .02

# 13.9% chance
stats.binom(n,success).sf(96)

# simulation

n_trials = 10000
p_fail = .98
views = 4326
click_thru = 97

trials = pd.DataFrame(np.random.random((n_trials,views)))
trials['click_thru'] = trials[trials>p_fail].count(axis=1)
over_96 = trials['click_thru'] >=click_thru
over_96.mean()


# 4 You are working on some statistics homework consisting of 100 questions where all of the answers are a probability rounded to the hundreths place. Looking to save time, you put down random probabilities as the answer to each question.

n_trials = 100000
p_success = .01
n_questions = 60

# 45% chance of one question right
questions = pd.DataFrame(np.random.random((n_trials,n_questions)))
questions
right_answer = questions <=p_success

(right_answer.sum(axis=1) > 0).mean()

#4 simulation 
stats.binom(60,.01).sf(0)


#5 The codeup staff tends to get upset when the student break area is not cleaned up. Suppose that there's a 3% chance that any one student cleans the break area when they visit it, and, on any given day, about 90% of the 3 active cohorts of 22 students visit the break area. How likely is it that the break area gets cleaned up each day? How likely is it that it goes two days without getting cleaned up? All week?

# theoretical
n_trials
visits = 59
p_success = .03
# success is 86%
success = stats.binom(59,.03).sf(0)

#simulation

n_trials = 100000
success = .03
students = 59

visits = pd.DataFrame(np.random.random((n_trials,students)))
visits['cleaned'] = visits[visits<=success].count(axis=1)
cleaned_up = visits['cleaned'] >=1
cleaned_up.mean()


#chance of two days in a row with no cleaning is 2.7%
failure = 1-success
failure*failure


#6 You want to get lunch at La Panaderia, but notice that the line is usually very long at lunchtime. After several weeks of careful observation, you notice that the average number of people in line when your lunch break starts is normally distributed with a mean of 15 and standard deviation of 3. If it takes 2 minutes for each person to order, and 10 minutes from ordering to getting your food, what is the likelihood that you have at least 15 minutes left to eat your food before you have to go back to class? Assume you have one hour for lunch, and ignore travel time to and from La Panaderia.

students = 15
avg_std = 3
order_minutes = 2
lunch_distro = stats.norm(students,avg_std)
lunch_distro

#6.a 2 min per order and 10 min to complete order. 
#Total orders need to < 35 minutes, or 17.5 customers

#theoretical
lunch_distro.cdf(17.5)


# simulation

n_trials = 10000

customers = pd.DataFrame(np.random.normal(15,3,n_trials))

enough_time = customers[0]<=16.5
customers[enough_time].size/customers.size

import env
def get_db_url():
    user = env.user
    password = env.password
    host = env.host
    database = input("Database: ")
    url = f'mysql+pymysql://{user}:{password}@{host}/{database}'
    return url

url = get_db_url()
salaries = pd.read_sql('SELECT * FROM salaries',url)
salaries = pd.DataFrame(salaries)

#7 Connect to the employees database and find the average salary of current employees, along with the standard deviation. Model the distribution of employees salaries with a normal distribution and answer the following questions:

#7.a What percent of employees earn less than 60,000?

salary_distro.cdf(60000)

#7.b What percent of employees earn more than 95,000?

salary_distro.sf(95000)

#7.c What percent of employees earn between 65k and 80k?
# 47% earn more than 65000 and 83% earn less than 80000. 35.9% earn between that.s
print(salary_distro.sf(65000))
print(salary_distro.cdf(80000))

#7.d What did the top 5% of employees make?
salary_distro.isf(.05)