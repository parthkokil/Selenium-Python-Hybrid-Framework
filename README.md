# 🧸 ELC Hybrid Automation Framework

> **Selenium + Python + PyTest** — A clean, keyword-driven UI automation suite for the [Early Learning Centre](https://www.elc.co.uk/) website.

---

## 🌟 What Is This Project?

This is a **Hybrid Test Automation Framework** built to test the **Early Learning Centre (ELC)** e-commerce website automatically — like a robot 🤖 that opens Chrome, clicks through the site, searches for toys, adds items to the basket, checks the footer links, and verifies everything works as expected.

It's called **"Hybrid"** because it blends **two powerful design patterns**:

| Pattern | What it means in simple words |
| --- | --- |
| 🗂️ **Page Object Model (POM)** | Every web page has its own Python class. Home page logic lives in `home_page.py`, product page logic in `first_product_page.py`, and so on. Clean and organized! |
| 🎛️ **Keyword-Driven** | One smart method — `perform_action("CLICK", ...)` — handles *all* actions (click, hover, search, verify). No repeating code everywhere! |

> 💡 **Think of it like a TV remote:** instead of a separate button for every channel, you have ONE remote (`perform_action`) that does everything based on which button (keyword) you press.

---

## ✨ Key Features

- 🎯 **One Unified Dispatcher** — `perform_action()` uses Python's `match-case` to handle CLICK, HOVER, SEARCH, VERIFY, and more.
- 🌐 **Runs on Local Chrome** — no Selenium Grid needed. WebDriver auto-downloads via `webdriver-manager`.
- 📊 **Data-Driven Testing** — all test data (URLs, expected texts) is read from an **Excel file**, so no hardcoded values in code.
- 📸 **Auto Screenshots** — captures screenshots on both successful checks *and* failures.
- 📝 **Smart Logging** — every action is logged into a timestamped log file.
- 📈 **Allure Reports** — beautiful HTML reports generated automatically after each run.
- 🔁 **Stale-Element Retry** — auto-retries flaky clicks so tests are more stable.
- ⚙️ **Config-Driven** — the app URL, timeouts, and folder paths all live in one `config.properties` file.

---

## 🛠️ Technologies Used

| Technology | Purpose | Why We Use It |
| --- | --- | --- |
| 🐍 **Python 3.12** | Core programming language | Simple, readable, huge automation ecosystem |
| 🌿 **Selenium 4** | Browser automation | Controls Chrome, clicks & types like a real user |
| ✅ **PyTest** | Test runner | Discovers & runs tests, manages markers (`@smoke`) |
| 📦 **webdriver-manager** | Auto driver setup | Downloads the correct ChromeDriver automatically |
| 📗 **openpyxl** | Excel reader | Pulls test data from `data.xlsx` |
| 📊 **Allure** | Reporting | Turns raw results into a gorgeous HTML dashboard |
| ⚙️ **configparser** | Config reader | Reads settings from `config.properties` |

---

## 📁 Project Structure

```
Project/
├── config/
│   └── config.properties        # App URL, timeout & folder paths
├── pages/                       # Page Object Model classes
│   ├── base_page.py             # The heart — perform_action() dispatcher
│   ├── home_page.py             # Home page actions
│   ├── product_listing_page.py  # Category & filter workflows
│   ├── first_product_page.py    # Product detail & basket flows
│   └── footer_component.py      # Footer links & multi-tab handling
├── uistore/                     # All locators (selectors) live here
│   ├── home_locators.py
│   ├── product_listing_locators.py
│   ├── first_product_locators.py
│   └── footer_locators.py
├── utilities/                   # Reusable helper toolbox
│   ├── web_driver_helper.py     # Clicks, waits, verifications
│   ├── config_reader.py         # Reads config.properties
│   ├── excel_reader.py          # Reads test data from Excel
│   ├── logger.py                # Timestamped logging
│   ├── screenshot.py            # Captures screenshots
│   ├── eventhandler.py          # Selenium event listener
│   └── report.py                # Allure report helper
├── testdata/
│   └── data.xlsx                # All test input data
├── tests/
│   └── test_page.py             # 10 smoke test cases
├── logs/                        # Auto-generated log files
├── screenshots/                 # Auto-captured screenshots
├── Report/                      # Allure results & HTML report
├── base.py                      # WebDriver setup (local Chrome)
├── conftest.py                  # PyTest hook -> auto Allure report
├── pytest.ini                   # PyTest config & markers
└── requirements.txt             # Python dependencies
```

---

## 🚀 Getting Started — Run It On Your System

Follow these steps and you'll have the framework running in minutes!

### ✅ Step 1: Prerequisites

Make sure these are installed on your machine:

| Requirement | Check Command | Notes |
| --- | --- | --- |
| 🐍 Python 3.12+ | `python --version` | Download from python.org/downloads |
| 🌐 Google Chrome | — | Any recent version works |
| 📊 Allure CLI | `allure --version` | Install guide: allurereport.org/docs/install |

### 📥 Step 2: Clone the Repository

```bash
git clone <your-repository-url>
cd Project
```

### 📦 Step 3: Install Dependencies

Install everything in one command using the `requirements.txt` file:

```bash
py -m pip install -r requirements.txt
```

> 💡 Prefer installing manually? Use this instead:
>
> ```bash
> py -m pip install selenium pytest allure-pytest webdriver-manager openpyxl
> ```

### ▶️ Step 4: Run the Tests

Make sure you are **inside the `Project/` folder**, then pick any of these:

```bash
# Run ALL test cases
py -m pytest

# Run a SINGLE test case
py -m pytest tests/test_page.py::TestCaseClass::test_footer_links_navigation -v

# Run only tests marked as "smoke"
py -m pytest -m smoke -v

# Run with Allure results (auto-configured in pytest.ini)
py -m pytest tests/test_page.py -v
```

### 📈 Step 5: View the Allure Report

After the run, an Allure report is generated automatically. To open it:

```bash
allure open Report/AllureReport
```

A browser window will pop up with your interactive test dashboard!

---

## 🧪 What Do The Tests Actually Check?

The suite contains **10 smoke test cases** covering real user journeys:

| # | Test Case | What It Does |
| --- | --- | --- |
| 1 | 👶 Newborn Gifts | Navigate → filter → open product → add to basket |
| 2 | 🧸 Soft Toys | Browse soft toys category & verify product |
| 3 | 🚲 Outdoor Toys (Bikes) | Filter bikes → add to basket → checkout |
| 4 | 🎨 Creativity Products | Arts & crafts flow → basket verification |
| 5 | 🐾 Paw Patrol | Brand navigation → add product to basket |
| 6 | 🎁 Dolls / Gift Cards | Explore menu → doll checkout flow |
| 7 | 🧩 Puzzles Search | Search "puzzles" → filter → verify wishlist |
| 8 | 🚗 Cars Search | Search "cars" → filter → verify product heading |
| 9 | 📞 Footer Help Links | Verify Contact, Delivery, Returns, Privacy links |
| 10 | 🔗 Footer Info Links | Verify Store Finder, Careers, Klarna & more |

---

## ⚙️ Configuration

All settings live in **`config/config.properties`** — change them without touching any code:

```properties
[ELC]
url = https://www.elc.co.uk/
timeout = 10

[PATH]
logger_path = logs
screenshot_path = screenshots
excel_path = testdata/data.xlsx
```

---

## 💡 Quick Troubleshooting

| ⚠️ Problem | ✅ Solution |
| --- | --- |
| `allure: command not found` | Install Allure CLI & add it to PATH |
| `No module named selenium` | Run the install command in Step 3 |
| `pip is not recognized` | Use `py -m pip` instead of `pip` |
| Chrome doesn't open | Make sure Google Chrome is installed |
| Tests can't find elements | The ELC website may have changed — locators in `uistore/` may need updating |
| Running from wrong folder | Always run tests from **inside** the `Project/` folder |

---

# 1bc7b2d9-96c7-46e0-81e2-735174028d25-b19e1e76-4464-4c0d-8112-3efd3a071fc4
https://sonar.server.examly.io/dashboard?id=iamneo-production-2_1bc7b2d9-96c7-46e0-81e2-735174028d25-b19e1e76-4464-4c0d-8112-3efd3a071fc4&amp;codeScope=overall
