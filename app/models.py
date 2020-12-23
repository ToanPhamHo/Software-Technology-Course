from sqlalchemy import Column, Integer, String, Boolean, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from flask import redirect, abort
from flask_admin.contrib.sqla import ModelView
from flask_admin import BaseView, expose
from flask_login import UserMixin, current_user, logout_user
from app import db, admin
from datetime import datetime


class User(db.Model, UserMixin):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    is_active = Column(Boolean, default=False)
    username = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    bookLists = relationship('BookList', backref='user', lazy=True)

    def __str__(self):
        return self.name


class Book(db.Model):
    __tablename__ = "book"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)
    quantity = Column(Integer, default=0)
    price = Column(Float, default=0)
    importedDate = Column(Date, nullable=False)
    book_details = relationship('BookListDetail', backref='book', lazy=True)

    def __str__(self):
        return self.name


class BookList(db.Model):
    __tablename__ = "bookList"

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_date = Column(Date, nullable=False, default=datetime.today())
    user_id = Column(Integer, ForeignKey(User.id))
    details = relationship('BookListDetail', backref='bookList', lazy=True)


class BookListDetail(db.Model):
    __tablename__ = "bookListDetail"

    id = Column(Integer, primary_key=True, autoincrement=True)
    createdDate = Column(Date, nullable=False)
    bookList_id = Column(Integer, ForeignKey(BookList.id))
    book_id = Column(Integer, ForeignKey(Book.id))
    quantity = Column(Integer, default=0)
    price = Column(Float, default=0)


class Review(db.Model):
    __tablename__ = "review"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    comment = Column(String(255), nullable=False)

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
admin.add_view(ModelView(Book, db.session))
admin.add_view(ModelView(BookList, db.session))
admin.add_view(ModelView(BookListDetail, db.session))
admin.add_view(AboutUsView(name='About us'))
admin.add_view(LogoutView(name="Logout"))


if __name__ == "__main__":
    db.create_all()
