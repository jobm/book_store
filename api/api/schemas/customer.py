from ...models import Customer
from ...extensions import ma, db


class CustomerSchema(ma.SQLAlchemyAutoSchema):

    id = ma.Int(dump_only=True)

    class Meta:
        model = Customer
        sqla_session = db.session
        load_instance = True
