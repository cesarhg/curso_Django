from django.contrib.auth.models import BaseUserManager

class UsuarioManager(BaseUserManager):
    def create_user(self, usuario, password=None):
        if not usuario:
            raise ValueError('Debes elegir un nombre')

        user = self.model(usuario=usuario)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, usuario, password):
        user = self.create_user(usuario, password)
        user.perfil = 'Administrador'
        user.administrador = True
        user.is_superuser = True
        user.save(using=self._db)
        return user