import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import Qt, Signal


class FileSlotWidget(QWidget):
    signal = Signal(str)
    def __init__(self, parent):
        super().__init__(parent)

        self.setAcceptDrops(True)
        # self.setMinimumSize(300, 200)

        layout = QVBoxLayout()
        self.label = QLabel("拖动文件到这里")
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)

        self.setLayout(layout)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        for url in event.mimeData().urls():
            file_path = url.toLocalFile()
            self.signal.emit(file_path)
            print(f"文件名: {file_path}")

        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = FileSlotWidget()
    widget.show()
    sys.exit(app.exec())