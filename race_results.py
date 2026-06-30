# Harvard CS50 Python Practice on Lists 

results = ["Mario", "Luigi"]

results.append("Princess") #adds more items after the list
results.append("Yoshi")
results.append("Koopa Troopa")
results.append("Toad")

results.append(["Bowser", "Donkey Kong Jr."]) #adds a list to the list
results.remove(["Bowser", "Donkey Kong Jr."]) # removes the list from the list
results.extend(["Bowser", "Donkey Kong Jr."]) # adds elements from another list

results.remove("Bowser") #removes an item from the list
results.insert(1, "Bowser") #inserts an item at a specific index

results.pop() #removes the last item from the list
results.sort() #sorts the list in alphabetical order
results.reverse() #reverses the order of the list

print(results) #prints the list