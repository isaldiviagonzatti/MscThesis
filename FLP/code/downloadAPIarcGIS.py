# -*- coding: utf-8 -*-
"""
@author: isaldiviagonzatti
"""

import arcgis
from arcgis.gis import GIS

gis = GIS("https://wur-girs.maps.arcgis.com",'wur-girs\\email address', 'key', verify_cert=False)

save_to= r'\output'

# Download all data from a user
def downloadUserItems(owner, downloadFormat):
    try:
        # Search items by username
        items = gis.content.search('owner:{0}'.format(owner))
        print(items)
        # Loop through each item and if equal to Feature service then download it
        for item in items:
            if item.type == 'Feature Service':
                result = item.export('sample {}'.format(item.title), downloadFormat)
                result.download(save_to)
                print("Exported"+ item.title)
                # Delete the item after it downloads to save on space
    except Exception as e:
        print(e)


# Function takes in two parameters. Username and the type of download format
downloadUserItems('USERNAME', downloadFormat='File Geodatabase')


roadsCR=gis.content.get("07245640fce14f519c21150c7a3f5ce5")
roadsCR.export(save_to, 'File Geodatabase', parameters=None, wait=True)
result.download(save_to)


