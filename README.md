# Lloyds Banking Group - Engineering Skills Project

This project was completed for the Internship Experience UK (IEUK) program. It provides a complete solution to analyse a web server log file, identify the source of a bot attack, and automatically generate a professional report with findings and recommendations.

## Project Structure

This repository contains the following key files:

*   `log_analyzer.py`: A Python script that parses the `sample-log.log` file and prints a summary of the top traffic sources to the console.
*   `create_report.py`: A Python script that automates the creation of the final, formatted Microsoft Word report (`.docx`), complete with a data visualisation chart and references.
*   `sample-log.log`: The raw data file provided for the project.
*   `README.md`: This file, explaining the project and how to use it.

---

## Part 1: Log Analysis Script

This script performs the initial data analysis on the log file.

### Prerequisites

*   Python 3.6 or newer.
*   The `sample-log.log` file must be in the same directory.

### How to Run

1.  Open a terminal or command prompt.
2.  Navigate to the project directory.
3.  Run the script using the following command:

    ```bash
    python log_analyzer.py
    ```
4.  The analysis results will be printed directly to the terminal.

---
