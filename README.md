# Selenium — Web Automation Scripts

A collection of browser-automation scripts built with
[Selenium](https://www.selenium.dev/) and Chrome WebDriver.

## Scripts

| File | Description |
|------|-------------|
| `basic.py` | Opens Google, searches for "python", and clicks the first result. |
| `installing.py` | Minimal WebDriver smoke test; opens Google and saves a screenshot. |
| `kurlar.py` | Scrapes daily exchange rates from the Central Bank of Turkey (TCMB) site. |
| `insta.py` | `Instagram` class that logs in and automates Instagram actions. |
| `instaUserInfo.py` | Holds Instagram credentials imported by `insta.py`. |

## Usage

```bash
python basic.py
python kurlar.py
python insta.py
```

A local Chromium build is bundled under `chrome-win32/` (Windows). On other
platforms, install Chrome + a matching `chromedriver` (or let Selenium Manager
resolve the driver automatically).

## ⚠️ Security note

`instaUserInfo.py` currently contains **hard-coded credentials in plain text**.
Do not commit real secrets — move them to environment variables or a local,
git-ignored config file, and rotate any password that has already been exposed.

## Requirements

- Python 3.x
- `selenium` (`pip install selenium`)
- Google Chrome / Chromium + ChromeDriver
