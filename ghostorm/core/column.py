class Column:
    def __init__(self, type_, primary_key=False, nullable=True, default=None):
        self.name = None
        self.type_ = type_
        self.primary_key = primary_key
        self.nullable = nullable
        self.default = default


    def __set_name__(self, instance, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name, self.default)

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value









# def get_attribute(instance, name):
#
#     cls = type(instance)
#
#     # Step 1
#     class_attr = cls.__dict__.get(name)
#
#     # Step 2
#     # DATA DESCRIPTOR?
#
#     if hasattr(class_attr, "__get__") and (
#             hasattr(class_attr, "__set__")
#             or hasattr(class_attr, "__delete__")):
#
#         return class_attr.__get__(instance, cls)
#
#     # Step 3
#     # Instance dictionary
#
#     if name in instance.__dict__:
#
#         return instance.__dict__[name]
#
#     # Step 4
#     # NON DATA DESCRIPTOR
#
#     if hasattr(class_attr, "__get__"):
#
#         return class_attr.__get__(instance, cls)
#
#     # Step 5
#
#     return class_attr

