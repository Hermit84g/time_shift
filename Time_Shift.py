import pandas as pd
import numpy as np
import pandas.tseries.offsets as offsets

df=pd.read_excel('Location.xlsx',header=1)
spdate=df['時間'].str.split('(^[0-9]+\/[0-9]+\/[0-9]+\s[0-9]+\:[0-9]+\:[0-9]+)',expand=True)
spdate['fixdate']=pd.to_datetime(spdate[1])
spdate['UTC9']=0
spdate.loc[spdate[2]=='(UTC+9)','UTC9']=spdate['fixdate']+offsets.Hour(-9)
spdate.loc[spdate[2]==' AM','UTC9']=spdate['fixdate']
spdate.loc[spdate[2]==' PM','UTC9']=spdate['fixdate']+offsets.Hour(12)
df=pd.concat([df,spdate['UTC9']],axis=1)
df=df.set_index('UTC9')
df.index=pd.to_datetime(df.index,utc=True)
df.index=df.index.tz_convert('Asia/Tokyo')
df.to_csv('TS_Fix.csv')
