import flet as ft

from licloud.icloud.api import login

class User:
    def __init__(self) -> None:
        self.account = None

def main(page: ft.Page):
    user = User()
    email = ft.TextField(label="Email")
    password = ft.TextField(label="Password", password=True, can_reveal_password=True)

    def login_page(e):
        if not email.value:
            email.error_text = "Please enter your email"
            page.update()
        elif not password.value:
            password.error_text = "Please enter your password"
            page.update()
        else:
            try:
                user.account = login(email=email.value, password=password.value)
                page.go("/home")
            except Exception as e:
                page.add(ft.Text(f"There was an error when logging in: {str(e)}"))


    def route_change(route):
        page.views.clear()  # CLEAR THE VIEWS
        page.views.append(  # BUILD THE VIEW 1
            ft.View(
                route='/',
                controls=[
                    email, password,
                    ft.ElevatedButton("Login", on_click=login_page)
                ]
            )
        )
        if page.route == "/home":
            page.views.append(  # BUILD THE VIEW 2
                ft.View(
                    route='/home',
                    controls=[ft.Text("test")]
                )
            )
        page.update()

    page.on_route_change = route_change
    page.go(page.route)

ft.app(target=main)