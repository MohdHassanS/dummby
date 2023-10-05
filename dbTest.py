import pandas as pd
import streamlit as st
import plotly.express as px
df = pd.read_csv('agg_trans.csv')
s =  {'andaman-&-nicobar-islands' : 'Andaman & Nicobar',
      'andhra-pradesh' :'Andhra Pradesh',
      'arunachal-pradesh' : 'Arunachal Pradesh',
      'assam' : 'Assam',
      'bihar' : 'Bihar',
      'chandigarh': 'Chandigarh',
      'chhattisgarh':'Chhattisgarh',
      'dadra-&-nagar-haveli-&-daman-&-diu' : 'Dadra and Nagar Haveli and Daman and Diu',
      'delhi' : 'Delhi',
      'goa' :'Goa',
      'gujarat' :'Gujarat',
      'haryana': 'Haryana',
      'himachal-pradesh': 'Himachal Pradesh',
      'jammu-&-kashmir': 'Jammu & Kashmir',
      'jharkhand' :'Jharkhand',
      'karnataka': 'Karnataka',
      'kerala' :'Kerala',
      'ladakh' :'Ladakh',
      'lakshadweep': 'Lakshadweep',
      'madhya-pradesh': 'Madhya Pradesh',
      'maharashtra': 'Maharashtra',
      'manipur': 'Manipur',
      'meghalaya': 'Meghalaya',
      'mizoram': 'Mizoram',
      'nagaland': 'Nagaland',
      'odisha': 'Odisha',
      'puducherry': 'Puducherry',
      'punjab': 'Punjab',
      'rajasthan': 'Rajasthan',
      'sikkim': 'Sikkim',
      'tamil-nadu': 'Tamil Nadu',
      'telangana': 'Telangana',
      'tripura': 'Tripura',
      'uttar-pradesh': 'Uttarakhand',
      'uttarakhand': 'Uttar Pradesh',
      'west-bengal': 'West Bengal'}
df["State"] = df["State"].map(s)
gk = df.groupby('State')['Transacion_amount'].sum()
st.dataframe(gk)
fig = px.bar(gk, x=gk.index, y='Transacion_amount')
st.plotly_chart(fig, use_container_width=True)

fig1 = px.choropleth(
    gk,
    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
    featureidkey='properties.ST_NM',
    locations=gk.index,
    color='Transacion_amount',
    color_continuous_scale='Reds'
)

fig1.update_geos(fitbounds="locations", visible=False)
st.plotly_chart(fig1, use_container_width=True)
