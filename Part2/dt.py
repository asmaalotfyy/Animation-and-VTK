import vtk
import os
import numpy
ren = vtk.vtkRenderer()
renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren)
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)

dir = './Ankle'

reader = vtk.vtkDICOMImageReader()
reader.SetDirectoryName(dir)
reader.Update()

imageData = reader.GetOutput()

volumeMapper = vtk.vtkSmartVolumeMapper()
if vtk.VTK_MAJOR_VERSION <= 5:
  volumeMapper.SetInputConnection(imageData.GetProducerPort())
else:
  volumeMapper.SetInputData(imageData)

volumeColor = vtk.vtkColorTransferFunction()
volumeColor.AddRGBPoint(50,    1.00, 0.000, 0.00) 
volumeColor.AddRGBPoint(100,    1.00, 0.000, 0.00)   #mold
volumeColor.AddRGBPoint(500,    1.0, 1.00, 1.00)   #skin
volumeColor.AddRGBPoint(1000,   1.00, 1.00, 1.00)   #skin
volumeColor.AddRGBPoint(1500,   1.0, 1.0, 1.0)   #bones
volumeColor.AddRGBPoint(2000,   1.00, 1.00, 1.00)   #dense bones e.g. teeth

# The opacity transfer function is used to control the opacity
# of different tissue types.
volumeScalarOpacity = vtk.vtkPiecewiseFunction()
volumeScalarOpacity.AddPoint(0,  0.000)
volumeScalarOpacity.AddPoint(1,  0.00)
volumeScalarOpacity.AddPoint(100,  0.00)
volumeScalarOpacity.AddPoint(500,  1.0000)
volumeScalarOpacity.AddPoint(1000, 1.000)
volumeScalarOpacity.AddPoint(1500, 1.0)
volumeScalarOpacity.AddPoint(2000, 0.00)

# The gradient opacity function is used to decrease the opacity
# in the "flat" regions of the volume while maintaining the opacity
# at the boundaries between tissue types.  The gradient is measured
# as the amount by which the intensity changes over unit distance.
# For most medical data, the unit distance is 1mm.
volumeGradientOpacity = vtk.vtkPiecewiseFunction()
volumeGradientOpacity.AddPoint(0,   0.0)
volumeGradientOpacity.AddPoint(1,   0.0)
volumeGradientOpacity.AddPoint(100,   0.0)
volumeGradientOpacity.AddPoint(500, 1.0)
volumeGradientOpacity.AddPoint(1000,  1.0)
volumeGradientOpacity.AddPoint(1500,1.0)
volumeGradientOpacity.AddPoint(2000, 1.0)

# The VolumeProperty attaches the color and opacity functions to the
# volume, and sets other volume properties.  The interpolation should
# be set to linear to do a high-quality rendering.  The ShadeOn option
# turns on directional lighting, which will usually enhance the
# appearance of the volume and make it look more "3D".  However,
# the quality of the shading depends on how accurately the gradient
# of the volume can be calculated, and for noisy data the gradient
# estimation will be very poor.  The impact of the shading can be
# decreased by increasing the Ambient coefficient while decreasing
# the Diffuse and Specular coefficient.  To increase the impact
# of shading, decrease the Ambient and increase the Diffuse and Specular.
volumeProperty = vtk.vtkVolumeProperty()
volumeProperty.SetColor(volumeColor)
volumeProperty.SetScalarOpacity(volumeScalarOpacity)
volumeProperty.SetGradientOpacity(volumeGradientOpacity)
volumeProperty.SetInterpolationTypeToLinear()
volumeProperty.ShadeOn()
# volumeProperty.SetAmbient(0.5)
# volumeProperty.SetDiffuse(0.6)
# volumeProperty.SetSpecular(0.2)

# The vtkVolume is a vtkProp3D (like a vtkActor) and controls the position
# and orientation of the volume in world coordinates.
volume = vtk.vtkVolume()
volume.SetMapper(volumeMapper)
volume.SetProperty(volumeProperty)

# Finally, add the volume to the renderer
ren.AddViewProp(volume)

# Set up an initial view of the volume.  The focal point will be the
# center of the volume, and the camera position will be 400mm to the
# patient's left (whis is our right).
camera =  ren.GetActiveCamera()
c = volume.GetCenter()
camera.SetFocalPoint(c[0], c[1], c[2])
camera.SetPosition(c[0] + 400, c[1], c[2])
camera.SetViewUp(0, 0, -1)

# Increase the size of the render window
renWin.SetSize(640, 480)

# Interact with the data.
iren.Initialize()
renWin.Render()
iren.Start()

