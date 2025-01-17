# Kismet To Csv

This Python script is meant to be used with Kismet and its built-in tool kismetdb_to_wiglecsv to export .kismet-files to CSV format. Script will go through all the files in the directory and export the .kismet files as one single CSV file for further processing or for example uploading to wigle.net.

Requirements:
```
pip install pandas
```
Copy the Python script to your wardrivinig machine and name it accordingly.

Change the directory in the script to where you have your .kismet-files saved (absolute path):
```
os.chdir('/PATH/TO/DIRECTORY')
```

Give the script rights to execute
```
sudo chmod +x kismet_to_csv.py
```

Run the code with:
```
python3 kismet_to_csv.py
```

Links:
- https://www.kismetwireless.net/
- https://github.com/kismetwireless
- https://wigle.net
