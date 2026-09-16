


class UnitOfWork:
    def __init__(self, session):
        self.session = session

    def collect_new(self):
        return self.session.new

    def collect_dirty(self):
        return self.session.dirty

    def collect_deleted(self):
        return self.session.deleted

    def show_operations(self):
        print(self.collect_new())
        print(self.collect_dirty())
        print(self.collect_deleted())