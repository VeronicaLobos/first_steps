def calculate_average_grades(list_students):  # *bonus 1*
    """
    sums values across the dictionaries in a list and
    calculates their averages, returns "a tuple"
    """
    sum_english_grades = 0
    sum_math_grades = 0
    sum_average_grades = 0
    count_english_students = 0 # "Calculate the sum of grades and count of students per subject (English and Math)"
    count_math_students = 0 # len() or a single count+=1 should work but ok

    for student_info in list_students:
        sum_english_grades += student_info["english_grade"]
        sum_math_grades += student_info["math_grade"]
        sum_average_grades += (student_info["english_grade"] + student_info["math_grade"]) / 2
        count_english_students += 1
        count_math_students += 1

    avg_grade_english = sum_english_grades / count_english_students
    avg_grade_math = sum_math_grades / count_math_students
    overall_average = sum_average_grades / len(list_students)
    return (("English", avg_grade_english), ("Math", avg_grade_math)), overall_average
    # "Return a tuple containing the average grades per subject and the overall average grade."
    # and 'a tuple' I did return


def calculate_failing_grades(students): # *bonus 2*
    """
    Returns: 1. a dictionary where each key is the student’s
    name and the value is the count of failing grades; 2. the
    total number of failing grades across all students and all subjects.
    """
    failed_grades_per_student = []
    failed_grades_by_student = 0
    total_failed_grades = 0

    for student in students:
        eng_grade = int(student["english_grade"] * 10)
        math_grade = int(student["math_grade"] * 10)
        student_fails_english = eng_grade <= 55
        student_fails_math = math_grade <= 55

        if student_fails_english and student_fails_math:
            failed_grades_by_student += 2
            total_failed_grades += 2
        elif student_fails_english or student_fails_math:
            failed_grades_by_student += 1
            total_failed_grades += 1

        failed_student = student["student_name"], failed_grades_by_student
        failed_grades_per_student.append(failed_student)
        failed_grades_by_student = 0 # reset for next student in loop

    failed_grades_per_student_dict = dict(failed_grades_per_student)
    return failed_grades_per_student_dict, total_failed_grades

""" ^^^ bonus functions ^^^ """


def get_grade(subject):
    """
    requests an int from the user and returns a float,
    if input is a non-numeric value, returns prompt until
    correct input
    """
    while True:
        try:
            subject_grade = input(f'Enter {subject} grade: ')
            if int(subject_grade) <= 10:
                return float(subject_grade)
        except ValueError as e:
            print("Error! Please input integer value", e)


def get_student_info():
    """
    requests data from the user, compiles a dictionary
    from it and returns it
    """
    student_keys = ["student_name", "english_grade", "math_grade"]
    student_values = [input("Enter student's name: "), get_grade("English"), get_grade("Math")]
    student_info = dict(zip(student_keys, student_values))
    return student_info


def print_student_info(list_students):
    """
    prints a string generated after calculating max
    grade and average grade for each dictionary in the list
    """
    for student_info in list_students:
        best_grade = max(student_info["english_grade"], student_info["math_grade"])
        avg_grade = (student_info["english_grade"] + student_info["math_grade"]) / 2
        print(f'{student_info["student_name"]}, Best Grade: {best_grade}, Average Grade: {avg_grade}')


def main():
    """
    requests data from the user to create a dictionary,
    prints the data and information calculated from the data
    such as student name, student max grade and average grades
    for student, subject and overall students
    """
    # Step1. Make list of dictionaries
    students = []
    for i in range(int(input("Enter number of students: "))):
        students.append(get_student_info())

    # Step 2. Print student info
    print()
    print("*** STUDENT GRADES' INFO ***")
    print("––––––––––––––––––––––––––––")
    print("  *  Student best and average grades: ")
    print_student_info(students)
    average_grades_per_subject, overall_average_grade = calculate_average_grades(students)

    # Step 3. Bonus 1. Calculate average grades per subject and average
    print("––––––––––––––––––––––––––––")
    print("  *  Average grades per subject:")
    for subject, average_grade in average_grades_per_subject:
        print(f"{subject}: {average_grade:.2f}")
    print(f"Overall average grade across all subjects: {overall_average_grade}")

    # Step 4.  Bonus 2. Identify and display students with failed grades and the overall failed grades
    print("––––––––––––––––––––––––––––")
    print(f'  *  Failing grades per student:')
    failed_grades_per_student_dict, total_failed_grades = calculate_failing_grades(students)
    for student, failed_grades in failed_grades_per_student_dict.items():
        print(f'{student}: {failed_grades} failing grade(s)')
    print(f'Total number of failing grades across all students: {total_failed_grades}')
    print("––––––––––––––––––––––––––––")


if __name__ == "__main__":
    main()
