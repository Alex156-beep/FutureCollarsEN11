from lesson10.workshop.DataStore import DataStore
from lesson10.workshop.LoggingDataStore import LoggingDataStore

if __name__ == "__main__":
    store1 = LoggingDataStore("Store1", "Example store")
    # storeWithoutLogs = DataStore("Store1", "Example store")

    # Set data
    store1['a'] = 10
    store1['b'] = 20

    # Get data
    print(store1['a'])
    print(store1['b'])

    # Object info (__str__)
    print(store1)

    # Iterating (__iter__)
    for key in store1:
        print(f"{key} = {store1[key]}")

    # Method iter()
    for k, v in store1.items():
        print(f"{k}: {v}")
