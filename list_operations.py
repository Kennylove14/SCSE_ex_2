participants = [
    "Alice Wong",
    "Chen Wei",
    "David Kim",
    "Fatima Ali",
    "George Smith",
    "Hana Lee",
    "Audrey Hepburn",
    "James Stewart",
    "George Scott"
]

scores = [78, 92, 64, 87, 55, 73, 69, 96, 90]

qualification_score = 70
distinction_score = 90


# Make sure the lists have the same number of elements
assert len(participants) == len(scores), "participants and scores must have the same number of elements"


def get_status(score):
    """Classify a score as DISTINCTION, QUALIFIED or NOT QUALIFIED."""
    if score > distinction_score:
        return "DISTINCTION"
    if score > qualification_score:
        return "QUALIFIED"
    return "NOT QUALIFIED"


# First, display all the current participants with their scores. Use zip()
print("=" * 64)
print("CURRENT PARTICIPANTS AND THEIR SCORES")
print("=" * 64)
for name, score in zip(participants, scores):
    print(f"  {name:<16} {score}")
print()


# Write the logic to accept a new participant's name and their score. 
# While entering, also check if they are already in the list of participants. 
# If the participant is already registered, display a message and do not add them to the list.
# If the name is empty, then print an error saying that the name cannot be empty, and don't add them to the list.
# If the score is not a number, then print an error saying that the score must be a number, and don't add them to the list.
# If the score is less than 0 or greater than 100, then print an error saying that the score must be between 0 and 100, and don't add them to the list.
# Otherwise, add the participant and their score to the lists and display a message saying that they have been successfully registered.
def add_participant(name, score):
    if name in participants:
        print(f"  Error: '{name}' is already registered. Not added.")
        return False
    if not name or not name.strip():
        print("  Error: The name cannot be empty. Not added.")
        return False
    try:
        score = float(score)
    except (TypeError, ValueError):
        print("  Error: The score must be a number. Not added.")
        return False
    if score < 0 or score > 100:
        print("  Error: The score must be between 0 and 100. Not added.")
        return False
    if score.is_integer():
        score = int(score)
    participants.append(name)
    scores.append(score)
    print(f"  '{name}' has been successfully registered with a score of {score}.")
    return True


print("=" * 64)
print("ADDING NEW PARTICIPANTS")
print("=" * 64)
add_participant("Alice Wong", 85)      # already registered
add_participant("", 80)                # empty name
add_participant("Bob Johnson", "abc")  # score is not a number
add_participant("Bob Johnson", -5)     # score out of range (below 0)
add_participant("Bob Johnson", 150)    # score out of range (above 100)
add_participant("Bob Johnson", 88)     # valid -> registered
print()



# Write the logic to search for a specific participant.
# If the participant is found, display their name, score, and whether they are qualified or not.
# If the score is more than the distinction score, display that they have a DISTINCTION.
# If the score is more than the qualification score, display that they are QUALIFIED.
# Otherwise, display that they are NOT QUALIFIED.
# If the participant is not found, display a message saying that they are not found.
def search_participant(name):
    if name not in participants:
        print(f"  '{name}' was not found.")
        return
    index = participants.index(name)
    score = scores[index]
    print(f"  {name} -> score: {score}, status: {get_status(score)}")


print("=" * 64)
print("SEARCHING FOR PARTICIPANTS")
print("=" * 64)
search_participant("Alice Wong")     # QUALIFIED
search_participant("James Stewart")  # DISTINCTION
search_participant("George Smith")   # NOT QUALIFIED
search_participant("Nobody Here")    # not found
print()



# Display every participant's name, score, and whether they are qualified or not. 
print("=" * 64)
print("ALL PARTICIPANTS WITH QUALIFICATION STATUS")
print("=" * 64)
for name, score in zip(participants, scores):
    print(f"  {name:<16} {score:<6} {get_status(score)}")
print()



# Write the logic to find if there's even one participant that has a distinction, and if all the participants have passed (i.e., scored 50 or more).
any_distinction = any(score > distinction_score for score in scores)
all_passed = all(score >= 50 for score in scores)
print("=" * 64)
print("DISTINCTION / PASS CHECKS")
print("=" * 64)
print(f"  At least one participant has a DISTINCTION: {any_distinction}")
print(f"  All participants passed (scored 50 or more): {all_passed}")
print()

# Write the logic to update a participant's score.
# Ensure that the participant exists in the list before updating their score. 
# Also ensure that the new score is a valid number between 0 and 100.
def update_score(name, new_score):
    if name not in participants:
        print(f"  Error: '{name}' is not in the list. Score not updated.")
        return False
    try:
        new_score = float(new_score)
    except (TypeError, ValueError):
        print("  Error: The new score must be a number. Score not updated.")
        return False
    if new_score < 0 or new_score > 100:
        print("  Error: The new score must be between 0 and 100. Score not updated.")
        return False
    if new_score.is_integer():
        new_score = int(new_score)
    index = participants.index(name)
    old_score = scores[index]
    scores[index] = new_score
    print(f"  '{name}' score updated from {old_score} to {new_score}.")
    return True


print("=" * 64)
print("UPDATING SCORES")
print("=" * 64)
update_score("Nobody Here", 80)    # not in the list
update_score("Chen Wei", 150)      # out of range
update_score("Chen Wei", "abc")    # not a number
update_score("Alice Wong", 92)     # valid update (78 -> 92, becomes DISTINCTION)
print()



# Write the logic to withdraw (remove) a participant from the list.
# Ensure that the score for that specific participant is also removed from the scores list
def withdraw_participant(name):
    if name not in participants:
        print(f"  Error: '{name}' is not in the list. Nothing to withdraw.")
        return False
    index = participants.index(name)
    removed_score = scores.pop(index)
    participants.pop(index)
    print(f"  '{name}' (score: {removed_score}) has been withdrawn.")
    return True

print("=" * 64)
print("WITHDRAWING PARTICIPANTS")
print("=" * 64)
withdraw_participant("Nobody Here")    # not in the list
withdraw_participant("David Kim")      # valid withdrawal
print()



# Create and display a scoreboard where all the participants and their scores are displayed in descending order.
# Display their rank alongside the participant name and score
ranked = sorted(zip(participants, scores), key=lambda item: item[1], reverse=True)
print("=" * 64)
print("SCOREBOARD (DESCENDING ORDER)")
print("=" * 64)
for rank, (name, score) in enumerate(ranked, start=1):
    print(f"  Rank {rank:<2} {name:<16} {score}")
print()




# Calculate statistics: 
# Calculate what the highest score is, what lowest score is, what the average score is.
# Calculate how many participants have the highest score and the lowest score
# Calculate how many participants have distinctions, how many are qualified, and how many are not qualified
highest_score = max(scores)
lowest_score = min(scores)
average_score = sum(scores) / len(scores)
count_highest = scores.count(highest_score)
count_lowest = scores.count(lowest_score)
count_distinction = sum(1 for score in scores if score > distinction_score)
count_qualified = sum(1 for score in scores if qualification_score < score <= distinction_score)
count_not_qualified = sum(1 for score in scores if score <= qualification_score)
print("=" * 64)
print("STATISTICS")
print("=" * 64)
print(f"  Highest score:            {highest_score} (held by {count_highest} participant(s))")
print(f"  Lowest score:             {lowest_score} (held by {count_lowest} participant(s))")
print(f"  Average score:            {average_score:.2f}")
print(f"  With DISTINCTION:         {count_distinction}")
print(f"  QUALIFIED (not distinct): {count_qualified}")
print(f"  NOT QUALIFIED:            {count_not_qualified}")
print()



# Generate a final report that displays the participant name, their rank, their score, and their qualification (DISTINCTION, QUALIFIED, NOT QUALIFIED)
# Also the display all the statistics you calculated above
print("=" * 64)
print("FINAL REPORT")
print("=" * 64)
print(f"  {'Rank':<5}{'Name':<18}{'Score':<8}{'Qualification'}")
print("  " + "-" * 56)
for rank, (name, score) in enumerate(ranked, start=1):
    print(f"  {rank:<5}{name:<18}{score:<8}{get_status(score)}")
print()
print("  STATISTICS SUMMARY")
print(f"    Highest score:            {highest_score} (held by {count_highest} participant(s))")
print(f"    Lowest score:             {lowest_score} (held by {count_lowest} participant(s))")
print(f"    Average score:            {average_score:.2f}")
print(f"    With DISTINCTION:         {count_distinction}")
print(f"    QUALIFIED (not distinct): {count_qualified}")
print(f"    NOT QUALIFIED:            {count_not_qualified}")