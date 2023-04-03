import datetime
import sys
import numpy as np
import scipy.io as sio
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QMessageBox, QFileDialog
from matplotlib import pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.colors as mcolors

from untitled import Ui_MainWindow
from new_untitled import Ui_Form
from export_menu import Ui_Form as Ui_Form_2
from scipy.signal import get_window
from qt_material import apply_stylesheet

class Widget(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Form()
        self.setupUi(self)

        self.lineEdit.setText('512')
        self.comboBox.setCurrentIndex(0)

class Export(QWidget,Ui_Form_2):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Form_2()
        self.setupUi(self)


class MainWindow(QMainWindow, Ui_MainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.setupUi(self)

        # 实例化一个widget
        self.widget=Widget()
        self.export=Export()
        # 点击analyse_parameter按钮，弹出widget
        self.actionAnalyse_Parameter.triggered.connect(self.widget.show)
        # 点击export按钮，弹出export
        self.actionExport.triggered.connect(self.export.show)
        # 点击widget在中的apply按钮，将参数传递到主窗口
        self.widget.pushButton.clicked.connect(self.apply)

        # 创建一个字典用来保存窗口的参数
        self.window={}

        # 一些参数的初始化
        self.i = 1
        self.plot_deafault()
        self.point_num=512
        self.combo_index=0
        self.log_mode=0
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_4.setEnabled(False)
        self.legend_bool=0
        # 让combobox_3一开始选择第二个
        self.response_mode = 1
        self.widget.comboBox_3.setCurrentIndex(1)

        # 让widget可以被多选
        self.listWidget.setSelectionMode(3)

        # 修改MainWindow的名字
        self.setWindowTitle('Window Designer')

        # 修改按钮的名字
        self.pushButton.setText('Add_window')
        self.pushButton_2.setText('Delete')
        self.pushButton_3.setText('Apply')
        self.pushButton_4.setText('Copy')


        # 按钮点击创建窗
        self.pushButton.clicked.connect(self.listwidget_add)
        self.pushButton_2.clicked.connect(self.listwidget_del)

        self.listWidget.itemClicked.connect(self.listwidget_click)
        self.listWidget.itemClicked.connect(self.plot)

        # 点击按钮修改窗口参数
        self.pushButton_3.clicked.connect(self.window_change)

        # 让菜单栏的选项设为可勾选状态，并默认被勾选
        self.actionTime_Domain.setCheckable(True)
        self.actionFrequency_Domain_2.setCheckable(True)

        self.actionTime_Domain.setChecked(True)
        self.actionFrequency_Domain_2.setChecked(True)

        self.actionLegend.setCheckable(True)
        self.actionLegend.setChecked(False)

        # 点击Tool的Full analysis，弹出一个窗口
        self.actionFull_View.triggered.connect(self.full_analysis)

        # 点击菜单栏的选项，显示或者隐藏对应的图像
        self.actionTime_Domain.triggered.connect(self.show_time)
        self.actionFrequency_Domain_2.triggered.connect(self.show_freq)
        self.actionLegend.triggered.connect(self.show_legend)
        # 点击复制按钮复制一个窗
        self.pushButton_4.clicked.connect(self.copy_window)
        self.export.pushButton.clicked.connect(self.export_window)

        # combo选中窗Kaiser后，lineEdit_2可用
        self.comboBox.currentIndexChanged.connect(self.setting_enable)
        # 点击close按钮关闭窗口
        self.export.pushButton_2.clicked.connect(self.export.close)
        # 点击Exit退出程序
        self.actionExit.triggered.connect(self.close)
        # 点击About弹出一个版本信息
        self.actionAbout.triggered.connect(self.about)
    def setting_enable(self):
        # 当选中窗Kaiser时
        if self.comboBox.currentText()=='kaiser':
            self.lineEdit_2.setEnabled(True)
            self.label_4.setText('beta')
        # 当选中窗tukey时
        elif self.comboBox.currentText()=='tukey':
            self.lineEdit_2.setEnabled(True)
            self.label_4.setText('alpha')
        # taylor窗
        elif self.comboBox.currentText()=='taylor':
            self.lineEdit_2.setEnabled(True)
            self.label_4.setText('nbar')
        # 当选中窗chebwin时
        elif self.comboBox.currentText()=='chebwin':
            self.lineEdit_2.setEnabled(True)
            self.label_4.setText('attn')
         # Gaussian窗
        elif self.comboBox.currentText()=='gaussian':
            self.lineEdit_2.setEnabled(True)
            self.label_4.setText('std')
        else:
            self.lineEdit_2.setEnabled(False)
            self.lineEdit_4.setEnabled(False)
            self.label_4.setText('Parameter')
            self.label_5.setText('Parameter2')
    def apply(self):
        # 获取点数
        self.point_num = int(self.widget.lineEdit.text())
        # 获取combo选择了第几个
        self.combo_index = self.widget.comboBox.currentIndex()
        # 获取线性还是对数模式
        self.log_mode = self.widget.comboBox_2.currentIndex()
        # 获取response模式
        self.response_mode = self.widget.comboBox_3.currentIndex()
        # 刷新图像(仅在选中窗口的情况下)
        if self.listWidget.currentItem():
            self.plot()

    def show_time(self):
        if self.actionTime_Domain.isChecked():
            self.graphicsView.show()
        else:
            self.graphicsView.hide()
    def show_freq(self):
        if self.actionFrequency_Domain_2.isChecked():
            self.graphicsView_2.show()
        else:
            self.graphicsView_2.hide()

    def create_window(self):
        # 类型和长度默认为 Hanning 和 64
        self.window_type='hann'
        self.window_length=64
        self.s_mode='symmetric'
        self.parameter_1=''
        self.parameter_2=''
        self.window[self.window_name]={'type':self.window_type,'length':self.window_length,'s_mode':self.s_mode,
                                       'parameter_1':self.parameter_1,'parameter_2':self.parameter_2}

    def listwidget_add(self):

        self.listWidget.addItem('window_'+str(self.i))
        # 得到创建的窗口名字
        self.window_name='window_'+str(self.i)
        # 把窗口的参数保存到字典中
        self.create_window()
        self.i+=1

    def listwidget_del(self):
        # 仅在选中窗口的情况下
        if self.listWidget.currentItem():
            # 获得删除的窗口名字，并且在字典中删除
            self.window_name = self.listWidget.currentItem().text()
            self.window.pop(self.window_name)
            self.listWidget.takeItem(self.listWidget.currentRow())

            # 删除后，把lineEdit和comboBox清空
            self.lineEdit.setText('')
            self.comboBox.setCurrentText('')
            self.lineEdit_3.setText('')


    def listwidget_click(self):

        self.window_name=self.listWidget.currentItem().text()
        # 选定窗口后，把窗口的参数显示在lineEdit中
        self.lineEdit.setText(self.window_name)
        # 将窗口类型显示到comboBox中
        self.comboBox.setCurrentText(self.window[self.window_name]['type'])
        # 显示长度
        self.lineEdit_3.setText(str(self.window[self.window_name]['length']))
        # 显示对称模式
        self.comboBox_2.setCurrentText(self.window[self.window_name]['s_mode'])
        # 显示参数
        self.lineEdit_2.setText(str(self.window[self.window_name]['parameter_1']))
        self.lineEdit_4.setText(str(self.window[self.window_name]['parameter_2']))
    def window_change(self):
        # 先判断是否有窗口被选中，如果没有就是再重新创建一个窗口
        if self.listWidget.currentItem():
            # 当parameter可用时，一定要填入参数
            if self.lineEdit_2.isEnabled():
                try:
                    # 判断是否为数字
                    number = float(self.lineEdit_2.text())
                except:
                    QMessageBox.warning(self, 'Warning', 'Please input number!', QMessageBox.Yes)
                    return
            # 检测是否为数字参数，否则弹出窗口警告
            if self.lineEdit.text() != '' and self.lineEdit_3.text().isdigit():
                # 获取lineEdit,comboBox,lineEdit_3的值,,并且更新到字典中
                self.window_name = self.lineEdit.text()
                self.window_type = self.comboBox.currentText()
                self.window_length = int(self.lineEdit_3.text())

                if self.lineEdit_2.isEnabled():
                    self.parameter_1 = float(self.lineEdit_2.text())
                if self.lineEdit_4.isEnabled():
                    self.parameter_2 = float(self.lineEdit_4.text())

                self.s_mode = self.comboBox_2.currentText()
                self.window[self.window_name] = {'type': self.window_type, 'length': self.window_length,
                                                 's_mode': self.s_mode,'parameter_1': self.parameter_1,'parameter_2': self.parameter_2}
                # 更新listWidget的显示
                self.listWidget.currentItem().setText(self.window_name)
                # 更新图像
                self.plot()
            else:
                QMessageBox.warning(self, 'Warning', 'Please input number!', QMessageBox.Yes)
        else:
            QMessageBox.warning(self, 'Warning', 'Please select a window!', QMessageBox.Yes)

    def plot(self):

        self.canvas1.figure.clf()
        self.canvas2.figure.clf()
        ax1 = self.canvas1.figure.add_subplot(111)
        ax2 = self.canvas2.figure.add_subplot(111)
        COLORS = list(mcolors.TABLEAU_COLORS.values()) + list(mcolors.CSS4_COLORS.values())
        j=0
        # 遍历listWidget中的窗口，画出所有窗口的图像
        for i in self.listWidget.selectedItems():
            t = np.arange(self.window[i.text()]['length'])
            # 获取窗口的类型，并获取窗函数,如果是Kaiser，还要获取beta

            window=self.getwindow(i)

            ax1.plot(t, window)
            # 计算频域
            freqs = np.arange(self.point_num) / self.point_num * 2 * np.pi
            fft_vals = np.abs(np.fft.fft(window, self.point_num)[:self.point_num])
            freqs_normalized = freqs / np.pi

            # 当选中dB模式，将幅度响应转换为dB
            if self.response_mode == 1:
                ax2.set_ylabel('Magnitude(dB)')
                ax2.set_ylim([-100, 50])
                fft_vals = np.log10(fft_vals + 1e-15) * 20
            elif self.response_mode == 0:
                ax2.set_ylabel('Magnitude')

            ax2.plot(freqs_normalized, fft_vals, color=COLORS[j])
            ax2.plot(-freqs_normalized, fft_vals, color=COLORS[j])

            j += 1

       # 设置坐标轴的范围
        if self.log_mode==1:
            if self.response_mode == 1:
                ax2.set_ylim([-150, 1e2])
            elif self.response_mode == 0:
                ax2.set_ylim([0, 50])
            ax2.set_xscale('log')
            ax2.set_xlim([1e-3, 1])
        elif self.log_mode==0:
            ax2.set_yscale('linear')
            if self.combo_index==0:
                ax2.set_xlim([0, 1])
            elif self.combo_index==1:
                ax2.set_xlim([0, 2])
            elif self.combo_index==2:
                ax2.set_xlim([-1, 1])

       # 设置图例
        if self.legend_bool==1:
            legend_name = []
            # 显示图例，用窗口的名字
            for i in self.listWidget.selectedItems():
                legend_name.append(i.text())
            ax1.legend(legend_name, loc='upper right')
            ax2.legend(legend_name)

        ax1.grid(True)
        ax1.set_xlabel('Time')
        ax1.set_ylabel('Amplitude')
        ax1.set_title('Time Domain')
        self.canvas1.draw()

        ax2.grid(True)
        ax2.set_xlabel('Frequency')
        ax2.set_ylabel('Magnitude(dB)')
        ax2.set_title('Frequency Domain')
        self.canvas2.draw()

        plt.close('all')

    def plot_deafault(self):
        self.fig1 = plt.figure()
        self.canvas1 = FigureCanvas(self.fig1)
        layout = QVBoxLayout()  # 垂直布局
        layout.addWidget(self.canvas1)
        self.fig1.subplots_adjust(left=0.2, bottom=0.2, right=0.9, top=0.9, wspace=None, hspace=None)
        self.graphicsView.setLayout(layout)  # 设置好布局之后调用函数

        self.fig2 = plt.figure()
        self.canvas2 = FigureCanvas(self.fig2)
        layout = QVBoxLayout()  # 垂直布局
        layout.addWidget(self.canvas2)
        self.graphicsView_2.setLayout(layout)  # 设置好布局之后调用函数

    def copy_window(self):
        if self.listWidget.currentItem():
            self.window[self.window_name+'_copy']={'type':self.window[self.window_name]['type'],'length':self.window[self.window_name]['length'],'s_mode':self.window[self.window_name]['s_mode']}
            self.listWidget.addItem(self.window_name+'_copy')

    def show_legend(self):
        # 如果actionLegend被选中，显示图例
        if self.actionLegend.isChecked():
            self.legend_bool = 1
            self.plot()
        else:
            self.legend_bool = 0
            self.plot()

    def full_analysis(self):
        plt.close('all')
        fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(8, 3))

        COLORS = list(mcolors.TABLEAU_COLORS.values()) + list(mcolors.CSS4_COLORS.values())
        j = 0
        # 遍历listWidget中的窗口，画出所有窗口的图像
        for i in self.listWidget.selectedItems():
            t = np.arange(self.window[i.text()]['length'])
            # 获取窗口的类型，并获取窗函数,如果是Kaiser，还要获取beta

            window=self.getwindow(i)

            ax1.plot(t, window)
            # 计算频域
            freqs = np.arange(self.point_num) / self.point_num * 2 * np.pi
            fft_vals = np.abs(np.fft.fft(window, self.point_num)[:self.point_num])
            freqs_normalized = freqs / np.pi

            # 当选中dB模式，将幅度响应转换为dB
            if self.response_mode == 1:
                ax2.set_ylabel('Magnitude(dB)')
                ax2.set_ylim([-100, 50])
                fft_vals = np.log10(fft_vals + 1e-15) * 20
            elif self.response_mode == 0:
                ax2.set_ylabel('Magnitude')
            ax2.plot(freqs_normalized, fft_vals, color=COLORS[j])
            ax2.plot(-freqs_normalized, fft_vals, color=COLORS[j])

            j += 1

        # 设置坐标轴的范围
        if self.log_mode == 1:
            if self.response_mode == 1:
                ax2.set_ylim([-150, 1e2])
            elif self.response_mode == 0:
                ax2.set_ylim([0, 50])
            ax2.set_xscale('log')
            ax2.set_xlim([1e-3, 1])
        elif self.log_mode == 0:
            ax2.set_yscale('linear')
            if self.combo_index == 0:
                ax2.set_xlim([0, 1])
            elif self.combo_index == 1:
                ax2.set_xlim([0, 2])
            elif self.combo_index == 2:
                ax2.set_xlim([-1, 1])

        # 设置图例
        if self.legend_bool == 1:
            j = 0
            legend_name = []
            # 显示图例，用窗口的名字
            for i in self.listWidget.selectedItems():
                legend_name.append(i.text())
            ax1.legend(legend_name, loc='upper right')
            ax2.legend(legend_name)

        ax1.grid(True)
        ax1.set_xlabel('Time')
        ax1.set_ylabel('Amplitude')
        ax1.set_title('Time Domain')

        ax2.grid(True)
        ax2.set_xlabel('Frequency')
        ax2.set_ylabel('Magnitude(dB)')
        ax2.set_title('Frequency Domain')

        plt.subplots_adjust(left=0.1, bottom=0.2, right=0.9, top=0.9, wspace=0.4, hspace=0.4)
        plt.show()
    def export_window(self):
        # 判断用户是否选择了窗口
        if not self.listWidget.currentItem():
            # 警告用户选择一个窗口
            QMessageBox.warning(self, "Warning", "Please select a window first!")
            return

        # 获取用户选择的文件路径
        if self.export.comboBox.currentIndex() == 0:
            save_path, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Text Files (*.txt)")
        elif self.export.comboBox.currentIndex() == 1:
            save_path, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Matlab Files (*.mat)")

        # 如果用户没有选择文件则退出函数
        if not save_path:
            return

        # 覆盖文件的时候先清空里面的内容
        with open(save_path, 'w') as f:
            f.write('')

        data_dict = {}
        # 将窗函数保存到文件
        for i in self.listWidget.selectedItems():
            # 获取窗口
            if self.comboBox.currentText() == 'kaiser' or self.comboBox.currentText() == 'gaussian' or self.comboBox.currentText() == 'tukey'or self.comboBox.currentText() == 'taylor' or self.comboBox.currentText() == 'chebwin':
                window = get_window((self.window[i.text()]['type'], float(self.window[i.text()]['parameter_1'])), int(self.window[i.text()]['length']))

            else:
                if self.window[i.text()]['s_mode'] == 'symmetric':
                    s_mode = False
                elif self.window[i.text()]['s_mode'] == 'periodic':
                    s_mode = True
                window = get_window(self.window[i.text()]['type'], int(self.window[i.text()]['length']), fftbins=s_mode)

            # 获取当前时间
            now = datetime.datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            # 将窗函数保存到txt文件
            if self.export.comboBox.currentIndex() == 0:
                with open(save_path, 'a') as f:
                    f.write('# Generated by pywindow\n')
                    f.write('# Generated at ' + dt_string + '\n')
                    f.write('Window name: ' + i.text() + '\n')
                    f.write('Window type: ' + self.window[i.text()]['type'] + '\n')
                    f.write('Window length: ' + str(self.window[i.text()]['length']) + '\n')
                    f.write('Window symmetric mode: ' + self.window[i.text()]['s_mode'] + '\n')
                    f.write('\n')
                    np.savetxt(f, window, fmt='%.7f')
                    f.write('\n')
                    f.write('\n')
            elif self.export.comboBox.currentIndex() == 1:
                window = window.reshape(-1, 1)
                data_dict[i.text()] = window
            # 将窗函数保存到mat文件
        if self.export.comboBox.currentIndex() == 1:
            sio.savemat(save_path, data_dict)
    def about(self):
        QMessageBox.about(self, "About", "pywindow Dev edition\nEmail:purehyacinth@Outlook.com")

    def getwindow(self,i):
        # 获取窗口的类型，并获取窗函数,如果是Kaiser，还要获取beta
        window_type = self.window[i.text()]['type']
        if window_type == 'kaiser' or window_type == 'gaussian' or window_type == 'tukey' or window_type == 'taylor' or window_type == 'chebwin':

            if window_type == 'kaiser':
                window_param = self.window[i.text()]['parameter_1']
            elif window_type == 'gaussian':
                window_param = float(self.window[i.text()]['parameter_1'])
            elif window_type == 'tukey':
                window_param = float(self.window[i.text()]['parameter_1'])
            elif window_type == 'taylor':
                window_param = int(self.window[i.text()]['parameter_1'])
                # 判断是否小于1
                if window_param < 1:
                    QMessageBox.warning(self, 'Warning', 'Taylor window parameter must be greater than 1!', QMessageBox.Yes)
                    return
            elif window_type == 'chebwin':
                window_param = float(self.window[i.text()]['parameter_1']), int(
                    self.window[i.text()]['parameter_2'])
            window_length = int(self.window[i.text()]['length'])
            window = get_window((window_type, window_param), Nx=window_length)

        else:
            if self.window[i.text()]['s_mode']=='symmetric':
                s_mode=False
            elif self.window[i.text()]['s_mode']=='periodic':
                s_mode=True
            window = get_window(self.window[i.text()]['type'], int(self.window[i.text()]['length']),fftbins=s_mode)

        return window
if __name__ == "__main__":
    app = QApplication(sys.argv)
    QApplication.setStyle('Fusion')
    mainWindow = MainWindow()
    # apply_stylesheet(app, theme='dark_blue.xml')
    mainWindow.show()
    sys.exit(app.exec_())