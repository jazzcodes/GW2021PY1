class User:

    def __init__(self, uid, name, phone):
        self.uid = uid
        self.name = name
        self.phone = phone

    def show(self):
        print("User Details:", self.uid, self.name, self.phone)


def main():
    print(vars(User))
    user1 = User(uid=991, name="John", phone="+91 99999 11111")

    # user1.show() # this is translated into ->  User.show(user1)
    User.show(user1)

if __name__ == '__main__':
    main()