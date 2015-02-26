from project.tests.test_base import BaseTestCase
from project.models.person import Person
from project.tests.factories import PersonFactory
from project import db


class TestPerson(BaseTestCase):
    def test_model_creation(self):
        PersonFactory.create(name="John Doe")
        db.session.commit()
        person = Person.query.filter_by(name='John Doe').first()

        self.assertTrue(person.name == "John Doe")
