"""
Main window of the drawing application.
"""

from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QComboBox,
    QPushButton,
    QColorDialog
)
from PyQt6.QtGui import QColor

from canvas import DrawingCanvas


class MainWindow(QMainWindow):
    """Main application window."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt Drawing App")
        self.resize(800, 600)

        self.current_color = QColor("black")

        self._setup_ui()

    def _setup_ui(self):
        """Create and arrange UI components."""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout()
        main_layout.setSpacing(10)
        main_layout.setContentsMargins(10, 10, 10, 10)

        controls_layout = QHBoxLayout()

        # Drawing canvas
        self.canvas = DrawingCanvas()

        # Shape selector
        self.shape_selector = QComboBox()
        self.shape_selector.addItems([
            "Line",
            "Rectangle",
            "Ellipse"
        ])
        self.shape_selector.currentTextChanged.connect(
            self.canvas.set_shape
        )

        # Color picker button
        self.color_button = QPushButton("Select Color")
        self.color_button.clicked.connect(self.select_color)

        # Clear canvas button
        self.clear_button = QPushButton("Clear Canvas")
        self.clear_button.clicked.connect(self.clear_canvas)

        # Improve control sizes
        self.shape_selector.setMinimumHeight(30)
        self.color_button.setMinimumHeight(30)
        self.clear_button.setMinimumHeight(30)

        # Tooltips
        self.shape_selector.setToolTip("Select shape type")
        self.color_button.setToolTip("Choose drawing color")
        self.clear_button.setToolTip("Clear the canvas")

        controls_layout.addWidget(self.shape_selector)
        controls_layout.addWidget(self.color_button)
        controls_layout.addWidget(self.clear_button)

        main_layout.addLayout(controls_layout)
        main_layout.addWidget(self.canvas)

        central_widget.setLayout(main_layout)

        # Basic UI styling
        self.setStyleSheet("""
            QPushButton {
                font-size: 14px;
                padding: 5px 10px;
            }
            QComboBox {
                font-size: 14px;
                padding: 5px;
            }
        """)

    def select_color(self):
        """Open color dialog and set selected color."""
        color = QColorDialog.getColor(self.current_color, self)

        if color.isValid():
            self.current_color = color
            self.canvas.set_color(color)
            self.color_button.setStyleSheet(
                f"background-color: {color.name()};"
            )

    def clear_canvas(self):
        """Clear all drawings from the canvas."""
        self.canvas.clear()
