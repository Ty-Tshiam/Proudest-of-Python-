Course Grading

Student Performance Analysis Script
This Python script processes student information, exercise scores, and exam points to calculate total scores and assign grades. The results are saved in both .txt and .csv formats.

Features:
Data Processing: Reads and processes multiple input files containing student info, exercise completion, and exam scores.

Automated Grade Calculation: Computes total points by combining exercise and exam scores, and assigns grades based on predefined criteria.

File Output: Outputs the results in a structured .txt report and a .csv file for further analysis.

Technologies:
Python (file handling, data processing)
CSV and text file generation

Part 1:
This program works with two CSV files. One of them contains information about some students on a course:
id;first;last
12345678;peter;pythons
12345687;jean;javanese
12345699;alice;adder
The other contains the number of exercises each student has completed each week:
id;e1;e2;e3;e4;e5;e6;e7
12345678;4;1;1;4;5;2;4
12345687;3;5;3;1;5;4;6
12345699;10;2;2;7;10;2;2
As you can see above, both CSV files also have a header row, which tells you what each column contains.
Please write a program which asks the user for the names of these two files, reads the files, and then prints out the total number of exercises completed by each student. If the files have the contents in the examples above, the program should print out the following:
Sample output
Student information: students1.csv
Exercises completed: exercises1.csv
pekka peloton 21
jaana javanainen 27
liisa virtanen 35
Hint: while testing your program, you may quickly run out of patience if you always have to type in the file names at the prompt. You might want to hard-code the user input, like so:
if False:
    # this is never executed
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
else:
    # hard-coded input
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"
The actual functionality of the program is now "hidden" in the False branch of an if statement. It will never be executed.
Now, if you want to quickly verify the program works correctly also with user input, you can just replace False with True:

if True:
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
else:
    # now this is the False branch, and is never executed
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"
When you have verified your program works correctly, you can remove the if structure, keeping the commands asking for input.

Part 2:
Let's expand the program created in the previous exercise. Now also the exam points awarded to each student are contained in a CSV file. The contents of the file follow this format:
id;e1;e2;e3
12345678;4;1;4
12345687;3;5;3
12345699;10;2;2
In the above example the student whose student number is 12345678 was awarded 4+1+4 points in the exam, which equals a total of 9 points.
The program should again ask the user for the names of the files. Then the program should process the files and print out a grade for each student.
Sample output
Student information: students1.csv
Exercises completed: exercises1.csv
Exam points: exam_points1.csv
pekka peloton 0
jaana javanainen 1
liisa virtanen 3
Each completed exercise is counted towards exercise points, so that completing at least 10 % of the total exercices awards 1 point, completing at least 20 % awards 2 points, etc. Completing all 40 exercises awards 10 points. The number of points awarded is always an integer number.
The final grade for the course is determined based on the sum of exam and exercise points according to the following table:
exam points + exercise points
grade
0-14
0 (fail)
15-17
1
18-20
2
21-23
3
24-27
4
28-
5

Part 3:
This exercise will continue from the previous one. Now we shall print out some statistics based on the CSV files.
Sample output
Student information: students1.csv
Exercises completed: exercises1.csv
Exam points: exam_points1.csv
name                          exec_nbr  exec_pts. exm_pts.  tot_pts.  grade
pekka peloton                 21        5         9         14        0
jaana javanainen              27        6         11        17        1
liisa virtanen                35        8         14        22        3


Each row contains the information for a single student. The number of exercises completed, the number of exercise points awarded, the number of exam points awarded, the total number of points awarded, and the grade are all displayed in tidy columns. The width of the column for the name should be 30 characters, while the other columns should be 10 characters wide.
You might find the f-strings covered in part 4 useful here.
F-strings differentiate between strings and numbers when it comes to justifying columns:
word = "python"
print(f"{word:10}continues")
print(f"{word:>10}continues")
Sample output
python    continues
    pythoncontinues


As you can see above, by default strings are justified to the left edge of the area specified for them. The > symbol can be used to justify to the right edge.
With number values the logic is reversed:
number = 42
print(f"{number:10}continues")
print(f"{number:<10}continues")
Sample output
       42continues
42        continues


With numbers the default behaviour is to justify to the right edge. The symbol < can be used to justify to the left edge.

Part 4:
Let's revisit the course grading project from the previous section.
As we left if last time, the program read and processed files containing student information, completed exercises and exam results. We'll add a file containing information about the course. An example of the format of the file:
Sample data
name: Introduction to Programming
study credits: 5


The program should then create two files. There should be a file called results.txt with the following contents:
Sample data
Introduction to Programming, 5 credits
======================================
name                          exec_nbr  exec_pts. exm_pts.  tot_pts.  grade
pekka peloton                 21        5         9         14        0
jaana javanainen              27        6         11        17        1
liisa virtanen                35        8         14        22        3


The statistics section is identical to the results printed out in part 3 of the project. The only addition here is the header section.
Additionally, there should be a file called results.csv with the following format:
Sample data
12345678;pekka peloton;0
12345687;jaana javanainen;1
12345699;liisa virtanen;3


When the program is executed, it should look like this:
Sample output
Student information: students1.csv
Exercises completed: exercises1.csv
Exam points: exam_points1.csv
Course information: course1.txt
Results written to files results.txt and results.csv
That is, the program only asks for the names of the input files. All output should be written to the files. The user will only see a message confirming this.


