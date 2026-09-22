# GTFS GTT Checker

## Usage with Docker Compose

Install the default configuration file:

```
cp .env.example .env
```

Then you can execute the one-shot command with:

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

To automatically update these files, run `docker compose up` from a crontab, every some minutes. Example:

```
$ sudo crontab -l

# Run every 10 minutes
*/10 * * * * cd /path/to/gtfs_gtt_checker && /usr/bin/docker compose up --no-color > /dev/null
```
