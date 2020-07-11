# SynPolarityAnalysis
Image data analysis of synthetic unipolarity in E. coli


`SynPolarityAnalysis` is a Python script for analyzing spatial organizing protein distribution in bacterial cell. 

- [Overview](#overview)
- [Documentation](#documentation)
- [System Requirements](#system-requirements)
- [Installation Guide](#installation-guide)
- [Data Analysis](#setting-up-the-development-environment)

# Overview
Our script serves as an interface containing self-defined scores and statistical tools to visualize the characteristics of spatial features such as polarity. The software Oufti is required to convert the image data into MATLAB structure array and save in `.mat` files. Our script serves as an interface containing tools to visualize the characteristics of spatial features such as polarity.

# System Requirements

## Software requirements
### OS Requirements
The scripthas been tested on the following systems:
+ Windows: Microsoft Windows 10 Home (1903)
+ Linux: Centos Linux 7 (core)

### Oufti: an open-source software
For exporting `.mat` files from microscopy data, Oufti is essential for users to obtain information of single bacterial cells. The software is free to download from [https://oufti.org/download/register.php](https://oufti.org/download/register.php) in which minimal MATLAB runtime is provided. To understand more uses based on Oufti, please visit [https://oufti.org/tutorial.htm](https://oufti.org/tutorial.htm).

### Python Dependencies
The scientific-related packages are imported and applied by our analysis scripts.
```
numpy
scipy
pandas
matplotlib
seaborn
```

# Installation Guide:

### Install from Github
```
git clone https://github.com/dwgoblue/SynPolarityAnalysis.git
```

## Data Acquisitions

### Raw Data Acquisitions
You need to follow the following workflow to ensure correct analysis. 
- Load phase contrast images into Oufti as channel 0.
- Load fluorescence signals with unipolar protein, e.g. PopZ, as channel 1.
- Load fluorescence signals into channel 2 from the proteins with or without the controls of the unipolar protein, such as SpmX and DivIVA in our paper.

Once finished, cells could be isolated manually or automatically which initiates a structure array to record information of each cell. The next step is to reuse meshes which records the positions of cells in order to extract fluorescent signals. We recommend visit the Oufti instructions (https://oufti.org/application.htm) and get more details about the uses of Oufti.

### Time-lapse data acquisitions
The procedure to analyze time-lapse images is similar to the process for snapshot images. Specifically, the recordings have to be separated by time points. It is noted that the images can only contain one cell and its daughter cell if you plan to analyze single cell division e.g. kymograph. More importantly, one folder must contain one cell data, and the name of the `.mat` files must stick to the series of time points. For example, time-lapse `.mat` files of a cell with `ID:1` have to be put in the same folder and. The files inside the folder are named `1`, `2`, `3` if the files are recorded at three sequential time points.
```
.
+-- [Jul72020]TimeLapseData
+-- Cell1
|   +-- 1.mat
|   +-- 2.mat
|   +-- 3.mat
+-- Cell2
|   +-- 1.mat
|   +-- 2.mat
|   +-- 3.mat
...
```

## Data Analysis

### Data inputs
There are two ways that you can inform the program where the files are for analysis:

1. You are able to add a new function block in `DataInput.py` for which here provides a template.
```
def fig1a():

	parent_path = r'you_path'

	# If every channel is separated, np.array(['TwoInOne']) should be added in the list.
	# If there is no PopZ or other controller protein in channel one, np.array(['NP']) should be added in the list.
	group1 = [np.array(['TwoInOne']), np.array(['NP'])]
	group2 = [np.array(['TwoInOne'])]

	# File names are named by their ID.
	for mark in ['01', '02', '03']:
		img = np.array(['CTRL-{}.mat'.format(mark)])
		group1.append(img)

	for mark in ['01', '02', '03']:
		img = np.array(['EXP-{}.mat'.format(mark)])
		group2.append(img)
		
	# Name of each group.
	labels = np.array(['CTRL', 'EXP'])

	Data = {}
	Data['parent_path'] = parent_path
	Data['exp'] = exp
	Data['labels'] = labels

	return Data
```
2. The second way is to create or edit `DataInput.txt`.

### Execute the scripts
The script offers four pipelines to analyze microscopy data converted from Oufti, including 
```
PopZOnlyPipline 
DiffuseSignalPipline
TwoChannelPipline
TimeLapsePipline
```
### PopZ-only Data
If there is only one channel which is PopZ signal saved in the `.mat` file, we can apply the `PopZOnlyPipline` in which `tot` (total intensity) and `pks` (peak score) analysis are offered. Here is an example to call the function.
```
from Piplines import*
Starter = PiplinesObj(fig2j,
                      TimeLapse=False,
                      columns=[(0,1)])
Starter.TwoChannelPipline(plots=['tot'])
```
### Signals Recorded from Diffusible Protein
If you are not assumed the protein with spatial patterns, and there is only one channel saved in the `.mat` file, we can apply the `DiffuseSignalPipline` in which `tot-box` (total intensity with boxplot) and`tot-box` (total intensity with violinplot) analysis are offered. Here is an example to call the function.
```
from Piplines import*
Starter = PiplinesObj(fig2j,
                      TimeLapse=False,
                      columns=[(0,1)])
Starter.DiffuseSignalPipline(plots=['tot-box'])
```

### Signals recorded in two or more channels
If you are not assumed the protein with spatial patterns, and there is only one channel saved in the `.mat` file, we can apply the `DiffuseSignalPipline` in which `tot-box` (total intensity with boxplot) and`tot-box` (total intensity with violinplot) analysis are offered. Here is an example to call the function.
```
from Piplines import*
Starter = PiplinesObj(fig2j,
                      TimeLapse=False,
                      columns=[(0,1)])
Starter.TwoChannelPipline(plots=['tot'])
```
To analyze the linescans of two profiles, however, it requires an additional input which is the labels of the select groups.
```
Starter.TwoChannelPipline(plots=['twoprofiles'],
                          twoselect=['NSSCPG', 'NSSCG'])
```
Because Oufti only offers two channels for analysis, you may want to combine two files together if there are three types of fluorescence. For this scenario, we need to ask the function to analyze two files shared the same PopZ (or other controller protein) channel. Thus, the additional input contains the indices of the files that should be bound together.
```
Starter.TwoChannelPipline(plots=['pearson'],
                          FPextension=[1, 2])
```
Moreover, the function offers choices `tot`, `pearson`, `ps`, `lr`, `twoprofile`, `ms`, `trace` and `statprofile` for analysis.

### Time-lapse Data
After rearranging files and folders following to the rules mentioned in the previous section, you are able to execute the analysis for time-lapse data.
```
from Piplines import*
Starter = PiplinesObj(TL_Exp, TimeLapse=True)
Starter.TimeLapsePipline()
```
