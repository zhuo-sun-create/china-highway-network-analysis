import pandas as pd
import folium

# 1. Read highway data
df = pd.read_csv("china_highways.csv")

# 2. Create base map
m = folium.Map(
    location=[35.8, 104.2],
    zoom_start=4
)

# 3. City coordinates
city_coords = {
    "Beijing": [39.9042, 116.4074],
    "Harbin": [45.8038, 126.5349],
    "Shanghai": [31.2304, 121.4737],
    "Taipei": [25.0330, 121.5654],
    "Hong Kong-Macao": [22.3193, 114.1694],
    "Kunming": [25.0389, 102.7183],
    "Lhasa": [29.6520, 91.1721],
    "Urumqi": [43.8256, 87.6168],
    "Hegang": [47.3501, 130.2979],
    "Dalian": [38.9140, 121.6147],
    "Shenyang": [41.8057, 123.4315],
    "Haikou": [20.0440, 110.1999],
    "Changchun": [43.8171, 125.3235],
    "Shenzhen": [22.5431, 114.0579],
    "Jinan": [36.6512, 117.1201],
    "Guangzhou": [23.1291, 113.2644],
    "Daqing": [46.5893, 125.1038],

    "Suifenhe": [44.3969, 131.1640],
    "Manzhouli": [49.5978, 117.3785],
    "Hunchun": [42.8625, 130.3660],
    "Ulanhot": [46.0727, 122.0930],
    "Dandong": [40.1243, 124.3947],
    "Xilinhot": [43.9440, 116.0861],
    "Rongcheng": [37.1652, 122.4867],
    "Wuhai": [39.6550, 106.7942],
    "Qingdao": [36.0671, 120.3826],
    "Yinchuan": [38.4872, 106.2309],
    "Lanzhou": [36.0611, 103.8343],
    "Lianyungang": [34.5967, 119.2216],
    "Khorgos": [44.2140, 80.4130],
    "Nanjing": [32.0603, 118.7969],
    "Luoyang": [34.6197, 112.4540]
}

# 4. Create separate layers
capital_layer = folium.FeatureGroup(name="Capital Radial")
north_south_layer = folium.FeatureGroup(name="North-South")
east_west_layer = folium.FeatureGroup(name="East-West")

# 5. Draw highways
for _, row in df.iterrows():

    start_city = row["start_city"]
    end_city = row["end_city"]

    if start_city not in city_coords or end_city not in city_coords:
        continue

    start = city_coords[start_city]
    end = city_coords[end_city]

    popup_text = (
        f"<b>{row['highway_code']} "
        f"{row['highway_name']}</b><br>"
        f"Type: {row['network_type']}<br>"
        f"Start: {start_city}<br>"
        f"End: {end_city}"
    )

    if row["network_type"] == "Capital Radial":
        target_layer = capital_layer

    elif row["network_type"] == "North-South":
        target_layer = north_south_layer

    else:
        target_layer = east_west_layer

    folium.PolyLine(
        locations=[start, end],
        weight=4,
        opacity=0.8,
        popup=popup_text
    ).add_to(target_layer)

# 6. Add layers to map
capital_layer.add_to(m)
north_south_layer.add_to(m)
east_west_layer.add_to(m)

# 7. Add layer control
folium.LayerControl(
    collapsed=False
).add_to(m)

# 8. Save map
m.save("china_highway_layer_map.html")

print("Layer map created successfully!")
print("Saved as: china_highway_layer_map.html")