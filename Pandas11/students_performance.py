import pandas as pd
from IPython.display import display
stud_perf=pd.read_csv('Pandas11/students_performance.csv', sep = ',')
display(stud_perf.info())
print(stud_perf.iloc[155, 7])
print(round(stud_perf['math score'].mean()))
display(stud_perf['race/ethnicity'].mode())
aver_read = stud_perf[stud_perf['test preparation course'] == "completed"]['reading score'].mean()
print(round(aver_read))
zero_math = stud_perf[stud_perf['math score'] == 0].shape[0]
print(zero_math)
group_food = stud_perf[stud_perf['lunch'] == 'standard']['math score'].mean()
group_starve = stud_perf[stud_perf['lunch'] == 'free/reduced']['math score'].mean()
print(round(group_food), round(group_starve))
display(stud_perf['parental level of education'].value_counts(normalize = True))
group_A = stud_perf[stud_perf['race/ethnicity'] == 'group A']['writing score'].median()
group_C = stud_perf[stud_perf['race/ethnicity'] == 'group C']['writing score'].mean()
print(round(abs(group_A - group_C)))
