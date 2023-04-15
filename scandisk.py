#edited jj
import os
import zipfile
import datetime
from prettytable import PrettyTable

# function to display available drives
def display_available_drives():
    drives = ['%s:' % d for d in range(1, 27) if os.path.exists('%s:' % d)]
    print("Available drives: ", drives)
    return drives

# function to select a drive to scan
def select_drive(drives):
    while True:
        drive = input("Enter drive letter to scan (e.g. C): ").upper()
        if drive in drives:
            return drive
        else:
            print("Invalid drive letter. Please select from available drives.")

# function to scan drive and find top 10 files by size
def scan_drive(drive):
    file_sizes = []
    for root, dirs, files in os.walk(drive):
        for file in files:
            # ignore zipped or compressed files
            if not zipfile.is_zipfile(os.path.join(root, file)):
                file_path = os.path.join(root, file)
                file_size = os.path.getsize(file_path)
                file_sizes.append((file_path, file_size))

    top_10_files = sorted(file_sizes, key=lambda x: x[1], reverse=True)[:10]
    return top_10_files

# function to display results in a table
def display_results(top_10_files):
    table = PrettyTable(['File Name', 'Location', 'Creation Date', 'Size (GB)'])
    for file, size in top_10_files:
        creation_time = os.path.getctime(file)
        creation_date = datetime.datetime.fromtimestamp(creation_time).strftime('%Y-%m-%d %H:%M:%S')
        size_in_gb = round(size / (1024 * 1024 * 1024), 2)
        table.add_row([os.path.basename(file), os.path.dirname(file), creation_date, size_in_gb])
    print(table)

# main function to run the program
def main():
    drives = display_available_drives()
    drive = select_drive(drives)
    top_10_files = scan_drive(drive)
    display_results(top_10_files)

if __name__ == '__main__':
    main()
