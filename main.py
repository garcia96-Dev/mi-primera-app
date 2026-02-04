import flet as ft

def main(page: ft.Page):
    page.title = "Mi Conversor App"
    page.window_width = 400
    page.window_height = 600
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK # Modo oscuro para que se vea pro

    titulo = ft.Text("CONVERSOR PRO", size=30, weight="bold", color="blue")
    entrada = ft.TextField(label="Cantidad en Dólares", border_radius=15)
    resultado = ft.Text("Resultado: $0 pesos", size=20)

    def calcular(e):
        try:
            # Usamos el precio del dólar que definiste
            total = float(entrada.value) * 3950
            resultado.value = f"Resultado: ${total:,.0f} pesos"
            resultado.color = "green"
        except:
            resultado.value = "Error: Ingresa un número"
            resultado.color = "red"
        page.update()

    boton = ft.ElevatedButton("CALCULAR", on_click=calcular, width=200)

    page.add(
        ft.Container(
            content=ft.Column([titulo, entrada, boton, resultado], spacing=20),
            padding=30
        )
    )

ft.app(main)