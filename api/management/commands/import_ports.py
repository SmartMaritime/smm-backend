import json
from django.core.management.base import BaseCommand
from api.models import Port  # adapte selon ton app


class Command(BaseCommand):
    help = 'Description courte de la commande'

    def add_arguments(self, parser):
        parser.add_argument('filename', type=str, help='chemin du fichier')
        # Ici tu ajoutes les arguments en ligne de commande
        # Ex: parser.add_argument('filename', type=str, help='Chemin du fichier')
       

    def handle(self, *args, **options):
        
        json_file = options.get('filename')
        
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        
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
        with open('c:/smartmaritime/SMM_BACKEND/ports_cln.json', 'w') as f:
            cnt=json.dump(ports_clean,f, indent= 2)
       
        
        Port.objects.all().delete()
        for port in ports_clean:
            prt,created = Port.objects.update_or_create(
                code = port['locode'],
                defaults={  
                    'name': port['name'],
                    'latitude': port['latitude'],
                    'longitude': port['longitude']
                }
            )
 
        self.stdout.write('Hello world !')
