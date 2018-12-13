import csv
import pandas as pd
import sys
df = pd.read_csv('./master.csv')

filetail='.csv'
for key in df.keys()[1:]:
    simp=df[['street',key]]
    s=simp.dropna()
    s=s[['street']]
    s.street=s.street.str.replace(" \(\w\)$","", regex=True)
    s['city']='Portsmouth'
    s['state']='VA'
    name=str(key)
    name=name.replace("/", " ")
    s.to_csv(name+filetail, sep=',', encoding='utf-8', index=False)