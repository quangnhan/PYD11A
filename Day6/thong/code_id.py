import random


class CodeId:
    def __init__(self):
        self.unique_id_list = [1234]

    def create_id(self, initial):
        new_id = round(random.randint(1000, 9999))
        if new_id not in self.unique_id_list:
            self.unique_id_list.append(new_id)
        else:
            new_id = round(random.random() * 10000)
            self.unique_id_list.append(new_id)

        # print(self.unique_id_list)
        return f"{initial}{self.unique_id_list[-1]}"


if __name__ == "__main__":
    make_new_id = CodeId()

    print(make_new_id.create_id("TQT"))
    print(make_new_id.create_id("VQN"))
    print(make_new_id.create_id("TDT"))
    print(make_new_id.create_id("CVN"))


# test
# n = round(random.random() * 10000)
# print(n)
