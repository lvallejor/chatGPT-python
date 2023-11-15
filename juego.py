import tkinter as tk
import tkinter.messagebox

def start_game():
    # Configuración inicial
    root = tk.Tk()
    canvas = tk.Canvas(root, width=800, height=600, bg='black')
    canvas.pack()

    # Paleta
    paddle = canvas.create_rectangle(400, 580, 460, 590, fill='white')

    # Bola
    ball = canvas.create_oval(400, 300, 410, 310, fill='white')
    ball_dx = 3
    ball_dy = 3

    # Ladrillos
    bricks = [canvas.create_rectangle(x, y, x+50, y+20, fill='red') for x in range(100, 700, 60) for y in range(50, 150, 30)]

    # Movimiento de la paleta
    def move_paddle(event):
        x = event.x
        canvas.coords(paddle, x, 580, x+60, 590)

    canvas.bind_all('<Motion>', move_paddle)

    # Juego principal
    def game_loop():
        x1, y1, x2, y2 = canvas.coords(ball)

        # Movimiento de la bola
        if x1 <= 0 or x2 >= 800:
            nonlocal ball_dx
            ball_dx *= -1
        if y1 <= 0:
            nonlocal ball_dy
            ball_dy *= -1

        # Game over
        if y2 >= 600:
            tkinter.messagebox.showinfo("Game Over", "Game Over")
            root.destroy()
            start_game()
            return

        canvas.move(ball, ball_dx, ball_dy)

        # Colisión con la paleta
        overlapping = canvas.find_overlapping(*canvas.coords(ball))
        if len(overlapping) > 1:
            ball_dy *= -1
            for brick in overlapping:
                if brick in bricks:
                    canvas.delete(brick)
                    bricks.remove(brick)

        root.after(10, game_loop)

    game_loop()
    root.mainloop()

start_game()