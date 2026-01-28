from app.models.member import Member


class Student(Member):
    @property
    def borrow_limit(self):
        return 2
