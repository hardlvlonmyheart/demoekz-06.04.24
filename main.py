import flet
import flet as ft
from src.database.models import *
from src.client.auth_component import AuthComponent

def on_login_click(event: flet.ControlEvent, doctor_id, auth_component, patient_data_component, page):
    user = UserLogin.get_or_none(UserLogin.login == auth_component.login_field.value, UserLogin.password == auth_component.password_field.value)

    if user:
        doctor_id = user.id
        auth_component.visible = False
        patient_data_component.visible = True
        page.update()
    else:
        print('Неверные данные')

def show_client_data(event: flet.ControlEvent, patient_data_component, page):
    data = Patient.get(Patient.fullname == patient_data_component.controls[0].value)
    alert_dialog = flet.AlertDialog(content=flet.Text(data.__dict__.values()))
    page.dialog = alert_dialog
    alert_dialog.open = True
    page.update()

def show_records(event: flet.ControlEvent, doctor_id, patient_data_component, page):
    if doctor_id == 0:
        return

    data = Patient.get(Patient.fullname == patient_data_component.controls[0].value)
    doctor = Staff.get_by_id(doctor_id)
    record = Services.select().where(Services.doctor == doctor, Services.patient_id == data)
    d = [s.__dict__ for s in record]
    
    alert_dialog = flet.AlertDialog(content=flet.Text(str(d)))
    page.dialog = alert_dialog
    alert_dialog.open = True
    page.update()

def main(page: ft.Page):
    doctor_id = 0

    auth_component = AuthComponent()
    auth_component.login_button.on_click = lambda event: on_login_click(event, doctor_id, auth_component, patient_data_component, page)

    patient_data_component = flet.Column(
        controls = [
            flet.TextField(label='Имя пациента'),
            flet.Row(
                alignment = flet.MainAxisAlignment.CENTER,
                controls = [flet.FilledButton(text='Показать информацию', on_click = lambda event: show_client_data(event, patient_data_component, page))]
            ),
            flet.Row(
                alignment = flet.MainAxisAlignment.CENTER,
                controls = [flet.FilledButton(text='Просмотр записей пациентов', on_click = lambda event: show_records(event, doctor_id, patient_data_component, page))]
            )
        ],
        visible = False,
        alignment = flet.MainAxisAlignment.CENTER
    )

    page.window_width = 800
    page.window_height = 600
    page.vertical_alignment = flet.MainAxisAlignment.CENTER
    page.horizontal_alignment = flet.CrossAxisAlignment.CENTER

    page.add(
        flet.Column(
            controls = [auth_component, patient_data_component]
        )
    )

    ft.app(main, page)