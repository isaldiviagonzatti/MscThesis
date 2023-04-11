# A Needle In A Pineapple Field

Repository for the MSc Thesis on the Study of the Current State of Pineapple Leaves Valorisation in the Context of Circular Bioeconomy in Costa Rica by [Ignacio Saldivia Gonzatti](https://www.isaldiviagonzatti.nl/)

## Usage

You can run any file and it should work out of the box. If not, check that the working directory in the script points to the parent folder (e.g., ..\\FLP)

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

The data processing was divided into different scripts. These must be run in order:

[Visualise and save road network](FLP/code/streetNetwork_manipulation.ipynb)
FLP\code\candidatesGrid.ipynb
FLP\code\distanceMatrix.ipynb
FLP\code\downloadAPIarcGIS.py
FLP\code\mergeAll.ipynb
FLP\code\nearestPALstreet.ipynb
FLP\code\optimisation.ipynb
FLP\code\PAL_manipulation.ipynb
FLP\code\planesReguladores_zoning.ipynb
FLP\code\resultsOpti.ipynb
FLP\code\sanCarlosPlan.ipynb

## License

[MIT](https://choosealicense.com/licenses/mit/)
