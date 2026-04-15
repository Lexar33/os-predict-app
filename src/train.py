import pandas as pd
import os
import pickle
from sklearn.multiclass import OneVsRestClassifier
from sklearn.tree import DecisionTreeClassifier


def read_file_csv(filename):
    current_dir = os.path.dirname(__file__)

    df=pd.read_csv(os.path.join(current_dir,"..","data","processed", filename))
    X_train = df.drop(["clase"], axis=1)
    X_train.columns.values[0] = "ID"
    #X_train=X_train.drop(columns=["ID"])
    X_train=X_train.drop(["ID"],axis=1)
    y_train = df[["clase"]]

    ovr_model = OneVsRestClassifier(
        DecisionTreeClassifier(criterion="gini",random_state=100, max_depth=5,min_samples_leaf=4)
        )
    ovr_model.fit(X_train, y_train)
    print("Modelo entrenado")
    modelname = "best_model.pkl"
    pickle.dump(ovr_model, open(os.path.join(current_dir,"..","models", modelname), "wb"))
    print("Modelo exportado correctamente en la carpeta models")

# Entrenamiento completo
def main():
    read_file_csv("data_train.csv")
    print("Finalizó el entrenamiento del Modelo")

if __name__ == "__main__":
    main()
