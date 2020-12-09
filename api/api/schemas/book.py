from ...models import Book
from ...extensions import ma, db


class BookSchema(ma.SQLAlchemyAutoSchema):

    id = ma.Int(dump_only=True)

    class Meta:
        model = Book
        sqla_session = db.session
        load_instance = True
