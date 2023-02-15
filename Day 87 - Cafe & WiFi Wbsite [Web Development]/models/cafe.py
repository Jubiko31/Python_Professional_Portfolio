from db import db

class CafeModel(db.Model):
    __tablename__ = "cafes"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    open_time = db.Column(db.String(10), nullable=False)
    close_time = db.Column(db.String(10), nullable=False)
    coffee = db.Column(db.Integer, nullable=False)
    wifi = db.Column(db.Integer, nullable=False)
    power = db.Column(db.Integer, nullable=False)
    
    @classmethod
    def to_dictionary(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}
    
    @classmethod
    def find_by_id(cls, id):
        return cls.query.get(id)
    
    @classmethod
    def find_all(cls):
        return cls.query.all()
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()