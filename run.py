from app import create_app, db
from app.models import Product

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

       if not Product.query.first():
            print("Adding initial products...")
            p1 = Product(name="Laptop", price=50000.00, description="A powerful laptop for work and gaming.")
            p2 = Product(name="Wireless Mouse", price=450.50, description="Ergonomic mouse with a long battery life.")
            p3 = Product(name="Keyboard", price=750.00, description="Mechanical keyboard with custom RGB lighting.")
            p4 = Product(name="Moniter", price=2750.00, description="4k 15.6inch moniter with Wifi options.")
            p5 = Product(name="Webcam", price=60.00, description="Full HD webcam with a built-in microphone.")


            db.session.add(p1)
            db.session.commit()
            print("Initial products added!")

    app.run(debug=True)
