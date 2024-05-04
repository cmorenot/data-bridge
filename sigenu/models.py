from django.db import models

# Create your models here.

from django.db import models

class Student(models.Model):
    
    # Datos personales
    id_student = models.CharField(primary_key=True, max_length=1024)
    identification = models.CharField(max_length=1024, blank=True, null=True)
    name = models.CharField(max_length=1024, blank=True, null=True)
    middle_name = models.CharField(max_length=1024, blank=True, null=True)
    last_name = models.CharField(max_length=1024, blank=True, null=True)
    native_of = models.CharField(max_length=1024, blank=True, null=True)
    birth_date = models.CharField(max_length=1024, blank=True, null=True)
    address = models.CharField(max_length=1024, blank=True, null=True)
    son_count = models.IntegerField(blank=True, null=True)
    phone = models.CharField(max_length=1024, blank=True, null=True)
    email = models.CharField(max_length=1024, blank=True, null=True)
    
    # Datos académicos
    higher_education_in_date = models.CharField(max_length=1024, blank=True, null=True)
    university_in_date = models.CharField(max_length=1024, blank=True, null=True)
    scale = models.FloatField(blank=True, null=True)
    academic_index = models.FloatField(blank=True, null=True)
    
    # Relaciones con otras entidades
    # country_fk = models.ForeignKey(Country, models.DO_NOTHING, db_column='country_fk')
    # student_type_fk = models.ForeignKey('StudentType', models.DO_NOTHING, db_column='student_type_fk')
    # career_fk = models.ForeignKey(Career, models.DO_NOTHING, db_column='career_fk', blank=True, null=True)
    # entry_source_fk = models.ForeignKey(EntrySource, models.DO_NOTHING, db_column='entry_source_fk')
    # course_type_fk = models.ForeignKey(CourseType, models.DO_NOTHING, db_column='course_type_fk')
    # scholastic_origin_fk = models.ForeignKey(ScholasticOrigin, models.DO_NOTHING, db_column='scholastic_origin_fk')
    # politic_org_fk = models.ForeignKey(PoliticOrg, models.DO_NOTHING, db_column='politic_org_fk')
    # sex_fk = models.ForeignKey(Sex, models.DO_NOTHING, db_column='sex_fk')
    # town_university_fk = models.ForeignKey('TownUniversity', models.DO_NOTHING, db_column='town_university_fk', blank=True, null=True)
    # marital_status_fk = models.ForeignKey(MaritalStatus, models.DO_NOTHING, db_column='marital_status_fk')
    # study_regimen_fk = models.ForeignKey('StudyRegimen', models.DO_NOTHING, db_column='study_regimen_fk')
    # academic_situation_fk = models.ForeignKey(AcademicSituation, models.DO_NOTHING, db_column='academic_situation_fk')
    # town_fk = models.ForeignKey('Town', models.DO_NOTHING, db_column='town_fk', blank=True, null=True)
    # skin_color_fk = models.ForeignKey(SkinColor, models.DO_NOTHING, db_column='skin_color_fk')
    # student_status_fk = models.ForeignKey('StudentStatus', models.DO_NOTHING, db_column='student_status_fk', blank=True, null=True)
    # faculty_fk = models.ForeignKey(Faculty, models.DO_NOTHING, db_column='faculty_fk', blank=True, null=True)
    # orphan_fk = models.ForeignKey(Orphan, models.DO_NOTHING, db_column='orphan_fk')
    
    # Campos de administración
    register_date = models.CharField(max_length=1024, blank=True, null=True)
    photo = models.CharField(max_length=1024, blank=True, null=True)
    reoffer = models.BooleanField(blank=True, null=True)
    option = models.IntegerField(blank=True, null=True)
    block = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student'
