from tkinter import *
from tkinter import messagebox
import tkinter.filedialog
from tkinter import ttk
from tkinter import colorchooser

class Application:
    def __init__(self, root):
        self.root = root
        self.root.title("Універсальна програма")
        self.current_file = None
        
        # Default settings for shapes
        self.shape_settings = {
            'triangle': {'color': 'yellow', 'size': 1.0},
            'rectangle': {'color': 'blue', 'size': 1.0},
            'circle': {'color': 'red', 'size': 1.0}
        }
        
        # Default settings for text
        self.text_settings = {
            'color': 'blue',
            'size': 14
        }
        
        # Create main menu
        self.create_main_menu()
        
        # Створення основного інтерфейсу
        self.create_notebook()
        self.create_text_editor_tab()
        self.create_drawing_tab()
        
    def create_main_menu(self):
        """Create the main menu with settings options"""
        menubar = Menu(self.root)
        
        # Settings menu
        settings_menu = Menu(menubar, tearoff=0)
        settings_menu.add_command(label="Налаштування зображень", command=self.configure_shapes)
        settings_menu.add_command(label="Налаштування тексту", command=self.configure_text)
        
        menubar.add_cascade(label="Налаштування", menu=settings_menu)
        
        self.root.config(menu=menubar)
    
    def configure_shapes(self):
        """Open dialog to configure shape settings"""
        self.shape_dialog = Toplevel(self.root)
        self.shape_dialog.title("Налаштування зображень")
        self.shape_dialog.geometry("400x300")
        
        # Triangle settings
        Label(self.shape_dialog, text="Трикутник").grid(row=0, column=0, padx=5, pady=5)
        Button(self.shape_dialog, text="Колір", 
               command=lambda: self.choose_color('triangle')).grid(row=0, column=1, padx=5, pady=5)
        Scale(self.shape_dialog, from_=0.5, to=2.0, resolution=0.1, orient=HORIZONTAL,
              command=lambda v: self.set_shape_size('triangle', v)).grid(row=0, column=2, padx=5, pady=5)
        self.shape_dialog.grid_rowconfigure(0, minsize=30)
        
        # Rectangle settings
        Label(self.shape_dialog, text="Прямокутник").grid(row=1, column=0, padx=5, pady=5)
        Button(self.shape_dialog, text="Колір", 
               command=lambda: self.choose_color('rectangle')).grid(row=1, column=1, padx=5, pady=5)
        Scale(self.shape_dialog, from_=0.5, to=2.0, resolution=0.1, orient=HORIZONTAL,
              command=lambda v: self.set_shape_size('rectangle', v)).grid(row=1, column=2, padx=5, pady=5)
        self.shape_dialog.grid_rowconfigure(1, minsize=30)
        
        # Circle settings
        Label(self.shape_dialog, text="Коло").grid(row=2, column=0, padx=5, pady=5)
        Button(self.shape_dialog, text="Колір", 
               command=lambda: self.choose_color('circle')).grid(row=2, column=1, padx=5, pady=5)
        Scale(self.shape_dialog, from_=0.5, to=2.0, resolution=0.1, orient=HORIZONTAL,
              command=lambda v: self.set_shape_size('circle', v)).grid(row=2, column=2, padx=5, pady=5)
        self.shape_dialog.grid_rowconfigure(2, minsize=30)
        
        # Close button
        Button(self.shape_dialog, text="Закрити", command=self.shape_dialog.destroy).grid(row=3, column=1, pady=10)
    
    def choose_color(self, shape_type):
        """Choose color for a shape"""
        color = colorchooser.askcolor()[1]
        if color:
            self.shape_settings[shape_type]['color'] = color
            self.update_shapes()
    
    def set_shape_size(self, shape_type, size):
        """Set size for a shape"""
        self.shape_settings[shape_type]['size'] = float(size)
        self.update_shapes()
    
    def update_shapes(self):
        """Update all shapes with current settings"""
        if hasattr(self, 'canvas'):
            # Update triangle if visible
            if self.canvas.coords(self.triangle) != [0, 0, 0, 0, 0, 0]:
                self.draw_triangle()
            
            # Update rectangle if visible
            if self.canvas.coords(self.rectangle) != [0, 0, 0, 0]:
                self.draw_rectangle()
            
            # Update circle if visible
            if self.canvas.coords(self.circle) != [0, 0, 0, 0]:
                self.draw_circle()
    
    def configure_text(self):
        """Open dialog to configure text settings"""
        self.text_dialog = Toplevel(self.root)
        self.text_dialog.title("Налаштування тексту")
        self.text_dialog.geometry("300x200")
        
        # Color settings
        Label(self.text_dialog, text="Колір тексту:").grid(row=0, column=0, padx=5, pady=5)
        Button(self.text_dialog, text="Обрати", 
               command=self.choose_text_color).grid(row=0, column=1, padx=5, pady=5)
        
        # Size settings
        Label(self.text_dialog, text="Розмір тексту:").grid(row=1, column=0, padx=5, pady=5)
        Spinbox(self.text_dialog, from_=8, to=72, 
                command=self.update_text_size).grid(row=1, column=1, padx=5, pady=5)
        
        # Close button
        Button(self.text_dialog, text="Закрити", command=self.text_dialog.destroy).grid(row=2, column=1, pady=10)
    
    def choose_text_color(self):
        """Choose color for text"""
        color = colorchooser.askcolor()[1]
        if color:
            self.text_settings['color'] = color
            self.update_text()
    
    def update_text_size(self):
        """Update text size"""
        self.text_settings['size'] = int(self.text_dialog.children['!spinbox'].get())
        self.update_text()
    
    def update_text(self):
        """Update text appearance"""
        if hasattr(self, 'text'):
            self.text.tag_config('title', 
                               font=('Times', self.text_settings['size']), 
                               foreground=self.text_settings['color'])
    
    def create_notebook(self):
        """Створення панелі вкладок"""
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=BOTH, expand=True)
        
    def create_text_editor_tab(self):
        """Створення вкладки текстового редактора"""
        self.text_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.text_tab, text="Текстовий редактор")
        
        # Панель кнопок
        self.panelFrame = Frame(self.text_tab, height=30, bg='lightblue')
        self.panelFrame.pack(side='top', fill='x')
        
        # Область тексту
        self.textFrame = Frame(self.text_tab)
        self.textFrame.pack(side='bottom', fill='both', expand=True)
        
        # Віджети
        self.textbox = Text(self.textFrame, font='Arial 12', wrap='word')
        self.scrollbar = Scrollbar(self.textFrame)
        
        # Налаштування прокрутки
        self.scrollbar['command'] = self.textbox.yview
        self.textbox['yscrollcommand'] = self.scrollbar.set
        
        # Розміщення віджетів
        self.textbox.pack(side='left', fill='both', expand=True)
        self.scrollbar.pack(side='right', fill='y')
        
        # Кнопки
        self.loadBtn = Button(self.panelFrame, text='Відкрити', command=self.load_file)
        self.loadBtn.pack(side='left', padx=5, pady=2)
        
        self.saveBtn = Button(self.panelFrame, text='Зберегти', command=self.save_file)
        self.saveBtn.pack(side='left', padx=5, pady=2)
        
        self.saveAsBtn = Button(self.panelFrame, text='Зберегти як...', command=self.save_file_as)
        self.saveAsBtn.pack(side='left', padx=5, pady=2)
        
    def create_drawing_tab(self):
        """Створення вкладки для малювання фігур"""
        self.draw_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.draw_tab, text="Малювання фігур")
        
        # Кнопки керування
        self.controls_frame = Frame(self.draw_tab)
        self.controls_frame.pack(side='left', fill='y')
        
        # Область малювання
        self.canvas_frame = Frame(self.draw_tab)
        self.canvas_frame.pack(side='right', fill='both', expand=True)
        
        # Створення кнопок
        self.b_triangle = Button(self.controls_frame, text="Трикутник", width=15, command=self.draw_triangle)
        self.b_triangle.pack(pady=5)
        
        self.b_rectangle = Button(self.controls_frame, text="Прямокутник", width=15, command=self.draw_rectangle)
        self.b_rectangle.pack(pady=5)
        
        self.b_circle = Button(self.controls_frame, text="Коло", width=15, command=self.draw_circle)
        self.b_circle.pack(pady=5)
        
        self.b_clear = Button(self.controls_frame, text="Очистити", width=15, command=self.clear_canvas)
        self.b_clear.pack(pady=5)
        
        # Canvas для малювання
        self.canvas = Canvas(self.canvas_frame, width=400, height=300, bg='white')
        self.canvas.pack(side='top', fill='both', expand=True, padx=10, pady=10)
        
        # Текстова область для опису
        self.text = Text(self.canvas_frame, width=55, height=5, bg='white', wrap=WORD)
        self.text.pack(side='bottom', fill='x', padx=10, pady=10)
        
        # Створення фігур (спочатку приховані)
        self.triangle = self.canvas.create_polygon(0, 0, 0, 0, 0, 0, fill='yellow', outline='black')
        self.rectangle = self.canvas.create_rectangle(0, 0, 0, 0, fill='blue', outline='black')
        self.circle = self.canvas.create_oval(0, 0, 0, 0, fill='red', outline='black')
        
        # Початкове повідомлення
        self.update_description("Оберіть фігуру для відображення")
        
    # Методи для роботи з текстовим редактором
    def load_file(self):
        """Завантаження текстового файлу"""
        fn = tkinter.filedialog.askopenfilename(filetypes=[('Текстові файли', '*.txt')])
        if not fn:
            return
            
        try:
            with open(fn, 'rt', encoding='utf-8') as f:
                content = f.read()
        except UnicodeDecodeError:
            with open(fn, 'rt', encoding='cp1251') as f:
                content = f.read()
                
        self.textbox.delete('1.0', 'end')
        self.textbox.insert('1.0', content)
        self.current_file = fn
        self.root.title(f"Універсальна програма - {fn}")
        
    def save_file(self):
        """Збереження файлу"""
        if not self.current_file:
            self.save_file_as()
            return
            
        self._save_to_file(self.current_file)
        
    def save_file_as(self):
        """Збереження файлу під новим ім'ям"""
        fn = tkinter.filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[('Текстові файли', '*.txt')]
        )
        if not fn:
            return
            
        self._save_to_file(fn)
        self.current_file = fn
        self.root.title(f"Універсальна програма - {fn}")
        
    def _save_to_file(self, filename):
        """Збереження вмісту текстового поля у файл"""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(self.textbox.get('1.0', 'end-1c'))
        except Exception as e:
            messagebox.showerror("Помилка", f"Не вдалося зберегти файл: {str(e)}")
            
    # Методи для роботи з малюванням фігур
    def draw_triangle(self):
        """Малювання трикутника"""
        self.clear_shapes()
        size = self.shape_settings['triangle']['size']
        base = 290 * size
        height = 140 * size
        x1 = 200 - base/2
        x2 = 200 + base/2
        y1 = 200
        y2 = 200 - height
        self.canvas.itemconfig(self.triangle, 
                             fill=self.shape_settings['triangle']['color'], 
                             outline='black')
        self.canvas.coords(self.triangle, x1, y1, x2, y1, 200, y2)
        self.update_description("Зображення трикутника")
        
    def draw_rectangle(self):
        """Малювання прямокутника"""
        self.clear_shapes()
        size = self.shape_settings['rectangle']['size']
        width = 240 * size
        height = 150 * size
        x1 = 200 - width/2
        y1 = 125 - height/2
        x2 = 200 + width/2
        y2 = 125 + height/2
        self.canvas.itemconfig(self.rectangle, 
                             fill=self.shape_settings['rectangle']['color'], 
                             outline='black')
        self.canvas.coords(self.rectangle, x1, y1, x2, y2)
        self.update_description("Зображення прямокутника")
        
    def draw_circle(self):
        """Малювання кола"""
        self.clear_shapes()
        size = self.shape_settings['circle']['size']
        diameter = 100 * size
        x1 = 200 - diameter/2
        y1 = 150 - diameter/2
        x2 = 200 + diameter/2
        y2 = 150 + diameter/2
        self.canvas.itemconfig(self.circle, 
                             fill=self.shape_settings['circle']['color'], 
                             outline='black')
        self.canvas.coords(self.circle, x1, y1, x2, y2)
        self.update_description("Зображення кола")
        
    def clear_canvas(self):
        """Очищення полотна"""
        self.clear_shapes()
        self.update_description("Оберіть фігуру для відображення")
        
    def clear_shapes(self):
        """Приховує всі фігури"""
        self.canvas.coords(self.triangle, (0, 0, 0, 0, 0, 0))
        self.canvas.coords(self.rectangle, (0, 0, 0, 0))
        self.canvas.coords(self.circle, (0, 0, 0, 0))
        
    def update_description(self, text):
        """Оновлення текстового опису"""
        self.text.delete(1.0, END)
        self.text.insert(1.0, text)
        self.text.tag_add('title', '1.0', '1.end')
        self.text.tag_config('title', 
                           font=('Times', self.text_settings['size']), 
                           foreground=self.text_settings['color'])

if __name__ == "__main__":
    root = Tk()
    app = Application(root)
    root.geometry("800x600")
    root.mainloop()