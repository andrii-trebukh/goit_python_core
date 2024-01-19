from main import get_birthdays_per_week
from datetime import date, datetime
from freezegun import freeze_time




@freeze_time("2023-11-27")
def main():
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
        {"name": "Jan2", "birthday": datetime(1985, 11, 28).date()},
        {"name": "Jan3", "birthday": datetime(1988, 11, 29).date()},
        {"name": "me", "birthday": datetime(1980, 11, 30).date()},
        {"name": "Jan4", "birthday": datetime(1976, 12, 1).date()},
        {"name": "Jan5", "birthday": datetime(1978, 12, 2).date()},
        {"name": "Jan6", "birthday": datetime(1982, 12, 3).date()},
        {"name": "Jan7", "birthday": datetime(1983, 12, 4).date()},
        {"name": "Jan8", "birthday": datetime(1976, 12, 5).date()},
        {"name": "Jan9", "birthday": datetime(1973, 12, 6).date()},
        {"name": "Jan10", "birthday": datetime(1966, 11, 26).date()},
        {"name": "Jan11", "birthday": datetime(1988, 2, 29).date()}
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")


if __name__ == "__main__":
    main()