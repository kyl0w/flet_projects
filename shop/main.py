import flet as ft

from flet import (
    ElevatedButton, 
    Page, 
    Text,
    View, 
    colors,
    Container,
    Icon,
    Page,
    Text,
    AppBar,
    PopupMenuButton,
    PopupMenuItem,
    colors,
    icons,
    margin
)

class Bar(ft.AppBar):
    def __init__(self, page: Page):
        super().__init__()
        
        self.page = page
        
        self.leading=Icon(icons.SHOP_2)
        self.leading_width=100
        self.title=Text(size=25, text_align="start")
        self.center_title=False
        self.toolbar_height=75
        self.bgcolor=colors.ORANGE
        self.actions=[
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text="Home", on_click=self.go_home),
                    ft.PopupMenuItem(text="Cart"),
                    ft.PopupMenuItem(text="Login", on_click=self.go_login),
                ]
            ),
        ]
        
    def go_home(self, e):
        self.page.route = '/'
        self.page.update()
          
    def go_login(self, e):
        self.page.route = '/auth'
        self.page.update()
    
    def go_cart(self, e):
        self.page.route = '/cart'
        self.page.update() 
    
class Main(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__()
        
        self.page = page
        
        self.appbar = Bar(page=page)
        self.title = ft.Text("SIMPLE STORE".upper(), size=20, weight="bold")
        self.subtitle = ft.Text("Made With Flet", size=11)
        
        self.menu = ft.Row(
                    wrap=True,
                    width=page.window.width,
                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                    controls=[
                        ft.Container(
                            content=ft.Text("Programado"),
                            alignment=ft.alignment.center,
                            bgcolor=ft.colors.AMBER,
                            width=100,
                            height=75,
                            border_radius=10,
                        ),
                        ft.Container(
                            content=ft.Text("Live"),
                            alignment=ft.alignment.center,
                            bgcolor=ft.colors.AMBER,
                            width=100,
                            height=75,
                            border_radius=10,
                        ),
                        ft.Container(
                            content=ft.Text("Reboques"),
                            alignment=ft.alignment.center,
                            bgcolor=ft.colors.AMBER,
                            width=100,
                            height=75,
                            border_radius=10,
                        ),
                        ft.Container(
                            content=ft.Text("Parques"),
                            alignment=ft.alignment.center,
                            bgcolor=ft.colors.AMBER,
                            width=100,
                            height=75,
                            border_radius=10,
                        )
                    ]
                )       
        
        self.product = ft.Container(
                    content=ft.Text("Non clickable"),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.AMBER,
                    width=page.window.width,
                    height=150,
                    border_radius=10,
        )
        
        self.controls = [
            self.appbar,
            self.title,
            self.subtitle,
            self.menu,
            self.product
        ]

class Auth(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__(horizontal_alignment="center")
        
        self.page = page
        
        self.appbar = Bar(page=page)
        
        self.controls = [
            self.appbar,
        ]
        
    def login(self):
        pass
    
    def register(self):
        pass
    
class Cart(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__()
        
        self.page = page
        self.appbar = Bar(page=page)
    
        self.controls = [
            self.appbar
        ]
        
def main(page: ft.Page):
    
    page.theme_mode = ft.ThemeMode.LIGHT
    
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    def route_change(route):
        page.views.clear()
        
        if page.route == "/":
            page.views.append(Main(page))
        
        if page.route == "/cart":
            page.views.append(Cart(page))
            
        if page.route == "/auth":
            page.views.append(Auth(page))
             
        page.update()

    page.on_route_change = route_change
    page.go(page.route)
    
ft.app(target=main, view=ft.AppView.WEB_BROWSER)
