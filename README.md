# Python SSH Log Analyzer

This is a command-line tool built with Python to parse and analyze SSH authentication logs (`auth.log`) for security events. Its primary goal is to identify potential brute-force attacks by detecting and reporting IP addresses with a high number of failed login attempts.

This project demonstrates proficiency in Python scripting, file I/O, and the use of regular expressions for pattern matching and data extraction.

## Features
- Parses standard `auth.log` files to find security-relevant lines.
- Uses regular expressions to accurately identify and extract failed login attempts.
- Aggregates and counts the number of failed attempts for each unique IP address.
- Generates a clean, sorted summary report of suspicious IPs, ordered from most to least frequent.

## How It Works
The script reads a log file (e.g., `auth.log`) line by line. A specific regular expression pattern is used to match lines that indicate a "Failed password" event. For each match, the source IP address is extracted. The script then uses a dictionary to keep a running count of attempts from each IP. Finally, it sorts the results and prints a formatted report to the console.

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites
You will need Python 3 installed on your system.

### Installation & Usage

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/MikeM365/log-analyzer.git
    ```

2.  **Navigate to the project directory:**
    ```bash
    cd log-analyzer
    ```

3.  **Add a log file:**
    Place your `auth.log` file (or any similarly formatted SSH log file) in this directory.

4.  **Run the script:**
    Execute the script from your terminal. It will automatically look for a file named `auth.log`.
    ```bash
    python log_analyzer.py
    ```

## Sample Output
After running, the script will produce a report similar to the following:

