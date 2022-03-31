from django.test import TestCase

from guia_servs_clima.core.models import User


class UserTestCase(TestCase):

    def test_create_user(self):
        User.objects.create_user(email='projeto@incrivel.com', password='incrivelmesmo')
        self.assertEquals(User.objects.count(), 1)

    def test_if_user_isnot_superuser(self):
        user = User.objects.create_user(email='projeto@incrivel.com', password='incrivelmesmo')
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User.objects.create_superuser(email='projeto@superincrivel.com', password='superincrivelmesmo')
        self.assertEquals(User.objects.count(), 1)

    def test_if_superuser_is_superuser(self):
        user = User.objects.create_superuser(email='projeto@superincrivel.com', password='superincrivelmesmo')
        self.assertTrue(user.is_superuser)

    def test_create_user_sem_email(self):
        """
        TESTE DE CREATE USER SEM EMAIL
        """
        with self.assertRaises(ValueError):
            User.objects.create_user(email=None)

    def test_str_function(self):
        """
        TESTE MÉTODO __str__
        """
        email = "projeto@incrivel.com"
        password = "incrivelmesmo"
        user = User.objects.create_user(email=email, password=password)
        self.assertEquals(user.__str__(), email)

    def test_get_full_name(self):
        """
        TESTE MÉTODO GET_FULL_NAME
        """
        email = "projeto@incrivel.com"
        password = "incrivelmesmo"
        name = "usuarioincrivel"
        user = User.objects.create_user(
            email=email, password=password, name=name
        )

        self.assertEquals(user.get_full_name(), name)

    def test_get_short_name(self):
        """
        TESTE MÉTODO GET_SHORT_NAME
        """
        email = "projeto@incrivel.com"
        password = "incrivelmesmo"
        name = "Usuário Incrível"
        user = User.objects.create_user(
            email=email, password=password, name=name
        )

        self.assertEquals(user.get_short_name(), name.split(" ")[0])

    def test_get_username(self):
        """
        TESTE MÉTODO GET_USERNAME
        """
        email = "projeto@incrivel.com"
        password = "incrivelmesmo"
        name = "Usuário Incrível"
        user = User.objects.create_user(
            email=email, password=password, name=name
        )

        self.assertEquals(user.get_username(), email)
