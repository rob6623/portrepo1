# -*- coding: utf-8 -*-




import os,sys,urlparse

from resources.lib.modules import control
from resources.lib.modules import trakt
from resources.lib.modules import cache
import xbmc
import xbmcaddon
import xbmcgui

sysaddon = sys.argv[0] ; syshandle = int(sys.argv[1]) ; control.moderator()

artPath = control.artPath() ; addonFanart = control.addonFanart()

imdbCredentials = False if control.setting('imdb.user') == '' else True

traktCredentials = trakt.getTraktCredentialsInfo()

traktIndicators = trakt.getTraktIndicatorsInfo()

queueMenu = control.lang(32065).encode('utf-8')

		
		
class navigator:
	def root(self):
		self.addDirectoryItem(32001, 'movieNavigator', 'movies.gif', 'Defaultmovies.gif')
		self.addDirectoryItem(32002, 'tvNavigator', 'tvshows.gif', 'Defaulttvshows.gif')




		if not control.setting('lists.widget') == '0':
			self.addDirectoryItem(32003, 'mymovieNavigator', 'movies.gif', 'DefaultVideoPlaylists.jpg')
			self.addDirectoryItem(32004, 'mytvNavigator', 'tvshows.gif', 'DefaultVideoPlaylists.jpg')

		self.addDirectoryItem(32008, 'toolNavigator', 'tools.gif', 'DefaultAddonProgram.jpg')

		downloads = True if control.setting('downloads') == 'true' and (len(control.listDir(control.setting('movie.download.path'))[0]) > 0 or len(control.listDir(control.setting('tv.download.path'))[0]) > 0) else False
		if downloads == True:
			self.addDirectoryItem(32009, 'downloadNavigator', 'dir.gif', 'DefaultFolder.jpg')

		self.endDirectory()


	def movies(self, lite=False):
		self.addDirectoryItem('Franchise', 'FranchiseNavigator', 'movies.gif', 'Defaultmovies.gif')
		self.addDirectoryItem('Scream Queens', 'screamq', 'queens.gif', 'Defaulttvshows.gif')
		self.addDirectoryItem('Top Fifty Horror Directors', 'namegenre', 'queens.gif', 'Defaultmovies.gif')
		self.addDirectoryItem('Anime', 'movies&url=anime', 'movies.gif', 'Defaultmovies.gif')
		self.addDirectoryItem(32011, 'movieGenres', 'genres.gif', 'Defaultmovies.gif')

		self.addDirectoryItem(32012, 'movieYears', 'movies.gif', 'Defaultmovies.gif')
		self.addDirectoryItem('Certificates', 'movieCertificates', 'movies.gif', 'Defaultmovies.gif')
		self.addDirectoryItem('Popular', 'movies&url=popular', 'movies.gif', 'Defaultmovies.gif')
		self.addDirectoryItem('Highest Voted', 'movies&url=views', 'movies.gif', 'Defaultmovies.gif')
		self.addDirectoryItem('Featured', 'movies&url=featured', 'movies.gif', 'Defaultmovies.gif')
		self.addDirectoryItem(32021, 'movies&url=oscars', 'movies.gif', 'Defaultmovies.gif')
		self.addDirectoryItem('boxoffice', 'movies&url=boxoffice', 'movies.gif', 'Defaultmovies.gif')
		self.addDirectoryItem(32022, 'movies&url=theaters', 'movies.gif', 'DefaultRecentlyAddedmovies.gif')

		
		if lite == False:
			if not control.setting('lists.widget') == '0':
				self.addDirectoryItem(32003, 'mymovieliteNavigator', 'movies.gif', 'DefaultVideoPlaylists.jpg')

			#self.addDirectoryItem('Actor Search', 'moviePerson', 'actorsearch.jpg', 'Defaultmovies.gif')
			#self.addDirectoryItem(32010, 'movieSearch', 'search.jpg', 'Defaultmovies.gif')

		self.endDirectory()


	def Franchise(self, lite=False):
		self.addDirectoryItem('A Nightmare on Elm Street Franchise', 'movies&url=ANightmareonElmStreet', 'nightmare-on-elm-street-ranked-slice-600x200.jpg', 'Defaultmovies.gif')
		self.addDirectoryItem('Halloween Franchise', 'movies&url=HalloweenFranchise', 'halloween.jpg', 'Defaultmovies.gif')
		self.addDirectoryItem('Friday the 13th Franchise', 'movies&url=FridaythethFranchise', 'f13th.jpg', 'Defaultmovies.gif')
		self.addDirectoryItem('Scream Franchise', 'movies&url=ScreamFranchise', 'ScreamFranchise.jpg', 'Defaultmovies.gif')
		self.addDirectoryItem('Saw Franchise', 'movies&url=SawFranchise', 'saw.jpg', 'Defaultmovies.gif')
		self.addDirectoryItem('Aliens and Predators Franchise', 'movies&url=AliensAndPredatorsFranchise', 'AliensAndPredatorsFranchise.png', 'Defaultmovies.gif')
		self.addDirectoryItem('Texas Chainsaw Massacre Franchise', 'movies&url=TexasChainsawMassacreFranchise', 'TexasChainsawMassacreFranchise.jpg', 'Defaultmovies.gif')
		self.addDirectoryItem('Evil Dead Franchise', 'movies&url=EvilDeadFranchise', 'evildead.jpg', 'Defaultmovies.gif')
		self.addDirectoryItem('Childs Play Franchise', 'movies&url=ChildsPlayFranchise', 'chucky.jpg', 'Defaultmovies.gif')
		self.addDirectoryItem('Romeros Dead Zombie Franchise', 'movies&url=RomerosDeadZombieFranchise', 'george.jpg', 'Defaultmovies.gif')
		self.addDirectoryItem('Final Destination Franchise', 'movies&url=FinalDestinationFranchise', 'Final_Destination.jpg', 'Defaultmovies.gif')
		self.addDirectoryItem('Jaws Franchise', 'movies&url=JawsFranchise', 'jaws-posters-all.jpg', 'Defaultmovies.gif')
		self.addDirectoryItem('Jeepers Creepers Franchise', 'movies&url=JeepersCreepersFranchise', 'jeepers-creepers.jpg', 'Defaultmovies.gif')
		self.addDirectoryItem('Hellraiser Franchise', 'movies&url=HellraiserFranchise', 'hellraiser.jpg', 'Defaultmovies.gif')
		self.addDirectoryItem('Insidious Franchise', 'movies&url=InsidiousFranchise', 'Insidious_05072014_1.jpg', 'Defaultmovies.gif')
		self.addDirectoryItem('The Exorcist Franchise', 'movies&url=TheExorcistFranchise', 'the-exorcist-one.jpg', 'Defaultmovies.gif')
		self.addDirectoryItem('The Hills Have Eyes Franchise', 'movies&url=TheHillsHaveEyesFranchise', 'the-hills-have-eyes-franchise-u2.jpg', 'Defaultmovies.gif')
		self.addDirectoryItem('The Ring Franchise', 'movies&url=TheRingFranchise', 'ring.jpg', 'Defaultmovies.gif')
		self.addDirectoryItem('Jurassic Park Franchise', 'movies&url=JurassicParkFranchise', 'park.jpg', 'Defaultmovies.gif')
		self.addDirectoryItem('Poltergeist Franchise', 'movies&url=PoltergeistFranchise', 'poltergeist-clown-poster-bg.jpg', 'Defaultmovies.gif')
		self.addDirectoryItem('Psycho Franchise', 'movies&url=PsychoFranchise', 'Psycho_logos.JPG', 'Defaultmovies.gif')
		self.addDirectoryItem('Candyman Franchise', 'movies&url=CandymanFranchise', 'Candyman.jpg', 'Defaultmovies.gif')
		self.addDirectoryItem('Resident Evil Franchise', 'movies&url=ResidentEvilFranchise', 'Resident-Evil-750x401.jpg', 'Defaultmovies.gif')
		self.addDirectoryItem('Amityville Franchise', 'movies&url=AmityvilleFranchise', 'amityville.jpg', 'Defaultmovies.gif')
		self.addDirectoryItem('I Know What You Did Last Summer Franchise', 'movies&url=IKnowWhatYouDidLastSummerFranchise', 'I_know_what_you_did_last_summer.jpg', 'Defaultmovies.gif')
		self.addDirectoryItem('The Purge Franchise', 'movies&url=ThePurgeFranchise', 'purge.jpg', 'Defaultmovies.gif')
		self.addDirectoryItem('Creepshow Franchise', 'movies&url=CreepshowFranchise', 'creepshow-7.jpg', 'Defaultmovies.gif')
		self.addDirectoryItem('Gremlins Franchise', 'movies&url=GremlinsFranchise', 'grimlins.jpg', 'Defaultmovies.gif')
		self.addDirectoryItem('The Omen Franchise', 'movies&url=TheOmenFranchise', 'the-omen.jpg', 'Defaultmovies.gif') 
		self.addDirectoryItem('Silent Hill Franchise', 'movies&url=SilentHillFranchise', 'Silent_Hill_film_logo.png', 'Defaultmovies.gif')
		self.addDirectoryItem('Wrong Turn Franchise', 'movies&url=WrongTurnFranchise', 'wrong-turn-5-bloodlines-review.jpg', 'Defaultmovies.gif')
		self.addDirectoryItem('Children of the Corn Franchise', 'movies&url=ChildrenoftheCornFranchise', 'children.jpg', 'Defaultmovies.gif')
		self.addDirectoryItem('Blade Franchise', 'movies&url=BladeFranchise', 'blade.png', 'Defaultmovies.gif')
		self.addDirectoryItem('The Mummy Franchise', 'movies&url=TheMummyFranchise', 'the-mummy-franchise-1024x983.jpg', 'Defaultmovies.gif')
		self.addDirectoryItem('From Dusk till Dawn Franchise', 'movies&url=FromDusktillDawnFranchise', 'fromdusk.jpg', 'Defaultmovies.gif')
		self.addDirectoryItem('Tremors Franchise', 'movies&url=TremorsFranchise', 'tremors-movie-poster.jpg', 'Defaultmovies.gif')
		self.addDirectoryItem('The Conjuring Franchise', 'movies&url=TheConjuringFranchise', 'conj.jpg', 'Defaultmovies.gif')
		self.addDirectoryItem('Cube Franchise', 'movies&url=CubeFranchise', 'cube.jpg', 'Defaultmovies.gif')
		self.addDirectoryItem('The Thing Franchise', 'movies&url=TheThingFranchise', 'thing.jpg', 'Defaultmovies.gif')
		self.addDirectoryItem('Paranormal Activity Franchise', 'movies&url=ParanormalActivityFranchise', 'marked-ones.jpg', 'Defaultmovies.gif')
		self.addDirectoryItem('Phantasm Franchise', 'movies&url=PhantasmFranchise', 'Phantasm_Simple.jpg', 'Defaultmovies.gif')
		self.addDirectoryItem('Scary Movie Franchise', 'movies&url=ScaryMovieFranchise', 'scary-movie-5-1.jpg', 'Defaultmovies.gif')
		self.addDirectoryItem('Return of the Living Dead Franchise', 'movies&url=ReturnoftheLivingDeadFranchise', 'return-of-the-living-dead-series.jpg', 'Defaultmovies.gif')
		self.addDirectoryItem('Carrie Franchise', 'movies&url=CarrieFranchise_link', 'crit.jpg', 'Defaultmovies.gif')
		self.addDirectoryItem('Sinister Franchise', 'movies&url=SinisterFranchise', 'sinister-2.jpg', 'Defaultmovies.gif')
		self.addDirectoryItem('Underworld Franchise', 'movies&url=UnderworldFranchise', 'under.jpg', 'Defaultmovies.gif')
		self.addDirectoryItem('Puppet Master Franchise', 'movies&url=PuppetMasterFranchise', 'puppetmaster.jpg', 'Defaultmovies.gif')
		self.addDirectoryItem('The Grudge Franchise', 'movies&url=TheGrudgeFranchise', 'The_Grudge_logo.jpg', 'Defaultmovies.gif')
		self.addDirectoryItem('Joy Ride Franchise', 'movies&url=JoyRideFranchise', 'joyride3.jpg', 'Defaultmovies.gif')
		self.addDirectoryItem('Goulies Franchise', 'movies&url=GouliesFranchise', 'GhouliesF.jpg', 'Defaultmovies.gif')
		self.addDirectoryItem('Critters Franchise', 'movies&url=CrittersFranchise', 'crit.jpg', 'Defaultmovies.gif')
		self.addDirectoryItem('Wishmaster Franchise', 'movies&url=WishmasterFranchise', 'wish.jpg', 'Defaultmovies.gif')
		self.addDirectoryItem('Pumpkin head Franchise', 'movies&url=PumpkinheadFranchise', 'pumpkinhead-in-church.jpg', 'Defaultmovies.gif')
		self.addDirectoryItem('Demonic toys Franchise', 'movies&url=DemonictoysFranchise', 'Demonic-Toys.jpg', 'Defaultmovies.gif')		
		self.addDirectoryItem('Gate Franchise', 'movies&url=GateFranchise', 'gate.jpg', 'Defaultmovies.gif')		
		self.addDirectoryItem('C H U D Franchise', 'movies&url=CHUDFranchise', 'CHUD.jpg', 'Defaultmovies.gif')		
		self.addDirectoryItem('House the movies Franchise', 'movies&url=HouseFranchise', 'house.jpg', 'Defaultmovies.gif')
		self.addDirectoryItem('Faces of death ', 'movies&url=Facesofdeath', 'fod.jpg', 'Defaultmovies.gif')
		self.addDirectoryItem('Hatchet', 'movies&url=Hatchet', 'Victor-Crowley-Hatchet-4-700x300.jpg', 'Defaultmovies.gif')
		self.addDirectoryItem('leprechaun', 'movies&url=leprechaun', 'leprechaun-original102611.jpg', 'Defaultmovies.gif')
		self.addDirectoryItem('Alone in the Dark‎', 'movies&url=Alone', 'alone.jpg', 'Defaultmovies.gif')
		self.addDirectoryItem('Anaconda', 'movies&url=Anaconda', 'anaconda.jpg', 'Defaultmovies.gif')
		self.addDirectoryItem('Blair Witch', 'movies&url=BlairWitch', 'blair.jpg', 'Defaultmovies.gif')
		self.endDirectory()	


	def mymovies(self, lite=False):
		self.accountCheck()

		if traktCredentials == True and imdbCredentials == True:
			self.addDirectoryItem(32032, 'movies&url=traktcollection', 'acc.gif', 'Defaultmovies.gif', queue=True, context=(32551, 'moviesToLibrary&url=traktcollection'))
			self.addDirectoryItem(32033, 'movies&url=traktwatchlist', 'acc.gif', 'Defaultmovies.gif', queue=True, context=(32551, 'moviesToLibrary&url=traktwatchlist'))
			self.addDirectoryItem(32034, 'movies&url=imdbwatchlist', 'acc.gif', 'Defaultmovies.gif', queue=True)

		elif traktCredentials == True:
			self.addDirectoryItem(32032, 'movies&url=traktcollection', 'acc.gif', 'Defaultmovies.gif', queue=True, context=(32551, 'moviesToLibrary&url=traktcollection'))
			self.addDirectoryItem(32033, 'movies&url=traktwatchlist', 'acc.gif', 'Defaultmovies.gif', queue=True, context=(32551, 'moviesToLibrary&url=traktwatchlist'))

		elif imdbCredentials == True:
			self.addDirectoryItem(32032, 'movies&url=imdbwatchlist', 'acc.gif', 'Defaultmovies.gif', queue=True)
			self.addDirectoryItem(32033, 'movies&url=imdbwatchlist2', 'acc.gif', 'Defaultmovies.gif', queue=True)

		if traktCredentials == True:
			self.addDirectoryItem(32035, 'movies&url=traktfeatured', 'acc.gif', 'Defaultmovies.gif', queue=True)

		elif imdbCredentials == True:
			self.addDirectoryItem(32035, 'movies&url=featured', 'acc.gif', 'Defaultmovies.gif', queue=True)

		if traktIndicators == True:
			self.addDirectoryItem(32036, 'movies&url=trakthistory', 'acc.gif', 'Defaultmovies.gif', queue=True)

		self.addDirectoryItem(32039, 'movieUserlists', 'movies.gif', 'Defaultmovies.gif')

		if lite == False:
			self.addDirectoryItem(32031, 'movieliteNavigator', 'movies.gif', 'Defaultmovies.gif')
			self.addDirectoryItem('Actor Search', 'moviePerson', 'actorsearch.jpg', 'Defaultmovies.gif')
			self.addDirectoryItem(32010, 'movieSearch', 'search.jpg', 'Defaultmovies.gif')

		self.endDirectory()


	def tvshows(self, lite=False):
		self.addDirectoryItem('Anime', 'tvshows&url=anime', 'tvshows.gif', 'Defaultmovies.gif')
		self.addDirectoryItem(32012, 'tvYears', 'tvshows.gif', 'Defaultmovies.gif')
		self.addDirectoryItem(32011, 'tvGenres', 'genres.gif', 'Defaulttvshows.gif')


		self.addDirectoryItem('Certificates', 'tvCertificates', 'tvshows.gif', 'playlist.jpg')
		self.addDirectoryItem(32026, 'tvshows&url=premiere', 'tvshows.gif', 'Defaulttvshows.gif')
		self.addDirectoryItem('Popular', 'tvshows&url=popular', 'tvshows.gif', 'playlist.jpg')

		if lite == False:
			if not control.setting('lists.widget') == '0':
				self.addDirectoryItem(32004, 'mytvliteNavigator', 'tvshows.gif', 'DefaultVideoPlaylists.jpg')




		self.endDirectory()


	def mytvshows(self, lite=False):
		self.accountCheck()

		if traktCredentials == True and imdbCredentials == True:
			self.addDirectoryItem(32032, 'tvshows&url=traktcollection', 'acc.gif', 'Defaulttvshows.gif', context=(32551, 'tvshowsToLibrary&url=traktcollection'))
			self.addDirectoryItem(32033, 'tvshows&url=traktwatchlist', 'acc.gif', 'Defaulttvshows.gif', context=(32551, 'tvshowsToLibrary&url=traktwatchlist'))
			self.addDirectoryItem(32034, 'tvshows&url=imdbwatchlist', 'acc.gif', 'Defaulttvshows.gif')

		elif traktCredentials == True:
			self.addDirectoryItem(32032, 'tvshows&url=traktcollection', 'acc.gif', 'Defaulttvshows.gif', context=(32551, 'tvshowsToLibrary&url=traktcollection'))
			self.addDirectoryItem(32033, 'tvshows&url=traktwatchlist', 'acc.gif', 'Defaulttvshows.gif', context=(32551, 'tvshowsToLibrary&url=traktwatchlist'))

		elif imdbCredentials == True:
			self.addDirectoryItem(32032, 'tvshows&url=imdbwatchlist', 'acc.gif', 'Defaulttvshows.gif')
			self.addDirectoryItem(32033, 'tvshows&url=imdbwatchlist2', 'acc.gif', 'Defaulttvshows.gif')

		if traktCredentials == True:
			self.addDirectoryItem(32035, 'tvshows&url=traktfeatured', 'acc.gif', 'Defaulttvshows.gif')

		elif imdbCredentials == True:
			self.addDirectoryItem(32035, 'tvshows&url=trending', 'acc.gif', 'Defaultmovies.gif', queue=True)

		if traktIndicators == True:
			self.addDirectoryItem(32036, 'calendar&url=trakthistory', 'acc.gif', 'Defaulttvshows.gif', queue=True)
			self.addDirectoryItem(32037, 'calendar&url=progress', 'acc.gif', 'DefaultRecentlyAddedEpisodes.jpg', queue=True)
			self.addDirectoryItem(32038, 'calendar&url=mycalendar', 'acc.gif', 'DefaultRecentlyAddedEpisodes.jpg', queue=True)

		self.addDirectoryItem(32040, 'tvUserlists', 'mytvshows.gif', 'Defaulttvshows.gif')

		if traktCredentials == True:
			self.addDirectoryItem(32041, 'episodeUserlists', 'mytvshows.gif', 'Defaulttvshows.gif')

		if lite == False:
			self.addDirectoryItem(32031, 'tvliteNavigator', 'tvshows.gif', 'Defaulttvshows.gif')
			self.addDirectoryItem('Actor Search', 'tvPerson', 'actorsearch.jpg', 'Defaulttvshows.gif')
			self.addDirectoryItem(32010, 'tvSearch', 'search.jpg', 'Defaulttvshows.gif')

		self.endDirectory()

		

	def tools(self):
		self.addDirectoryItem(32043, 'openSettings&query=0.0', 'tools.gif', 'DefaultAddonProgram.jpg')
		self.addDirectoryItem(32044, 'openSettings&query=3.1', 'tools.gif', 'DefaultAddonProgram.jpg')
		self.addDirectoryItem(32045, 'openSettings&query=1.0', 'tools.gif', 'DefaultAddonProgram.jpg')
		self.addDirectoryItem(32046, 'openSettings&query=6.0', 'tools.gif', 'DefaultAddonProgram.jpg')
		self.addDirectoryItem(32047, 'openSettings&query=2.0', 'tools.gif', 'DefaultAddonProgram.jpg')
		self.addDirectoryItem(32556, 'libraryNavigator', 'tools.gif', 'DefaultAddonProgram.jpg')
		self.addDirectoryItem(32048, 'openSettings&query=5.0', 'tools.gif', 'DefaultAddonProgram.jpg')
		self.addDirectoryItem(32049, 'viewsNavigator', 'tools.gif', 'DefaultAddonProgram.jpg')
		self.addDirectoryItem(32050, 'clearSources', 'tools.gif', 'DefaultAddonProgram.jpg')
		self.addDirectoryItem(32052, 'clearCache', 'tools.gif', 'DefaultAddonProgram.jpg')

		self.endDirectory()

	def library(self):
		self.addDirectoryItem(32557, 'openSettings&query=4.0', 'tools.gif', 'DefaultAddonProgram.jpg')
		self.addDirectoryItem(32558, 'updateLibrary&query=tool', 'library_update.jpg', 'DefaultAddonProgram.jpg')
		self.addDirectoryItem(32559, control.setting('library.movie'), 'movies.gif', 'Defaultmovies.gif', isAction=False)
		self.addDirectoryItem(32560, control.setting('library.tv'), 'tvshows.gif', 'Defaulttvshows.gif', isAction=False)

		if trakt.getTraktCredentialsInfo():
			self.addDirectoryItem(32561, 'moviesToLibrary&url=traktcollection', 'acc.gif', 'Defaultmovies.gif')
			self.addDirectoryItem(32562, 'moviesToLibrary&url=traktwatchlist', 'acc.gif', 'Defaultmovies.gif')
			self.addDirectoryItem(32563, 'tvshowsToLibrary&url=traktcollection', 'acc.gif', 'Defaulttvshows.gif')
			self.addDirectoryItem(32564, 'tvshowsToLibrary&url=traktwatchlist', 'acc.gif', 'Defaulttvshows.gif')

		self.endDirectory()

	def downloads(self):
		movie_downloads = control.setting('movie.download.path')
		tv_downloads = control.setting('tv.download.path')

		if len(control.listDir(movie_downloads)[0]) > 0:
			self.addDirectoryItem(32001, movie_downloads, 'movies.gif', 'Defaultmovies.gif', isAction=False)
		if len(control.listDir(tv_downloads)[0]) > 0:
			self.addDirectoryItem(32002, tv_downloads, 'tvshows.gif', 'Defaulttvshows.gif', isAction=False)

		self.endDirectory()


	def search(self):
		self.addDirectoryItem(32001, 'movieSearch', 'movies.gif', 'Defaultmovies.gif')
		self.addDirectoryItem(32002, 'tvSearch', 'tvshows.gif', 'Defaulttvshows.gif')
		self.addDirectoryItem('Actor Search', 'moviePerson', 'movies.gif', 'Defaultmovies.gif')
		self.addDirectoryItem('TV Actor Search', 'tvPerson', 'tvshows.gif', 'Defaulttvshows.gif')

		self.endDirectory()


	def views(self):
		try:
			control.idle()

			items = [ (control.lang(32001).encode('utf-8'), 'movies'), (control.lang(32002).encode('utf-8'), 'tvshows'), (control.lang(32054).encode('utf-8'), 'seasons'), (control.lang(32038).encode('utf-8'), 'episodes') ]

			select = control.selectDialog([i[0] for i in items], control.lang(32049).encode('utf-8'))

			if select == -1: return

			content = items[select][1]

			title = control.lang(32059).encode('utf-8')
			url = '%s?action=addView&content=%s' % (sys.argv[0], content)

			poster, banner, fanart = control.addonPoster(), control.addonBanner(), control.addonFanart()

			item = control.item(label=title)
			item.setInfo(type='Video', infoLabels = {'title': title})
			item.setArt({'icon': poster, 'thumb': poster, 'poster': poster, 'banner': banner})
			item.setProperty('Fanart_Image', fanart)

			control.addItem(handle=int(sys.argv[1]), url=url, listitem=item, isFolder=False)
			control.content(int(sys.argv[1]), content)
			control.directory(int(sys.argv[1]), cacheToDisc=True)

			from resources.lib.modules import views
			views.setView(content, {})
		except:
			return


	def accountCheck(self):
		if traktCredentials == False and imdbCredentials == False:
			control.idle()
			control.infoDialog(control.lang(32042).encode('utf-8'), sound=True, icon='WARNING')
			sys.exit()




	def clearCache(self):
		control.idle()
		yes = control.yesnoDialog(control.lang(32056).encode('utf-8'), '', '')
		if not yes: return
		from resources.lib.modules import cache
		cache.cache_clear()
		control.infoDialog(control.lang(32057).encode('utf-8'), sound=True, icon='INFO')


	def addDirectoryItem(self, name, query, thumb, icon, context=None, queue=False, isAction=True, isFolder=True):
		try: name = control.lang(name).encode('utf-8')
		except: pass
		url = '%s?action=%s' % (sysaddon, query) if isAction == True else query
		thumb = os.path.join(artPath, thumb) if not artPath == None else icon
		cm = []
		if queue == True: cm.append((queueMenu, 'RunPlugin(%s?action=queueItem)' % sysaddon))
		if not context == None: cm.append((control.lang(context[0]).encode('utf-8'), 'RunPlugin(%s?action=%s)' % (sysaddon, context[1])))
		item = control.item(label=name)
		item.addContextMenuItems(cm)
		item.setArt({'icon': thumb, 'thumb': thumb})
		if not addonFanart == None: item.setProperty('Fanart_Image', addonFanart)
		control.addItem(handle=syshandle, url=url, listitem=item, isFolder=isFolder)


	def endDirectory(self):
		control.content(syshandle, 'addons')
		control.directory(syshandle, cacheToDisc=True)


