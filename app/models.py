from sqlalchemy import Column, Integer, String, Boolean, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from flask import redirect, abort
from flask_admin.contrib.sqla import ModelView
from flask_admin import BaseView, expose
from flask_login import UserMixin, current_user, logout_user
from app import db, admin


class User(db.Model, UserMixin):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    is_active = Column(Boolean, default=False)
    username = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    bookBorrowSlips = relationship('BookBorrowSlip', backref='user', lazy=True)

    def __str__(self):
        return self.name


class BookBorrowSlip(db.Model):
    __tablename__ = "bookBorrowSlip"

    id = Column(Integer, primary_key=True, autoincrement=True)
    createdDate = Column(Date, nullable=False)
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    books = relationship('Book', backref='bookBorrowSlip', lazy=True)


class Book(db.Model):
    __tablename__ = "book"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)
    price = Column(Float, default=0)
    importedDate = Column(Date, nullable=False)
    bookBorrowSlip_id = Column(Integer, ForeignKey(BookBorrowSlip.id), nullable=True)

    def __str__(self):
        return self.name


class LogoutView(BaseView):
    @expose("/")
    def index(self):
        logout_user()
        return redirect("/")


class Controller(ModelView):
    column_searchable_list = ['name', 'username']
    column_display_pk = True
    can_export = True


class AboutUsView(BaseView):
    @expose('/')
    def __index__(self):
        return self.render('/about-us.html')


admin.add_view(Controller(User, db.session))
admin.add_view(ModelView(BookBorrowSlip, db.session))
admin.add_view(ModelView(Book, db.session))
admin.add_view(LogoutView(name="Logout"))
admin.add_view(AboutUsView(name='About us'))

if __name__ == "__main__":
    db.create_all()
