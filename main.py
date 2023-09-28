import flet as ft           #Biblioteca usada
from flet import colors     #Cores da biblioteca

#Página principal
def main(page: ft.Page):
    page.bgcolor = '#000'
    page.window_resizable = False
    page.window_width = 290
    page.window_height = 440
    page.title = 'Calculadora'
    page.window_always_on_top = True
    
    #Resultado das operações
    resultado = ft.Text(value="0", color='FFFFFF', size=40)


    #Função para calcular
    def calculo():
        pass
    #Seleção de números e operações
    def select(e):
        valor_atual = resultado.value if resultado.value != '0' else ''
        value = e.control.content.value

        if value.isdigit():
            value = valor_atual+value
        elif value == 'AC':
            value='0'
        else:
            if valor_atual and valor_atual[-1] in ('+', '-', '/', '*', '.'):
                valor_atual = valor_atual[:-1]

            value = valor_atual+value

            if value[-1] in ('=', '%','+/-'):
                value = calculo()

        resultado.value = value
        resultado.update()


    display = ft.Row(
        width=290,
        controls=[resultado],
        alignment='end',
    )

    #Cor, fundo e texto dos botões
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
    {'operador': '2', 'fonte': colors.WHITE, 'fundo': colors.WHITE24 },
    {'operador': '3', 'fonte': colors.WHITE, 'fundo': colors.WHITE24 },
    {'operador': '+', 'fonte': colors.WHITE, 'fundo': colors.ORANGE },
    {'operador': '0', 'fonte': colors.WHITE, 'fundo': colors.WHITE24 },
    {'operador': '.', 'fonte': colors.WHITE, 'fundo': colors.WHITE24 },
    {'operador': '=', 'fonte': colors.WHITE, 'fundo': colors.ORANGE },
]
    

    bt = [ft.Container(
        content=ft.Text(value=bt['operador'], color=bt['fonte'], size=20),
        width=54,
        height=54,
        bgcolor= bt['fundo'],
        border_radius=90,
        alignment=ft.alignment.center,
        on_click=select
    )for bt in botoes ]


    keyboard = ft.Row(
        width=250,
        wrap= True,
        controls=bt,
        alignment='end'

    )
    page.add(display,keyboard)


ft.app(target = main)