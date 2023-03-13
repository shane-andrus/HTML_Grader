import os
import logging
from bs4 import BeautifulSoup


# Get directory of HTML files
directory = input('Please enter the directory of HTML files: ')

report_file_location = input("Please enter the directory where you would like to have the report file: ")
report_file_name = input("Please enter the name of the file (do not add file extension): ")
# Create a report file
report_file = open(report_file_location + "/" + report_file_name + ".csv", 'w')

# Set up logging
logging.basicConfig(filename=report_file_location + "/" + report_file_name + "_logging.log", level=logging.INFO)

# Create a dictionary of tags to check
tags_to_check = {}
while True:
    tag = input('Please enter a tag to check (or enter "done" to finish): ')
    if tag == 'done':
        break
    else:
        num_times = int(input('Please enter the number of times this tag should be present: '))
        tags_to_check[tag] = num_times

report_file.write('%s,%s\n' % ("Name", ','.join([str(tag) for tag in tags_to_check])))

# Create a list of HTML files
html_files = []
for file in os.listdir(directory):
    if file.endswith('.html'):
        html_files.append(file)
    else:
        logging.error("File is not an html file: " + file)
        # Write the results to the report file
        report_file.write('%s,%s\n' % (file.split("_")[0] , ','.join([str(tag_counts[tag]) for tag in []])))

# Iterate through HTML files
for file in html_files:
    # Open HTML file
    try:
        with open(os.path.join(directory, file)) as f:
            html = f.read()
    except UnicodeDecodeError:
        print("There was an error reading from " + f.name + ".")
            # Log the results
        logging.info('File: %s, Tag counts: %s', file, tag_counts)
        # Write the results to the report file
        report_file.write('%s,%s\n' % (file.split("_")[0], ','.join([str(tag_counts[tag]) for tag in tags_to_check])))
        continue

    # Parse HTML file
    soup = BeautifulSoup(html, 'html.parser')
    # Create a dictionary to store tag counts
    tag_counts = {}
    # Iterate through tags to check
    for tag in tags_to_check:
        # Count the number of times the tag appears
        count = len(soup.find_all(tag))
        # Store the count in the dictionary
        tag_counts[tag] = count
    # Log the results
    logging.info('File: %s, Tag counts: %s', file, tag_counts)
    # Write the results to the report file
    report_file.write('%s,%s\n' % (file.split("_")[0], ','.join([str(tag_counts[tag]) for tag in tags_to_check])))

# Close the report file
report_file.close()