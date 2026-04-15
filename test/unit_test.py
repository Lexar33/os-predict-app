import pandas as pd
import os 
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.make_dataset import data_preparation

#Realiza el test del proceso
def test_make_dataset():
    current_dir = os.path.dirname(__file__)
    filename="usuarios_win_mac_lin_exp_cmp.csv"
    df1=pd.read_csv(os.path.join(current_dir,"..","data","raw", filename),encoding='latin1', sep = ';')
    print("Tests de Carga")
    assert df1.shape == (1230, 11), "El archivo está vacío"

test_make_dataset()