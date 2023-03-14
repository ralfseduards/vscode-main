str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]

# use built-in function filter to filter empty value
new_str_list = list(filter(None, str_list))

print("After removing empty strings")
print(new_str_list)