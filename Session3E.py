# Multi Value Container
# Set -> supports uniqueness i.e. duplicate data not allowed
john_followers = {"jennie", "fionna", "kia", "harry", "fionna", "george"}
kims_followers = {"kia", "harry", "fionna", "lee", "sia"}

print(john_followers, type(john_followers), hex(id(john_followers)))
print(kims_followers, type(kims_followers), hex(id(kims_followers)))

mutual_followers = john_followers.intersection(kims_followers)
print("MUTUAL FOLLOWERS")
print(mutual_followers)


# error -> set works on hashing and not on indexing
# print(john_followers[0])

# for each loop or enhanced for loop
for follower in john_followers:
    print(follower)
