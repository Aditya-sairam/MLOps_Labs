import seaborn as sns
import pandas as pd 
import sklearn.model_selection as test_train_split

def load_data(): 
    penguins = sns.load_dataset('penguins')
    return penguins 


def clean_data(df):
    print("Data size before cleaning:", df.shape)
    df.dropna(inplace=True)
    print("Data size after cleaning:", df.shape)
    return df

def feature_engineering(df):
    columns_to_keep = ['species', 'sex', 'bill_length_mm', 'bill_depth_mm', 'flipper_length_mm','body_mass_g']
    df = df[columns_to_keep]
    df['sex'] = df['sex'].map({'Male':0,'Female':1})
    return df


def split_data(df):
    X = df.drop('species', axis=1)  # All columns except species
    y = df['species']                # Only species
    X_train,X_test,y_trian,y_test = test_train_split.train_test_split(X,y,test_size=0.2,random_state=42) 
    return X_train,X_test,y_trian,y_test

if __name__ == "__main__":
    df = load_data()
    clean_data(df)
    print(df.head())