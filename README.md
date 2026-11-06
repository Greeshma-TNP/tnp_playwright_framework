# TNP Playwright Framework

Reusable Playwright functions for TNP test projects.

## Install in your project

```
pip install "git+https://github.com/Greeshma-TNP/tnp_playwright_frameworkTest.git#subdirectory=tnp_playwright_framework"
playwright install chromium
```

## Folder structure

```
tnp_playwright_framework/
├── framework/        reusable functions (one file per module)
├── config/           framework defaults
├── examples/         sample pages, tests and test data
├── pyproject.toml    lets projects install the framework with pip
├── requirements.txt  libraries needed to work on the framework
├── README.md
└── .gitignore
```

## Available functions

| File | Function | What it does |
|---|---|---|---|
| form_actions.py` | `select_radio_button` | Selects a radio button by its value. 
| form_actions.py` | `select_multiple_dropdown_options` | Selects multiple values from a native `<select multiple>` or custom searchable dropdown. | 
| table_actions.py` | `check_table_pagination` | Navigates through pages using Next, or clicks a specified page number. Returns the number of pages visited or the selected page number. |

