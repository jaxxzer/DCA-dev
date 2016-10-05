unfiltered = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 9, 4, 5, 4, 5, 4, 5, 12, 4, 5, 3, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5]

filter = 0

passes = 7

filtered = []

for val in unfiltered:
    print val,
    print "\t",
    filter = filter + (val * (1.0/passes))
    filter = filter / (1 + (1.0/passes))
    print "%0.2f" % filter
    filtered.append(filter)

print unfiltered
print filtered
