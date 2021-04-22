sudo mysql blackswan_event_tracker < blackswan_create_schema.sql
python3 -m cProfile -s tottime Scraper.py > profile.txt
sudo mysql blackswan_event_tracker < demo.sql >out.csv
#libreoffice out.csv
