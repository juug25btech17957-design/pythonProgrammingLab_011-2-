def evaluate(m1, m2, m3, attendance):
    average = (m1 + m2 + m3) / 3
    all_pass = m1 >= 40 and m2 >= 40 and m3 >= 40
    if all_pass and average >= 75 and attendance >= 75:
        return average, "Eligible"
    return average, "Not Eligible"


data = input("Enter marks and attendance: ").split()
if len(data) != 4:
    print("Please enter exactly four values.")
else:
    try:
        m1, m2, m3, attendance = (float(x) for x in data)
    except ValueError:
        print("Marks and attendance must be numbers.")
    else:
        result = evaluate(m1, m2, m3, attendance)
        print("Average:", round(result[0], 2))
        print("Status:", result[1])
