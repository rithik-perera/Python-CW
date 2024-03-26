
# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution. 
# Student ID: 20222011
# UoW ID: w1985685
# Date: 18/4/2023

progress = 0
trailer = 0
retriever = 0
excluded = 0
no_students = 0
version = ""
total_list = ""
total_dictionary = {}

while version != str(1) and version != str(2):
    version = input("Enter 1 if you are a student and 2 if you are a staff member: ")
    if version != "1" and version != "2":
        print("please enter either 1 or 2")
student_version = False
staff_version = False
if version == "1":
    student_version = True
elif version == "2":
    staff_version = True
    
def output(p_credit, d_credit, f_credit):
    """ This function provides what the student is supposed to meet next""" 
    if p_credit == 120:
        return("Progress")
    elif p_credit == 100:
        return("Progress (module trailer)")
    elif (p_credit + d_credit) >= f_credit:
        return("Do not progress – module retriever")
    else:
        return("Exclude")
    

accepted_values = (0, 20, 40, 60, 80, 100, 120)
proceed = True

def output_list(result, p_credit, d_credit, f_credit):
    """ converts the output result into a list """
    return(["" + str(result) + " - " + str(p_credit) + ", " + str(d_credit) + ", " + str(f_credit) + ""])


while True:
    try:
        proceed = True
        student_id = input("Enter student id: ")
        p_credit = int(input("Please enter your credits at pass: "))
        if p_credit not in accepted_values:
            print("Out of range")
            proceed = False
            continue
        d_credit = int(input("Please enter your credits at defer: "))
        if d_credit not in accepted_values:
            print("Out of range")
            proceed = False
            continue
        f_credit = int(input("Please enter your credits at fail: "))
        if f_credit not in accepted_values:
            print("Out of range")
            proceed = False
            continue
        if (p_credit + d_credit + f_credit) != 120:
            print("Total incorrect")
            proceed = False
            continue
        if staff_version == True:
            print(output(p_credit, d_credit, f_credit))
            if output(p_credit, d_credit, f_credit) == "Progress":
                progress += 1
                total_list = total_list + (" ".join(output_list("progress", p_credit, d_credit, f_credit)) + "\n") #Reference - https://www.programiz.com/python-programming/methods/string/join
                total_dictionary[student_id] = (" ".join(output_list("progress", p_credit, d_credit, f_credit)))
            elif output(p_credit, d_credit, f_credit) == "Progress (module trailer)":
                trailer += 1
                total_list = total_list + (" ".join(output_list("module trailer", p_credit, d_credit, f_credit)) + "\n")
                total_dictionary[student_id] = (" ".join(output_list("module trailer", p_credit, d_credit, f_credit)))
            elif output(p_credit, d_credit, f_credit) == "Do not progress – module retriever":
                retriever += 1
                total_list = total_list + (" ".join(output_list("module retriever", p_credit, d_credit, f_credit)) + "\n")
                total_dictionary[student_id] = (" ".join(output_list("module trailer", p_credit, d_credit, f_credit)))
            elif output(p_credit, d_credit, f_credit) == "Exclude":
                excluded += 1
                total_list = total_list + (" ".join(output_list("Exclude", p_credit, d_credit, f_credit)) + "\n")
                total_dictionary[student_id] = (" ".join(output_list("Exclude", p_credit, d_credit, f_credit)))
            if proceed == True:
                no_students += 1
            print("Would you like to enter another set of data? ")
            con = ""
            while con != "y" and con != "q":
                con = input("Enter 'y' for yes or 'q' to quit and view results: ")
                if con != "y" and con != "q":
                    print("Please enter either y or q")
            if con == "q":
                break
            elif con == "y":
                continue
           
        else:
            print(output(p_credit, d_credit, f_credit))
            break
    except ValueError:
        print("Intiger required")


print(total_dictionary)    

        
    
            
        
        
    
