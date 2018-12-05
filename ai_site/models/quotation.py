from ai_site import db


class Quotation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(50), nullable=False)
    position = db.Column(db.String(50), nullable=False)
    text = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(20), nullable=False, default='default.jpg')

    def __repr__(self):
        return f"Quotation('{self.author}', '{self.position}', '{self.text}')"
