import ip
import latency

mylist = ["8.8.8.8", "192.168.0.5"]
my_list1 = [22, 33, 44, 55]

while True:
    print("\n=== Menu ===")
    print("1. IP Reachability Test")
    print("2. Latency Summary")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    # convert to int safely
    if not choice.isdigit():
        print("Invalid input! Enter a number.")
        continue

    choice = int(choice)

    if choice == 1:
        print("\nRunning IP Reachability Test...")
        print(ip.run(mylist))

    elif choice == 2:
        print("\nRunning Latency Summary...")
        print(latency.get_summary(my_list1))

    elif choice == 3:
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please enter 1, 2, or 3.")
2