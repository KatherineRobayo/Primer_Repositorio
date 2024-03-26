import tkinter as tk
from tkinter import messagebox


class Triqui:

    def __init__(self):
        self.turno = "X"
        self.tablero = [[" " for _ in range(3)] for _ in range(3)]

    def crear_interfaz(self):
        self.ventana = tk.Tk()
        self.ventana.title("Triqui ")

        # Marco principal con color de fondo
        self.marco_principal = tk.Frame(self.ventana, bg="#222222")
        self.marco_principal.pack()

        # Título del juego
        titulo = tk.Label(self.marco_principal, text="Triqui", fg="#28a745", font=("Arial", 30),  bg="#333333",)
        titulo.grid(row=0, column=1)

        # Mensaje de bienvenida
        mensaje_bienvenida = tk.Label(
            self.marco_principal,
            text="¡Bienvenido al juego! ",
            fg="#28a745",
            font=("Arial", 16),
            bg="#333333",
            
            
        )
        mensaje_bienvenida.grid(row=1, column=1)

        # Cuadrícula de botones con mayor tamaño y fuente
        for i in range(3):
            for j in range(3):
                boton = tk.Button(
                    self.marco_principal,
                    text=" ",
                    command=lambda i=i, j=j: self.marcar_casilla(i, j),
                    padx=20,
                    pady=20,
                    font=("Arial", 20),
                    bg="#333333",
                    fg="#FFFFFF"
                )
                boton.grid(row=i + 2, column=j)

        # Botón para reiniciar con borde
        self.boton_reiniciar = tk.Button(
            self.marco_principal,
            text="Reiniciar",
            command=self.reiniciar_juego,
            borderwidth=2,
            relief="groove"
        )
        self.boton_reiniciar.grid(row=5, column=1)

    def marcar_casilla(self, i, j):
        # Validar casilla vacía
        if self.tablero[i][j] != " ":
            return

        # Marcar la casilla que se oprime
        self.tablero[i][j] = self.turno

        # Actualizar la interfaz
        boton = self.marco_principal.grid_slaves(row=i + 2, column=j)[0]
        boton["text"] = self.turno

        # Revisar el ganador
        if self.comprobar_ganador():
            self.mostrar_mensaje_ganador()
            return

        # Cambiar el turno del jugador
        self.turno = "O" if self.turno == "X" else "X"

    def comprobar_ganador(self):
        # Orden de filas
        for i in range(3):
            if self.tablero[i][0] == self.tablero[i][1] == self.tablero[i][2] != " ":
                return True

        # Orden de columnas
        for j in range(3):
            if self.tablero[0][j] == self.tablero[1][j] == self.tablero[2][j] != " ":
                return True

        # Diagonal del triqui
        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] != " ":
            return True

        if self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] != " ":
            return True

        # Cuando se genera un empate
        for i in range(3):
            for j in range(3):
                if self.tablero[i][j] == " ":
                    return False

        self.mostrar_mensaje_empate()
        return True

    def mostrar_mensaje_ganador(self):
        tk.messagebox.showinfo("¡Felicidades !", f"¡El jugador {self.turno} ha ganado!")
        self.reiniciar_juego()

    def mostrar_mensaje_empate(self):
        tk.messagebox.showinfo("Empate ", "No hay ganador. ¡Vuelvan a intentarlo!")
        self.reiniciar_juego()

    def reiniciar_juego(self):  # Se agrega el paréntesis faltante
        self.turno = "X"
        self.tablero = [[" " for _ in range(3)] for _ in range(3)]

        for i in range(3):
            for j in range(3):
                boton = self.marco_principal.grid_slaves(row=i + 2, column=j)[0]
                boton["text"] = " "

juego = Triqui()
juego.crear_interfaz()
juego.ventana.mainloop()



