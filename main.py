import flet as ft   #Biblioteca usada

#Página principal
def main(page: ft.Page):
    page.bgcolor = '#000'
    page.window_resizable = False
    page.window_width = 300
    page.window_height = 450
    page.title = 'Calculadora'
    page.window_always_on_top = True
    
    #Resultado das operações
    resultado = ft.Text(value="0", color='FFFFFF', size=20)
    
    display = ft.Row(
        width=300,
        controls=[resultado],
        alignment='end'
    )
    page.add(display)





ft.app(target = main)