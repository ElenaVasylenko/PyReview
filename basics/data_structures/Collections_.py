from collections import deque, namedtuple

# Queue
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
queue.popleft()             # The first to arrive now leaves

# Named tuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(11, y=22)
t = [11, 22]
Point._make(t) # Class method that makes a new instance from an existing sequence or iterable.
## Point(x=11, y=22)
p = Point(x=11, y=22)
p._asdict()
## {'x': 11, 'y': 22}
EmployeeRecord = namedtuple('EmployeeRecord', 'name, age, title, department, paygrade')
import csv
for emp in map(EmployeeRecord._make, csv.reader(open("employees.csv", "rb"))):
    print(emp.name, emp.title)

# import sqlite3
# conn = sqlite3.connect('/companydata')
# cursor = conn.cursor()
# cursor.execute('SELECT name, age, title, department, paygrade FROM employees')
# for emp in map(EmployeeRecord._make, cursor.fetchall()):
#     print(emp.name, emp.title)
