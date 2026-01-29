# Running the tests

This document describes how to run the DemoQA automation suite locally.

---

## 1. Prerequisites
- Python 3.x installed
- Google Chrome installed
- (Optional) Allure command-line tool installed, if you want to generate the HTML report

---

## 2. Clone the repository

git clone https://github.com/weston-gallant/DemoQA-AUTOMATION-WWG.git
cd DemoQA-AUTOMATION-WWG

---

## 3. Create and activate a virtual environment (recommended)

python -m venv .venv

---

Windows (PowerShell):

.venv\Scripts\Activate.ps1

---

Windows (cmd):

.venv\Scripts\activate.bat

---

macOS / Linux:

source .venv/bin/activate

---

## 4. Install dependencies
pip install -r requirements.txt

---

## 5. Run the regression suite (visible browser)
behave -t @regression

---

## 6. Generate and open report
allure generate --clean -o reports/allure-report reports/allure-results

allure open reports/allure-report