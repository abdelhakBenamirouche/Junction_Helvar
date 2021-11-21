import pandas as pd
import numpy as np
import base64
import imageio as iio
from plotting import Plotting
import plotly.graph_objects as go
from numpy.linalg import norm

site = 'site_2'
df_events = pd.read_pickle('C:/Users/GCBµ/Desktop/site2/site_2.pkl', compression='gzip')
df_events.loc[:, 'timestamp'] = (pd.to_datetime(df_events['timestamp'], utc=True)
                                 .dt.tz_convert('Europe/Helsinki')
                                 .dt.tz_localize(None))

print(df_events.shape)

df_devices = pd.read_json('C:/Users/GCBµ/Desktop/site2/site_2.json')
n,m = df_devices.shape

distance  = []
a = df_devices['x']
b = df_devices['y']

for i in range (0, n) :
	for j in range (i,n) :
		x = np.array(a[i],b[i])
		y = np.array(a[j],b[j])
		d = np.linalg.norm(x-y)
		distance.append([i,j,d])


dist = pd.DataFrame(distance, columns = ['sensors1','sensors2','distance'])


print(dist.loc[ dist['distance'] < 10])
with open('C:/Users/GCBµ/Desktop/site2/site_2.png', "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode()
img = iio.imread('C:/Users/GCBµ/Desktop/site2/site_2.png')
print(img.shape)