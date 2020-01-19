import os.path
from os import path
from bs4 import BeautifulSoup
import urllib.request
import pandas as pd



def main():
    l = os.getcwd()
    df = pd.read_csv(l+'/exported_links.csv',dtype ={'Names' : str, 'Links': str})
    links = df['Links'].tolist()
    final_names = df['Names'].tolist()


    p = os.getcwd()+"/images"
    os.mkdir(p)
    

    for i,j in zip(links,final_names):
        print("Downloading " + j)
        j = p +"/"+j+".png"
        urllib.request.urlretrieve(i, j)

if __name__ == "__main__":
    main()
