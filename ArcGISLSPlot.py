import os
import subprocess

import arcpy

# get the input parameters
graip_database_file = arcpy.GetParameterAsText(0)
desc = arcpy.Describe(graip_database_file)
graip_database_file = str(desc.catalogPath)

low_esi = arcpy.GetParameterAsText(1)
medium_esi = arcpy.GetParameterAsText(2)
high_esi = arcpy.GetParameterAsText(3)
alpha = arcpy.GetParameterAsText(4)

# construct command to execute
current_script_dir = os.path.dirname(os.path.realpath(__file__))
# put quotes around file paths in case they have spaces
graip_database_file = '"' + graip_database_file + '"'

py_script_to_execute = os.path.join(current_script_dir, 'LSPlot.py')
py_script_to_execute = '"' + py_script_to_execute + '"'
cmd = py_script_to_execute + \
      ' --mdb ' + graip_database_file + \
      ' --high-esi ' + high_esi + \
      ' --medium-esi ' + medium_esi + \
      ' --low-esi ' + low_esi + \
      ' --alpha ' + alpha

# NOTE: contents of shell command is not captured and displayed in arcgis geoprocessing window
# like other arcgis graip scripts since the display of the matplotlib blocks the process
#process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)

process = subprocess.Popen(cmd, shell=True)
arcpy.AddMessage('\nProcess started:\n')
start_message = "Please wait. It may take few seconds. Computation is in progress ..."
arcpy.AddMessage(start_message)
arcpy.AddMessage("LS Plot generated....")
