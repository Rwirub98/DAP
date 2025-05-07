num = int(input("Enter a number: "))
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
if start <= num <= end:
    print(f"{num} is in the range of {start} to {end}.")
else:
    print(f"{num} is not in the range of {start} to {end}.")
