# Hash sets provide constant-time insertion, retrieval and deletion -> O(1) time
# Hash sets eliminates duplicates

### Hash set basics

# Defining a hash set
student_ids = set()
# Add elements to the hash set
student_ids.add(123)
student_ids.add(456)
student_ids.add(789)
# Check existence
print(123 in student_ids)
print(111 in student_ids)
# Remove an item
student_ids.remove(123)
print(123 in student_ids)

### Uniqueness of hash sets

hash_set1 = set()

hash_set1.add("element1")
hash_set1.add("element1")

print(hash_set1)

### Unordered nature of hash sets

hash_set2 = set()

hash_set2.add("element3")
hash_set2.add("element2")
hash_set2.add("element1")

print(hash_set2)

### Hands-on example

grocery_list = set()
grocery_list.add("Milk")
grocery_list.add("Eggs")
grocery_list.add("Butter")

print("Milk" in grocery_list)
print("Cheese" in grocery_list)

grocery_list.add("Cheese")
print("Cheese" in grocery_list)

grocery_list.remove("Milk")
print("Milk" in grocery_list)


### Clearing and Copying Hash sets
# 1. Clearing -> Removing all items in it
grocery_list.clear()
print(grocery_list)
# 2. Creating a SEPARATE copy
new_list = set(["Eggs", "Jams", "Ham"])
copied_list = new_list.copy()

print(new_list, copied_list)