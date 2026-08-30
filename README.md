# 🛡️ ST-Vault: Automated File Backup & Cleanup Script

A smart, lightweight Python automation tool designed to handle secure file backups and automated storage management for Linux server environments. 

## 🌟 Key Features
* **Automated Archiving:** Instantly compresses target project directories into timestamped `.zip` archives.
* **Smart Storage Cleanup:** Automatically scans and deletes older backup files (e.g., older than 7 days) to prevent server storage overflow.
* **Set-and-Forget:** Fully optimized to run continuously in the background using Linux `cron` jobs.

## 🛠️ Technologies Used
* **Python 3**
* Core Python Modules: `os`, `shutil`, `datetime`, `time`

## 🚀 Why I Built This
This tool was primarily developed to ensure zero data loss for backend infrastructures, such as my custom e-commerce platform (**ST HUB**). It acts as a reliable, self-cleaning backup mechanism for critical databases and project files.
