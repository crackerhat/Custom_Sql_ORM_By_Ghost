_UNSET = object()
class AttributeState:
    def __init__(self):
        self.original = _UNSET
        self.current = _UNSET
        self.modified = False
    # we should have to use _UNSET instead of None to avoid bug
    def set_value(self, value):
        if self.original is _UNSET:
            self.original = value
        self.current = value
        if self.original != self.current:
            self.modified = True
        else:
            self.modified = False
        
