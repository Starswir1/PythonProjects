password = "s3cur1tyC0d3"
target = 4
password1 = password[:target]
password2 = password[target:]
final = password2 + password1
print(final)
