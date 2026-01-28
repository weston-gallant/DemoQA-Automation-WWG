# DemoQA-Automation-WWG

Automated end-to-end UI tests for [DemoQA](https://demoqa.com) using **Python**, **Behave BDD**, **Selenium WebDriver**, and the **Page Object Model (POM)**. This project is designed as a lightweight, production-style UI regression suite.

## What this project demonstrates

- **Page Object Model**: Clean separation of locators and page actions for DemoQA pages (forms, buttons, alerts, text box).
- **Behave BDD**: Readable Gherkin feature files with reusable step definitions and tagged regression scenarios.
- **Explicit waits**: Stable interactions using WebDriverWait/expected conditions instead of `time.sleep()`.
- **Browser lifecycle via hooks**: Single shared browser per test run using `environment.py` hooks under `features/`.
- **Headless & CI-ready**: Headless Chrome support via environment variable (`HEADLESS=true`) for reliable CI runs.
- **Allure reporting**: Rich test reports with step-level logging and screenshots on failure.

## Project structure

DemoQA-AUTOMATION-WWG/
├── data/
│   ├── practice_form_data.py
│   └── text_box_data.py
├── features/
│   ├── alerts.feature
│   ├── buttons.feature
│   ├── checkboxes.feature
│   ├── environment.py
│   ├── practice_form.feature
│   ├── text_box.feature
│   └── steps/
│       ├── alerts_steps.py
│       ├── buttons_steps.py
│       ├── checkboxes_steps.py
│       ├── practice_form_steps.py
│       └── text_box_steps.py
├── pages/
│   ├── __pycache__/        # ignored by git
│   ├── alerts_page.py
│   ├── buttons_page.py
│   ├── checkboxes_page.py
│   ├── practice_forms_page.py
│   └── text_box_page.py
├── reports/
│   ├── allure-report/      # generated HTML reports (gitignored)
│   └── allure-results/     # raw Allure results from Behave (gitignored)
├── utils/                  # (empty/for future helpers – optional)
├── .gitattributes
├── .gitignore
├── behave.ini
├── config.ini              # (not currently used in the project)
├── pyproject.toml          # (if present for tooling/deps)
├── README.md
└── requirements.txt
