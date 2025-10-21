# Practice Question 1
# Store the following word meaning in a python dictionary
# "table" : "a piece of furnicture", "list of facts and figures" ,"cat" : "a small animal"

WordMeaning = {
    "table" : ["a piece of furnicture", "list of facts and figures"],
    "cat" : "a small animal"
}

print(WordMeaning)

# Practice Question 2 
# You are given a lsit of subjects for students.Assume one classroom is required for 1 subject.
#  How many class room are needed for all the students 

set = {"python","java","c++","python","javascript","java","python","java","c++","c"}

print(len(set))



# Practice Question 3
# WAP to enter the marks of 3 subjects from the user and store them in a dictionary. Start with an empty 
# dictionary & add one by one. Use subject name as key and marks as value

sample = {}

subject1 = input("Enter the mark Subject math: ")
sample.update({"math" : subject1})

subject2 = input("Enter the mark Subject chem: ")
sample.update({"chem" : subject2})

subject3 = input("Enter the mark Subject phy: ")
sample.update({"phy" : subject3})

print(sample)

# Practice Question 3
# Figure out a way to store 9 and 9.0 as separate values in the set 

values = {
    ("float",9.0),
    ("int",9)
}
print((values))





