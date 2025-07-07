#Deiontay Dawson
#7 July 2025
#P4HW1_DawsonDeiontay
#Creating Loop to collect data


num_scores = int(input("How many scores do you want to enter? "))
test_scores = []  # Move grades list outside the loop to store all scores

# Create while loop to check against num_scores
while num_scores > 0:  
    score = float(input(f"Enter score #{6 - num_scores}: "))  
    # Check if the score is valid
    if 0 <= score <= 100:  
        test_scores.append(score)  
        num_scores -= 1  
    else:
        print("\nINVALID Score entered!!!!\nScore should be between 0 and 100")
        print(input(f'Enter score #{num_scores} again: ')) #Unable to get score input prompt correct

print(f"\n------------Results------------")
if test_scores:  # Make sure there are scores in the list
    low = min(test_scores)  # Find the lowest score
    test_scores.remove(low)  # Remove the lowest score
    if test_scores:  # Check if list is not empty after removing lowest
        num_items = len(test_scores)
        total = sum(test_scores)  # Calculate total of modified list
        avg = total / num_items  # New average after dropping lowest

        # Determine letter grade based on average
        if avg >= 90:
            grade = 'A'
        elif avg >= 80:
            grade = 'B'
        elif avg >= 70:
            grade = 'C'
        elif avg >= 60:
            grade = 'D'
        else:
            grade = 'F'#Display min, max, sum, avg

#Spacing, with float 2
print(f"Lowest Grade   : {low:.2f}")
print(f"Modified List  : {test_scores}")
print(f"Scores Average : {avg:.2f}")
print(f"Grade          : {grade}")
print("----------------------------------------------")
#Pseudocode

