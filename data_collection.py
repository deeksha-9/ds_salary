import glassdoor_scaper as gs 
import pandas as pd 
 
path="C:/chromedriver_win32/chromedriver.exe"
df=gs.get_jobs('data scientist',1000,False,path,15)
df.to_csv('glassdoor.csv',index=False)
