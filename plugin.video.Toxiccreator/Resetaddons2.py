import time
import os
import xbmc
import xbmcgui
import xbmcaddon

databasePath = xbmc.translatePath('special://profile/addon_data/script.GCguide')
d = xbmcgui.Dialog()

for root, dirs, files in os.walk(databasePath,topdown=True):
	dirs[:] = [d for d in dirs]
	for name in files:
		if "addons2.ini" in name:
			try:
				os.remove(os.path.join(root,name))
			except: 
				d = xbmcgui.Dialog()
				d.ok('Toxic Creator', 'Error Removing ' + str(name),'','[COLOR yellow]Thank you for using Toxic Creator[/COLOR]')
				pass
		else:
			continue
			

d = xbmcgui.Dialog()			
d.ok('Toxic Creator', 'Please restart Ivueguide for ','the changes to take effect','[COLOR yellow]Thank you for using Toxic Creator[/COLOR]')
