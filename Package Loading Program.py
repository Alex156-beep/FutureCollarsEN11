max_items = int(input("Enter the maximum number of items to be shipped: "))

current_weight = 0
total_weight = 0
package_number = 1
packages_sent = 0
most_unused = 0
most_unused_package = 0
item_count = 0

while item_count < max_items:
    weight = float(input("Enter item weight (1–10 kg, or 0 to stop): "))

    if weight == 0:
        print("Program stopped by user.")
        break

    if weight < 1 or weight > 10:
        print("Invalid weight. Please enter a value between 1 and 10.")
        continue


    if current_weight + weight > 20:

        print("Package", package_number, "sent with", current_weight, "kg.")
        packages_sent = packages_sent + 1
        total_weight = total_weight + current_weight

        unused = 20 - current_weight
        if unused > most_unused:
            most_unused = unused
            most_unused_package = package_number


        package_number = package_number + 1
        current_weight = weight
    else:
        current_weight = current_weight + weight

    item_count = item_count + 1


if current_weight > 0:
    print("Package", package_number, "sent with", current_weight, "kg.")
    packages_sent = packages_sent + 1
    total_weight = total_weight + current_weight
    unused = 20 - current_weight
    if unused > most_unused:
        most_unused = unused
        most_unused_package = package_number


if packages_sent > 0:
    total_unused = packages_sent * 20 - total_weight
    print("\n--- Summary ---")
    print("Packages sent:", packages_sent)
    print("Total weight:", total_weight, "kg")
    print("Total unused capacity:", total_unused, "kg")
    print("Package", most_unused_package, "had the most unused capacity:", most_unused, "kg")
else:
    print("No packages were sent.")