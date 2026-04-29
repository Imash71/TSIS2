import tkinter as tk
from tkinter.colorchooser import askcolor
from datetime import datetime
root = tk.Tk()
root.title("TSIS 2 Paint")
WIDTH = 1000
HEIGHT = 700
canvas = tk.Canvas(root, bg="white", width=WIDTH, height=HEIGHT)
canvas.pack(fill="both", expand=True)
color = "black"
brush_size = 2
tool = "pencil"
start_x = 0
start_y = 0
# ---------------- START DRAW ----------------
def start_draw(event):
   global start_x, start_y
   start_x = event.x
   start_y = event.y

# ---------------- DRAW ----------------
def draw(event):
   global start_x, start_y
   # pencil
   if tool == "pencil":
       canvas.create_line(
           start_x,
           start_y,
           event.x,
           event.y,
           fill=color,
           width=brush_size,
           capstyle=tk.ROUND,
           smooth=True
       )
       start_x = event.x
       start_y = event.y

# ---------------- RELEASE ----------------
def release(event):
   # line
   if tool == "line":
       canvas.create_line(
           start_x,
           start_y,
           event.x,
           event.y,
           fill=color,
           width=brush_size
       )
   # rectangle
   elif tool == "rectangle":
       canvas.create_rectangle(
           start_x,
           start_y,
           event.x,
           event.y,
           outline=color,
           width=brush_size
       )
   # circle
   elif tool == "circle":
       canvas.create_oval(
           start_x,
           start_y,
           event.x,
           event.y,
           outline=color,
           width=brush_size
       )
   # square
   elif tool == "square":
       side = min(abs(event.x - start_x), abs(event.y - start_y))
       canvas.create_rectangle(
           start_x,
           start_y,
           start_x + side,
           start_y + side,
           outline=color,
           width=brush_size
       )
   # triangle
   elif tool == "triangle":
       canvas.create_polygon(
           start_x,
           event.y,
           (start_x + event.x) // 2,
           start_y,
           event.x,
           event.y,
           outline=color,
           fill="",
           width=brush_size
       )
   # rhombus
   elif tool == "rhombus":
       mid_x = (start_x + event.x) // 2
       mid_y = (start_y + event.y) // 2
       canvas.create_polygon(
           mid_x, start_y,
           event.x, mid_y,
           mid_x, event.y,
           start_x, mid_y,
           outline=color,
           fill="",
           width=brush_size
       )

# ---------------- TOOL SELECT ----------------
def set_tool(t):
   global tool
   tool = t

# ---------------- COLOR ----------------
def choose_color():
   global color
   selected = askcolor()[1]
   if selected:
       color = selected

# ---------------- BRUSH SIZE ----------------
def small():
   global brush_size
   brush_size = 2

def medium():
   global brush_size
   brush_size = 5

def large():
   global brush_size
   brush_size = 10

# ---------------- TEXT TOOL ----------------
def add_text():
   text = text_entry.get()
   canvas.create_text(
       300,
       300,
       text=text,
       fill=color,
       font=("Arial", 24)
   )

# ---------------- SAVE ----------------
def save_canvas(event=None):
   filename = f"paint_{datetime.now().strftime('%Y%m%d_%H%M%S')}.ps"
   canvas.postscript(file=filename)
   print("Saved:", filename)

# ---------------- TOP MENU ----------------
top = tk.Frame(root)
top.pack()
tk.Button(top, text="Pencil", command=lambda: set_tool("pencil")).pack(side="left")
tk.Button(top, text="Line", command=lambda: set_tool("line")).pack(side="left")
tk.Button(top, text="Rectangle", command=lambda: set_tool("rectangle")).pack(side="left")
tk.Button(top, text="Circle", command=lambda: set_tool("circle")).pack(side="left")
tk.Button(top, text="Square", command=lambda: set_tool("square")).pack(side="left")
tk.Button(top, text="Triangle", command=lambda: set_tool("triangle")).pack(side="left")
tk.Button(top, text="Rhombus", command=lambda: set_tool("rhombus")).pack(side="left")
tk.Button(top, text="Color", command=choose_color).pack(side="left")
tk.Button(top, text="Small", command=small).pack(side="left")
tk.Button(top, text="Medium", command=medium).pack(side="left")
tk.Button(top, text="Large", command=large).pack(side="left")
text_entry = tk.Entry(top)
text_entry.pack(side="left")
tk.Button(top, text="Add Text", command=add_text).pack(side="left")

# ---------------- EVENTS ----------------
canvas.bind("<Button-1>", start_draw)
canvas.bind("<B1-Motion>", draw)
canvas.bind("<ButtonRelease-1>", release)
root.bind("<Control-s>", save_canvas)
root.mainloop()