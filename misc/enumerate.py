tasks = [
    'Write report', 
    'Attend meeting', 
    'Review code', 
    'Submit timesheet'
]

# The enumerate() function adds a counter to the iterable and returns it as an enumerate object
# It returns pairs of (index, element), where the index starts from 0 by default
# Here, we're using it to number the tasks as we loop through them
for index, task in enumerate(tasks):
    print(f'{index + 1}. {task}')

# Output:
# 1. Write report
# 2. Attend meeting
# 3. Review code
# 4. Submit timesheet
