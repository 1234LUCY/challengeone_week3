def missing_numbers(list1):
      initial_list = [i for i in range(list1[0], list1[-1] + 1)]
      list1 = set(list1)
      return (list(list1 ^ set(initial_list)))

print(missing_numbers([1, 2, 3, 5, 6, 7,9]))
