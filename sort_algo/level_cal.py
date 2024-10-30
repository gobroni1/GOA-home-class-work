from datetime import datetime, timedelta


group_info = {
    23: {"start_date": datetime(2024, 5, 16), "speed": 2},
    29: {"start_date": datetime(2024, 5, 19), "speed": 1},
    31: {"start_date": datetime(2024, 5, 18), "speed": 1},
    33: {"start_date": datetime(2024, 5, 18), "speed": 1},
    35: {"start_date": datetime(2024, 6, 24), "speed": 1},
    36: {"start_date": datetime(2024, 6, 27), "speed": 1},
    37: {"start_date": datetime(2024, 6, 25), "speed": 1},
    38: {"start_date": datetime(2024, 6, 25), "speed": 2}
}

def calculate_lessons(grupe):

    if grupe not in group_info:
        print("Group not found.")
        return

    current_date = datetime.now()

    start_date = group_info[grupe]["start_date"]
    speed = group_info[grupe]["speed"]

    weeks_passed = (current_date - start_date).days // 7
    
    total_lessons = weeks_passed * speed
    print(f"Group {grupe} is on level {total_lessons+2}.")


grupe = int(input("Enter group number: "))
calculate_lessons(grupe)
