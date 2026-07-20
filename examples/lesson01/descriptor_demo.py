class GhostDescriptor:
    def __get__(self, instance, owner):
        print("you are inside __get__")
        print(f"instance: {instance}")
        print(f"owner: {owner}")
        print(type(instance))
        print(type(owner))
        print(id(instance))
        print(id(owner))

        return "Ghost Descriptor"

    def __set__(self, instance, value):
        print("you are inside __set__")
        print(f"instance: {instance}")
        print(f"value: {value}")


class User:
    name = GhostDescriptor()


u = User()
u.name = "hackerX"
# print(u.name)
# print(User.name)