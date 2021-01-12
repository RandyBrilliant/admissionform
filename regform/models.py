from django.db import models
from django_countries.fields import CountryField


# Create your models here.
class StudyProgram(models.Model):
    BUSINESS = "BA"
    TECHNOLOGY = "TI"
    HOTEL = "HM"
    TYPE = [
        (BUSINESS, 'Business'),
        (TECHNOLOGY, 'Technology'),
        (HOTEL, 'Hotel Management'),
    ]

    major = models.CharField(max_length=30)
    description = models.TextField()
    category = models.CharField(
        max_length=2,
        choices=TYPE,
    )
    image = models.ImageField(default="default.jpg", upload_to="major_pics")

    def __str__(self):
        return self.major


class StudentData(models.Model):
    MALE = "MA"
    FEMALE = "FE"
    OTHER = "OT"
    GENDER = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
    ]

    BUDDHA = "BU"
    PROTESTAN = "KP"
    KATOLIK = "KK"
    HINDU = "HI"
    ISLAM = "IS"
    RELIGION = [
        (BUDDHA, "Buddha"),
        (PROTESTAN, "Kristen Protestan"),
        (KATOLIK, "Kristen Katolik"),
        (HINDU, "Hindu"),
        (ISLAM, "Islam"),
        (OTHER, 'Other'),
    ]

    ALIVE = "AL"
    DEATH = "DT"
    MORTALITY = [
        (ALIVE, "Alive"),
        (DEATH, "Deceased"),
    ]

    NOON = "NO"
    NIGHT = "NI"
    SCHEDULE = [
        (NOON, "Afternoon (05.00 PM)"),
        (NIGHT, "Evening (07.00 PM)"),
    ]

    NATIONAL = "NDP"
    JOINT = "JDP"
    GRADUATION = [
        (NATIONAL, "National Degree Program"),
        (JOINT, "Joint Degree Program"),
    ]

    first_name = models.CharField(max_length=50, verbose_name="First Name")
    last_name = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="Last Name")
    place_of_birth = models.CharField(
        max_length=50, verbose_name="Place of Birth")
    date_of_birth = models.DateField(verbose_name="Date of Birth")
    gender = models.CharField(
        max_length=2,
        choices=GENDER,
        verbose_name="Gender"
    )
    nationality = CountryField()
    religion = models.CharField(
        max_length=2,
        choices=RELIGION,
        verbose_name="Religion"
    )
    address = models.TextField()
    district = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=5, verbose_name="Postal Code")
    province = models.CharField(max_length=50)
    mobile_number = models.CharField(
        max_length=15, verbose_name="Phone Number")
    line_id = models.CharField(max_length=50, verbose_name="LINE ID")
    email = models.EmailField(
        max_length=254, primary_key=True, verbose_name="Email Address")
    whatsapp_no = models.CharField(
        max_length=15, verbose_name="Whatsapp Number")
    school_name = models.CharField(
        max_length=100, verbose_name="Former School Name")
    concentration = models.CharField(max_length=10)
    school_location = models.CharField(
        max_length=50, verbose_name="School Location")
    graduation_year = models.SmallIntegerField(verbose_name="Graduation Year")
    father_name = models.CharField(
        max_length=50, verbose_name="Father's Full Name")
    father_mobile_number = models.CharField(
        max_length=15, verbose_name="Father's Phone Number")
    father_mortality_status = models.CharField(
        max_length=2,
        choices=MORTALITY,
        verbose_name="Mortality Status"
    )
    father_address = models.TextField(verbose_name="Father's Address")
    mother_name = models.CharField(
        max_length=50, verbose_name="Mother's Full Name")
    mother_mobile_number = models.CharField(
        max_length=15, verbose_name="Mother's Phone Number")
    mother_mortality_status = models.CharField(
        max_length=2,
        choices=MORTALITY,
        verbose_name="Mortality Status"
    )
    mother_address = models.TextField(verbose_name="Mother's Address")
    guardian_name = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="Guardian's Full Name")
    guardian_mobile_number = models.CharField(
        max_length=15, blank=True, null=True, verbose_name="Guardian's Phone Number")
    guardian_mortality_status = models.CharField(
        max_length=2,
        choices=MORTALITY,
        blank=True,
        null=True,
        verbose_name="Mortality Status"
    )
    guardian_address = models.TextField(
        blank=True, null=True, verbose_name="Guardian's Address")
    study_program = models.ForeignKey(
        StudyProgram, on_delete=models.CASCADE, verbose_name="Study Program")
    schedule = models.CharField(
        max_length=2,
        choices=SCHEDULE,
        verbose_name="Class Schedule"
    )
    graduation_program = models.CharField(
        max_length=3,
        choices=GRADUATION,
        verbose_name="Graduation Program",
        blank=True,
        null=True
    )
    registration_paid = models.BooleanField(
        default=False, verbose_name="Registration Paid")
    register_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "(%s %s's Profile Data)" % (self.first_name, self.last_name)

    class Meta:
        # Add verbose name
        verbose_name = 'Student List'
