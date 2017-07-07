from django.db import models

# Create your models here.
class Schilderij(models.Model):
	beschrijving = models.CharField(max_length=500)
	formaat = models.CharField(max_length=500)
	image = models.ImageField(upload_to='img')
	zichtbaar = models.BooleanField(default=True)

	def __str__(self):
		return self.beschrijving + ", " + self.formaat
