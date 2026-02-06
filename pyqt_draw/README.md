# PyQt Drawing Application

## Overview
This is a simple desktop drawing application built using **Python 3** and **PyQt6**.
The application allows users to draw basic shapes on a canvas using the mouse.

The focus of this project is clarity, simplicity, and clean object-oriented design.

---

## Features
- Draw shapes using the mouse:
  - Line
  - Rectangle
  - Ellipse
- Live preview while dragging the mouse
- Color selection using a color dialog
- Clear/reset canvas

---

## Technologies Used
- Python 3
- PyQt6

---

## Project Structure

```
pyqt_draw/
│
├── main.py            # Application entry point
├── main_window.py     # Main window and UI controls
├── canvas.py          # Custom drawing canvas
├── README.md          # Project documentation
└── requirements.txt   # Dependencies
```

---

## Installation

1. Make sure Python 3 is installed on your system.
2. Install the required dependency:
pip install PyQt6

---

## Running the Application
From inside the pyqt_draw directory, run:
python main.py

---

## How to Use
1. Select a shape from the dropdown menu.
2. Click Select Color to choose a drawing color.
3. Press and drag the left mouse button on the canvas to draw.
4. Release the mouse button to finalize the shape.
5. Click Clear Canvas to remove all drawings.





