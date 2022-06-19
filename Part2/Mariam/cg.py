# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cg.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import Qt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout , QShortcut, QLabel, QSlider, QStyle, QSizePolicy, QFileDialog
import vtk
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor as qvtk

class Ui_part2(object):
        def setupUi(self, part2):
                part2.setObjectName("part2")
                part2.resize(910, 640)
                self.centralwidget = QtWidgets.QWidget(part2)
                self.centralwidget.setObjectName("centralwidget")
                self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
                self.verticalLayout.setObjectName("verticalLayout")
                self.widget = QtWidgets.QWidget(self.centralwidget)
                self.widget.setObjectName("widget")
                self.groupBox = QtWidgets.QGroupBox(self.widget)
                self.groupBox.setGeometry(QtCore.QRect(30, 20, 351, 341))
                self.groupBox.setObjectName("groupBox")
                self.horizontalLayoutWidget = QtWidgets.QWidget(self.groupBox)
                self.horizontalLayoutWidget.setGeometry(QtCore.QRect(9, 20, 331, 311))
                self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
                self.window = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
                self.window.setContentsMargins(0, 0, 0, 0)
                self.window.setObjectName("window")
                self.textEdit = QtWidgets.QTextEdit(self.widget)
                self.textEdit.setGeometry(QtCore.QRect(160, 380, 201, 31))
                self.textEdit.setObjectName("textEdit")
                self.groupBox_2 = QtWidgets.QGroupBox(self.widget)
                self.groupBox_2.setGeometry(QtCore.QRect(510, 20, 351, 341))
                self.groupBox_2.setObjectName("groupBox_2")
                self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_2)
                self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 20, 331, 311))
                self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
                self.window_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
                self.window_2.setContentsMargins(0, 0, 0, 0)
                self.window_2.setObjectName("window_2")
                self.pushButton = QtWidgets.QPushButton(self.widget)
                self.pushButton.setGeometry(QtCore.QRect(60, 382, 75, 31))
                self.pushButton.setObjectName("pushButton")
                self.textEdit_2 = QtWidgets.QTextEdit(self.widget)
                self.textEdit_2.setGeometry(QtCore.QRect(640, 378, 201, 31))
                self.textEdit_2.setObjectName("textEdit_2")
                self.pushButton_2 = QtWidgets.QPushButton(self.widget)
                self.pushButton_2.setGeometry(QtCore.QRect(540, 380, 75, 31))
                self.pushButton_2.setObjectName("pushButton_2")
                self.line = QtWidgets.QFrame(self.widget)
                self.line.setGeometry(QtCore.QRect(420, 0, 51, 601))
                self.line.setFrameShape(QtWidgets.QFrame.VLine)
                self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
                self.line.setObjectName("line")
                self.s = QtWidgets.QSlider(self.widget)
                self.s.setGeometry(QtCore.QRect(210, 450, 160, 22))
                self.s.setOrientation(QtCore.Qt.Horizontal)
                self.s.setObjectName("s")
                self.s_2 = QtWidgets.QSlider(self.widget)
                self.s_2.setGeometry(QtCore.QRect(100, 530, 160, 22))
                self.s_2.setOrientation(QtCore.Qt.Horizontal)
                self.s_2.setObjectName("s_2")
                self.s_4 = QtWidgets.QSlider(self.widget)
                self.s_4.setGeometry(QtCore.QRect(100, 560, 160, 22))
                self.s_4.setOrientation(QtCore.Qt.Horizontal)
                self.s_4.setObjectName("s_4")
                self.s_5 = QtWidgets.QSlider(self.widget)
                self.s_5.setGeometry(QtCore.QRect(100, 500, 160, 22))
                self.s_5.setOrientation(QtCore.Qt.Horizontal)
                self.s_5.setObjectName("s_5")
                self.s_6 = QtWidgets.QSlider(self.widget)
                self.s_6.setGeometry(QtCore.QRect(570, 560, 160, 22))
                self.s_6.setOrientation(QtCore.Qt.Horizontal)
                self.s_6.setObjectName("s_6")
                self.s_7 = QtWidgets.QSlider(self.widget)
                self.s_7.setGeometry(QtCore.QRect(570, 500, 160, 22))
                self.s_7.setOrientation(QtCore.Qt.Horizontal)
                self.s_7.setObjectName("s_7")
                self.s_3 = QtWidgets.QSlider(self.widget)
                self.s_3.setGeometry(QtCore.QRect(680, 450, 160, 22))
                self.s_3.setOrientation(QtCore.Qt.Horizontal)
                self.s_3.setObjectName("s_3")
                self.s_8 = QtWidgets.QSlider(self.widget)
                self.s_8.setGeometry(QtCore.QRect(570, 530, 160, 22))
                self.s_8.setOrientation(QtCore.Qt.Horizontal)
                self.s_8.setObjectName("s_8")
                self.comboBox = QtWidgets.QComboBox(self.widget)
                self.comboBox.setGeometry(QtCore.QRect(570, 450, 71, 22))
                self.comboBox.setObjectName("comboBox")
                self.comboBox.addItem("1")
                self.comboBox.addItem("100")
                self.comboBox.addItem("1000")
                self.comboBox.addItem("1500")
                self.label = QtWidgets.QLabel(self.widget)
                self.label.setGeometry(QtCore.QRect(30, 500, 47, 31))
                self.label.setObjectName("label")
                self.label_2 = QtWidgets.QLabel(self.widget)
                self.label_2.setGeometry(QtCore.QRect(30, 530, 47, 21))
                self.label_2.setObjectName("label_2")
                self.label_3 = QtWidgets.QLabel(self.widget)
                self.label_3.setGeometry(QtCore.QRect(30, 560, 47, 21))
                self.label_3.setObjectName("label_3")
                self.label_4 = QtWidgets.QLabel(self.widget)
                self.label_4.setGeometry(QtCore.QRect(510, 560, 47, 21))
                self.label_4.setObjectName("label_4")
                self.label_5 = QtWidgets.QLabel(self.widget)
                self.label_5.setGeometry(QtCore.QRect(510, 500, 47, 31))
                self.label_5.setObjectName("label_5")
                self.label_6 = QtWidgets.QLabel(self.widget)
                self.label_6.setGeometry(QtCore.QRect(510, 530, 47, 21))
                self.label_6.setObjectName("label_6")
                self.label_7 = QtWidgets.QLabel(self.widget)
                self.label_7.setGeometry(QtCore.QRect(90, 440, 101, 31))
                self.label_7.setObjectName("label_7")
                self.line_2 = QtWidgets.QFrame(self.widget)
                self.line_2.setGeometry(QtCore.QRect(0, 355, 901, 31))
                self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
                self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
                self.line_2.setObjectName("line_2")
                self.verticalLayout.addWidget(self.widget)
                part2.setCentralWidget(self.centralwidget)
                self.statusbar = QtWidgets.QStatusBar(part2)
                self.statusbar.setObjectName("statusbar")
                part2.setStatusBar(self.statusbar)

                sliders = [self.s_2,self.s_4,self.s_5,self.s_6,self.s_7,self.s_3,self.s_8]
                for i in sliders:
                        self.slider_set(i)
                self.iso_s(self.s)

                self.s.valueChanged.connect(self.valueChange1)
                self.s_2.valueChanged.connect(self.valueChange1)
                self.s_4.valueChanged.connect(self.valueChange1)
                self.s_5.valueChanged.connect(self.valueChange1)

                self.s_3.valueChanged.connect(self.valueChange2)
                self.s_6.valueChanged.connect(self.valueChange2)
                self.s_7.valueChanged.connect(self.valueChange2)
                self.s_8.valueChanged.connect(self.valueChange2)


                self.pushButton.clicked.connect(self.loading1)
                self.pushButton_2.clicked.connect(self.loading2)
                self.retranslateUi(part2)
                QtCore.QMetaObject.connectSlotsByName(part2)

        def valueChange2(self):
                self.vtk2.volumeScalarOpacity.AddPoint(int(self.comboBox.currentText()), self.s_3.value()/10)
                self.vtk2.volumeColor.AddRGBPoint(int(self.comboBox.currentText()),self.s_6.value()/10, self.s_7.value()/10, self.s_8.value()/10)
                self.vtk2.renWin.update()


        def valueChange1(self):
                self.vtk1.contour.SetValue(0, self.s.value())
                self.vtk1.actor.GetProperty().SetColor(self.s_2.value()/10, self.s_4.value()/10, self.s_5.value()/10)
                self.vtk1.renWin.update()

        
        def loading1(self):
                for i in reversed(range(self.window.count())): 
                        self.window.itemAt(i).widget().deleteLater()
                file = QFileDialog.getExistingDirectory()
                self.textEdit.setPlainText(file)
                self.vtk1 = vtkk(file)
                self.vtk1.surface_rendering()
                self.window.addWidget(self.vtk1.frame)
                

        def loading2(self):
                for i in reversed(range(self.window_2.count())): 
                        self.window_2.itemAt(i).widget().deleteLater()
                file = QFileDialog.getExistingDirectory()
                self.textEdit_2.setPlainText(file)
                self.vtk2 = vtkk(file)
                self.vtk2.ray_casting()
                self.window_2.addWidget(self.vtk2.frame)



        def iso_s(self,set_slider):
                
                set_slider.setTickPosition(QSlider.TicksRight)
                set_slider.setTickInterval(1)
                set_slider.setSingleStep(1)
                set_slider.setValue(1500)
                set_slider.setMinimum(0)
                set_slider.setMaximum(1500)

        def slider_set(self,set_slider):

                set_slider.setTickPosition(QSlider.TicksRight)
                set_slider.setTickInterval(100)
                set_slider.setSingleStep(100)
                set_slider.setValue(10)
                set_slider.setMinimum(0)
                set_slider.setMaximum(10)



        def retranslateUi(self, part2):
                _translate = QtCore.QCoreApplication.translate
                part2.setWindowTitle(_translate("part2", "Part_2"))
                self.groupBox.setTitle(_translate("part2", "surface rendering"))
                self.groupBox_2.setTitle(_translate("part2", "Ray Casting"))
                self.pushButton.setText(_translate("part2", "Browse"))
                self.pushButton_2.setText(_translate("part2", "Browse"))
                self.label.setText(_translate("part2", "<html><head/><body><p><span style=\" font-size:14pt;\">R</span></p></body></html>"))
                self.label_2.setText(_translate("part2", "<html><head/><body><p><span style=\" font-size:14pt;\">G</span></p></body></html>"))
                self.label_3.setText(_translate("part2", "<html><head/><body><p><span style=\" font-size:14pt;\">B</span></p></body></html>"))
                self.label_4.setText(_translate("part2", "<html><head/><body><p><span style=\" font-size:14pt;\">B</span></p></body></html>"))
                self.label_5.setText(_translate("part2", "<html><head/><body><p><span style=\" font-size:14pt;\">R</span></p></body></html>"))
                self.label_6.setText(_translate("part2", "<html><head/><body><p><span style=\" font-size:14pt;\">G</span></p></body></html>"))
                self.label_7.setText(_translate("part2", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">ISO value</span></p></body></html>"))



class vtkk : 

        def __init__(self,direc_path):
                self.dirc = direc_path
                self.frame = Qt.QFrame()
                self.contour = 0
                self.load_data()
                self.renWin = 0
                
        def load_data(self):
                self.reader = vtk.vtkDICOMImageReader()
                self.reader.SetDirectoryName(self.dirc)
                self.reader.Update()
                # vtkImageData
                self.imageData = self.reader.GetOutput()
        def surface_rendering(self):
                self.contour = vtk.vtkContourFilter()
                self.contour.SetValue(0,1500) # 0.5*(minVal + maxVal))
                self.contour.SetInputData(self.imageData)
                surfaceNormals = vtk.vtkPolyDataNormals()
                surfaceNormals.SetInputConnection(self.contour.GetOutputPort())
                surfaceNormals.SetFeatureAngle(90.0)
                mapper = vtk.vtkPolyDataMapper()
                mapper.ScalarVisibilityOff()
                mapper.SetInputConnection(surfaceNormals.GetOutputPort())
                self.actor = vtk.vtkActor()
                self.actor.SetMapper(mapper)
                self.actor.GetProperty().SetColor(222/256., 184/256., 135/256.)
                self.sr_rendering()
        def ray_casting(self):
                self.volumeMapper = vtk.vtkSmartVolumeMapper()
                self.volumeMapper.SetInputData(self.imageData)
                self.volumeColor = vtk.vtkColorTransferFunction()
                self.volumeColor.AddRGBPoint(0,    0.00, 0.000, 0.00) 
                self.volumeColor.AddRGBPoint(1,    0.00, 0.000, 0.00) 
                self.volumeColor.AddRGBPoint(100,    1.00, 1.000, 1.00)   
                self.volumeColor.AddRGBPoint(500,    1.0, 1.00, 1.00)   
                self.volumeColor.AddRGBPoint(1000,   1.00, 1.00, 1.00)   
                self.volumeColor.AddRGBPoint(1500,   1.0, 1.0, 1.0) 
                self.volumeColor.AddRGBPoint(2000,   0, 0, 0)     
                
                self.volumeScalarOpacity = vtk.vtkPiecewiseFunction()

                self.volumeScalarOpacity.AddPoint(0,  0.00)
                self.volumeScalarOpacity.AddPoint(1,  0.00)
                self.volumeScalarOpacity.AddPoint(100,  1.00)
                self.volumeScalarOpacity.AddPoint(500,  1.0000)
                self.volumeScalarOpacity.AddPoint(1000, 1.000)
                self.volumeScalarOpacity.AddPoint(1500, 1.0)
                self.volumeScalarOpacity.AddPoint(2000, 0.00)

               
                volumeGradientOpacity = vtk.vtkPiecewiseFunction()

                volumeGradientOpacity.AddPoint(0,   1.0)
                volumeGradientOpacity.AddPoint(1,   1.0)
                volumeGradientOpacity.AddPoint(100,   1.0)
                volumeGradientOpacity.AddPoint(100,   1.0)
                volumeGradientOpacity.AddPoint(500, 1.0)
                volumeGradientOpacity.AddPoint(1000,  1.0)
                volumeGradientOpacity.AddPoint(1500, 1.0)

                
                volumeProperty = vtk.vtkVolumeProperty()
                volumeProperty.SetColor(self.volumeColor)
                volumeProperty.SetScalarOpacity(self.volumeScalarOpacity)
                volumeProperty.SetGradientOpacity(volumeGradientOpacity)
                volumeProperty.SetInterpolationTypeToLinear()
                volumeProperty.ShadeOn()
                
                self.volume = vtk.vtkVolume()
                self.volume.SetMapper(self.volumeMapper)
                self.volume.SetProperty(volumeProperty)
                self.rc_rendering()
                # Finally, add the volume to the renderer
              

        def sr_rendering(self):

                self.renWin = qvtk(self.frame)
                self.ren = vtk.vtkRenderer()
                self.ren.AddActor(self.actor)
                self.ren.SetBackground(0, 0, 0)
                self.renWin.GetRenderWindow().AddRenderer(self.ren)
                self.renWin.SetSize( 411, 411)

                self.iren = self.renWin.GetRenderWindow().GetInteractor()
                
        

                self.iren.Initialize()
                self.renWin.Render()
                self.iren.Start()
        def rc_rendering(self):
    
                self.renWin = qvtk(self.frame)
                self.ren = vtk.vtkRenderer()
                camera =  self.ren.GetActiveCamera()
                c = self.volume.GetCenter()
                camera.SetFocalPoint(c[0], c[1], c[2])
                camera.SetPosition(c[0] + 400, c[1], c[2])
                camera.SetViewUp(0, 0, -1)
                self.renWin.SetSize(640, 480)
                self.ren.AddViewProp(self.volume)
                self.renWin.GetRenderWindow().AddRenderer(self.ren)
                self.renWin.SetSize( 411, 411)
                self.iren = self.renWin.GetRenderWindow().GetInteractor()
                self.iren.Initialize()
                self.renWin.Render()
                self.iren.Start()






if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    p2 = QtWidgets.QMainWindow()
    ui = Ui_part2()
    ui.setupUi(p2)
    p2.show()
    sys.exit(app.exec_())