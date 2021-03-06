from django.db import models
from django.db.models import ImageField
from localflavor.us.models import USStateField, USZipCodeField, PhoneNumberField
from localflavor.us.us_states import STATE_CHOICES
from accounts.models import BaseAttornEaseUser


class LawCategory(models.Model):
    """
    Simple category information for the type of law practiced
    """
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class ServiceArea(models.Model):
    area = models.CharField(max_length=100)
    description = models.TextField(default=None, blank=True, null=True)
    state = USStateField(choices=STATE_CHOICES)

    def __str__(self):
        return self.area

class AttorneyUser(BaseAttornEaseUser):
    '''
    This is here because of a circular reference problem between the accounts app and the attorney app.
    Alternate method is to lazy load the foriegn key but this seems slightly cleaner.
    '''
    firm = models.CharField(max_length=100)
    phone = PhoneNumberField()
    website = models.URLField(default=None, blank=True, null=True)
    rate = models.DecimalField(max_digits=7, decimal_places=2)
    categories = models.ManyToManyField(LawCategory)
    service_areas = models.ManyToManyField(ServiceArea)
    school = models.CharField(max_length=50)
    year_started = models.IntegerField(default=2015)
    description = models.TextField()
    profile_pic = ImageField(default=None, null=True, blank=True)

    def is_complete(self):
        return self.categories.count() > 0 and self.license_set.count() > 0 and self.firmaddress_set.count() > 0

    def __str__(self):
        return "{first} {last}".format(first=self.first_name, last=self.last_name)

    def full_name(self):
        return self.first_name + " " + self.last_name

    def abridged(self):
        if len(self.description) < 150:
            desc = self.description
        else:
            desc = self.description[:150]
            desc = desc[:desc.rfind(".")+1]+"..."
        return desc


    class Meta:
        verbose_name="Attorney User"

class Attorney(models.Model):
    """
    Main attorney model
    """
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    firm = models.CharField(max_length=100)
    email = models.EmailField()
    phone = PhoneNumberField()
    website = models.URLField(default=None, blank=True)
    rate = models.DecimalField(max_digits=7, decimal_places=2)
    categories = models.ManyToManyField(LawCategory)
    service_areas = models.ManyToManyField(ServiceArea)
    school = models.CharField(max_length=50)
    year_started = models.IntegerField(default=2015)
    description = models.TextField()
    profile_pic = ImageField(default=None, null=True, blank=True)

    def is_complete(self):
        return self.categories.count() > 0 and self.license_set.count() > 0 and self.firmaddress_set.count() > 0

    def __str__(self):
        return "{first} {last}".format(first=self.first_name, last=self.last_name)

    def full_name(self):
        return self.first_name + " " + self.last_name

    def abridged(self):
        if len(self.description) < 150:
            desc = self.description
        else:
            desc = self.description[:150]
            desc = desc[:desc.rfind(".")+1]+"..."
        return desc


class License(models.Model):
    """
    License info for every state the attorney can practice
    """
    bar_number = models.CharField(max_length=50)
    year = models.IntegerField()
    state = USStateField(choices=STATE_CHOICES)
    attorney = models.ForeignKey(AttorneyUser)

    def __str__(self):
        return "{state} - {bar}".format(state=self.state, bar=self.bar_number)


class FirmAddress(models.Model):
    """
    Addresses of the firm offices
    """
    street = models.CharField(max_length=150)
    street2 = models.CharField(max_length=75)
    city = models.CharField(max_length=50)
    state = USStateField(choices=STATE_CHOICES)
    postal = USZipCodeField(db_index=True)
    attorney = models.ForeignKey(AttorneyUser)

    def __str__(self):
        return "{street} {street2}, {city} {state}, {postal}" \
            .format(street=self.street, street2=self.street2, city=self.city, state=self.state, postal=self.postal)


