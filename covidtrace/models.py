from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class MyAccountManager(BaseUserManager):

    def create_user(self, user_email, user_username, password=None):
        if not user_email:
            raise ValueError("Users must have a email")
        if not user_username:
            raise ValueError("Users must have a username")
        user = self.model(
            user_email = self.normalize_email(user_email),
            user_username =user_username,
            password = password
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_username, user_email, password):
        user = self.create_user(
            user_email = self.normalize_email(user_email),
            user_username =user_username,
            password = password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Sys_user(AbstractBaseUser):

    user_id = models.CharField(max_length=250, null=True)
    user_fname = models.CharField(max_length=250, null=True)
    user_lname = models.CharField(max_length=250, null=True)
    user_barangay_address = models.CharField(max_length=250, null=True)
    user_citymun_address = models.CharField(max_length=250, null=True)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True, null=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    user_username = models.CharField(max_length=250, null=True, unique=True)
    user_email = models.EmailField(verbose_name="email", max_length=255, unique=True)


    USERNAME_FIELD = "user_username"
    REQUIRED_FIELDS = ["user_email"]

    # There is a provided explanation for each user type level in the main directory

    user_types = (

        ("Level 0", "Level 0"),
        ("Level 1", "Level 1"),
        ("Level 2", "Level 2"),
        ("Level 3", "Level 3"),

    )
    user_type = models.CharField(max_length=250, null= True, choices= user_types)

    objects = MyAccountManager()

    def __str__(self):
        return self.user_username


    def has_perm (self, perm, obj = None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

class Establishment (models.Model):
    establishment_id = models.CharField(max_length=250, null=True)
    establishment_name = models.CharField(max_length=250, null=True)
    establishment_barangay = models.CharField(max_length=250, null=True)
    establishment_citymun = models.CharField(max_length=250, null=True)
    establishment_owner_name = models.CharField(max_length=250, null=True)
    establishment_owner_id = models.CharField(max_length=250, null=True)

    establishment_types = (

        ("Government", "Government"),
        ("Commercial", "Commercial"),
        ("Non-profit", "Non-profit"),
        ("Educational", "Educational"),
        ("Others", "Others"),

    )
    establishment_type = models.CharField(max_length=250, null= True, choices= establishment_types)
    def __str__(self):
        return self.establishment_name

class Visitor (models.Model):
    visitor_id = models.CharField(max_length=250, null=True)
    visitor_fname = models.CharField(max_length=250, null=True)
    visitor_lname = models.CharField(max_length=250, null=True)
    visitor_barangay_address = models.CharField(max_length=250, null=True)
    visitor_citymun_address = models.CharField(max_length=250, null=True)
    visitor_contact_no = models.CharField(max_length=250, null=True)
    visitor_email = models.EmailField
    visitor_visit_date = models.DateTimeField

    def __str__(self):
        return self.visitor_id

class Citymun(models.Model):
    cmdesc = models.CharField(max_length=250, null=True)
    latitude = models.FloatField(max_length=12, null=True)
    longitude = models.FloatField(max_length=12, null=True)
    remarks = models.CharField(max_length=500, null=True)
    CMCLASS = (

        ("City", "City"),
        ("Municipality", "Municipality")

    )
    cmclass = models.CharField(max_length=250, null=True, choices=CMCLASS)

    def __str__(self):
        return self.cmdesc

class Barangay(models.Model):
    bname = models.CharField(max_length=250, null=True)
    latitude = models.FloatField(max_length=12, null=True)
    longitude = models.FloatField(max_length=12, null=True)
    estpop = models.IntegerField(null=True)
    blevel = models.IntegerField(null=True)
    remarks = models.CharField(max_length=500, null=True)
    # citymun = models.ForeignKey(Citymun, on_delete=models.CASCADE, null = True)

    def __str__(self):
        return self.bname