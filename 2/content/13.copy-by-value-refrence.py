# copy by refrence vs copy by value

# all primitives are by default -> copy by value
# all none primitives are by default -> copy by refrence

################################################
# copy by refrence
# copying of ram address

scores = [10,20,30]
scores_copy = scores # copy by refrence
scores_copy.append(40)

print(scores) # [10,20,30,40]
print(scores_copy) # [10,20,30,40]

################################################
# copy by value
# copying value in ram

scores = [10,20,30]
scores_copy = scores.copy() # copy by value
scores_copy.append(40)

print(scores) # [10,20,30]
print(scores_copy) # [10,20,30,40]