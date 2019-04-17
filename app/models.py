from app.extensions import db
import os


class Base(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    create_time = db.Column(db.DateTime, server_default=db.func.now())
    modified_time = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())
    delete_time = db.Column(db.DateTime, nullable=True)


class Image(Base):
    __tablename__ = "image"
    url = db.Column(db.String(255), nullable=False)
    img_id = db.Column(db.Integer)
    bookmarked = db.Column(db.Integer, server_default='0')
    file_name = db.Column(db.String(255), nullable=False)

    @property
    def real_url(self):
        return "https:" + self.url

    @property
    def thumbnail_name(self):
        return 'thumbnail_' + self.file_name

    @property
    def image_url(self):
        return os.getenv('QINIU_DOMAIN') + self.file_name

    @property
    def thumbnail_url(self):
        return os.getenv('QINIU_DOMAIN') + self.thumbnail_name
