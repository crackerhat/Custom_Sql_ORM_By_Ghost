class InstrumentedList(list):
    def __init__(self, owner, relationship):
        super().__init__()
        self.owner = owner
        self.relationship = relationship

    def append(self, item):
        if item in self:
            return
        super().append(item)

        reverse_name = self.relationship.back_populates
        if reverse_name:
            setattr(item, reverse_name, self.owner)
    def remove(self, item):
        super().remove(item)
        reverse_name = self.relationship.back_populates

        if reverse_name:
            setattr(item, reverse_name, None)