# Harvard CS50 Python Practice on Lists 

results = ["Mario", "Luigi"]

results.append("Princess") #adds more items after the list
results.append("Yoshi")
results.append("Koopa Troopa")
results.append("Toad")

results.append(["Bowser", "Donkey Kong Jr."]) #adds a list to the list
results.remove(["Bowser", "Donkey Kong Jr."]) # removes the list from the list
results.extend(["Bowser", "Donkey Kong Jr."]) # adds elements from another list

print(results) #prints the list