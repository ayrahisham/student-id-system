# Assignment 3
# subject code : CSIT110
# name : Nur Suhaira
# student number : 5841549
# date : 21/10/2018

partition =  "------------------------------------------------------------------------------------------"
# Question 1 (20 marks)
# Write a function isValidStudentIDFormat
# that takes in a student ID, and apply the following rules
# to check whether it has a valid format.
#The valid format is SNNNNNNNL where 
#  S represents the letter S
#  N represents an integer and 
#  L represents a letter (B to M).

def isValidStudentIDFormat (ok, sid) :
    reason = " "
    # Has a length of 9. 
    if (len (sid) == 9) :
        # Starts with a letter 'S' and ends with a letter.
        if (sid[0] == 'S') :
            if (sid[len (sid)-1].isalpha()) :
                #Contains 7 numbers between the two letters.
                for i in range (1, len (sid)-1) :
                    if (not sid [i].isdigit()) :
                        reason = "Must contain 7 numbers"
                        return ok, reason
                ok = True
                reason = "Valid student ID"
                return ok, reason
            else :
                reason = "Invalid last letter"
        else :
            reason  = "Must start with a letter \"S\""
    else :
        reason = "Length is not 9"
        
    return ok, reason

# The function returns a True if the format is right,
# else it returns the invalid reason.
ok = False
while (ok == False) :
    studentid = input ("Enter student ID: ")
    ok, reason = isValidStudentIDFormat (ok, studentid)
    print (reason)

print (partition)

# Question 2 (30 marks)
# Write a function isValidStudentIDLetter
# to check the last letter of the student ID is valid.
# The function assume that the student id is in valid format.
# Apply the following rules in sequence to check the last letter.

# 0	B
# 1	C
# 2	D
# 3	E
# 4	F
# 5	G
# 6	H
# 7	I
# 20	J
# 9	K
# 10	L

# The function returns a True if the format is right,
# else it returns False.

# For example S1012342D and S1014322H is valid.
# S1023456I is invalid as the last letter should be H.

# Match the remainder with the letter in the table.

def matchletter (rnum) :
    if (rnum == 0) :
        letter = 'B'
    elif (rnum == 1) :
        letter = 'C'
    elif (rnum == 2) :
        letter = 'D'
    elif (rnum == 3) :
        letter = 'E'
    elif (rnum == 4) :
        letter = 'F'
    elif (rnum == 5) :
        letter ='G'
    elif (rnum == 6) :
        letter = 'H'
    elif (rnum == 7) :
        letter = 'I'
    elif (rnum == 20) :
        letter = 'J'
    elif (rnum == 9) :
        letter = 'K'
    elif (rnum == 10) :
        letter = 'L'
    else :
        letter = "NULL"
    return letter

def isValidStudentIDLetter (sid) :
    letterok = False
    # Multiply each of the numbers with 2, 7, 6, 5, 4, 3, 2
    # in sequence.
    total = 0
    one = int (sid [1]) * 2
    two = int (sid [2]) * 7
    three = int (sid [3]) * 6
    four = (int (sid [4])) * 5
    five = int (sid [5]) * 4
    six = int (sid [6]) * 3
    seven = int (sid [7]) * 2
    
    # Sum up the multiplication results
    total =  one + two + three + four + five + six + seven 
    # Divide the sum by 11 and get the remainder
    remainder = total % 11

    alpha = matchletter (remainder)
    if (not alpha == "NULL") :
        if (sid [len (sid) - 1] == alpha) :
            letterok = True
            
    return letterok, alpha

ok = False
while (ok == False) :
    studentid = input ("Enter student ID: ")
    ok, reason = isValidStudentIDFormat (ok, studentid)
    print (reason)

valid, alpha = isValidStudentIDLetter (studentid)

if (valid == True) :
    print ("{0} is valid".format (studentid))
else :
    print ("{0} is invalid as the last letter should be {1}".
           format (studentid, alpha))
    
print (partition)

# Question 3 (30 marks)
# Write a program to read in a data.csv file and list the down
# the student ID that is invalid.
# The program should print the student name, ID and
# the reason for being invalid.
# Below is a sample output:
# First Name     Last Name      Student ID     Comments       
# CFN            CLN            S1023456I      Invalid last letter
# DFN            DLN            S123A          Length of Student ID is not 9

import csv
filePath = "data.csv"

fname = "First Name"
lname = "Last Name"
sid = "Student ID"
comments = "Comments"
ok = False

with open(filePath) as csvfile:
    reader = csv.DictReader(csvfile)    
    print ("{0:<20} | {1:<20} | {2:<20} | {3:<20}".format (fname, lname, sid, comments))
    for row in reader:
        ok = False
        studentid = row ['student_id']
        ok, reason = isValidStudentIDFormat (ok, studentid)
        if (ok == False) :
            fn = row ['first_name']
            ln = row ['last_name']
            rule = row ['Rule to test']
            print ("{0:<20} | {1:<20} | {2:<20} | {3:<20}".format (fn, ln, studentid, rule))
        else :
            valid, alpha = isValidStudentIDLetter (studentid)
            fn = row ['first_name']
            ln = row ['last_name']
            rule = row ['Rule to test']
            print ("{0:<20} | {1:<20} | {2:<20} | {3:<20}".format (fn, ln, studentid, rule))
    
print (partition)

# Question 4 (20 marks)
# State the Student IDs that you have used to test your program,
# the rule to test and the expected output in the data.csv file.
# (See the data.csv for examples.)
