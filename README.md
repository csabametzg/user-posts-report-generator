# User Posts Report Generator

A simple Python automation script that fetches user and post data from a public API, connects the data, and generates reports in JSON, TXT, and CSV formats.

## Quick Start

```bash
python user_posts_report.py
```

### 2. An example input

```markdown
Example:

Enter user id:
1
```


## Features
- Fetches users data from API
- Fetches posts data from API
- Validates user input
- Handles API errors with try/except
- Connects users and posts by user ID
- Exports the result to:
  - `report.json`
  - `report.txt`
  - `report.csv`

## Technologies
- Python
- requests
- json
- csv

## How to run
```bash
python user_posts_report.py
```

Then enter a user ID when prompted.

## Example output

The script generates:

- user ID
- username
- post count
- first post title
- Purpose

This project was built as a practice project for Python automation, API handling, input validation, error handling, and file export.