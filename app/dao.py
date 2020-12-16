from app import app, db
from app.models import Book, User, BookBorrowSlip


def read_products(keyword=None):
    q = Book.query
    if keyword:
        q = q.filter(Book.name.contains(keyword))
    return q.all()


def read_user(email=None):
    a = User.query

    if email:
        a = a.filter(User.email.contains(email))
    return a.all()


def read_product_by_id(product_id):
    return Product.query.get(product_id)


def read_book_by_name(keyword=None):
    q = Book.query

    if keyword:
        q = q.filter(Book.name.contains(keyword))
    return q.all()


def add_user(name, email, is_active, username, password):
    new_user = User(name=name, email=email, is_active=is_active, username=username, password=password)
    db.session.add(new_user)
    db.session.commit()


def add_receipt(items):
    try:
        r = Orders()
        db.session.add(r)
        db.session.commit()

        for item in items:
            d = OrderDetail()
            d.quantity = item['quantity']
            d.price = item['price']
            d.product_id = item['id']
            d.receipt_id = r.id

            db.session.add(d)

        db.session.commit()
        return True
    except Exception as ex:
        print(ex)
        return False
