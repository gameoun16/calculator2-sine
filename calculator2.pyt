import flet as ft
import math

def main(page: ft.Page):
    page.title = "Scientific Calculator"
    page.window_width = 360
    page.window_height = 600
    page.bgcolor = "#F9F9F9"
    page.scroll = "adaptive"

    result = ft.TextField(
        value="0",
        text_align="right",
        width=340,
        read_only=True,
        border_color="transparent",
        bgcolor="#F9F9F9",
        color="black",
        text_size=36
    )
    expression = ""

    def button_click(e):
        nonlocal expression
        value = e.control.text
        try:
            if value == "AC":
                expression = ""
                result.value = "0"
            elif value == "⌫":
                expression = expression[:-1]
                result.value = expression if expression else "0"
            elif value == "=":
                try:
                    expr = expression.replace("×", "*").replace("÷", "/")
                    expr = expr.replace("π", str(math.pi)).replace("e", str(math.e))
                    result.value = str(eval(expr))
                    expression = result.value
                except:
                    result.value = "Error"
                    expression = ""
            elif value == "sin⁻¹":
                result.value = str(math.degrees(math.asin(float(result.value))))
                expression = result.value
            elif value == "cos⁻¹":
                result.value = str(math.degrees(math.acos(float(result.value))))
                expression = result.value
            elif value == "tan⁻¹":
                result.value = str(math.degrees(math.atan(float(result.value))))
                expression = result.value
            elif value == "xʸ":
                expression += "**"
                result.value = expression
            elif value == "√x":
                result.value = str(math.sqrt(float(result.value)))
                expression = result.value
            elif value == "x!":
                result.value = str(math.factorial(int(float(result.value))))
                expression = result.value
            elif value == "1/x":
                result.value = str(1 / float(result.value))
                expression = result.value
            elif value == "lg":
                result.value = str(math.log10(float(result.value)))
                expression = result.value
            elif value == "ln":
                result.value = str(math.log(float(result.value)))
                expression = result.value
            else:
                expression += value
                result.value = expression
        except:
            result.value = "Error"
            expression = ""

        page.update()

    # กำหนดสีปุ่มตามประเภท
    def styled_button(text, color="white", tcolor="black"):
        return ft.ElevatedButton(
            text=text,
            width=65,
            height=65,
            bgcolor=color,
            color=tcolor,
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=35)),
            on_click=button_click
        )

    buttons = [
        ["2nd", "deg", "sin⁻¹", "cos⁻¹", "tan⁻¹"],
        ["xʸ", "lg", "ln", "(", ")"],
        ["√x", "AC", "⌫", "%", "÷"],
        ["x!", "7", "8", "9", "×"],
        ["1/x", "4", "5", "6", "-"],
        ["π", "1", "2", "3", "+"],
        ["e", "0", ".", "="],
    ]

    # สีแต่ละหมวด
    func_color = "#EEEEEE"  # ฟังก์ชัน
    control_color = "#FFA726"  # AC, ⌫
    op_color = "#FB8C00"  # + - × ÷ %
    eq_color = "#EF6C00"  # ปุ่ม =
    num_color = "white"

    grid = []
    for row in buttons:
        row_buttons = []
        for b in row:
            if b in ["AC", "⌫"]:
                row_buttons.append(styled_button(b, control_color, "white"))
            elif b in ["+", "-", "×", "÷", "%"]:
                row_buttons.append(styled_button(b, op_color, "white"))
            elif b == "=":
                row_buttons.append(styled_button(b, eq_color, "white"))
            elif b.isdigit() or b in ["."]:
                row_buttons.append(styled_button(b, num_color, "black"))
            else:
                row_buttons.append(styled_button(b, func_color, "black"))
        grid.append(ft.Row(row_buttons, alignment="center"))

    page.add(result, *grid)

ft.app(target=main)
