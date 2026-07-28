from ghostorm.core.declarative_meta import DeclarativeMeta
from ghostorm.orm.instance_state import InstanceState

class Model(metaclass=DeclarativeMeta):
    def __init__(self):
        self._state = InstanceState(self)

        

