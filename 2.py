import glassdoor_scaper as gs 
import pandas as pd 
 
path="C:/chromedriver_win32/chromedriver.exe"
df=gs.get_jobs('data scientist',15,False,path,15)
