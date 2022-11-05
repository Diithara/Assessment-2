import csv                                       # importing csv module.

# Part a, calculating the average salary of a manager

file = open("employees.csv", "r")                # opening the employee csv file and reading it.

try:                                             # using try statement for further processing.
    csv_reader = csv.reader(file)                # reading the contents of csv file using the csv reader.
    total = 0                                    # creating a variable called total to calculate the total of salaries.
    i = 0                                        # creating a variable to repeat.
    for column in csv_reader:                    # using for loop to iterate columns in csv file.
        if column[3] == "Manager":               # using if statement to only select the managers from column[3].
            total += int(column[2])              # getting the total of salaries in column[2] with column[3] as Manager.
            i += 1                               # iterating the entries of column[2] with employee type as Manager.
    print("The average salary of managers is", int(total / i), "dollars.")  #printing the average salary of managers (as a integer to match the sample output) by dividing the total salary of managers by the number of managers

finally:                                         # using finally statement to close file.
    file.close()


# part b, getting the full name of the staff member who has the lowest salary

file = open("employees.csv", "r")                # opening the given csv file to read.

try:                                             # using try statement for further processing.
    csv_reader = csv.reader(file)                # reading the contents of csv file using the csv reader.
    row = 0                                      # creating variable for lower bound.
    lowest_value = int(column[2]) +1                       # creating variable to find lowest value.
    for column in csv_reader:                    # using for loop to iterate the columns in employee csv file.
        if row > 0 and int(column[2]) <= lowest_value:  # using if statement to compare the salaries in column[2], (row[1] vs row[2])
            lowest_value = int(column[2])       # using lowest value variable to find lowest salary in column[2].
            name = column[0] + " " + column[1]   # getting the first and last name from column[0] and column[1].
        row += 1                                 # iterating rows to find the lowest salary.
    print(name, "has the lowest salary ($",float(lowest_value),").")  #printing the full name and the salary (as a float to match sample output)of the lowest salary employee.

finally:                                         # using finally statement to close the csv file.
    file.close()
