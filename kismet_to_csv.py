# Author: AndyGitNix
# Version: 0.3

import os
import pandas as pd


os.chdir('/PATH/TO/DIRECTORY')                     # Path to where .kismet log-files are stored
number = 1
file_exists = True
csv_name = ''

files = os.listdir()
file_parts = []
for file in files:
    file_parts.append([os.path.splitext(file)[0], os.path.splitext(file)[1]])


# Begin the script. Ask for name of the final csv-file.

def main(file_parts):
    if len(file_parts) == 0:
        print('The folder has no files. Exiting...')
        quit()
    else:
        csv_name = input('Name the csv-file you want to export the kismet-files to:\n> ')
        if type(csv_name) != str:
            print('Name is not valid. Try again. Exiting...')
            quit()
        return csv_name


# Chekcs if folder has '.kismet-journal' files and cleans them if there is.

def clean_check(file_parts):
    for f_name, f_ext in file_parts:
        if f_ext == '.kismet-journal':
            clean_command = 'kismetdb_clean foo.kismet --in {}.kismet'.format(f_name)
            print('Cleaning file {}.kismet'.format(f_name) + ' with command: kismetdb_clean foo.kismet --in {}.kismet'.format(f_name))
            os.system(clean_command)


# Check if csv-files exist in destination folder and asks for input if files exist.

def csv_check(file_parts):

    for _, f_ext in file_parts:

        if f_ext == '.csv':
            csv_exists = input('There is previous .csv-files in your directory. They will be combined to the finished file.\nDo you want to continue anyway? Yes/No? [y/n] ')

            if csv_exists.lower().strip() != 'y':
                print('Exiting...')
                quit()
            break


# Run kismetdb_to_wiglecsv command

def to_csv(file_parts, file_exists, number, csv_name):

    for f_name, f_ext in file_parts:

        if f_ext == '.kismet':
            while (file_exists == True):
                if os.path.exists('{}%{}.csv'.format(csv_name, number)):
                    print('File named {}%{}.csv already exists. Renaming...'.format(csv_name, number))
                    number += 1
                else:
                    file_exists = False

            command = 'kismetdb_to_wiglecsv --in {}{} --out {}%{}.csv'.format(f_name, f_ext, csv_name, number)
            print('Executing command: ' + command)
            os.system(command)
            number += 1


# Combine the exported csv-files into one

def combine_csv(csv_name):

    print('Combining csv files...')

    header = "WigleWifi-1.4,appRelease=Kismet2024120,model=Kismet,release=2024.12.0.8,device=kismet,display=kismet,board=kismet,brand=kismet"

    dataframes = []

    for file in os.listdir(os.getcwd()):
        if file.endswith('.csv'):
            df = pd.read_csv(file, skiprows=1, header=0)
            dataframes.append(df)

    master_df = pd.concat(dataframes, ignore_index=True)

    master_df.to_csv(f'{csv_name}.csv', index=False)

    with open('{}.csv'.format(csv_name), 'r+') as file:
        content = file.read()
        file.seek(0, 0)
        file.write(f"{header}\n{content}")

    print(f"Combined CSV saved as {csv_name}.csv")


# Ask to remove excess csv-files that are created in the process.

def remove_csv():

    remove = input('Do you want to remove the excess csv-files? [y/n] ')

    if remove.lower().strip() == 'y':

        for file in os.listdir():
            f_name, f_ext = os.path.splitext(file)

            if '%' in f_name and f_ext == '.csv':
                print('File {}{} removed'.format(f_name, f_ext))
                os.remove(file)
            else:
                continue
        

if __name__ == '__main__':
    csv_name = main(file_parts)
    clean_check(file_parts)
    csv_check(file_parts)
    to_csv(file_parts, file_exists, number, csv_name)
    combine_csv(csv_name)
    remove_csv()