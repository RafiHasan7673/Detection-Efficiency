****Requairements****

Environmant = Python 3.8 or 3.8 plus
IDE = Pycham or spyder or vscode
package = os and pandas

****Description**

This Python code processes CSV files in a specified input folder. It reads each CSV file using the pandas library, filters the data based on the 'icheight' column values, and then saves the filtered data into two separate CSV files in the same output folder. The new files are named with prefixes "CG" and "CC" indicating different conditions based on the 'icheight' column. If the 'icheight' column values is equal to 0 (for cloud-to-ground lightning), it will separate the rows in CG file.  If the 'icheight' column value is greater than 0 (for cloud-to-cloud lightning), it will separate the rows in CC file.