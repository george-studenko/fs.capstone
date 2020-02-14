from backend.models.db_config import db

class Category(db.Model):
    __tablename__ = 'Category'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    slug = db.column(db.String)
    language = db.relationship('language', backref='Language')

    def __init__(self, name, description, slug, language):
        self.language = language
        self.slug = slug
        self.name = name
        self.description = description

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'slug': self.slug,
            'language': self.language
        }