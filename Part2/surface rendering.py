import vtk
import os
import numpy

dir = './Head'

reader = vtk.vtkDICOMImageReader()
reader.SetDirectoryName(dir)
reader.Update()



# vtkImageData
imageData = reader.GetOutput()


contour = vtk.vtkContourFilter()
contour.SetInput(imageData)
contour.SetValue(0, 10.0) # 0.5*(minVal + maxVal))
contour.SetArrayComponent(0) # scalar
contour.ComputeNormalsOn()
contour.SetNumberOfContours(1)
#contour.SetInputConnection(reader.GetOutputPort())
#contour.SetInputConnection(smooth.GetOutputPort())

mapper = vtk.vtkPolyDataMapper()
mapper.ScalarVisibilityOff()
mapper.SetInputConnection(contour.GetOutputPort())

actor = vtk.vtkActor()
actor.SetMapper(mapper)
actor.GetProperty().SetColor(222/256., 184/256., 135/256.)

renWin = vtk.vtkRenderWindow()
ren = vtk.vtkRenderer()
ren.AddActor(actor)
ren.SetBackground(0, 0, 0)

renWin.AddRenderer(ren)
renWin.SetSize(800, 800)

iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)

iren.Initialize()
renWin.Render()
iren.Start()
