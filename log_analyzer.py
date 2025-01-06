import re
import sys
from collections import Counter

# Configuration for log file (adjust path accordingly)
LOG_FILE = '/path/to/web/server/logfile.log'

# Regular expression patterns to extract data from the log lines
IP_PATTERN = r'(\d+\.\d+\.\d+\.\d+)'  # Extracts IP addresses
STATUS_CODE_PATTERN = r'"\s(\d{3})\s'  # Extracts HTTP status codes (e.g., 404, 200)
REQUEST_PATTERN = r'"(GET|POST|PUT|DELETE)\s(.*?)\sHTTP'  # Extracts requested URLs

def analyze_log_file(log_file_path):
    try:
        with open(log_file_path, 'r') as file:
            lines = file.readlines()

        ip_addresses = []
        status_codes = []
        requests = []

        for line in lines:
            # Extract IP addresses
            ip_match = re.search(IP_PATTERN, line)
            if ip_match:
                ip_addresses.append(ip_match.group(1))
            
            # Extract HTTP status codes
            status_code_match = re.search(STATUS_CODE_PATTERN, line)
            if status_code_match:
                status_codes.append(status_code_match.group(1))
            
            # Extract requested URLs
            request_match = re.search(REQUEST_PATTERN, line)
            if request_match:
                requests.append(request_match.group(2))

        # Analyzing log data
        ip_count = Counter(ip_addresses)
        status_count = Counter(status_codes)
        request_count = Counter(requests)

        # Report results
        print("\nMost Frequent IP Addresses:")
        for ip, count in ip_count.most_common(5):
            print(f"{ip}: {count}")

        print("\nMost Common Status Codes:")
        for status, count in status_count.most_common():
            print(f"Status {status}: {count}")

        print("\nMost Requested Pages:")
        for request, count in request_count.most_common(5):
            print(f"Page: {request}, Requests: {count}")

    except FileNotFoundError:
        print(f"Error: Log file {log_file_path} not found.")
    except Exception as e:
        print(f"An error occurred while analyzing the log file: {e}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python log_analyzer.py <path_to_log_file>")
        sys.exit(1)

    log_file_path = sys.argv[1]
    analyze_log_file(log_file_path)
