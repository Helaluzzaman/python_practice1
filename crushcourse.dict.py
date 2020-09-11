def groups_per_user(group_dictionary):
    user_group={}
    grp = list()
    allusers = list()
    for group, users in group_dictionary.items():
        
        for user in users:
            if user not in user_group.keys():
                user_group[user] = list()
                user_group[user].append(group)
            else:
                user_group[user].append(group)
        #for u,gps in user_group.items():
        #    print(gps)
    return user_group
        

print(groups_per_user({"local": ["admin", "userA"], "public":  ["admin", "userB"], "administrator": ["admin"] }))

#-----------------------------------------------------------
#Module 4

1.
def format_address(address_string):
  # Declare variables

  # Separate the address string into parts
  lst = address_string.split()
  hnum = lst[0]
  lradd = lst[1:]
  radd = " ".join(lradd)
  # Traverse through the address parts
  #for word in lst:
    # Determine if the address part is the
    # house number or part of the street name

  # Does anything else need to be done 
  # before returning the result?
  
  # Return the formatted string  
  return "house number {} on street named {}".format(hnum,radd)

print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"

2.

