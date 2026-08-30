import shutil
import datetime
import os
import time

print("ST-Vault: Backup process started...\n")

# 1. Creating a new backup
current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
backup_name = "backup_" + current_time
shutil.make_archive(backup_name, 'zip', 'my_data')
print("New backup successfully created: " + backup_name + ".zip")

# 2. Deleting old backups (Cleanup)
print("\nChecking for old backups...")

days_to_keep = 7 # Delete files older than 7 days
current_time_sec = time.time() # Current time in seconds

# Check every file in the current directory
for file in os.listdir('.'):
    # Select only files starting with 'backup_' and ending with '.zip'
    if file.startswith("backup_") and file.endswith(".zip"):

        # Get file creation time and calculate its age in days
        file_age_sec = current_time_sec - os.path.getmtime(file)
        file_age_days = file_age_sec / (24 * 3600)

        # If older than 7 days, delete the file
        if file_age_days > days_to_keep:
            os.remove(file)
            print("Deleted old backup: " + file)

print("\nST-Vault process completed!")