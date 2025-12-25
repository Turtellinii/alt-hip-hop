# Alternate Hip Hop History Generator

This project generates an alternate history of hip hop's top 100 albums with random rappers, personalities, and release dates.

## Features

- Generates 100 albums ranked from #100 to #1
- Each album has a random name from a curated list of classic hip hop albums
- Rappers are assigned random personalities using the character generator
- Complex group album probability system that adjusts based on group album ratio
- Future album reservation system ensures artists appear multiple times
- Group albums can reuse existing groups or create new ones
- Outputs both a ranked list (100→1) and chronological list

## Files

- `hip_hop_generator.py` - Main generator script
- `character generator.py` - Personality profile generator using MBTI and Enneagram
- `alternate_hip_hop_top100.txt` - Example output

## Usage

Run the generator:

```bash
python3 hip_hop_generator.py
```

To save output to a file:

```bash
python3 hip_hop_generator.py > my_alternate_history.txt
```

## How It Works

### Album Generation

Each album (from position 100 down to 1) gets:
- Random album name from the list
- Random release date (1985-2025)
- Solo or group determination based on probability rules
- Primary rapper with personality profile

### Group Album Probability

The generator uses dynamic probability:
- Starts at 1/4 chance
- Adjusts to 1/3 when 1/6 of albums are group albums
- Returns to 1/4 when 1/4 of albums are group albums
- Can escalate to 1/2 or even 1/1 (guaranteed) if group ratio drops too low

### Future Album Reservations

When a rapper is first created, they get 0-6 future album slots reserved:
- Roll 1-28 to determine number of reservations
- 1-7: 0 albums (25%)
- 8-13: 1 album (21.4%)
- 14-18: 2 albums (17.9%)
- 19-22: 3 albums (14.3%)
- 23-25: 4 albums (10.7%)
- 26-27: 5 albums (7.1%)
- 28: 6 albums (3.6%)

### Personality Profiles

Each rapper gets a unique personality using:
- MBTI type (16 types)
- Enneagram wing (weighted by MBTI type)
- Instinctual variant stacking
- Valid tritype

Example: `ENTP 7w8 sp/sx 7w8 1w2 3w4`

## Output Format

### Top 100 List
```
#100 - Album Name
   Artist: Rapper Name
      Personality: MBTI Enneagram Instinct Tritype
   Release Date: M/D/YYYY
```

### Group Albums
```
#50 - Album Name
   Artists: Rapper 1, Rapper 2, Rapper 3
      - Rapper 1: Personality
      - Rapper 2: Personality
      - Rapper 3: Personality
   Release Date: M/D/YYYY
```

### Chronological List
```
M/D/YYYY - Album Name by Artist Name (#Position)
```
