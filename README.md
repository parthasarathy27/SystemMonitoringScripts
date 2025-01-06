# System Monitoring and Health Checker Scripts

This repository contains a collection of scripts designed to monitor the health of a Linux system, automate backup tasks, analyze log files, and check the health of applications. The scripts are written in **Python** and **Bash**, and they provide useful reports and alerts based on predefined thresholds.

## Objectives

### 1. **System Health Monitoring Script**

This script monitors the health of a Linux system by checking the following system metrics:
- **CPU usage**
- **Memory usage**
- **Disk space**
- **Running processes**

If any of these metrics exceed predefined thresholds (e.g., CPU usage > 80%), the script will send an alert to the console or log file.

### 2. **Automated Backup Solution**

This script automates the backup of a specified directory to a remote server or cloud storage solution. After the backup operation, it generates a report detailing the success or failure of the operation.

### 3. **Log File Analyzer**

This script analyzes web server logs (e.g., Apache, Nginx) for common patterns:
- The number of **404 errors**
- The **most requested pages**
- IP addresses with the **most requests**

It outputs a summarized report, allowing you to quickly identify trends and issues in the server logs.

### 4. **Application Health Checker**

This script checks the uptime of an application by examining HTTP status codes. It determines whether the application is functioning correctly by assessing the status of its HTTP response. If the application is ‘up’, it returns a success message; otherwise, it indicates that the application is ‘down’ and needs attention.

---

## Requirements

To run the scripts in this repository, you'll need the following:
- Python 3.x
- Bash (for the backup and log file analysis scripts)
- Linux-based system (or WSL if using Windows)
- Required Python libraries (listed in `requirements.txt`)

To install the necessary dependencies, run:

```bash
pip install -r requirements.txt
```

---

## Usage

### 1. **System Health Monitoring Script**

To run the system health monitoring script, use the following command:

```bash
python system_health.py
```

This script will check system metrics and print alerts to the console if any thresholds are exceeded.

### 2. **Automated Backup Solution**

To initiate the automated backup, use the following command:

```bash
python backup.py
```

You can modify the script to specify the directory you wish to back up, as well as the remote destination for storage.

### 3. **Log File Analyzer**

To run the log file analysis, use the following command:

```bash
python log_analyzer.py /path/to/logfile
```

This will analyze the given log file and output a summarized report of the analysis.

### 4. **Application Health Checker**

To check the application’s health, use the following command:

```bash
python app_health.py http://your-app-url.com
```

This will check the HTTP status code of the application and inform you if it is up or down.

---

## File Structure

```
SystemMonitoringScripts/
├── README.md              # Project documentation
├── system_health.py       # Script for system health monitoring
├── backup.py              # Script for automated backup
├── log_analyzer.py        # Script for analyzing log files
├── app_health.py          # Script for application health checking
├── logs/                  # Directory for log files (empty initially, created by script)
│   ├── system_health.log  # Log file for system health monitoring (generated dynamically)
├── .gitignore             # To ignore unnecessary files in Git
└── requirements.txt       # Python dependencies
```

---
