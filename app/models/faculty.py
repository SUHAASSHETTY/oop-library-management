from app.models.member import Member


class Faculty(Member):
    @property
    def borrow_limit(self):
        return 5
