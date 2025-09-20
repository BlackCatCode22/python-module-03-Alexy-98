
num = 0
tot = 0.0
while True:
    sval = input("Enter a number: ")
    if sval == 'done':
        break
    try:
        fval = float(sval)
    except:
        print("Invalid input")
        continue
    fval = float(sval)
    num = num + 1
    tot = tot + fval
if num > 0:
    print("Total: ",tot)
    print("Count: ",num)
    print("Average: ",tot/num)
else:
    print("No numbers entered")

print("All done!")