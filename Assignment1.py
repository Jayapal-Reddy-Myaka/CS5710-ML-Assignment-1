### Assignment 1

import math
### Question 1

# The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# Sort the list and find the min and max age
# sorting list of ages
sorted_ages = sorted(ages)
print("sorted ages list :", sorted_ages)
# finding min age from sorted ages list
min_age = min(sorted_ages)
print("min age : ", min_age)
# finding max age from sorted ages list
max_age = max(sorted_ages)
print("max age : ", max_age)

# Add the min age and the max age again to the list
sorted_ages.extend((min_age, max_age))
print("sorted ages after adding min and max age : ", sorted_ages)

# calculating Median of Ages
sorted_ages = sorted(sorted_ages)
len_ages = len(sorted_ages)

if len_ages % 2 == 0:
    # median calculation for list with even items
    median_age = (sorted_ages[int(len_ages/2)-1] + sorted_ages[int(len_ages/2)]) / 2
else:
    # median calculation for list with odd items
    median_age = sorted_ages[math.ceil(len_ages/2)]
print("Median Age : ", median_age)
# calculating Average of Ages
avg_age = sum(sorted_ages)/len(sorted_ages)
print("Average Age : ", avg_age)
# calculating Range of Ages
range_age = max_age - min_age
print("Range of Age : ", range_age)

### Question 2
# Create an empty dictionary called dog
dog = dict()
# Adding data to dog dictionary
dog['name'] = 'puppy'
dog['color'] = 'brown'
dog['breed'] = 'Labrador'
dog['legs'] = 4
dog['age'] = 5
print("dog dictionary : ", dog)
# creating student dictionary with data
student = {
    "first_name": "jaypal",
    "last_name": "myaka",
    "gender": "male",
    "age": 23,
    "marital status": "single",
    "skills": ["python", "machine learning"],
    "country": "United States",
    "city": "lees summit",
    "address": "1104 Innovation Campus"
}
print("student dictionary : ", student)
# length of the student dictionary
len_student = len(student)
# skills of the student from the dictionary
skills = student['skills']
# type of skills
print("type of skills :",type(skills))
# updating student skills
student['skills'].extend(["AI"])
print("updated student skills : ", student["skills"])
# keys of student dictionary
print("keys of student dictionary : ", list(student.keys()))
# values of student dictionary
print("values of student dictionary : ", list(student.values()))

### Question 3
# creating tuple for brothers
brothers = ("Jayanth","Laxman")
print("brothers : ", brothers)
# creating tuple for sisters
sisters =  ("Sita","Geetha")
print("sisters : ", sisters)

# creating siblings by adding brothers and sisters
siblings = brothers + sisters
print("siblings : ", siblings)

# length of siblings tuple
len_of_siblings = len(siblings)
print("length of siblings tuple", len_of_siblings)

# adding parents with siblings tuple creating new tuple
family_members = siblings + ("mahi","raji")
print("family members : ", family_members)

### Question 4
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# length of it_companies set
print("length of it_companies set : ", len(it_companies))
# adding company to it_company
it_companies.add("Twitter")
# removing company from it_company
it_companies.discard("Oracle")
print("it companies : ", it_companies)
print(""" remove vs discard : 
remove deletes the element from the list if not present it returns Key error, 
discard deleted the element from the list otherwise return None""")
# joining A and B sets
print("Join of A and B : ", A.union(B))
# intersection of A and B sets
print("Intersection of A and B : ",A.intersection(B))
# checking if A is subset of B
print("Is A subset of B : ", A.issubset(B))
# check if A is disjoint of B
print("Is A disjoint of B : ", A.isdisjoint(B))
# A union B and B union A
print("A union B : ", A.union(B))
print("B union A : ", B.union(A))
# symmetric difference between two sets
print("set A difference with set B : ",A.difference(B))
# deleting sets A and B
A.clear()
B.clear()
# converting age list to set
set_ages = set(age)
# comparing length of list and length of set
print("Is length of age list same of length of age set : ", len(age) == len(set_ages))


### Question 5
# The radius of a circle is 30 meters.
# radius r
r = 30
# pi value constant
pi = 3.14
# calculating area of circle
_area_of_circle_ =  pi * r * r
print("Area of circle :", _area_of_circle_)
# calculating cirumference of circle
_circum_of_circle_ = 2 * pi * r
print("Circumference of circle :", _circum_of_circle_)

# input from user
r = float(input("Enter radius of circle : "))
# calculating area of circle from user inputs
area_of_circle = pi * r * r
print("Area of circle : ", area_of_circle)

### Question 6

sentence = """I am a teacher and I love to inspire and teach people"""
# splitting sentence into words
split_sent = sentence.split()
print("words : ", split_sent)
# getting unique words using set
unique_words = set(split_sent)
print("unique words : ", unique_words)

### Question 7

# Use a tab escape sequence to get the following lines.
data = "Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki"
print(data)

### Question 8
radius = 10
area = 3.14 * radius ** 2
# print string using format
sent = "The area of a circle with radius {} is {} meters square.".format(radius, area)
print(sent)

### Question 9

# input number of students
N = int(input("Enter Number of students : "))
# lb to kg conversion value
lbs_to_kg_convertion_value = 0.4536
lbs_weights = []
kg_weights = []

# input all student weights input
for i in range(0,N):
    lbs_weights.append(int(input("Enter student Weight(lbs) : ")))

print("lbs_weights : ",lbs_weights)

# converted weights to kg
for weight in lbs_weights:
    kg_weights.append(round(weight * lbs_to_kg_convertion_value,2))

print("kg_weights : ", kg_weights)


### Question 10

X = [[1],[2],[3],[6],[6],[7],[10],[11]]
y = [0,0,1,1,1,0,0,0]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5)

from sklearn.neighbors import KNeighborsClassifier
N = 3
neigh = KNeighborsClassifier(n_neighbors=N)
neigh.fit(X_train, y_train)
y_pred = neigh.predict(X_test)

print("predicted values : ",y_pred)

from sklearn.metrics import confusion_matrix
tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()

"""
Sensitivity/recall – how good a test is at detecting the positives. A test can cheat and maximize this by always returning “positive”.
Specificity – how good a test is at avoiding false alarms. A test can cheat and maximize this by always returning “negative”.
"""
# Accuracy
Accuracy = (tp+tn)/len(y_test)
### sensitivity or recall
Sensitivity = tp/(tp+fn)
Specificity = tn/(fp+tn)

print("Accuracy : ", Accuracy)
print("Sensitivity : ", Sensitivity)
print("Specificity : ", Specificity)