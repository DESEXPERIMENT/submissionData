import json


fx = open('TelAviv.geojson','r')

content = fx.read()
content = json.loads(content)
fx.close()

nhc = 0
for nh in content['features']:
    print(nhc)
    content['features'].remove(nh)
    if nhc >5:
        break
    nhc += 1


fx = open('edited.geojson','w')

fx.write(json.dumps(content))

fx.close()
