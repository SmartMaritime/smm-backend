import json

# Charger le fichier GeoJSON
with open('attributed_ports.geojson', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Créer un nouveau dictionnaire avec les données filtrées
ports_clean = []

for feature in data['features']:
    props = feature['properties']
    coords = feature['geometry']['coordinates']
    
    port_data = {
        "name": props.get("Name", "").strip(),
        "locode": props.get("LOCODE", "").strip(),
        "longitude": coords[0],
        "latitude": coords[1]
    }

    ports_clean.append(port_data)

# Exemple d'affichage
for port in ports_clean[:5]:  # afficher les 5 premiers ports
    print(port)


from .api.models import Port

for port in ports_clean: 
    p,created = Port.objects.update_or_create(
        code = port['locode'],
        defaults = {
            'name': port['name'],
            'latitude': port['latitude'],
            'longitude': port['longitude']
        }
    
           
)