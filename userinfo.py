def user_info(*names):
    print(names)
    for name,id in names:
     print(f"user name:{name}\n User id:{id}")
     print(f"user name:{name}")
     print(f"User id:{id}")
    

user = user_info(("bandana",20),("Binda", 50))
print(user)