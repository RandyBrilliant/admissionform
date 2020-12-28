from django.contrib import admin
from regform.models import StudentData


# Register your models here.
class DateAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'gender', 'email', 'study_program', 'schedule', 'register_date')
    list_filter = ('study_program', 'gender')
    readonly_fields = ('register_date',)
    search_fields = ['first_name']

    fieldsets = [
        ('Personal Information', {'fields': [
            'first_name',
            'last_name',
            'place_of_birth',
            'date_of_birth',
            'gender',
            'nationality',
            'religion',
            'address',
            'district',
            'city',
            'postal_code',
            'province',
        ]}),
        ('Contact Info', {'fields': [
            'email',
            'mobile_number',
            'whatsapp_no',
            'line_id',
        ]}),
        ('Former School Information', {'fields': [
            'school_name',
            'concentration',
            'school_location',
            'graduation_year',
        ]}),
        ('Family Information', {'fields': [
            'father_name',
            'father_mobile_number',
            'father_mortality_status',
            'father_address',
            'mother_name',
            'mother_mobile_number',
            'mother_mortality_status',
            'mother_address',
            'guardian_name',
            'guardian_mobile_number',
            'guardian_mortality_status',
            'guardian_address',
        ]}),
        ('Study Information', {'fields': [
            'study_program',
            'schedule',
        ]}),
    ]

    def full_name(self, obj):
        return "{} {}".format(obj.first_name, obj.last_name)


admin.site.register(StudentData, DateAdmin)