# GTFS GTT Checker

## Usage with Docker Compose

You can execute the one-shot command with:

```
docker compose up
```

Look into the `public_data/` directory. It should contain these files:

```
$ tree public_data

public_data/
├── agency.txt.gz
├── calendar_dates.txt.gz
├── calendar.txt.gz
├── fare_attributes.txt.gz
├── fare_rules.txt.gz
├── feed_info.txt.gz
├── routes.txt.gz
├── shapes.txt.gz
├── stop_attributes.txt.gz
├── stops.txt.gz
├── stop_times.txt.gz
├── timetable_pages.txt.gz
├── timetable_stop_order.txt.gz
├── timetables.txt.gz
├── trips_booking.txt.gz
├── trips.txt.gz
├── vehicle_categories.txt.gz
├── vehicles.txt.gz
└── versions.json
```

The suggestion is to add the `docker compose up` in a crontab, every some minutes.
