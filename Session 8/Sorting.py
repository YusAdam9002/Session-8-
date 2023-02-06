def bubble_sort(collection):
  num_items = len(collection)
  for i in range(num_items):
      for j in range(num_items - 1):
            if collection[j] > collection[j + 1]:
              tmp = collection[j]
              collection[j] = collection[j + 1]
              collection[j + 1] = tmp

a = [1,34,2,76,8,45,653]
bubble_sort(a)
print(a)

#task2
def count_words(str):
    return len(str.split(" "))

def longer(a, b):
    if count_words(a) > count_words(b):
        return True
    elif count_words(a) < count_words(b):
        return False
    else:
        if len(a) > len(b):
            return True
        else:
            return False

# test the function
print(longer("hello there", "hi there"))

#task 3
def bubble_sort(collection):
  num_items = len(collection)
  for i in range(num_items):
      for j in range(num_items - 1):
            if longer(collection[j], collection[j + 1]):
              tmp = collection[j]
              collection[j] = collection[j + 1]
              collection[j + 1] = tmp

dos = ["hello there", "hi there"]
bubble_sort(dos)
for d in dos:
    print(d.center(130))
