import tkinter as tk

# Функция для выполнения вычислений
def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        label_result.config(text=f"Результат: {result}")
    except Exception as e:
        label_result.config(text=f"Ошибка: {e}")

# Создаем главное окно приложения
root = tk.Tk()
root.title("Калькулятор")

# Поле ввода выражения
entry = tk.Entry(root, width=35)
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Кнопка для вычисления результата
button_equal = tk.Button(root, text="=", command=calculate)
button_equal.grid(row=1, column=2)

# Метка для отображения результата
label_result = tk.Label(root, text="", font=('Arial', 12))
label_result.grid(row=2, column=0, columnspan=3)

# Запускаем главный цикл приложения
root.mainloop()