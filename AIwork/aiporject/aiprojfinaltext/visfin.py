#1. Setup: Importing required modules
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as pl

#2. Preprocessing the data
def processed_data(df,l):
    df_vis=df.copy()
    #processing
    df_vis=df_vis.drop(l, axis=1)
    return df_vis
#3. the functions
def heatmap(pre_df): #input=preprocessed data, output=fig
    fig, ax = pl.subplots()
    fig = sb.heatmap(pre_df.corr(numeric_only=True), cmap='coolwarm', annot=True, ax=ax)
    ax.set_title("Heatmap")
    pl.show()

def scatterplot(pre_df):
    fig, ax = pl.subplots()
    fig = sb.scatterplot(x=pre_df['Area'], y=pre_df['Price'], hue=pre_df['Bathroom'], ax=ax)
    ax.set_title("Scatterplot")
    pl.show()

def lmplot(pre_df):
    fig = sb.lmplot(x='Area', y='Price', hue='Bathroom', data=pre_df)
    pl.show()

def hist(pre_df):
    pl.hist(pre_df['Bathroom'].dropna(), bins=6)
    pl.show()

def invalid(pre_df):
    print("❌ Invalid choice")

#MENU

def vis(pre_df):
    actions={
    #'0' : QUIT,
    '1' : heatmap,
    '2' : scatterplot,
    '3' : lmplot,
    '4' : hist,
    }
    while True:
        print('\n','DATA VISUALISATION')
        print('1 - Heatmap showing correlation between different features')
        print('2 - Scatterplot')
        print('3: lmplot')
        print('4: histogram')
        print('0 - quit submenu')
        choice = input('choose an option:')
        if choice == '0':
            print("Quiting \'Data Visualization\' menu")
            break
        actions.get(choice, invalid)(pre_df)
#main
#data=pd.read_csv('dataproject.csv')
#vis(processed_data(data, ['Locality']))
#to add: titles, and better text
#Without joblib, every time you run your program, you’d have to train the model again, which is slow and annoying.