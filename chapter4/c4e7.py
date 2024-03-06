total = 0
count = 0

while True:
	nums = input("Enter a number: ")
	if nums == "done":
		break
	try:
		num = float(nums)
	except:
		print("Invalid input")
		continue

	total = total + num
	count = count + 1

print(total, count, total/count)
