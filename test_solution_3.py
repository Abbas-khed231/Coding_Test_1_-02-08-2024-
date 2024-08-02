#3. Write a Python function to count the occurrences of a specific element in a list.

def count_occurrences(lst, element):
  count = 0
  for item in lst:
    if item == element:
      count += 1
  return count

my_list = [1, 2, 3, 2, 4, 2, 5]
element_to_count = 2
count = count_occurrences(my_list, element_to_count)
print(f"The element {element_to_count} appears {count} times in the list.")

'''
Output:
The element 2 appears 3 times in the list.
'''
