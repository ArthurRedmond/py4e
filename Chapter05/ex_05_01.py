count = 0
total = 0
while True:
    num = input("Enter a number:")
    if num == "done":
        break
    try:
       total += int(num)
       count += 1
    except:
        print("Invalid input")

print(total, count, total / count)
