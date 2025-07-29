from mongoengine import Document, StringField, FloatField

class Job(Document):
    title = StringField(required=True, max_length=200)
    description = StringField(required=True)
    budget = FloatField(required=True)
    country = StringField(required=True, max_length=100)
