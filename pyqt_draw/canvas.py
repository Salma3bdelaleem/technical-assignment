"""
Drawing canvas widget for the PyQt drawing application.
"""

from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QPainter, QPen
from PyQt6.QtCore import Qt, QRect


class DrawingCanvas(QWidget):
    """
    Custom widget that allows drawing shapes using the mouse.
    """

    def __init__(self):
        super().__init__()
        self.setMinimumSize(400, 300)

        # Canvas styling
        self.setStyleSheet("""
        background-color: #f9f9f9;
        border: 1px solid #cccccc;
    """)
        
        self.shapes = []
        self.start_point = None
        self.end_point = None

        self.current_shape = "Line"
        self.current_color = Qt.GlobalColor.black

    def set_shape(self, shape):
        """Set the current shape type."""
        self.current_shape = shape

    def set_color(self, color):
        """Set the current drawing color."""
        self.current_color = color

    def clear(self):
        """Clear all drawn shapes."""
        self.shapes.clear()
        self.update()

    def mousePressEvent(self, event):
        """Record the starting point when mouse is pressed."""
        if event.button() == Qt.MouseButton.LeftButton:
            self.start_point = event.position().toPoint()
            self.end_point = self.start_point
            self.update()

    def mouseMoveEvent(self, event):
        """Update the ending point while dragging for preview."""
        if self.start_point is not None:
            self.end_point = event.position().toPoint()
            self.update()

    def mouseReleaseEvent(self, event):
        """Finalize the shape when mouse is released."""
        if event.button() == Qt.MouseButton.LeftButton and self.start_point:
            self.end_point = event.position().toPoint()

            self.shapes.append((
                self.current_shape,
                self.start_point,
                self.end_point,
                self.current_color
            ))

            self.start_point = None
            self.end_point = None
            self.update()

    def paintEvent(self, event):
        """Paint all shapes and the preview shape."""
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Draw finalized shapes
        for shape, start, end, color in self.shapes:
            pen = QPen(color, 2)
            painter.setPen(pen)
            self._draw_shape(painter, shape, start, end)

        # Draw preview shape
        if self.start_point and self.end_point:
            pen = QPen(self.current_color, 2, Qt.PenStyle.DashLine)
            painter.setPen(pen)
            self._draw_shape(
                painter,
                self.current_shape,
                self.start_point,
                self.end_point
            )

    def _draw_shape(self, painter, shape, start, end):
        """Draw a shape based on its type."""
        if shape == "Line":
            painter.drawLine(start, end)

        elif shape == "Rectangle":
            rect = QRect(start, end)
            painter.drawRect(rect.normalized())

        elif shape == "Ellipse":
            rect = QRect(start, end)
            painter.drawEllipse(rect.normalized())
