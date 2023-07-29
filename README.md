# Export-data-of-one-calculation-point-from-Sobek
Sobek is a program used for hydrological calculations

This Python script is designed to extract the water levels of a specified calculation point from a Sobek HIS-file. The output is exported to a .csv file and visualized through a plot.
Sobek is program made by Deltares and used by Hydrologists.
![alt text](https://github.com/HulsterHydrology/Export-data-of-one-calculation-point-from-Sobek/blob/main/1184.png)

**Prerequisites**
To run this script, you need to have Python 3 installed on your system. The script also depends on several packages, which can be installed via pip.

If you are using Miniconda or Anaconda, you can install geopandas using:

conda install geopandas
The hkvsobekpy package, which this script uses, will automatically install tqdm and fire as dependencies. However, other required packages need to be installed separately as Windows cannot compile these packages from the source.

You can install these packages using pip:

pip install numpy scipy pandas GDAL shapely pyproj Fiona geopandas matplotlib
Please note that if Python is not installed on your system, it's recommended to use Anaconda.

**Setup**
Place the export_waterlevels_one_location_in_sobek.py script in a directory on your system.

Next, you need to update the following parameters in the script:

location_id: This is the id of the location from which you want to export water levels.
his_file_path: This is the path to your HIS-file.
How to Run
The script can be executed in any Python environment.

**To run the script:
**Navigate to the directory containing ahn3_download.py using your file explorer.
Run the script with your Python interpreter. For instance, if you are using Anaconda, you can run the script like so: C:\Users\n_de_\anaconda3\python.exe ahn3_download.py.

**Support**
If you have any questions or need further assistance, feel free to reach out at hulsterhydrology@gmail.com.
