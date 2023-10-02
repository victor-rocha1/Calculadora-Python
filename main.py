import flet as ft           #Biblioteca usada
from flet import colors     #Cores da biblioteca
from decimal import Decimal #Casas decimais no resultado


#Formato da calculadora
def main(page: ft.Page):               
    page.bgcolor = '#000'
    page.window_resizable = False
    page.window_width = 290
    page.window_height = 440
    page.title = 'Calculadora'
    page.window_always_on_top = True
    
    #Resultado das operações
    resultado = ft.Text(value="0", color='FFFFFF', size=40)


    #Função para calcular o resultado
    def calculo(operador, valor_atual):
        try:
            value = eval(valor_atual)
            if operador == '%':         #Se selecionar esse, divide por 100
                value /= 100
            elif operador == '±':       #Se for esse, inverte o sinal do número
                value = -value
        except:
            return 'ERROR'              #Com o try, tenta fazer a operaçõa, se não for possível retorna ERROR
        

        #Quantidade de casas decimais no resultado final
        digitos = min(abs(Decimal(value).as_tuple().exponent), 5)     #Verifica as casas decimais,
                                                                      #Se o n° de c.d for maior que 5, imprime só 5 delas
        return format(value, f'.{digitos}f')                          #Se o n° de c.d for menor que 5, imprime quantas tiver

    
    

    #Seleção de números e operações
    def select(e):
        valor_atual = resultado.value if resultado.value not in ('0','ERROR') else ''    
        value = e.control.content.value    #Captura do número/operação dos botões
                                           
        if value.isdigit():
            value = valor_atual+value      #Se for dígito, mostra o número
        elif value == 'AC':                #Se for AC, zera a conta
            value='0'
        else:                              #Se for esses, mostra o valor digotado mais o operador
            if valor_atual and valor_atual[-1] in ('+', '-', '/', '*', '.'):    
                valor_atual = valor_atual[:-1]

            value = valor_atual+value

            if value[-1] in ('=', '%', '±'):       #Se for esses, só mostra o resultado final
                value = calculo(operador=value[-1], valor_atual=valor_atual)

        resultado.value = value
        resultado.update()



    #Alinhamento do texto à direita
    display = ft.Row(        
        width=290,
        controls=[resultado],
        alignment='end',
    )

    #Cor, fundo e texto dos botões, em formato de listas que relaciona com o controls, que foi usado
    #como primeiro botão, mas agora configura todos
    botoes = [ 
    {'operador': 'AC', 'fonte': colors.BLACK, 'fundo': colors.BLUE_GREY_100 },
    {'operador': '±', 'fonte': colors.BLACK, 'fundo': colors.BLUE_GREY_100 },
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


    #Configuração pra quebra de linha na hora de organizar os botões
    keyboard = ft.Row(
        width=250,
        wrap= True,
        controls=bt,
        alignment='end'

    )
    page.add(display,keyboard)


ft.app(target = main)