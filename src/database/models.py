import peewee

database = peewee.SqliteDatabase('src/database/database.db')


class BaseModel(peewee.Model):
    class Meta:
        database = database


class UserLogin(BaseModel):
    username = peewee.CharField()
    password = peewee.CharField()


class Patient(BaseModel):
    full_name = peewee.CharField()
    passport = peewee.IntegerField()
    birth_date = peewee.DateField()
    gender = peewee.CharField()
    address = peewee.CharField()
    phone_number = peewee.IntegerField()
    email = peewee.CharField()
    last_visit_date = peewee.DateTimeField()
    polis_id = peewee.IntegerField()


class MedicalPolis(BaseModel):
    patient = peewee.ForeignKeyField(Patient, related_name='patient_polis')
    polis_id = peewee.IntegerField()
    polis_end_date = peewee.DateField()


class MedicalCard(BaseModel):
    patient = peewee.ForeignKeyField(Patient, related_name='patient_medical_card')
    card_id = peewee.IntegerField()
    created_date = peewee.DateField()


class Staff(BaseModel):
    user_login = peewee.ForeignKeyField(UserLogin, related_name='staff_user')
    full_name = peewee.CharField()


class Services(BaseModel):
    patient = peewee.ForeignKeyField(Patient, related_name='patient_services')
    date = peewee.DateField()
    doctor = peewee.ForeignKeyField(Staff, related_name='doctor_services')
    service_type = peewee.CharField()
    service_name = peewee.CharField()
    result = peewee.TextField()


database.create_tables([
    UserLogin,
    Patient,
    MedicalPolis,
    MedicalCard,
    Staff,
    Services
])