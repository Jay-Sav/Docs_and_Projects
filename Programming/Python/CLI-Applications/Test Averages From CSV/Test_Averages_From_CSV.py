# Variable Declaration. 
file_name = input()
output_file = 'report.csv'
nested_list = []
midterm1 = 0
midterm2 = 0
final = 0
student_average = 0
number_of_scores = 0

      
      
#Read CSV File Here. 
with open(file_name) as open_file:
    file_content = open_file.readlines()
    for line in file_content:
        line = line.split(',')
        nested_list.append(line)
   
   
#Compute student grades and exam averages, then output results to CSV file here. 
with open(output_file,'w') as file_output:
    file_output.write(f'First Name, Last Name, Mid Term Score 1, Mid Term Score 2, Mid Term Score 3, Grade Letter, Student Average\n')
    for student in nested_list:
        first_name, last_name = student[0:2]
        value1, value2, value3= map(int,student[2:5])
        midterm1 += value1
        midterm2 += value2
        final += value3
        number_of_scores +=1
        student_average = (value1 + value2 + value3) / 3
        if student_average >= 90:
            grade_letter = 'A'
        elif student_average >= 80 and student_average < 90:
            grade_letter = 'B'
        elif student_average >= 70 and student_average < 80:
            grade_letter = 'C'
        elif student_average >= 60 and student_average < 70:
            grade_letter = 'D'
        else:
            grade_letter = 'F'

        file_output.write(f'{first_name},{last_name},{value1},{value2},{value3},{grade_letter},{student_average:.2f}\n')

    midterm1 = f'{midterm1 / number_of_scores:.2f}'
    midterm2 = f'{midterm2 / number_of_scores:.2f}'
    final = f'{final / number_of_scores:.2f}'
    file_output.write(f'\n')
    file_output.write(f'Class Averages:, Mid Term 1:{midterm1}, Mid Term 2: {midterm2}, Final: {final}')
    file_output.write(f'\n')




    