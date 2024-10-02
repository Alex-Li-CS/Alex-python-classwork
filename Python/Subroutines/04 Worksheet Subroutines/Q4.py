car_park = [["Free" for _ in range(6)] for _ in range(20)]

def display_car_park():
    for row in range(20):
        print(f"Row {row + 1}: {car_park[row]}")
