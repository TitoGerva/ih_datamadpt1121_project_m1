<p align="left"><img src="https://cdn-images-1.medium.com/max/184/1*2GDcaeYIx_bQAZLxWM4PsQ@2x.png"></p>

# __ih_datamadpt1121_project_m1__

Ironhack Madrid - Data Analytics Part Time - November 2021 - Project Module 1

Student: Gervasio Feliciosi

# __EXERCISE_INSTRUCTIONS:__

## **Data:**

There are 2 main datasources:

- **Azure SQL Database.** The database contains information from the BiciMAD stations including their location (i.e.: latitude / longitude). In order to access the database you may need the following credentials:
```
Server name:   sqlironhack
Database:      BiciMAD
```
> __IMPORTANT =>__ Username and password will be provided in class.


- **API REST.** We will use the API REST from the [Portal de datos abiertos del Ayuntamiento de Madrid](https://datos.madrid.es/nuevoMadrid/swagger-ui-master-2.2.10/dist/index.html?url=/egobfiles/api.datos.madrid.es.json#/), where you can find the __Catálogo de datos__ with more than 70 datasets.

> __IMPORTANT =>__ Specific datasets will be assigned to each student in order to perform the challenges.


---

## **Main Challenge:**

You must create a Python App (**Data Pipeline**) that allow their potential users to find the nearest BiciMAD station to a set of places of interest. The output table should look similar to:

| Place of interest | Type of place (*) | Place address | BiciMAD station | Station location |
|---------|----------|-------|------------|----------|
| Auditorio Carmen Laforet (Ciudad Lineal)   | Centros Culturales | Calle Jazmin, 46 | Legazpi | Calle Bolívar, 3 |
| Centro Comunitario Casino de la Reina | Centros municipales de enseñanzas artísticas | Calle Casino, 3 | Chamartin | Calle Rodríguez Jaén, 40 |
| ...     | ...            | ...        | ...      | ...        |
> __(*)__ There is a list of datasets each one with different places. A specific dataset will be assigned to each student. 


**Your project must meet the following requirements:**

- It must be contained in a GitHub repository which includes a README file that explains the aim and content of your code. You may follow the structure suggested [here](https://github.com/potacho/data-project-template).

- It must create, at least, a `.csv` file including the requested table (i.e. Main Challenge). Alternatively, you may create an image, pdf, plot or any other output format that you may find convenient. You may also send your output by e-mail, upload it to a cloud repository, etc. 

- It must provide, at least, two options for the final user to select when executing using `argparse`: **(1)** To get the table for every 'Place of interest' included in the dataset (or a set of them), **(2)** To get the table for a specific 'Place of interest' imputed by the user.

**Additionally:**

- You must prepare a 4 minutes presentation (ppt, canva, etc.) to explain your project (Instructors will provide further details about the content of the presentation).

- The last slide of your presentation must include your candidate for the **'Ironhack Data Code Beauty Pageant'**. 


---

### **Bonus 1:**

You may include in your table the availability of bikes in each station.

---

### **Bonus 2:**

You may improve the usability of your app by using [FuzzyWuzzy](https://pypi.org/project/fuzzywuzzy/).

---

### **Bonus 3:**

Feel free to enrich your output data with any data you may find relevant (e.g.: wiki info for every place of interest).

--- 

## **Project Main Stack**

- [Azure SQL Database](https://portal.azure.com/)

- [SQL Alchemy](https://docs.sqlalchemy.org/en/13/intro.html) (alternatively you can use _Azure Data Studio_)

- [Requests](https://requests.readthedocs.io/)

- [Pandas](https://pandas.pydata.org/pandas-docs/stable/reference/index.html)

- Module `geo_calculations.py`

- [Argparse](https://docs.python.org/3.7/library/argparse.html)


<p align="left"><img src="https://cdn-images-1.medium.com/max/184/1*2GDcaeYIx_bQAZLxWM4PsQ@2x.png"></p>

# __FINAL SOLUTIONS:__

Dear USER, 

Thank you for test my first app using Python Code,
Remember this is a Student Project with the only purpose of learning about Python Code,
Feel Free to use it and enjoy as much as I have enjoyed during the coding process,
If you need  further information about this app, please feel free to contact me by email: gervafel@gmail.com

Thank you!

TitoGerva

pd: follow the next steps to install and execute the app,

## **Main Goal:*

This app returns the closest BiciMAD stations to the Place of Interest selected,
In this case, we only work with Museum and Cultural Centres,
If you select 'cercana' you should indicate which place are you looking info for and if you select 'todas', the app will return a main list,

## **To execute the APP remember to install the next libraries in your local:*

- [Python] (https://docs.python.org/3.7/)

- [Argparse] (https://docs.python.org/3/howto/argparse.html)

- [Pandas] (https://pandas.pydata.org/)

- [GeoPandas] (https://geopandas.org/en/stable/)

- [Numpy] (https://numpy.org/)

- [Re] (https://docs.python.org/es/3/library/re.html)

- [json] (https://docs.python.org/es/3.9/library/json.html)

- [Requests] (https://requests.readthedocs.io/)

- [Shapely] (https://pypi.org/project/Shapely/)

- [FuzzyWuzzy] (https://pypi.org/project/fuzzywuzzy/)

## **Next Steps*

1º Once you Install the Libraries, Copy the folder 'execute' where you are going to execute the app,

2º Access into the folder 'execute' through Windows Power Shell,

2º Execute in Windows Power Shell the next argument: 'python execute.py --tipo [value='cercana' or 'todas']',

3º In case of hesitation execute: 'python execute --help' and follow the instructions,

4º If you select option 'todas', app returns a list with all centers and the closest BiciMAD stations,

5º If you select option 'cercana', app returns the closest BiciMAD stations from the place you select,

6º The results are exported in the folder 'ddbb' in .csv,

7º Please use '|' to separate values in cells,

## **To developers*

The code is organized by 4 steps: acquisitions, wrangling, analyst & report. But remember: to use the app you only need to install the folder 'execute' and execute the file with the same name.

Enjoy!






 


 

