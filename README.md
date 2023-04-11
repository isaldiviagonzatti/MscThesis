# A Needle In A Pineapple Field

Repository for the MSc Thesis on the Study of the Current State of Pineapple Leaves Valorisation in the Context of Circular Bioeconomy in Costa Rica by [Ignacio Saldivia Gonzatti](https://www.isaldiviagonzatti.nl/)

## Usage

You can run any file and it should work out of the box. If not, check that the working directory in the script points to the parent folder (e.g., ..//FLP)

If you run the line 
```python
os.chdir('..')
```
twice, the wd will go one folder out. 

If you are replicating this project and run into problems, please open an issue. Pull requests are welcome

## Organisation of folders

Data contains all raw data as downloaded from the source

Code contains the code to analyse the data

Output contains the analysed data and the generated plots

The MSc thesis is divided into two main projects: Facility Location Problem (FLP) and Fuzzy Cognitive Map (FCM)

### FLP

The data processing was divided into different scripts. Some require data generated in other scripts. Running in the following order should work. In any case, all data is already in the [output](FLP/output) folder.

* Visualise and store road network [streetNetwork_manipulation](FLP/code/streetNetwork_manipulation.ipynb)

* Transform PAL data and store geometry and quantity [PAL_manipulation](FLP/code/PAL_manipulation.ipynb)

* Get nearest road node to PAL field [nearestPALstreet](FLP/code/nearestPALstreet.ipynb)

* Generate candidate locations [candidatesGrid](FLP/code/candidatesGrid.ipynb)

* Calculate distance between candidate facilities and PAL fields [distanceMatrix](FLP/code/distanceMatrix.ipynb)

* Merge all generated data for optimisation [mergeAll](FLP/code/mergeAll.ipynb)

* Run FLP optimisation [optimisation](FLP/code/optimisation.ipynb)

* Analyse and plot optimisation results [resultsOpti](FLP/code/resultsOpti.ipynb)

Other

* Zoning map of Quesada [sanCarlosPlan](FLP/code/sanCarlosPlan.ipynb)

* Download and access zoning areas information of Costa Rica [planesReguladores_zoning](FLP/code/planesReguladores_zoning.ipynb)

* Download all GIS data from profile [downloadAPIarcGIS](FLP/code/downloadAPIarcGIS.py)

### FCM

* Code to generate transcript from interviews [transcriptWhisper](FCM/code/transcriptWhisper.ipynb)

* Transform survey responses data for FCM analysis [expertsResClean](FCM/code/expertsResClean.ipynb)

* FCM analysis [FCMpy_analysis](FCM/code/FCMpy_analysis.ipynb)

* Plots for proof of Fuzzy Logic [proofFuzzyLogic](FCM/code/proofFuzzyLogic.ipynb)

## License

[MIT](https://choosealicense.com/licenses/mit/)
