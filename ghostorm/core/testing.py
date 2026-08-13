from ghostorm.core.column import Column
from ghostorm.orm.instance_state import InstanceState
from ghostorm.types import Integer, String
from ghostorm.core.table import Table
from ghostorm.core.metadata import metadata
from ghostorm.core.model import Model
from ghostorm.core.registry import registry
from ghostorm.core.relationship import  RelationshipProperty
from ghostorm.core.mapper import Mapper
from ghostorm.orm.session import session
from ghostorm.orm.identity_map import IdentityMap
from ghostorm.engine.engine import Engine

class User(Model):
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
class Posts(Model):
    id = Column(Integer, primary_key=False)

engine = Engine()
row = engine.select_by_primary_key("user", 1)

mapper = Mapper(User)
user = mapper.load(row)
print(user.id)
print(user.username)
print(user.age)
print(user.__dict__)
#
# identity_maps = IdentityMap()
# user = User()
# user.id = 2
# identity_maps.add(user)
# print(identity_maps.get(User, 2))
# print(type(identity_maps))
# u = User()
# u.id = 2
# u.id = 3
# print(u._state.session)
# session.add(u)
# print(session.new)
# u.id = 4
# print(session.dirty)

# print(state.original)
# print(state.current)
# print(state.modified)
# print(u._state.dirty)



# users = Table("users")
# mapper = Mapper(User, users)
# print(mapper.class_)
# print(mapper.table.name)
# # registry.register(User)
# rel = RelationshipProperty('User')
# rel.resolve()
# print(rel.target_class)

# u = User()
#
# users = Table("users")
# metadata.register_table(users)
# id_column = Column(Integer, primary_key=True)
# id_column.name = "id"
# users.add_column(id_column)

# print(metadata.tables)


