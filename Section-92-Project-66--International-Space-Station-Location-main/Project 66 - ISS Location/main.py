import requests, folium, webbrowser


response = requests.get('http://api.open-notify.org/iss-now.json')
data = response.json()

latitude = data['iss_position']['latitude']
longitude = data['iss_position']['longitude']
custom_map = folium.Map(location=[latitude,longitude],zoom_start=5)
custom_map.add_child(folium.Marker(location=[latitude,longitude],icon=folium.Icon(color='red')))
custom_map.save('iss.html')

# url = 'file:///Users/elshad/Desktop/Python For Everyone/Projects/Project 66 - ISS Location/iss.html'
url = 'file://YOUR_PATH/iss.html'
webbrowser.open(url)