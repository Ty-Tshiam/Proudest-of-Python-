studentFile = input('Studnent information: ')
exerciseFile = input('Exercises completed: ')
examFile = input('Exam points: ')
courseFile = input('Course Information: ')

with open(studentFile) as file:
    studentInfo = {}
    for line in file:
        fileInfo = []
        line = line.strip()
        fileInfo = line.split(';')
        if fileInfo[0] == 'id':
            continue
        studentInfo[fileInfo[0]] = f'{fileInfo[1]} {fileInfo[2]}'

with open(exerciseFile) as file:
    exercises = {}
    for line in file:
        fileInfo = []
        line = line.strip()
        fileInfo = line.split(';')
        if fileInfo[0] == 'id':
            continue
        sum = 0
        for num in range(1, 8):
            sum += int(fileInfo[num])
        exercises[fileInfo[0]] = sum

with open(examFile) as file:
    examPoints = {}
    for line in file:
        fileInfo = []
        line = line.strip()
        fileInfo = line.split(';')
        if fileInfo[0] == 'id':
            continue
        sum = 0
        for num in range(1, 4):
            sum += int(fileInfo[num])
        examPoints[fileInfo[0]] = sum

with open(courseFile) as file:
    courseInfo = []
    for line in file:
        info = line.split(':')
        courseInfo.append(info[1])
        
with open('results.txt', 'w') as file:
    grades = {}
    string = f'{courseInfo[0].strip()}, {courseInfo[1].strip()} credits\n'
    file.write(string)
    file.write('='*(len(string) - 1) +'\n')
    file.write(f'{'name':30}' + f'{'exec_nbr':10}' + f'{'exec_pts.':10}' + f'{'exm_pts.':10}' + f'{'tot_pts.':10}' + f'{'grade':10}\n')
    for id, exPoints in exercises.items():
        addPoints = int((exPoints / 40) * 10)
        points = examPoints[id] + addPoints
        grade = -1
        if points >= 0 and points <= 14:
            grade = 0
        elif points >= 15 and points <= 17:
            grade = 1
        elif points >= 18 and points <= 20:
            grade = 2
        elif points >= 21 and points <= 23:
            grade = 3
        elif points >= 24 and points <= 27:
            grade = 4
        elif points >= 28:
            grade = 5 
        grades[id] = grade
        file.write(f'{studentInfo[id]:30}' + f'{exPoints:<10}' + f'{addPoints:<10}' + f'{examPoints[id]:<10}' + f'{points:<10}' + f'{grade:<10}\n')

with open('results.csv', 'w') as file:
    for id in studentInfo:
        file.write(f'{id};{studentInfo[id]};{grades[id]}\n')

print('Results written to files results.txt and results.csv')