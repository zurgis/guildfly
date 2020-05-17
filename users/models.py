from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from PIL import Image

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE, 
        verbose_name=_('user')
    )
    image = models.ImageField(
        _('Image'), 
        default='default.jpg', 
        upload_to='profile_pics'
    )
    
    def __str__(self):
        return f'{self.user.username} profile'
    
    def save(self, force_insert=False, 
        force_update=False, 
        using=None,
        update_fields=None
    ):
        # Переопределяем метод, чтобы задать соответствующие
        # значения картинке
        super().save()
        
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image. path)