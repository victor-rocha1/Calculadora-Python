import flet as ft           #Biblioteca usada
from flet import colors     #Cores da biblioteca

botoes = [
    {'operador': 'AC', 'fonte': colors.BLACK, 'fundo': colors.BLUE_GREY_100 },
    {'operador': '+/-', 'fonte': colors.BLACK, 'fundo': colors.BLUE_GREY_100 },
    {'operador': '%', 'fonte': colors.BLACK, 'fundo': colors.BLUE_GREY_100 },
    {'operador': '/', 'fonte': colors.WHITE, 'fundo': colors.ORANGE },
    {'operador': '7', 'fonte': colors.WHITE, 'fundo': colors.WHITE24 },
    {'operador': '8', 'fonte': colors.WHITE, 'fundo': colors.WHITE24 },
    {'operador': '9', 'fonte': colors.WHITE, 'fundo': colors.WHITE24 },
    {'operador': '*', 'fonte': colors.WHITE, 'fundo': colors.ORANGE },
    {'operador': '4', 'fonte': colors.WHITE, 'fundo': colors.WHITE24 },
    {'operador': '5', 'fonte': colors.WHITE, 'fundo': colors.WHITE24 },
    {'operador': '6', 'fonte': colors.WHITE, 'fundo': colors.WHITE24 },
    {'operador': '-', 'fonte': colors.WHITE, 'fundo': colors.ORANGE },
    {'operador': '1', 'fonte': colors.WHITE, 'fundo': colors.WHITE24 },
    {'operador': '+', 'fonte': colors.WHITE, 'fundo': colors.ORANGE },
    {'operador': '0', 'fonte': colors.WHITE, 'fundo': colors.WHITE24 },
    {'operador': '.', 'fonte': colors.WHITE, 'fundo': colors.WHITE24 },
    {'operador': '=', 'fonte': colors.WHITE, 'fundo': colors.ORANGE },
]

#Página principal
def main(page: ft.Page):
    page.bgcolor = '#000'
    page.window_resizable = False
    page.window_width = 300
    page.window_height = 450
    page.title = 'Calculadora'
    page.window_always_on_top = True
    
    #Resultado das operações
    resultado = ft.Text(value="0", color='FFFFFF', size=40)
    
    display = ft.Row(
        width=300,
        controls=[resultado],
        alignment='end',
    )
    bt = [ft.Container(
        content=ft.Text(value=bt['operador'], color=bt['fonte'], size=20),
        width=55,
        height=55,
        bgcolor= bt['fundo'],
        border_radius=90,
        alignment=ft.alignment.center
    )for bt in botoes ]


    keyboard = ft.Row(
        width=250,
        wrap= True,
        controls=bt,
        alignment='end'

    )

    page.add(display,keyboard)





ft.app(target = main)