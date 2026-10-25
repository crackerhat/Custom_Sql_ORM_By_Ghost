from ghostorm.core.column import Column
from ghostorm.orm.instance_state import InstanceState
from ghostorm.types import Integer, String
from ghostorm.core.table import Table
from ghostorm.core.metadata import metadata
from ghostorm.core.model import Model
from ghostorm.core.registry import registry
from ghostorm.core.relationship import  RelationshipProperty
from ghostorm.core.mapper import Mapper
from ghostorm.orm.session import Session
from ghostorm.orm.identity_map import IdentityMap
from ghostorm.engine.engine import Engine



class User(Model):
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
class Posts(Model):
    id = Column(Integer, primary_key=True)

engine = Engine("ghostorm_session_test.db")
metadata.create_all(engine)

session = Session(engine)

user = session.get(User, 1)
user.age = 50
session.commit()
print(session.dirty)
print(user.age)

# user = User()
# user.username = "Ghostorm"
# user.age = 22
# print(f"before add: {user.id}")
# session.add(user)
# session.commit()
#
# # users = session.query(User).filter(User.age > 20).all()
# # for user in users:
# #     print(user.id, user.age, user.username)
#
# user_leul = session.get(User, 2)
# print(user_leul)
# print(user_leul.id)
# print(user_leul.username)
# print(user_leul.age)

# user = User()
# user.username = "Ghostorm"
# user.age = 22
# print(f"before add: {user.id}")
# session.add(user)
# session.commit()
# print(f"after add or generated id : {user.id}")
#

# engine = Engine("testing.db")
#
# metadata.create_all(engine)
#
# cursor = engine.execute("PRAGMA table_info(user)")
# for column in cursor.fetchall():
#     print(column)
#
# engine.connection.close()

# condition = User.age > 20
# print(type(condition))
# print(condition.column)
# print(condition.value)
# print(condition.operator)

# user1 = session.get(User, 1)
# user2 = session.query(User).filter_by(id=1).all()
# user3 = session.query(User).filter_by(User.age > 20).all()
# print(user3)
# print(user1 is user2[0])
# for user in user2:
#     print(user.id)
# # users = session.query(User).filter_by(username='Ghost').all()
# # for user in users:
# #     print(user.id, user.username, user.age)


# users = session.query(User).all()
# for user in users:
#     print(user.id, user.username, user.age)

# user = session.get(User, 2)
# # print(f"before {user.__dict__}")
# print(f"\nidentity map: {session.identity_map._objects}")
# session.delete(user)
#
# print(f"deleted objects: {session.deleted}")
#
# session.commit()
#
# user_again = session.get(User, 2)
# print(f"again {user_again}")

# user = session.get(User, 1)
#
# print("Original:", user.username)
#
# user.username = "Changed"
#
# print("Changed:", user.username)
# print("Dirty:", session.dirty)
#
# session.rollback()
#
# print("After rollback:", user.username)
# print("Dirty:", session.dirty)
# print("State dirty:", user._state.dirty)

# user = User()
# user.id = 4
# user.username = "db-copper"
# user.age = 19
#
# session.add(user)
# print("before commit")
# print(session.new)
# session.commit()
# print("after commit")
# print(session.new)
#
# print(f'object identity: {user._state.identity}')
# print(f"dirty: {user._state.dirty}")

# user = session.get(User, 1)
# print(f"before changes: {user._state.dirty}")
# user.username = "leul"
# print(f"after changes: {user._state.dirty}")
#
# print(f"dirty list {session.dirty}")
# session.commit()
#
# print(f"after commit {user._state.dirty}")
# print(f"dirty list {session.dirty}")
# print(f"original: {user._state.attributes["username"].original}")
# print(f"Current: {user._state.attributes["username"].current}")


# user = session.get(User, 1)
# print(f"before {user.username}")
# user.username = "leul"
#
# session.commit()
#
# print(f"after {user.username}")
# print(session.dirty)

# user = session.get(User, 1)
# user.username = "Newname"
# print(user.username)
# print(user._state.dirty)
# print(session.dirty)



# user = session.get(User, 1)
# print(user._state.mapper)
# print(user._state.session)
# print(user._state.identity)
# print(user._state.dirty)
# user.id = 3
# print(user._state.dirty)


# new_user = session.get(User, 2)
# new_user2 = session.get(User, 2)
# print(new_user is new_user2)

# new_user = session.get(User, 1)
# print(new_user.id)
# print(new_user.username)

# new_user = User()
# new_user.id = 2
# session.add(new_user)
# user_2 = session.get(User, 2)
# user_2.id = 3
# print(session.dirty)
# print(session.new)

# engine = Engine()
# row = engine.select_by_primary_key("user", 1)
#
# mapper = Mapper(User)
# user = mapper.load(row)
# print(user.id)
# print(user.username)
# print(user.age)
# print(user.__dict__)
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


