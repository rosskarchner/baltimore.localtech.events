# Baltimore Tech Events

Data directory for **Baltimore Tech Events** — technology conferences and meetups
in and around Baltimore, MD. Modeled on the DC Tech Events structure.

## Structure

- `config.yaml` — site configuration (name, location, timezone, base URL).
- `_categories/` — category definitions (name + description) shared across events.
- `_groups/` — recurring organizers. Each group has an `ical` feed that is polled
  to import upcoming events automatically.
- `_single_events/` — one-off events (conferences, summits). Filenames are
  prefixed with the event date: `YYYY-MM-DD-slug.yaml`.
- `_recurring_events/` — events defined by an `rrule` (e.g. weekly meetups).

## Adding a group

Create `_groups/<slug>.yaml`:

```yaml
name: My Baltimore Group
active: true
website: https://www.meetup.com/my-group/
ical: https://www.meetup.com/my-group/events/ical/
categories:
- software-development
suppress_urls: false
suppress_guid: false
scan_for_metadata: false
```

## Adding a single event

Create `_single_events/YYYY-MM-DD-slug.yaml`:

```yaml
title: 'My Event'
date: '2026-06-13'
url: 'https://example.com/'
location: 'Baltimore, MD'
cost: 'Free'
submitted_by: 'anonymous'
```
