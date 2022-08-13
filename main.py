# This is a sample Python script.
import hashlib
import asyncio




# async def async_main():
#     engine = create_async_engine("postgresql+asyncpg://scott:tiger@localhost/test",
#                                  echo=True, )
#
#     async with engine.begin() as conn:
#         await conn.rum_sync(meta.drop_all)
#         await conn.rum_sync(meta.create_all)
#
#         await conn.execute


def signup():
    # user_name = input("Enter user name: ")
    email = input("Enter email: ")
    password = input("Enter Password: ")
    confirm_password = input("Enter password again: ")

    if confirm_password == password:
        enc = confirm_password.encode()
        hash1 = hashlib.md5(enc).hexdigest()
        print(hash1)
        with open("credentials.txt", "w") as f:
            # f.write(user_name)
            f.write(email + "\n")
            f.write(hash1)
        f.close()
        print("You have registered successfully")

    else:
        print("Password is not same as above! \n")


def login():
    email = input("Enter email: ")
    password = input("Enter Password: ")

    auth = password.encode()
    auth_hash = hashlib.md5(auth).hexdigest()
    with open("credentials.txt", "r") as f:
        stored_email, stored_password = f.read().split("\n")
    f.close()

    print(email)
    if email == stored_email and auth_hash == stored_password:
        print("Logged in successfully!")
    else:
        print("Login failed! \n")


# Press the green button in the gutter to run the script.

if __name__ == '__main__':
    # login()
    # signup()
    while 1:
        print("********** Login System **********")
        print("1.Signup")
        print("2.Login")
        print("3.Exit")
        ch = int(input("Enter your choice: "))
        if ch == 1:
            signup()
        elif ch == 2:
            login()
        elif ch == 3:
            break
        else:
            print("Wrong Choice!")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
