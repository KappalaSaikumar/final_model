import json
import pickle
import sklearn
import numpy as np

__locations=None
__data_columns=None
__model=None

def get_location_names():
    global __locations
    load_saved_artifacts()
    return __locations

def get_estimated_price(loc,area_type,sqft,bhk,bath):
    load_saved_artifacts()
    try:
        loc_idx=__locations.index(loc)
    except:
        loc_idx=-1
    x=np.zeros(len(__data_columns))
    x[0]=area_type
    x[1]=bhk
    x[2]=sqft
    x[3]=bath
    if loc_idx>=0:
        x[loc_idx]=1
    return round(__model.predict([x])[0],2)

def load_saved_artifacts():
    print("loading artifacts")
    global __locations
    global __data_columns
    global __model

    with open('final_model/server/columns.json','r') as f:
        __data_columns=json.load(f)['data_columns']
        __locations=__data_columns[4:]

    with open('final_model/server/Lr_model.pickle','rb') as f1:
        __model=pickle.load(f1)
    print("loading artifacts done")

if __name__=='__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('location_1st phase jp nagar',2,1000,3,3))
