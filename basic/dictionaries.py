# Dictionaries

band = {"vocals": "Plant", "guitar": "Page"}

band2 = dict(vocals="Plant", guitar="Page")

# print(band)
# print(band2)
# print(type(band))
# print(len(band))

#! Access items
# print(band["vocals"])
# print(band.get("guitar"))

#! list all keys
# print(band.keys())

#! list values
# print(band.values())

#! list of key/values pairs as tuples
# print(band.items())

#! verify a key exist
# print("guitar" in band)
# print("triangle" in band)

#! change values
# band["vocals"] = "vowels"
# band.update({"bass": "JPJ"})
# print(band)

#! remove items
# print(band.pop("bass"))
# print(band)

# band["drums"] = "myDrum"
# print(band)

# print(band.popitem())  # * it returns as a tuple
# print(band)

#! Delete and Clear
# band["drums"] = "Demo"
# del band["drums"]
# print(band)

# band2.clear()
# print(band2)

# del band2

#! copy dictionaries
# band2 = band  # * it create a reference
# print("It is a bad way to copy!")
# print(band2)
# print(band)

# band2["drums"] = "Dulal"
# print(band)

# band2 = band.copy()
# band2["drums"] = "Hemlal"
# print("This is the good way to copy!")
# print(band)
# print(band2)

# * or we can use the constructor function
# band3 = dict(band)
# print("Good Copy!")
# print(band3)
# print(band)

#! Nested dictionaries
# member1 = {"name": "Plant", "instrument": "vocals"}
# member2 = {"name": "Page", "instrument": "guitar"}

# band = {"member1": member1, "member2": member2}
# print(band)
# print(band["member2"]["name"])

#! Sets
# nums = {1, 2, 3, 4}
# nums2 = set((1, 2, 3, 4))
# print(nums)
# print(nums2)
# print(type(nums))
# print(len(nums2))

#! No duplicate allowed
# nums = {1, 2, 2, 3}
# print(nums)

#! True is a dupe of 1, False is a dupe of zero
# nums = {1, True, 2, 2, False, 3, 4, 0}
# print(nums)

#! check if a value is in a set
# print(2 in nums)

#! Add a new element to a set
# nums.add(8)
# print(nums)

#! Add elements from one set to another
# morenums = {5, 6, 7, 8}
# nums.update(morenums)
# print(nums)

# * you can use update() with lists, tuples and dictionaries too

#! Merge two set to form a new set
# one = {1, 2, 3, 4}
# two = {4, 5, 6, 7, 8}

# mynewset = one.union(two)
# print(mynewset)

#! Keep only the duplicates
one = {1, 2, 3, 4}
two = {3, 4, 5}

one.intersection_update(two)
print(one)

#! Keep everything except duplicates
one = {1, 2, 3, 4}
two = {3, 4, 5}

one.symmetric_difference_update(two)
print(one)
