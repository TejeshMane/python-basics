# from cryptography.fernet import Fernet

# # def write_key():
# #     key = Fernet.generate_key()
# #     with open("key.key", "wb") as key_file:
# #         key_file.write(key)


# def load_key():
#     file = open("key.key", "rb")
#     key = file.read()
#     file.close()
#     return key


# mstpwd = input("Enter the MasterPassword : ")
# key = load_key() + mstpwd.bytes
# fer = Fernet(key)


# def view():
#     with open("password.txt", "r") as f:
#         for line in f.readlines():
#             data = line.rstrip()
#             user, passw = data.split("|")
#             print(f"User : {user} | password : {passw} ")


# def add():
#     account = input("Enter account name: ")
#     pwd = input("Enter the pwd for this account: ")
#     with open("password.txt", "a") as f:
#         f.write(f"{account}|{pwd}\n")


# while True:
#     mode = input(
#         "you want to view pwd or add new one select (view/add) ? enter q to quit the program : "
#     ).lower()
#     if mode == "q":
#         break
#     if mode == "add":
#         add()
#     elif mode == "view":
#         view()
#     else:
#         print("Not a valid option.choose valid option")
#         continue
