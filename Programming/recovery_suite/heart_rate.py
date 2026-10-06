try:
    user_age = int(input())

    if user_age < 0:
        raise ValueError("Invalid age")

    # Source: https://www.heart.org/en/healthy-living/fitness
    avg_max_heart_rate = 220 - user_age

    print(f"Avg: {avg_max_heart_rate}")

except ValueError as excpt:
    print(f"Error: {excpt}")