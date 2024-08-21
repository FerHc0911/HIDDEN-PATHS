from django.db import models
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from tours.models import Tours
from tours.models import Review
from django.contrib.auth.models import User


# Create your models here.

class TourBooking(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    numero_telefonico = models.CharField(max_length=15)
    fecha = models.DateField()
    hora = models.TimeField()
    num_personas = models.PositiveIntegerField()
    tipo_tour = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.nombre} - {self.fecha} - {self.hora}"


# Vista para iniciar el proceso de restablecimiento de contraseña
class CustomPasswordResetView(PasswordResetView):
    template_name = 'Registros/password_reset_form.html'
    email_template_name = 'Registros/password_reset_email.html'
    success_url = 'password_reset_done'

# Vista para confirmar que el correo de restablecimiento ha sido enviado
class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'Registros/password_reset_done.html'

# Vista para ingresar la nueva contraseña
class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'Registros/password_reset_confirm.html'
    success_url = 'password_reset_complete'

# Vista que confirma que la contraseña ha sido cambiada exitosamente
class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'Registros/password_reset_complete.html'

    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Añade campos adicionales si es necesario
    birthdate = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username
    
