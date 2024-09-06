import flet as ft

# CSS Style

toggle_style_sheet: dict = { "icon": ft.icons.DARK_MODE_ROUNDED, "icon_size": 18}
add_style_sheet: dict = {"icon": ft.icons.ADD_ROUNDED, "icon_size": 18}

item_style_sheet: dict = {
    "height": 50,
    
}

todo_item_css: dict = {
    "height": 50,
    "border_radius": 4
}

item_css = {
    "color": "green"
}

# Create a class for each todo item

class TodoItem(ft.Container):
    def __init__(self, hero: object, description: str) -> None:
        super().__init__(**todo_item_css)
        
        self.hero = hero
        self.description = description
        
        self.tick = ft.Checkbox(on_change=lambda e: self.check_item(e))
        self.text: ft.Text = ft.Text(self.description)
        
        self.content = ft.Row(
            alignment="spaceBetween",
            controls=[
                ft.Row(
                    controls=[
                        self.tick,
                        self.text,
                        ft.Divider()
                    ]
                )
            ]
        )
        
    def check_item(self, e):
        if e.control.value is True:
            self.text.style = ft.TextStyle(decoration=ft.TextDecoration.LINE_THROUGH, decoration_thickness=2)
            
            self.hero.todo_area.controls.remove(self)
            self.hero.todo_area.update()
            
            self.hero.completed_area.controls.append(self)
            self.hero.completed_area.update()
    
        else:
            if e.control.value is False:
                self.hero.completed_area.controls.remove(self)
                self.hero.completed_area.update()
                
                self.hero.todo_area.controls.append(self)
                self.hero.todo_area.update()
                
            self.text.style = ft.TextStyle()

        self.text.update() 
# Main content area

class Hero(ft.SafeArea):
    def __init__(self, page: ft.Page) -> None:
        super().__init__(minimum_padding=10, maintain_bottom_view_padding=True, content=None)
        
        self.page = page
        
        self.title = ft.Text("ToDo List", size=20, weight=True)
        self.toggle = ft.IconButton(**toggle_style_sheet, on_click=lambda e: self.switch(e))
        
        self.box = ft.TextField(label="Add your tasks here")
        self.add = ft.IconButton(icon=ft.icons.ADD, icon_color="white", on_click=lambda e: self.add_item(e))
        
        self.todo_area = ft.Column(
            expand=True, 
            spacing=18,
            controls=[
                ft.Text("My Tasks", size=20),
                ft.Divider()
            ]
        )

        self.completed_area = ft.Column(
            expand=True,
            spacing=18,
            controls=[
                ft.Text("Completed Taks", size=20),
                ft.Divider()
            ]
            )
        
        self.main = ft.Column(
            controls= [
                ft.Row(
                    alignment="spaceBetween",
                    controls=[
                        self.title, 
                        self.toggle
                    ]
                ),
                ft.Divider(height=20),
                ft.Row(
                    alignment="spaceAround",
                    controls=[
                        self.box,
                        self.add,
                    ]
                ),
                self.todo_area,
                self.completed_area
            ]
        )
        
        self.content = self.main

    def switch(self, e):
        if self.page.theme_mode == ft.ThemeMode.DARK:
            self.page.theme_mode = ft.ThemeMode.LIGHT
            self.toggle.icon = ft.icons.LIGHT_MODE_ROUNDED
            self.add.icon_color = 'black'
            
        else: 
            self.page.theme_mode = ft.ThemeMode.DARK
            self.toggle.icon = ft.icons.DARK_MODE_ROUNDED
            self.add.icon_color = 'white'
            
        self.page.update()

    def add_item(self, e):
        if self.box.value != "":
            self.todo_area.controls.append(
                TodoItem(self, self.box.value)
            )
            self.todo_area.update()
            self.box.value = ""
            self.box.update()

        else:
            pass
        
    def move_item(self, e):
        pass
        
def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.DARK
    theme = ft.Theme()
    page.theme = theme
    
    hero: object = Hero(page)
    
    page.add(hero)
    page.update()

ft.app(main)
