import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from api_fetcher import fetch_driver

def main():
    choice = ""
    while choice != "0":
        print("---------------------------")
        print("Menu:")
        print("1. Fetch driver by number")
        print("2. Show Throttle vs Brake usage by driver")
        print("3. Show Speed by driver")
        print("0. Exit")
        print("---------------------------")
        choice = int(input("Enter your choice: "))
        match choice:
            case 1:
                driver_number = int(input("Enter driver number: "))
                driver_data = fetch_driver("drivers", driver_number, speed="")
                if driver_data:
                    pd_driver_data = pd.DataFrame.from_dict(driver_data)
                    print(pd_driver_data.to_string())
                else:
                    print("No data found")
            case 2:
                driver_number = int(input("Enter driver number: "))
                car_data = fetch_driver("car_data", driver_number, "&speed>=1")
                if car_data:
                    pd_car_data = pd.DataFrame.from_dict(car_data)

                    pd_car_data["date"] = pd.to_datetime(pd_car_data["date"], utc=True)

                    x = pd_car_data["throttle"].iloc[::250]
                    y = pd_car_data["brake"].iloc[::250]

                    plt.plot(x.index, x.values, color="blue", label="throttle")
                    plt.plot(y.index, y.values, color="red", label="brake")

                    plt.title(f"Driver {driver_number} Throttle vs Brake")
                    plt.xlabel("Time")
                    plt.ylabel("Throttle & Brake in percent")

                    # Number of ticks you want on x-axis
                    num_ticks = 10  # adjust for readability

                    tick_positions = np.linspace(x.index[0], x.index[-1], num=num_ticks, dtype=int)
                    tick_labels = pd_car_data["date"].iloc[tick_positions].dt.strftime("%H:%M:%S.%f").str[:-3]
                    plt.xticks(tick_positions, tick_labels, rotation=45)

                    plt.legend()
                    plt.tight_layout()
                    plt.show()
                else:
                    print("No data found")
            case 3:
                driver_number = int(input("Enter driver number: "))
                car_data = fetch_driver("car_data", driver_number, "&speed>=1")
                if car_data:
                    pd_car_data = pd.DataFrame.from_dict(car_data)

                    speed = pd_car_data["speed"].iloc[::100]

                    plt.plot(speed.index, speed.values, color="blue", label="speed")

                    plt.show()
                else:
                    print("No data found")
            case _:
                print("Invalid input")
                break
if __name__ == "__main__":
    main()