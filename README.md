# Predicción del Sistema Operativo de un Usuario a Partir de su Comportamiento Digital
==============================

El modelo OVR predice qué sistema operativo usa el usuario acorde al comportamiento de usuarios en una plataforma digital, donde cada fila representa una sesión de navegación

Project Organization
------------

    ├── LICENSE
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering)
    │
    ├── requirements.txt   <- The requirronment, e.g.
    │                         generated with `pip freeze > requirements.txt`ements file for reproducing the analysis envi
    │
    ├── screenshots        <- save screenshots of executions of the model in swagger 
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── make_dataset.py<- Script to prepare data
    │   │
    │   ├── train.py       <- Script to train models
    │   │                    
    │   ├── evaluate.py    <- Script to evaluate models using kpi's
    │   │
    │   └── predict.py     <- Script to use trained models to make predictions
    │
    └── LICENSE            <- License

--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>

--------
Paso de ejecución

* pip install -r requirement.txt
* python make_dataset.py
* python train.py
* uvicorn main:app --reload