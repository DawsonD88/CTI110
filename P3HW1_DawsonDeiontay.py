#Deiontay Dawson
#29 June 2025
#P2HW2_DawsonDeiontay
#Creating Lists


# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]
# TO DO: determine lowest, highest , sum and average for grades

low = min(grades)
high = max(grades)
total = sum(grades)
num_items = len(grades)
avg = (total/num_items)

# determine letter grade for average
print(f"\n------------Results------------")
print(f"Lowest Grade:\t\t{low:.1f}")
print(f"Highest Grade:\t\t{high:.1f}")
print(f"Sum of Grade:\t\t{total:.1f}")
print(f"Average:\t\t{avg:.2f}")
print("----------------------------------------------")
if avg >= 90:
    print('Your grade is: A')
elif avg >= 80:
    print('Your grade is: B')

else:
    print('Your grade is: F') # TO DO: finish this

#Pseudocode



