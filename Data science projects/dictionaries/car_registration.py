def car_app():
    registry = {}
    while True:
        x = input("1. register car 2. search for a car 3. exit")
        if x == "3":
            break
        elif x == "1":
            plate = input("enter the license plate number: ")
            if plate not in registry:
                registry[plate] = []
                make = input("enter the make of the car: ")
                registry[plate].append(make)
                model = input("enter the model of the car: ")
                registry[plate].append(model)
                color = input("enter the color of the car: ")
                registry[plate].append(color)
                year = input("enter the year of the car: ")
                registry[plate].append(year)
            else:
                print("that plate is already in the registry")
        elif x == "2":
            plate = input("enter the license plate number: ")
            if plate in registry:
                print(registry[plate])
            else:
                print("that plate isn't in the registry")

car_app()