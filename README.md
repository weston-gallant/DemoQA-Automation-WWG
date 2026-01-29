# DemoQA-Automation-WWG

Automated end-to-end UI tests for [DemoQA](https://demoqa.com) using **Python**, **Behave BDD**, **Selenium WebDriver**, and the **Page Object Model (POM)**. This project is designed as a lightweight, production-style UI regression suite.

## What this project demonstrates

- **Page Object Model**: Clean separation of locators and page actions for DemoQA pages (forms, buttons, alerts, text box).
- **Behave BDD**: Readable Gherkin feature files with reusable step definitions and tagged regression scenarios.
- **Explicit waits**: Stable interactions using WebDriverWait/expected conditions instead of `time.sleep()`.
- **Browser lifecycle via hooks**: Single shared browser per test run using `environment.py` hooks under `features/`.
- **Headless & CI-ready**: Headless Chrome support via environment variable (`HEADLESS=true`) for reliable CI runs.
- **Allure reporting**: Rich test reports with step-level logging and screenshots on failure.

## Additional Info:

Want to run the tests? Check [docs/RUNNING_TESTS.md](https://github.com/weston-gallant/DemoQA-Automation-WWG/blob/main/docs/RUNNING_TESTS.md) to get started!

Feel free to email me wesgallant97@gmail.com for any questions / concerns / feedback

Thank you for taking a look at my homemade regression suite! 