
####  this will change the Instance only queries into create table statements
####  need seperate script for databases


import os

folder_path = '/Users/argaither/Documents/Diag/TestScripts'  # replace with the path to your folder
search_string = 'FROM'  # replace with the string you want to search



# loop through all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.sql'):  # process only text files
        file_path = os.path.join(folder_path, filename)
        with open(file_path, 'r') as file:
            file_content = file.read()
        
        # remove spaces from filename
        new_filename = filename.replace(' ', '')
        # only needed for database scripts # new_filename = new_filename.replace('-', '')
        new_filename = os.path.splitext(new_filename)[0]  # remove .sql extension
        replace_string = ' into ' + new_filename + ' FROM '
     #   replacement_string = ' into {new_filename} from '  # the replacement string with the filename
        
        # replace the string with the new filename
        new_content = file_content.replace(search_string, replace_string)
        
        # write the new content back to the file
        with open(file_path, 'w') as file:
            file.write(new_content)
