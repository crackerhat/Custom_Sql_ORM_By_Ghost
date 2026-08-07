# guys we use identity map because when we take data from the database we don't need two memory represetations for same database identity for example if someone say user = session.get(User, 1) user2 = session.get(User, 1) we want them to be same not different object
class IdentityMap:
    def __init__(self):
        self._objects = {}


    def add(self, instance):
        key = (type(instance), instance.id)
        self._objects[key] = instance

    def get(self, cls, primary_key):
        key = (cls, primary_key)
        return self._objects[key]

