import factory

from accounts.tests.factories import UserFactory
from data.models import Message


class MessageFactory(factory.django.DjangoModelFactory):
    author = factory.SubFactory(UserFactory)
    text = factory.Faker('text')

    class Meta:
        model = Message
