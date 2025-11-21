print("Enter the number of cars")
job_count = int(input())
workload1 = 0
workload2 = 0
workload3 = 0
for job in range(job_count):
    print("Enter the number of working hours for the car")
    job_hours = int(input ())
    if job_hours <= 0:
        print("Error: Invalid number of hours!")
        break
    if workload3 < workload1 and workload3 < workload2:
        workload3 += job_hours #workload3 = workload3 + job_hours
    elif workload2 < workload1:
        workload2 += job_hours
    else:
        workload1 += job_hours
print("The nearest mechanic will be free within {} days".format(
    int((min(workload1, workload2, workload3) + 7) / 8)
))
print("All mechanics will be free within {} days "
.format(int((max(workload1, workload2, workload3) +7) / 8)))

