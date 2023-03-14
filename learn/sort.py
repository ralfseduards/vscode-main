companies = [
    ("google", 2019, 134.81),
    ("apple", 2019, 260.2),
    ("facebook", 2019, 184.9)
]


companies.sort(key=lambda a : a[2], reverse=True)


# sort sasorto pirmatneejo listu, sorted - uztaisa jaunu

cipari = [34,654,8,5,23,6,2,1,24,7,8,965,632,41]

sorted_cipari = sorted(cipari)

print(cipari)
print(sorted_cipari)
del cipari[0:6:2]
cipari[-3:] = ["viens", "divi", "triis"]
print("\n", cipari, sep="")