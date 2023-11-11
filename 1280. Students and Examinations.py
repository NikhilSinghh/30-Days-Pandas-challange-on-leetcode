import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    two_df = students.merge(subjects, how='cross')
    
    exam_count = examinations.groupby(['student_id', 'subject_name']).agg(
        attended_exams=('subject_name', 'count')
    ).reset_index()
    
    all_df = two_df.merge(exam_count, on=['student_id','subject_name'], how='left').sort_values(by = ['student_id', 'subject_name'])
    return all_df.fillna(0)[['student_id', 'student_name', 'subject_name', 'attended_exams']]
    
