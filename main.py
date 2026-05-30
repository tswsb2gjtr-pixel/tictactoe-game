from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
import random

class TicTacToeGame(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        
        # Статус игры: кто ходит, кто выиграл
        self.status_label = Label(text='Ваш ход (X)', font_size=30, size_hint=(1, 0.2))
        self.add_widget(self.status_label)
        
        # Сетка 3x3 для кнопок
        self.grid = GridLayout(cols=3, size_hint=(1, 0.7))
        self.add_widget(self.grid)
        
        # Кнопка новой игры
        self.reset_button = Button(text='Новая игра', font_size=30, size_hint=(1, 0.1))
        self.reset_button.bind(on_press=self.reset_game)
        self.add_widget(self.reset_button)
        
        # Инициализация поля и состояния
        self.board = [None] * 9  # None = пусто, 'X' или 'O'
        self.buttons = []
        self.current_player = 'X'  # X ходит первым (пользователь)
        self.game_over = False
        
        # Создаём 9 кнопок для клеток
        for i in range(9):
            btn = Button(text='', font_size=50, disabled=False)
            btn.bind(on_press=lambda btn, idx=i: self.make_move(idx))
            self.grid.add_widget(btn)
            self.buttons.append(btn)
    
    def make_move(self, idx):
        # Если игра окончена или клетка занята или не ход пользователя - ничего не делаем
        if self.game_over or self.board[idx] is not None or self.current_player != 'X':
            return
        
        # Ход пользователя
        self.place_move(idx, 'X')
        
        # Проверка окончания игры
        if self.check_game_over():
            return
        
        # Ход компьютера (случайный)
        self.computer_move()
    
    def place_move(self, idx, player):
        self.board[idx] = player
        self.buttons[idx].text = player
        self.buttons[idx].disabled = True
        
        # Проверяем, не привёл ли этот ход к победе или ничьей
        winner = self.check_winner()
        if winner:
            self.game_over = True
            self.status_label.text = f'Победил {winner}!' if winner != 'Ничья' else 'Ничья!'
            self.disable_all_buttons()
        elif all(cell is not None for cell in self.board):
            self.game_over = True
            self.status_label.text = 'Ничья!'
        else:
            # Меняем игрока
            self.current_player = 'O' if player == 'X' else 'X'
            if not self.game_over:
                self.status_label.text = 'Ход компьютера (O)' if self.current_player == 'O' else 'Ваш ход (X)'
    
    def computer_move(self):
        if self.game_over or self.current_player != 'O':
            return
        
        # Случайный свободный ход
        empty_cells = [i for i, cell in enumerate(self.board) if cell is None]
        if empty_cells:
            idx = random.choice(empty_cells)
            self.place_move(idx, 'O')
    
    def check_winner(self):
        # Все выигрышные комбинации
        win_combinations = [
            [0,1,2], [3,4,5], [6,7,8],  # горизонтали
            [0,3,6], [1,4,7], [2,5,8],  # вертикали
            [0,4,8], [2,4,6]            # диагонали
        ]
        for combo in win_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] and self.board[combo[0]] is not None:
                return self.board[combo[0]]
        return None
    
    def check_game_over(self):
        winner = self.check_winner()
        if winner:
            self.game_over = True
            self.status_label.text = f'Победил {winner}!'
            self.disable_all_buttons()
            return True
        if all(cell is not None for cell in self.board):
            self.game_over = True
            self.status_label.text = 'Ничья!'
            return True
        return False
    
    def disable_all_buttons(self):
        for btn in self.buttons:
            btn.disabled = True
    
    def reset_game(self, instance):
        # Сброс поля и состояния
        self.board = [None] * 9
        self.current_player = 'X'
        self.game_over = False
        for btn in self.buttons:
            btn.text = ''
            btn.disabled = False
        self.status_label.text = 'Ваш ход (X)'

class TicTacToeApp(App):
    def build(self):
        return TicTacToeGame()

if __name__ == '__main__':
    TicTacToeApp().run()