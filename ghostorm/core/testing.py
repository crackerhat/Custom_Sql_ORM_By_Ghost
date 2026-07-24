from ghostorm.core.column import Column
from ghostorm.orm.instance_state import InstanceState
from ghostorm.types import Integer, String
from ghostorm.core.table import Table
from ghostorm.core.metadata import metadata
from ghostorm.core.model import Model
from ghostorm.core.registry import registry
from ghostorm.core.relationship import  RelationshipProperty
from ghostorm.core.mapper import Mapper

class User(Model):
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
class Posts(Model):
    id = Column(Integer, primary_key=False)

u = User()
u.id = 2
print(u._state.dirty)
u.id = 3
state = u._state.get_attribute_state("id")

print(state.original)
print(state.current)
print(state.modified)
print(u._state.dirty)



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


