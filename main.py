import json
import os

from numpy import average


NUM_STUDENTS = 1000
SUBJECTS = ["math", "science", "history", "english", "geography"]


def load_report_card(directory, student_number):
    base_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(directory, f"{student_number}.json")
    path = os.path.join(base_path, file_path)

    try:
        with open(path, "r") as file:
            report_card = json.load(file)
    except FileNotFoundError:
        return {}

    return report_card

report_card_folder = 'students'
report_cards = [load_report_card(report_card_folder, i) for i in range(NUM_STUDENTS)]

def get_average_student_mark():
    return round(average([report_card[subject] for report_card in report_cards for subject in SUBJECTS]), 2)

def get_subject_average_marks():
    subject_average_marks = [(subject, average([report_card[subject] for report_card in report_cards])) for subject in SUBJECTS]
    subject_average_marks.sort(key=lambda x: x[1], reverse=True)
    return subject_average_marks

def get_hardest_subject():
    subject_average_marks = get_subject_average_marks()
    return subject_average_marks[-1][0]

def get_easiest_subject():
    subject_average_marks = get_subject_average_marks()
    return subject_average_marks[0][0]

def get_grade_average_marks():
    grade_marks = {grade: {'marks_sum': 0, 'marks_count': 0} for grade in range(1, 9)}
    for report_card in report_cards:
        grade_marks[report_card['grade']]['marks_sum'] += average([report_card[subject] for subject in SUBJECTS])
        grade_marks[report_card['grade']]['marks_count'] += 1
    grade_average_marks = []
    for grade in range(1, 9):
        grade_marks[grade]['average_mark'] = grade_marks[grade]['marks_sum'] / grade_marks[grade]['marks_count']
        grade_average_marks.append((grade, grade_marks[grade]['average_mark']))
    grade_average_marks.sort(key=lambda x: x[1], reverse=True)
    return grade_average_marks

def get_best_performing_grade():
    grade_average_marks = get_grade_average_marks()
    return grade_average_marks[0][0]

def get_worst_performing_grade():
    grade_average_marks = get_grade_average_marks()
    return grade_average_marks[-1][0]

def get_student_average_marks():
    student_average_marks = [(report_card['id'], average([report_card[subject] for subject in SUBJECTS])) for report_card in report_cards]
    student_average_marks.sort(key=lambda x: x[1], reverse=True)
    return student_average_marks

def get_best_student_id():
    student_average_marks = get_student_average_marks()
    return student_average_marks[0][0]

def get_worst_student_id():
    student_average_marks = get_student_average_marks()
    return student_average_marks[-1][0]

def produce_summary():
    output = f'Average Student Mark: {get_average_student_mark()}\n'
    output += f'Hardest Subject: {get_hardest_subject()}\n'
    output += f'Easiest Subject: {get_easiest_subject()}\n'
    output += f'Best Performing Grade: {get_best_performing_grade()}\n'
    output += f'Worst Performing Grade: {get_worst_performing_grade()}\n'
    output += f'Best Student ID: {get_best_student_id()}\n'
    output += f'Worst Student ID: {get_worst_student_id()}'
    print(output)

produce_summary()
