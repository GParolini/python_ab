#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 12:42:19 2019

@author: giudittaparolini
"""

stud_name = input("Enter the student name:")
m_grade = int(input("Enter the grade achieved by the student in the mathematics exam:"))

p_grade = int(input("Enter the grade achieved by the student in the physics exam:"))

c_grade = int(input("Enter the grade achieved by the student in the chemistry exam:"))


grades = [m_grade, p_grade, c_grade]

worse =min(grades)

average = (m_grade + p_grade + c_grade)/3

    
if worse < 35:
    print (stud_name, "Exam failed")

elif average <= 59:
    print (stud_name, "Exam passed Grade C")
    
elif average <= 69:
    print (stud_name, "Exam passed Grade B") 

else:
    print (stud_name, "Exam passed Grade A")
    

