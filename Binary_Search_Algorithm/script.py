def generate_numbers_with_difference_of_two(start, end):
 

  numbers = []
  current_number = start
  while current_number <= end:
    numbers.append(current_number)
    current_number += 2
  return numbers



start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))


numbers = generate_numbers_with_difference_of_two(start, end)

print("The numbers with a difference of two between {} and {} are:".format(start, end))
for number in numbers:
  print(number)
