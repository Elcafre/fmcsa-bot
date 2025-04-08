
# FMCSA Bot

This project powers the FMCSA lead tracking and automation system used by Peco Insurance.

### Features:
- ✅ Scrapes DOT registrations by state
- ✅ Logs leads to `fmcsa_scraper_log.json`
- ✅ Displays status on a live dashboard
- ✅ Pushes leads to Google Sheets for tracking
- ✅ Automated daily runs and boot-up initialization

### Files:
- `fmcsa_scraper.py` – Lead scraping script
- `fmcsa_scraper_log.json` – Live log read by dashboard
- `dashboard.py` – Flask web app displaying bot status

### Maintained by:
Julio Batista @Elcafre
