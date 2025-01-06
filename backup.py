import os
import subprocess
import time
import logging

# Setup logging configuration
logging.basicConfig(filename='backup.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Configuration
SOURCE_DIR = '/path/to/source/directory'  # Directory to back up
REMOTE_SERVER = 'user@remote_server:/path/to/destination'  # Remote server destination
BACKUP_LOG_FILE = 'backup.log'

def perform_backup():
    try:
        # Check if source directory exists
        if not os.path.exists(SOURCE_DIR):
            logging.error(f"Source directory {SOURCE_DIR} does not exist.")
            print(f"Error: Source directory {SOURCE_DIR} does not exist.")
            return False

        # Perform the backup using rsync
        command = f"rsync -av --delete {SOURCE_DIR} {REMOTE_SERVER}"
        result = subprocess.run(command, shell=True, capture_output=True, text=True)

        if result.returncode == 0:
            logging.info(f"Backup successful: {SOURCE_DIR} to {REMOTE_SERVER}")
            print(f"Backup successful: {SOURCE_DIR} to {REMOTE_SERVER}")
            return True
        else:
            logging.error(f"Backup failed: {result.stderr}")
            print(f"Backup failed: {result.stderr}")
            return False
    except Exception as e:
        logging.error(f"Error during backup: {str(e)}")
        print(f"Error during backup: {str(e)}")
        return False

if __name__ == '__main__':
    logging.info("Backup process started.")
    success = perform_backup()
    if success:
        logging.info("Backup completed successfully.")
    else:
        logging.error("Backup process failed.")
