class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    @classmethod
    def from_list1(cls):
        print(younghoon.name, younghoon.email, younghoon.password)

    @classmethod
    def from_list2(cls):
        print(younsoo.name, younsoo.email, younsoo.password)


younghoon = User("Kang", "young@codrit.kr", "123456")
younsoo = User("lee", "yoonsoo@codeit.kr", "112233")

User.from_list1()
User.from_list2()
