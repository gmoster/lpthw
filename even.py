total_odd = 0
total_even = 0

for i in range(1, 100):
    if i % 2 == 0:
        total_even = total_even + i
    else:
        total_odd = total_odd + i

print("Total even", total_even)
print("Total odd", total_odd)
if total_odd > total_even:
    print(" odd is bigger")
else:
    print("even is bigger")
