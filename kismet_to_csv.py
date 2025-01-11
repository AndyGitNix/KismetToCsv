# Author: AndyGitNix
# Version: 0.1

import os

os.chdir('PATH/TO/DIRECTORY')
number = 1
file_exists = True
csv_name = ''

files = os.listdir()
file_parts = []
for file in files:
    file_parts.append([os.path.splitext(file)[0], os.path.splitext(file)[1]])

def main(file_parts):
    if len(file_parts) == 0:
        print('The folder has no files. Exiting...')
        quit()
    else:
        csv_name = input('Name the csv-file you want to export the kismet-files to:\n> ')
        if type(csv_name) != str:
            print('Name is not valid. Try again')
            quit()
        return csv_name

def csv_check(file_parts):

    for _, f_ext in file_parts:

        if f_ext == '.csv':
            csv_exists = input('There is previous .csv-files in your directory. Do you want to continue anyway? Yes/No? [y/n] ')

            if csv_exists.lower().strip() != 'y':
                quit()
            break

def to_csv(file_parts, file_exists, number, csv_name):

    for f_name, f_ext in file_parts:

        if f_ext == '.kismet':
            while (file_exists == True):
                if os.path.exists('{}{}.csv'.format(csv_name, number)):
                    print('File named {}{}.csv already exists. Renaming...'.format(csv_name, number))
                    number += 1
                else:
                    file_exists = False

            command = 'kismetdb_to_wiglecsv --in "{}{}" --out "{}{}.csv"'.format(f_name, f_ext, csv_name, number)
            print('Executing command: ' + command)
            os.system(command)
            number += 1

if __name__ == '__main__':
    csv_name = main(file_parts)
    csv_check(file_parts)
    to_csv(file_parts, file_exists, number, csv_name)