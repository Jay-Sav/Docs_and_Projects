from datetime import datetime, timezone
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError



def get_current_time():

    get_timezone = {
        "UTC": "UTC",
        "EST": "America/New_York",
        "CST": "America/Chicago",
        "MST": "America/Denver",
        "PST": "America/Los_Angeles"
}

    for zone_key,zone_value in get_timezone.items():
        print(f"{zone_key}: {zone_value}")
    select_timezone = input("\nSelect a timezone (e.g., UTC, EST, CST, MST, PST): ").upper().strip()
    while select_timezone not in get_timezone:
        print("Invalid input. Please enter a valid timezone.")
        select_timezone = input("\nSelect a timezone (e.g., UTC, EST, CST, MST, PST): ").upper().strip()

# Lookup the IANA TIMEZONE based on the user's selection
    target_zone_string = get_timezone[select_timezone]
    print(f"\nYou selected: {select_timezone} ({target_zone_string})\n")

    try:
        import tzdata  # Ensure tzdata is available for time zone information
        current_time = datetime.now(ZoneInfo("UTC"))
        current_time = current_time.astimezone(ZoneInfo(target_zone_string))
        print(f"Current date and time in {select_timezone}: {current_time.strftime('%Y-%m-%d %H:%M:%S')}")
    except (ZoneInfoNotFoundError, ImportError):
        print("Timezone failed to load. Defaulting to UTC.\n")
        current_time = datetime.now(timezone.utc)
        print(f"Current date and time in UTC: {current_time.strftime('%Y-%m-%d %H:%M:%S')}")

    return current_time.strftime('%Y-%m-%d %H:%M:%S')

    
    








