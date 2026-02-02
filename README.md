# Smart Resume Eligibility Analyzer 

A simple yet powerful tool to analyze candidate resumes based on their technical skills. Built with **Python** and **Gradio**.

## Features

- **File Support**: Upload `.txt`, `.pdf`, `.doc`, or `.docx` files.
- **Smart Analysis**: Automatically parses technical skills from `.txt` resumes.
- **Instant Feedback**: Provides immediate feedback on skill count and eligibility status.
- **Robustness**: Handles empty files, invalid formats, and corrupted data gracefully.

## Prerequisites

- Python 3.7 or higher
- `pip` (Python package manager)

## Installation

1.  **Clone the repository** (or download the files):
    ```bash
    # git clone <repository-url>
    # cd python_simple_resume_analyzer
    ```

2.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  **Run the application**:
    ```bash
    python app.py
    ```

2.  **Open the interface**:
    - The terminal will display a local URL (usually `http://127.0.0.1:7860`).
    - Click the link to open the Gradio UI in your browser.

3.  **Analyze a Resume**:
    - Click the "Upload Resume" area.
    - Select a file (e.g., `resume.txt`).
    - Click **"Analyze Resume"** to see the results.

## Eligibility Rules

| Skill Count | Status |
| :--- | :--- |
| 0 | `REJECTED` |
| 1–2 | `NOT ELIGIBLE` |
| 3–6 | `ELIGIBLE` |
| > 6 | `HIGHLY ELIGIBLE` |
| Error | `INVALID RESUME FILE` / `INVALID INPUT FORMAT` |

## Sample Input

Create a file named `sample_resume.txt` with:
```text
Python, SQL, Machine Learning, Deep Learning
```
**Expected Output**:
- Skill Count: 4
- Candidate Status: ELIGIBLE

## Notes

- Only `.txt` files are currently processed for skill extraction.
- Other formats will return an `INVALID INPUT FORMAT` message.
