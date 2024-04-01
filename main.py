# Built-in imports
import math

# Part 1
GRADE = {}
for i in range(1, 101):
  if i >= 70:
    GRADE[i] = "A"
  if 70 > i >= 60:
    GRADE[i] = "B"
  if 60 > i >= 55:
    GRADE[i] = "C"
  if 55 > i >= 50:
    GRADE[i] = "D"
  if 50 > i >= 45:
    GRADE[i] = "E"
  if 45 > i >= 40:
    GRADE[i] = "S"
  if i < 40:
    GRADE[i] = "U"



# Part 2
def read_testscores(filename):
  """
  determine grade of each student

  Parenthesis
  ------------
  filename: str
    name of file


  Returns
  --------
  list
    list of dicts, each dict representing row data for a single student
  """
  # classes = []
  # names = []
  # overalls = []
  # grades = []
  data = []

  with open(filename, 'r') as f:
    header = f.readline().split(',')
    for line in f:
      list_dict = {}
      line = line.split(',')
      class_ = line[0]
      name_ = line[1]
      p1 = int(line[2])
      p2 = int(line[3])
      p3 = int(line[4])
      p4 = int(line[5])
      overall_ = (p1 / 30 * 15) + (p2 / 40 * 30) + (p3 / 80 * 35) + (p4 / 30 *
                                                                     20)
      overall_ = math.ceil(overall_)
      grade_ = GRADE[overall_]
      list_dict['class'] = class_
      list_dict['name'] = name_
      list_dict['overall'] = overall_
      list_dict['grade'] = grade_
      data.append(list_dict)
  return data


# Part 3
def analyze_grades(studentdata):
  """
  returns a dict representing the count of each grade for each class

  Parenthesis
  ------------
  student data
    grades and class of student

  Returns
  -------
  int
    number of students in that class in that grade
  """
  analysis = {}
  GRADINGS = ['A', 'B', 'C', 'D', 'E', 'S', 'U']
  for i in range(18):
    class_grade = [0]*7 # 1 value for each grade
    for m in studentdata:  
      if m ["class"] == f'Class{i+1}': 
        # add 1 to the respective grade, GRADINGS.KEY[] is which [0](tied to a grade) to add +1 into. create keys and values, key = grade, value = num
        class_grade[GRADINGS.index(m["grade"])] += 1
    # put dict of grades as a value and link it to a key(ie class)
    analysis[f'Class{i+1}'] = {}
    # for every grade
    for x in range(7):
      analysis[f'Class{i+1}'][GRADINGS[x]] = class_grade[x]  # class_grade is list of num
  return analysis
  # { {class1: {"A": 2, "B", 3} {class2: {"A": 3, "B", 7} }


print(GRADE[48])
lists_dicts = read_testscores('testscores.csv')
print(lists_dicts)
analysis = analyze_grades(lists_dicts)
print(analysis['Class18']['U'])



