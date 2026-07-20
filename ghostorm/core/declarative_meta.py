from ghostorm.core.column import Column
from ghostorm.core.table import Table
from ghostorm.core.metadata import metadata
from ghostorm.core.registry import registry
from ghostorm.core.mapper import Mapper

class DeclarativeMeta(type):
    def __new__(cls, name, bases, attrs):

#         hey guys this is metaclass I created for you , this can create another class
        new_class = super().__new__(cls, name, bases, attrs)
        if name == "Model": #  I did this because we don't want the base class to be a Table
            return new_class

        mapper = Mapper(new_class)

        metadata.register_table(mapper.table)

        registry.register(mapper)
        return new_class


