#Deiontay Dawson
#22 June 2025
#P2HW2_DawsonDeiontay
#Creating Lists

#Create Empty List
test_scores = []

#User input for each test. Use separate statements.
#Store the grades in a list
mod1 = float(input("Enter grade for Module 1: "))
test_scores.append(mod1)
mod2 = float(input("Enter grade for Module 2: "))
test_scores.append(mod2)
mod3 = float(input("Enter grade for Module 3: "))
test_scores.append(mod3)
mod4 = float(input("Enter grade for Module 4: "))
test_scores.append(mod4)
mod5 = float(input("Enter grade for Module 5: "))
test_scores.append(mod5)
mod6 = float(input("Enter grade for Module 6: "))
test_scores.append(mod6)
print(f"\n------------Results------------")
#Display min, max, sum, avg
low = min(test_scores)
high = max(test_scores)
total = sum(test_scores)
num_items = len(test_scores)
avg = (total/num_items)
#Spacing, with float 2
print(f"Lowest Grade:\t\t{low:.2f}")
print(f"Highest Grade:\t\t{high:.2f}")
print(f"Sum of Grade:\t\t{total:.2f}")
print(f"Average:\t\t{avg:.2f}")
print("----------------------------------------------")
#Pseudocode
