age=int(input("Enter age of the candidate"))

def Vote(age):
    if age>18:
        return "The candidate eligible for voting"
    else:
        return "The candidate is not allowed for Voting"

print(Vote(age))