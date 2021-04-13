sudo mysql blackswan_event_tracker < blackswan_create_schema.sql
python3 Scraper.py
sudo mysql blackswan_event_tracker < demo.sql >out.csv
libreoffice out.csv
