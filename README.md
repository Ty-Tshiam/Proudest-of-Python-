# Student Grades Processing Program

## Overview
This program processes student data, including personal information, completed exercises, exam points, and course information, to calculate final grades and save them to text and CSV files. The program reads data from multiple input files and outputs formatted grade information for each student in both `results.txt` and `results.csv`.

## How It Works
1. **Input Files**: The program reads four files provided by the user:
   - **Student Information**: Contains student IDs and names.
   - **Exercises Completed**: Contains the number of exercises completed by each student.
   - **Exam Points**: Contains exam scores for each student.
   - **Course Information**: Contains course details, including the course name and credits.

2. **Processing**:
   - Each file is read and stored in a dictionary or list for efficient data manipulation.
   - The program calculates exercise points by summing the exercises completed.
   - Exam points are summed up for each student.
   - The total grade is calculated based on a weighted combination of exercise and exam points.

3. **Output**:
   - **results.txt**: A formatted text file listing student names, exercise counts, points, exam points, total points, and final grades.
   - **results.csv**: A CSV file containing student IDs, names, and final grades.

## Grading Criteria
The grading is based on the following point scale:
- 0-14: Grade 0
- 15-17: Grade 1
- 18-20: Grade 2
- 21-23: Grade 3
- 24-27: Grade 4
- 28+: Grade 5

## Usage
1. Run the program.
2. When prompted, enter the file names for the student, exercise, exam, and course information files.
3. The program will generate `results.txt` and `results.csv` files in the working directory.

## Example Output
**results.txt**:
```
Course Name, X credits
===============================================
name                           exec_nbr   exec_pts.  exm_pts.   tot_pts.   grade     
John Doe                       35         8          12         20         2
Jane Smith                     40         10         15         25         4
```

**results.csv**:
```
id;name;grade
123;John Doe;2
456;Jane Smith;4
```

## Requirements
- Python 3.x

