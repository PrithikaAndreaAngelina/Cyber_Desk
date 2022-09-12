import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import time

print(os.listdir("E:\Intrusion-Detection-System"))
with open("E:\Intrusion-Detection-System\dataset\kddcup.names",'r') as f:
    print(f.read())

cols="""duration,
protocol_type,
service,
flag,
src_bytes,
dst_bytes,
land,
wrong_fragment,
urgent,
hot,
num_failed_logins,
logged_in,
num_compromised,
root_shell,
su_attempted,
num_root,
num_file_creations,
num_shells,
num_access_files,
num_outbound_cmds,
is_host_login,
is_guest_login,
count,
srv_count,
serror_rate,
srv_serror_rate,
rerror_rate,
srv_rerror_rate,
same_srv_rate,
diff_srv_rate,
srv_diff_host_rate,
dst_host_count,
dst_host_srv_count,
dst_host_same_srv_rate,
dst_host_diff_srv_rate,
dst_host_same_src_port_rate,
dst_host_srv_diff_host_rate,
dst_host_serror_rate,
dst_host_srv_serror_rate,
dst_host_rerror_rate,
dst_host_srv_rerror_rate"""

columns=[]
for c in cols.split(','):
    if(c.strip()):
       columns.append(c.strip())

columns.append('target')
#print(columns)
print(len(columns))

with open("E:\Intrusion-Detection-System\dataset\\training_attack_types",'r') as f:
    print(f.read())

attacks_types = {
    'normal': 'normal',
'back': 'dos',
'buffer_overflow': 'u2r',
'ftp_write': 'r2l',
'guess_passwd': 'r2l',
'imap': 'r2l',
'ipsweep': 'probe',
'land': 'dos',
'loadmodule': 'u2r',
'multihop': 'r2l',
'neptune': 'dos',
'nmap': 'probe',
'perl': 'u2r',
'phf': 'r2l',
'pod': 'dos',
'portsweep': 'probe',
'rootkit': 'u2r',
'satan': 'probe',
'smurf': 'dos',
'spy': 'r2l',
'teardrop': 'dos',
'warezclient': 'r2l',
'warezmaster': 'r2l',
}

path = "E:\Intrusion-Detection-System\dataset\kddcup.data_10_percent.gz"
df = pd.read_csv(path,names=columns)

#Adding Attack Type column
df['Attack Type'] = df.target.apply(lambda r:attacks_types[r[:-1]])
df2 = df[['duration','src_bytes','dst_bytes','is_host_login','is_guest_login','diff_srv_rate','srv_diff_host_rate','dst_host_count','target','Attack Type']]
print(df2.iloc[423424])

path = "E:\Intrusion-Detection-System\dataset\kddcup.data_10_percent.gz"
df = pd.read_csv(path,names=columns)

#Adding Attack Type column
df['Attack Type'] = df.target.apply(lambda r:attacks_types[r[:-1]])
p1 = int(input("Enter duration : "))
p2 = int(input("Enter src_bytes : "))
p3 = int(input("Enter dst_bytes : "))
p4 = int(input("Enter is_host_login : "))
p5 = int(input("Enter is_guest_login : "))
p6 = float(input("Enter diff_srv_rate : "))
p7 = float(input("Enter srv_diff_host_rate : "))
p8 = int(input("Enter dst_host_count : "))
df2 = df[df['duration']==p1]
df3 = df2[df2['src_bytes']==p2]
df4 = df3[df3['dst_bytes']==p3]
df5 = df4[df4['is_host_login']==p4]
df6 = df5[df5['is_guest_login']==p5]
df7 = df6[df6['diff_srv_rate']==p6]
df8 = df7[df7['srv_diff_host_rate']==p7]
df9 = df8[df8['dst_host_count']==p8]
str1 = str(df9['target'][df9.index[0]])
str2 = str(df9['Attack Type'][df9.index[0]])
print("Target - " , str1,'\n',"Attacks Type - ",str2)

df.shape
df['target'].value_counts()
df['Attack Type'].value_counts()
df.dtypes\

df.isnull().sum()

#Finding categorical features
num_cols = df._get_numeric_data().columns

cate_cols = list(set(df.columns)-set(num_cols))
cate_cols.remove('target')
cate_cols.remove('Attack Type')

cate_cols

#Visualization
def bar_graph(feature):
    df[feature].value_counts().plot(kind="bar")

bar_graph('protocol_type')

plt.figure(figsize=(15,3))
bar_graph('service')
bar_graph('flag')
bar_graph('logged_in')
bar_graph('target')

bar_graph('Attack Type')

df.columns

df = df.dropna('columns')# drop columns with NaN

df = df[[col for col in df if df[col].nunique() > 1]]# keep columns where there are more than 1 unique values

corr = df.corr()

plt.figure(figsize=(15,12))

sns.heatmap(corr)

plt.show()

df['num_root'].corr(df['num_compromised'])
df['srv_serror_rate'].corr(df['serror_rate'])
df['srv_count'].corr(df['count'])
df['srv_rerror_rate'].corr(df['rerror_rate'])
df['dst_host_same_srv_rate'].corr(df['dst_host_srv_count'])
df['dst_host_srv_serror_rate'].corr(df['dst_host_serror_rate'])
df['dst_host_srv_rerror_rate'].corr(df['dst_host_rerror_rate'])
df['dst_host_same_srv_rate'].corr(df['same_srv_rate'])
df['dst_host_srv_count'].corr(df['same_srv_rate'])
df['dst_host_same_src_port_rate'].corr(df['srv_count'])
df['dst_host_serror_rate'].corr(df['serror_rate'])
df['dst_host_serror_rate'].corr(df['srv_serror_rate'])
df['dst_host_srv_serror_rate'].corr(df['serror_rate'])
df['dst_host_srv_serror_rate'].corr(df['srv_serror_rate'])
df['dst_host_rerror_rate'].corr(df['rerror_rate'])
df['dst_host_rerror_rate'].corr(df['srv_rerror_rate'])
df['dst_host_srv_rerror_rate'].corr(df['rerror_rate'])
df['dst_host_srv_rerror_rate'].corr(df['srv_rerror_rate'])
#This variable is highly correlated with num_compromised and should be ignored for analysis.
#(Correlation = 0.9938277978738366)
df.drop('num_root',axis = 1,inplace = True)

#This variable is highly correlated with serror_rate and should be ignored for analysis.
#(Correlation = 0.9983615072725952)
df.drop('srv_serror_rate',axis = 1,inplace = True)

#This variable is highly correlated with rerror_rate and should be ignored for analysis.
#(Correlation = 0.9947309539817937)
df.drop('srv_rerror_rate',axis = 1, inplace=True)

#This variable is highly correlated with srv_serror_rate and should be ignored for analysis.
#(Correlation = 0.9993041091850098)
df.drop('dst_host_srv_serror_rate',axis = 1, inplace=True)

#This variable is highly correlated with rerror_rate and should be ignored for analysis.
#(Correlation = 0.9869947924956001)
df.drop('dst_host_serror_rate',axis = 1, inplace=True)
#This variable is highly correlated with srv_rerror_rate and should be ignored for analysis.
#(Correlation = 0.9821663427308375)
df.drop('dst_host_rerror_rate',axis = 1, inplace=True)

#This variable is highly correlated with rerror_rate and should be ignored for analysis.
#(Correlation = 0.9851995540751249)
df.drop('dst_host_srv_rerror_rate',axis = 1, inplace=True)

#This variable is highly correlated with dst_host_srv_count and should be ignored for analysis.
#(Correlation = 0.9865705438845669)
df.drop('dst_host_same_srv_rate',axis = 1, inplace=True)
df.head()
df.shape()
df.columns()
df_std = df.std()
df_std = df_std.sort_values(ascending = True)
df_std

df['protocol_type'].value_counts()

#protocol_type feature mapping
pmap = {'icmp':0,'tcp':1,'udp':2}
df['protocol_type'] = df['protocol_type'].map(pmap)
df['flag'].value_counts()

#protocol_type feature mapping
fmap = {'SF':0,'S0':1,'REJ':2,'RSTR':3,'RSTO':4,'SH':5 ,'S1':6 ,'S2':7,'RSTOS0':8,'S3':9 ,'OTH':10}
df['flag'] = df['flag'].map(fmap)
#flag feature mapping
df.head()
df.drop('service',axis = 1,inplace= True)
df.shape
df.head()
df.shape
df.dtypes