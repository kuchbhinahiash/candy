print("shreya ashtek ar")

salary = [45000.50, 50000.25, 39000.80, 47000.90, 53000.30, 35000.20]

print("Original Salaries:")
print(salary)

selection_salary = salary.copy()
n = len(selection_salary)

print("\nSelection Sort")

for i in range(n):
    min = i

    for j in range(i + 1, n):
        if selection_salary[j] < selection_salary[min]:
            min = j

    selection_salary[i], selection_salary[min] = selection_salary[min], selection_salary[i]
    print("Pass", i + 1, ":", selection_salary)

print("\nSalaries after Selection Sort (Ascending Order):")
print(selection_salary)

print("\nTop 5 Highest Salaries (Selection Sort):")
print(selection_salary[-5:][::-1])

bubble_salary = salary.copy()

print("\nBubble Sort")

for i in range(n):
    for j in range(0, n - i - 1):
        if bubble_salary[j] > bubble_salary[j + 1]:
            bubble_salary[j], bubble_salary[j + 1] = bubble_salary[j + 1], bubble_salary[j]

    print("Pass", i + 1, ":", bubble_salary)

print("\nSalaries after Bubble Sort (Ascending Order):")
print(bubble_salary)

print("\nTop 5 Highest Salaries (Bubble Sort):")
print(bubble_salary[-5:][::-1])
