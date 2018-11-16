# List Functions
lucky_numbers = [4, 8, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Jim", "Jim", "Toby"]
friends.append("Sivar")
friends.insert(1, "Kelly")
friends.remove("Jim")
friends.pop()
lucky_numbers.sort()
lucky_numbers.reverse()
print(friends.sort())
friends.extend(lucky_numbers)
friends2 = friends.copy()
print(friends)
print(friends2)
print(friends.index("Oscar"))
print(friends.count("Jim"))
friends.clear()
print(friends)
