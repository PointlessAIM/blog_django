from django.db import models
import datetime

# Create your models here.
class User(models.Model):
    first_name = models.CharField("user's name",max_length=30)
    last_name = models.CharField("user's last name",max_length=30)
    cars = models.ManyToManyField('Car', verbose_name="user's cars")

STATUS_CHOICES = (
    ('R', 'Reviewed'),
    ('N', 'Not Reviewed'),
    ('E', 'Error'),
    ('A', 'Accepted')
)

class Website(models.Model):
    name = models.CharField(max_length= 100)
    url = models.URLField(unique=True) #if there's a duplicate before you add the 'unique' field, it will throw an error
    release_date = models.DateField()
    rating = models.IntegerField()
    status = models.CharField(choices=STATUS_CHOICES, max_length=1)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def was_released_last_week(self):
        if self.release_date < datetime.date(2023,4,27):
            return "released last week"
        return "released this week"
    
    @property
    def get_full_name(self):
        return f"el nombre del sitio es: {self.name}"
    
    def __str__(self) -> str:
        return super().__str__()
    
    def get_absolute_url(self):
        return f"/websites/{self.id}"
    
    def save(self, *args, **kwargs):
        print ("saving...")
        super().save(*args, **kwargs)

class Car(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    

