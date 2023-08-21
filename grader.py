import os
import driver
import assignment_maps
import students

# select assignment
print("Please select an assignment from the list to grade.")

# # Get directory of HTML files
directory = input('Please enter the directory of the assignment: ')

results = []
for file in os.listdir(directory):
    print(file)
    grade = driver.validateTags(assignment_maps.heading_element, directory + "\\" + file)
    name = file.split("_")[0]
    results.append((name, grade[0], grade[1]))

driver.goToCanvas(results)
