from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


DEFAULT_IMAGE = "https://tinyurl.com/demo-cupcake"


class Cupcake(db.Model):
    __tablename__ = "cupcakes"

    id = db.Column(db.Integer, 
                   primary_key=True,
                   autoincrement=True)
    
    flavor = db.Column(db.Text,
                     nullable=False,)
    
    size = db.Column(db.Text,
                        nullable=False)
              
    image = db.Column(db.Text,
                       nullable= True
                       )           
    rating = db.Column(db.Float,
                    nullable=True)
    
          
    
    def image_url(self):
        """Returns image for cupcake"""

        return self.image or DEFAULT_IMAGE
    
    def to_dict(self):
        """Adds cupcake to a dictionary."""

        return {
            "id": self.id,
            "flavor": self.flavor,
            "rating": self.rating,
            "size": self.size,
            "image": self.image,
        }
    
def connect_db(app):
        """Connect database to app"""

        db.app = app
        db.init_app(app)

