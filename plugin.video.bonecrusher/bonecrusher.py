# -*- coding: utf-8 -*-
import urlparse,sys
import xbmc,os,zipfile,ntpath,xbmcgui,xbmcaddon,xbmcplugin
import time
from resources.lib.sources  import sources
dialog = xbmcgui.Dialog()
params = dict(urlparse.parse_qsl(sys.argv[2].replace('?','')))

action = params.get('action')

name = params.get('name')

title = params.get('title')

year = params.get('year')

imdb = params.get('imdb')

tvdb = params.get('tvdb')

tmdb = params.get('tmdb')

season = params.get('season')

episode = params.get('episode')

tvshowtitle = params.get('tvshowtitle')

premiered = params.get('premiered')

url = params.get('url')

image = params.get('image')

meta = params.get('meta')

select = params.get('select')

query = params.get('query')

source = params.get('source')

content = params.get('content')


if action == None:
    from resources.lib.indexers import navigator
    navigator.navigator().root()

if action == 'docs2navNavigator':
    from resources.lib.indexers import docs2nav
    docs2nav.navigator().root()

if action == 'bioNavigator':
    from resources.lib.indexers import docs2nav
    docs2nav.navigator().bio()

if action == 'natutredocsNavigator':
    from resources.lib.indexers import docs2nav
    docs2nav.navigator().natutredocs()
	
if action == 'thebibleNavigator':
    from resources.lib.indexers import docs2nav
    docs2nav.navigator().bible()

if action == 'ConspiraciesNavigator':
    from resources.lib.indexers import docs2nav
    docs2nav.navigator().Conspiracies()
	
if action == 'mentalNavigator':
    from resources.lib.indexers import docs2nav
    docs2nav.navigator().mental()

if action == 'killersNavigator':
    from resources.lib.indexers import docs2nav
    docs2nav.navigator().killers()
	
if action == 'ufoNavigator':
    from resources.lib.indexers import docs2nav
    docs2nav.navigator().ufo()

if action == 'mythsNavigator':
    from resources.lib.indexers import docs2nav
    docs2nav.navigator().myths()
	
if action == 'addictionNavigator':
    from resources.lib.indexers import docs2nav
    docs2nav.navigator().addiction()

if action == 'kids2Navigator':
    from resources.lib.indexers import kidsnav
    kidsnav.navigator().root()
	
if action == 'toddlerNavigator':
    from resources.lib.indexers import kidsnav
    kidsnav.navigator().toddler()

if action == 'KidsNavigator':
    from resources.lib.indexers import kidsnav
    kidsnav.navigator().Kids()
	
if action == 'TeenNavigator':
    from resources.lib.indexers import kidsnav
    kidsnav.navigator().Teen()

	
if action == 'NatureNavigator':
    from resources.lib.indexers import kidsnav
    kidsnav.navigator().Nature()

if action == 'classicsNavigator':
    from resources.lib.indexers import classicnav
    classicnav.navigator().root()

if action == 'action2Navigator':
    from resources.lib.indexers import classicnav
    classicnav.navigator().action()
	
if action == 'adventure2Navigator':
    from resources.lib.indexers import classicnav
    classicnav.navigator().adventure()

if action == 'animation2Navigator':
    from resources.lib.indexers import classicnav
    classicnav.navigator().animation()
	
if action == 'comedy2Navigator':
    from resources.lib.indexers import classicnav
    classicnav.navigator().comedy()

if action == 'crime2Navigator':
    from resources.lib.indexers import classicnav
    classicnav.navigator().crime()
	
if action == 'drama2Navigator':
    from resources.lib.indexers import classicnav
    classicnav.navigator().drama()

if action == 'family2Navigator':
    from resources.lib.indexers import classicnav
    classicnav.navigator().family()
	
if action == 'fantasy2Navigator':
    from resources.lib.indexers import classicnav
    classicnav.navigator().fantasy()

if action == 'horror2Navigator':
    from resources.lib.indexers import classicnav
    classicnav.navigator().horror()
	
if action == 'mystery2Navigator':
    from resources.lib.indexers import classicnav
    classicnav.navigator().mystery()

if action == 'romance2Navigator':
    from resources.lib.indexers import classicnav
    classicnav.navigator().romance()
	
if action == 'scifi2Navigator':
    from resources.lib.indexers import classicnav
    classicnav.navigator().scifi()

if action == 'thriller2Navigator':
    from resources.lib.indexers import classicnav
    classicnav.navigator().thriller()
	
if action == 'war2Navigator':
    from resources.lib.indexers import classicnav
    classicnav.navigator().war()

if action == 'western2Navigator':
    from resources.lib.indexers import classicnav
    classicnav.navigator().western()
	


if action == 'boxsetsNavigator':
    from resources.lib.indexers import bxsets
    bxsets.navigator().root()
	
elif action == 'actionNavigator':
    from resources.lib.indexers import bxsets
    bxsets.navigator().action()
	
elif action == 'actionliteNavigator':
    from resources.lib.indexers import bxsets
    bxsets.navigator().action(lite=True)

elif action == 'adventureNavigator':
    from resources.lib.indexers import bxsets
    bxsets.navigator().adventure()
	
elif action == 'adventureliteNavigator':
    from resources.lib.indexers import bxsets
    bxsets.navigator().adventure(lite=True)
	
elif action == 'animationNavigator':
    from resources.lib.indexers import bxsets
    bxsets.navigator().animation()
	
elif action == 'animationliteNavigator':
    from resources.lib.indexers import bxsets
    bxsets.navigator().animation(lite=True)
	
elif action == 'comedyNavigator':
    from resources.lib.indexers import bxsets
    bxsets.navigator().comedy()
	
elif action == 'comedyliteNavigator':
    from resources.lib.indexers import bxsets
    bxsets.navigator().comedy(lite=True)
	
elif action == 'crimeNavigator':
    from resources.lib.indexers import bxsets
    bxsets.navigator().crime()
	
elif action == 'crimeliteNavigator':
    from resources.lib.indexers import bxsets
    bxsets.navigator().crime(lite=True)
	
elif action == 'dramaNavigator':
    from resources.lib.indexers import bxsets
    bxsets.navigator().drama()
	
elif action == 'dramaliteNavigator':
    from resources.lib.indexers import bxsets
    bxsets.navigator().drama(lite=True)
	
elif action == 'familyNavigator':
    from resources.lib.indexers import bxsets
    bxsets.navigator().family()
	
elif action == 'familyliteNavigator':
    from resources.lib.indexers import bxsets
    bxsets.navigator().family(lite=True)
	
elif action == 'fantasyNavigator':
    from resources.lib.indexers import bxsets
    bxsets.navigator().fantasy()
	
elif action == 'fantasyliteNavigator':
    from resources.lib.indexers import bxsets
    bxsets.navigator().fantasy(lite=True)

elif action == 'horrorNavigator':
    from resources.lib.indexers import bxsets
    bxsets.navigator().horror()
	
elif action == 'horrorliteNavigator':
    from resources.lib.indexers import bxsets
    bxsets.navigator().horror(lite=True)
	
elif action == 'mysteryNavigator':
    from resources.lib.indexers import bxsets
    bxsets.navigator().mystery()
	
elif action == 'mysteryliteNavigator':
    from resources.lib.indexers import bxsets
    bxsets.navigator().mystery(lite=True)
	
elif action == 'romanceNavigator':
    from resources.lib.indexers import bxsets
    bxsets.navigator().romance()
	
elif action == 'romanceliteNavigator':
    from resources.lib.indexers import bxsets
    bxsets.navigator().romance(lite=True)
	
elif action == 'scifiNavigator':
    from resources.lib.indexers import bxsets
    bxsets.navigator().scifi()
	
elif action == 'scifiliteNavigator':
    from resources.lib.indexers import bxsets
    bxsets.navigator().scifi(lite=True)
	
elif action == 'thrillerNavigator':
    from resources.lib.indexers import bxsets
    bxsets.navigator().thriller()
	
elif action == 'thrillerliteNavigator':
    from resources.lib.indexers import bxsets
    bxsets.navigator().thriller(lite=True)
	
elif action == 'westernNavigator':
    from resources.lib.indexers import bxsets
    bxsets.navigator().western()
	
elif action == 'westernliteNavigator':
    from resources.lib.indexers import bxsets
    bxsets.navigator().western(lite=True)

elif action == 'teamNavigator':
    from resources.lib.indexers import teamnav
    teamnav.navigator().root()

elif action == 'ldmovNavigator':
    from resources.lib.indexers import teamnav
    teamnav.navigator().ldmov()

elif action == 'EnforcermoNavigator':
    from resources.lib.indexers import teamnav
    teamnav.navigator().Enforcermo()
	
elif action == 'warhammermoNavigator':
    from resources.lib.indexers import teamnav
    teamnav.navigator().warhammermo()

elif action == 'katsmoNavigator':
    from resources.lib.indexers import teamnav
    teamnav.navigator().katsmo()
	
elif action == 'stalkermoNavigator':
    from resources.lib.indexers import teamnav
    teamnav.navigator().stalkermo()

elif action == 'oddsNavigator':
    from resources.lib.indexers import oddsnends
    oddsnends.navigator().root()

elif action == 'KfulegNavigator':
    from resources.lib.indexers import oddsnends
    oddsnends.navigator().Kfuleg()

elif action == 'qocNavigator':
    from resources.lib.indexers import oddsnends
    oddsnends.navigator().qoc()

elif action == 'giftsNavigator':
    from resources.lib.indexers import oddsnends
    oddsnends.navigator().gifts()

elif action == 'amNavigator':
    from resources.lib.indexers import oddsnends
    oddsnends.navigator().at()
	
elif action == 'MlNavigator':
    from resources.lib.indexers import oddsnends
    oddsnends.navigator().Tl()

elif action == 'restNavigator':
    from resources.lib.indexers import wishes 
    wishes.navigator().rest()

elif action == 'SwmNavigator':
    from resources.lib.indexers import oddsnends
    oddsnends.navigator().Swm()
	
elif action == 'ClmNavigator':
    from resources.lib.indexers import oddsnends
    oddsnends.navigator().Clts()

elif action == 'metalNavigator':
    from resources.lib.indexers import metal
    metal.navigator().root()

elif action == 'unexplainedNavigator':
    from resources.lib.indexers import oddsnends 
    oddsnends.navigator().unexplained()

elif action == 'metal2Navigator':
    from resources.lib.indexers import metal
    metal.navigator().metal()
	
elif action == 'classicNavigator':
    from resources.lib.indexers import metal
    metal.navigator().classic()

elif action == 'psyNavigator':
    from resources.lib.indexers import metal
    metal.navigator().psy()

elif action == 'grungeNavigator':
    from resources.lib.indexers import metal
    metal.navigator().grunge()

elif action == 'usersNavigator':
    from resources.lib.indexers import oddsnends
    oddsnends.navigator().users()
	
elif action == 'TmNavigator':
    from resources.lib.indexers import oddsnends
    oddsnends.navigator().Tts()

elif action == 'KzmNavigator':
    from resources.lib.indexers import oddsnends
    oddsnends.navigator().Kzt()

elif action == 'BftvNavigator':
    from resources.lib.indexers import teamnav
    teamnav.navigator().Bftv()

elif action == 'KrestsNavigator':
    from resources.lib.indexers import wishes
    wishes.navigator().root()

elif action == 'KrestswNavigator':
    from resources.lib.indexers import wishes
    wishes.navigator().krests()
	
elif action == 'usersNavigator':
    from resources.lib.indexers import oddsnends
    oddsnends.navigator().users()
	
elif action == 'ParamNavigator':
    from resources.lib.indexers import oddsnends
    oddsnends.navigator().Paratv()

elif action == 'DocsNavigator':
    from resources.lib.indexers import oddsnends
    oddsnends.navigator().Docstv()

elif action == 'BrNavigator':
    from resources.lib.indexers import oddsnends
    oddsnends.navigator().Br()

elif action == 'kocNavigator':
    from resources.lib.indexers import oddsnends
    oddsnends.navigator().koc()
	
elif action == 'MhNavigator':
    from resources.lib.indexers import oddsnends
    oddsnends.navigator().Mh()

elif action == 'darktvNavigator':
    from resources.lib.indexers import oddsnends
    oddsnends.navigator().darktv()
	
elif action == 'firestickNavigator':
    from resources.lib.indexers import oddsnends
    oddsnends.navigator().firestick()

elif action == 'movieNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().movies()

elif action == 'ShowChangelog':
    from resources.lib.modules import changelog
    changelog.get()
	
elif action == 'movieliteNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().movies(lite=True)

elif action == 'pairNavigator':
    from resources.lib.modules import control
    control.openSettings(id='script.triangulum.pair')


elif action == 'mymovieNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().mymovies()

elif action == 'mymovieliteNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().mymovies(lite=True)

elif action == 'tvNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().tvshows()

elif action == 'tvliteNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().tvshows(lite=True)

elif action == 'mytvNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().mytvshows()

elif action == 'mytvliteNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().mytvshows(lite=True)

elif action == 'downloadNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().downloads()

elif action == 'toolNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().tools()

elif action == 'searchNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().search()

elif action == 'viewsNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().views()

elif action == 'clearCache':
    from resources.lib.indexers import navigator
    navigator.navigator().clearCache()

elif action == 'movies':
    from resources.lib.indexers import movies
    movies.movies().get(url)
	
elif action == 'similar_movies':
    from resources.lib.indexers import movies
    movies.movies().similar_movies(imdb)
	
elif action == 'get_similar_movies':
    from resources.lib.indexers import movies
    movies.movies().get_similar_movies(imdb)	
	
elif action == 'movies2':
    from resources.lib.indexers import movies2
    movies2.movies().get(url)

elif action == 'movies':
    from resources.lib.indexers import movies
    movies.movies().get(url)

elif action == 'moviePage':
    from resources.lib.indexers import movies
    movies.movies().get(url)

elif action == 'movieWidget':
    from resources.lib.indexers import movies
    movies.movies().widget()

elif action == 'movieSearch':
    from resources.lib.indexers import movies
    movies.movies().search(query)

elif action == 'moviePerson':
    from resources.lib.indexers import movies
    movies.movies().person(query)

elif action == 'movieGenres':
    from resources.lib.indexers import movies
    movies.movies().genres()

elif action == 'movieLanguages':
    from resources.lib.indexers import movies
    movies.movies().languages()

elif action == 'movieCertificates':
    from resources.lib.indexers import movies
    movies.movies().certifications()

elif action == 'movieYears':
    from resources.lib.indexers import movies
    movies.movies().years()

elif action == 'moviePersons':
    from resources.lib.indexers import movies
    movies.movies().persons()

elif action == 'movieUserlists':
    from resources.lib.indexers import movies
    movies.movies().userlists()

elif action == 'channels':
    from resources.lib.indexers import channels
    channels.channels().get()

elif action == 'tvshows':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().get(url)
	
elif action == 'similar_shows':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().similar_shows(imdb)
	
elif action == 'get_similar_shows':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().get_similar_shows(imdb)	

elif action == 'tvshowPage':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().get(url)

elif action == 'tvSearch':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().search()

elif action == 'tvPerson':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().person()

elif action == 'tvGenres':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().genres()

elif action == 'tvNetworks':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().networks()

elif action == 'tvCertificates':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().certifications()

elif action == 'tvPersons':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().persons(url)

elif action == 'tvUserlists':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().userlists()

elif action == 'seasons':
    from resources.lib.indexers import episodes
    episodes.seasons().get(tvshowtitle, year, imdb, tvdb)

elif action == 'episodes':
    from resources.lib.indexers import episodes
    episodes.episodes().get(tvshowtitle, year, imdb, tvdb, season, episode)

elif action == 'calendar':
    from resources.lib.indexers import episodes
    episodes.episodes().calendar(url)

elif action == 'tvWidget':
    from resources.lib.indexers import episodes
    episodes.episodes().widget()

elif action == 'calendars':
    from resources.lib.indexers import episodes
    episodes.episodes().calendars()

elif action == 'episodeUserlists':
    from resources.lib.indexers import episodes
    episodes.episodes().userlists()

elif action == 'refresh':
    from resources.lib.modules import control
    control.refresh()

elif action == 'queueItem':
    from resources.lib.modules import control
    control.queueItem()

elif action == 'openSettings':
    from resources.lib.modules import control
    control.openSettings(query)

elif action == 'artwork':
    from resources.lib.modules import control
    control.artwork()

elif action == 'addView':
    from resources.lib.modules import views
    views.addView(content)

elif action == 'moviePlaycount':
    from resources.lib.modules import playcount
    playcount.movies(imdb, query)

elif action == 'episodePlaycount':
    from resources.lib.modules import playcount
    playcount.episodes(imdb, tvdb, season, episode, query)

elif action == 'tvPlaycount':
    from resources.lib.modules import playcount
    playcount.tvshows(name, imdb, tvdb, season, query)
	
elif action == 'tvPlaycountShow':
    from resources.lib.modules import playcount
    playcount.marktvshows(name, imdb, tvdb, query)

elif action == 'trailer':
    from resources.lib.modules import trailer
    trailer.trailer().play(name, url)

elif action == 'traktManager':
    from resources.lib.modules import trakt
    trakt.manager(name, imdb, tvdb, content)

elif action == 'authTrakt':
    from resources.lib.modules import trakt
    trakt.authTrakt()

elif action == 'rdAuthorize':
    from resources.lib.modules import debrid
    debrid.rdAuthorize()

elif action == 'download':
    import json
    from resources.lib.sources import sources
    from resources.lib.modules import downloader
    try: downloader.download(name, image, sources().sourcesResolve(json.loads(source)[0], True))
    except: pass

elif action == 'play':
    from resources.lib.modules import control
    select = control.setting('hosts.mode')
    if select == '3' and 'plugin' in control.infoLabel('Container.PluginName'):
		from resources.lib.sources import sources
		sources().play_dialog(title, year, imdb, tvdb, season, episode, tvshowtitle, premiered, meta, select)
    elif select == '4' and 'plugin' in control.infoLabel('Container.PluginName'):
		from resources.lib.sources import sources
		sources().play_dialog_list(title, year, imdb, tvdb, season, episode, tvshowtitle, premiered, meta, select)
    else:
		from resources.lib.sources import sources
		sources().play(title, year, imdb, tvdb, season, episode, tvshowtitle, premiered, meta, select)
		
elif action == 'play_alter':
		from resources.lib.sources import sources
		sources().play_alter(title, year, imdb, tvdb, season, episode, tvshowtitle, premiered, meta)

elif action == 'play_library':
    from resources.lib.sources import sources
    sources().play_library(title, year, imdb, tvdb, season, episode, tvshowtitle, premiered, meta, select)

elif action == 'addItem':
    from resources.lib.sources import sources
    sources().addItem(title)
	
elif action == 'movieFavourites':
    from resources.lib.indexers import movies
    movies.movies().favourites()
	
elif action == 'movieProgress':
    from resources.lib.indexers import movies
    movies.movies().in_progress()
	
elif action == 'showsProgress':
    from resources.lib.indexers import episodes
    episodes.episodes().in_progress()
	
elif action == 'deleteProgress':
    from resources.lib.modules import favourites
    favourites.deleteProgress(meta, content)
	
elif action == 'tvFavourites':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().favourites()
	
elif action == 'addFavourite':
    from resources.lib.modules import favourites
    favourites.addFavourite(meta, content)

elif action == 'deleteFavourite':
    from resources.lib.modules import favourites
    favourites.deleteFavourite(meta, content)
elif action == 'playItem':
    from resources.lib.sources import sources
    sources().playItem(title, source)

elif action == 'alterSources':
    from resources.lib.sources import sources
    sources().alterSources(url, meta)

elif action == 'clearSources'          :
    import universalscrapers
    universalscrapers.clear_cache()
	
elif action == 'clearProgress':
    from resources.lib.modules import control
    import os,xbmc,xbmcaddon,xbmcgui
    dialog = xbmcgui.Dialog()
    addonInfo = xbmcaddon.Addon().getAddonInfo
    dataPath = xbmc.translatePath(addonInfo('profile')).decode('utf-8')
    favouritesFile = os.path.join(dataPath, 'favourites.db')
    progressFile = os.path.join(dataPath, 'progress.db')
    yes = control.yesnoDialog(control.lang(32056).encode('utf-8'), '', '')
    if yes:
		try: 
			os.remove(progressFile)
			dialog.ok('Clear Progress','Clear Progress Complete','','')
		except:
			dialog.ok('Clear Progress','There was an error Deleting the Database','','')		
		
	
elif action == 'Darknessresolversettings':
    import resolveurl
    resolveurl.display_settings()	
	
elif action == 'movieToLibrary':
    from resources.lib.sources import sources
    sources().movieToLibrary(title,year,imdb,meta)

elif action == 'backupwatchlist':
    import xbmc,os,zipfile,ntpath,xbmcgui
    from resources.lib.modules import control
    dialog = xbmcgui.Dialog()
    USERDATA     =  xbmc.translatePath(os.path.join('special://home/userdata/addon_data/plugin.video.chaostheroy',''))
    if os.path.exists(os.path.join(USERDATA,'favourites.db')):
		backupdir = control.setting('remote_path')
		if not backupdir == '':
		   to_backup = xbmc.translatePath(os.path.join('special://','home/userdata/addon_data/'))	
		   rootlen = len(USERDATA)
		   backup_ui_zip = xbmc.translatePath(os.path.join(backupdir,'chaos theroy_watchlist.zip'))
		   zipobj = zipfile.ZipFile(backup_ui_zip , 'w', zipfile.ZIP_DEFLATED)
		   fn = os.path.join(USERDATA, 'favourites.db')
		   zipobj.write(fn, fn[rootlen:])
		   dialog.ok('Backup Watchlist','Backup complete','','')
		else:
		   dialog.ok('Backup Watchlist','No backup location found: Please setup your Backup location in the addon settings','','')
		   xbmc.executebuiltin('RunPlugin(%s?action=openSettings&query=5.0)' % sys.argv[0])
       
elif action == 'restorewatchlist':
    import xbmc,os,zipfile,ntpath,xbmcgui
    from resources.lib.modules import control
    dialog = xbmcgui.Dialog()
    USERDATA     =  xbmc.translatePath(os.path.join('special://home/userdata/addon_data/plugin.video.chaostheroy',''))
    if os.path.exists(USERDATA):
		zipdir=control.setting('remote_restore_path')
		if not zipdir == '':
		   with zipfile.ZipFile(zipdir, "r") as z:
				z.extractall(USERDATA)
				dialog.ok('Restore Watchlist','Restore complete','','')
		else:
				dialog.ok('Restore Watchlist','No item found: Please select your zipfile location in the addon settings','','')
				xbmc.executebuiltin('RunPlugin(%s?action=openSettings&query=5.0)' % sys.argv[0])
				
elif action == 'movielist':
    from resources.lib.indexers import navigator
    navigator.navigator().mymovies()	

elif action == 'tvlist':
    from resources.lib.indexers import navigator
    navigator.navigator().mytv()		
				
elif action == 'lists_navigator':
    from resources.lib.indexers import navigator
    navigator.navigator().lists_navigator()				
				
elif action == 'universalscraperssettings'    : xbmcaddon.Addon('script.module.universalscrapers').openSettings()			
elif action == 'Darknessresolversettings'    : xbmcaddon.Addon('script.module.resolveurl').openSettings()				