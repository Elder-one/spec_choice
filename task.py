elements = input('Введите строки, разделённые пробелом --> ').split()
n = len(elements)

i = 0
result = []
while i < n:
  if len(elements[i]) <= 3:
    result.append(elements[i])
  i += 1

print(result)
