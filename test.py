import numpy as np
from scipy.signal import get_window
from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow, QAction

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Window Function GUI")
        self.setGeometry(100, 100, 800, 600)

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("File")
        save_action = QAction("Save Window Function", self)
        save_action.triggered.connect(self.save_window)
        file_menu.addAction(save_action)

    def save_window(self):
        # 获取用户选择的文件路径
        save_path, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Text Files (*.txt)")

        # 如果用户没有选择文件则退出函数
        if not save_path:
            return

        # 将窗函数保存到文件
        han_window = get_window('hann', 64)
        np.savetxt(save_path, han_window, fmt='%.7f')

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
