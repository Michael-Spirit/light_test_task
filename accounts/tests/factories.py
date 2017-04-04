import factory

from django.contrib.auth.models import User


class UserFactory(factory.django.DjangoModelFactory):
    email = factory.Sequence(lambda n: 'user%s@example.com' % n)
    username = factory.Faker('first_name')
    password = factory.PostGenerationMethodCall('set_password', 'password')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    is_staff = False
    is_active = True

    class Meta:
        model = User
        django_get_or_create = ('email',)


class AdminFactory(UserFactory):
    email = 'admin@admin.com'
    is_superuser = True
