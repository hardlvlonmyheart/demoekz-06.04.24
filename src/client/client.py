from flet import UserControl, FilledButton, TextField, Column, Row, TextButton, MainAxisAlignment


class AuthComponent(UserControl):
    login_button = FilledButton(text='Войти')
    login_field = TextField(label='Логин')
    password_field = TextField(label='Пароль', password=True, can_reveal_password=True)

    def build(self):
        login_page = Column(
            controls=[
                self.login_field,
                self.password_field,
                Row(
                    controls=[
                        self.login_button
                    ],
                    alignment=MainAxisAlignment.CENTER
                ),
                Row(
                    controls=[
                        TextButton(
                            text='Создать аккаунт'
                        )
                    ],
                    alignment=MainAxisAlignment.CENTER
                )
            ]
        )
        return login_page