# -*- coding: utf-8 -*-

'''
    odin Add-on

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''


import urlparse,sys,urllib
from resources.lib.modules import control


import xbmcgui

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

windowedtrailer = params.get('windowedtrailer')
windowedtrailer = int(windowedtrailer) if windowedtrailer in ("0","1") else 0


######################LISTS SCRAPER#################################

if action == 'lists':
    from resources.lib.indexers import lists
    lists.indexer().root()

elif action == 'listsNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().lists()    

elif action == 'directory':
    from resources.lib.indexers import lists
    lists.indexer().get(url)

elif action == 'qdirectory':
    from resources.lib.indexers import lists
    lists.indexer().getq(url)

elif action == 'xdirectory':
    from resources.lib.indexers import lists
    lists.indexer().getx(url)

elif action == 'developer':
    from resources.lib.indexers import lists
    lists.indexer().developer()

elif action == 'tvtuner':
    from resources.lib.indexers import lists
    lists.indexer().tvtuner(url)

elif 'youtube' in str(action):
    from resources.lib.indexers import lists
    lists.indexer().youtube(url, action)

elif action == 'play':
    from resources.lib.indexers import lists
    lists.player().play(url, content)

elif action == 'browser':
    from resources.lib.indexers import lists
    lists.resolver().browser(url)

elif action == 'queueItem':
    from resources.lib.modules import control
    control.queueItem()

elif action == 'openSettings':
    from resources.lib.modules import control
    control.openSettings()

elif action == 'urlresolverSettings':
    from resources.lib.modules import control
    control.openSettings(id='script.module.urlresolver')

elif action == 'addView':
    from resources.lib.modules import views
    views.addView(content)

elif action == 'downloader':
    from resources.lib.modules import downloader
    downloader.downloader()

elif action == 'addDownload':
    from resources.lib.modules import downloader
    downloader.addDownload(name,url,image)

elif action == 'removeDownload':
    from resources.lib.modules import downloader
    downloader.removeDownload(url)

elif action == 'startDownload':
    from resources.lib.modules import downloader
    downloader.startDownload()

elif action == 'startDownloadThread':
    from resources.lib.modules import downloader
    downloader.startDownloadThread()

elif action == 'stopDownload':
    from resources.lib.modules import downloader
    downloader.stopDownload()

elif action == 'statusDownload':
    from resources.lib.modules import downloader
    downloader.statusDownload()

elif action == 'trailer':
    from resources.lib.modules import trailer
    trailer.trailer().play(name)

elif action == 'clearCache1':
    from resources.lib.modules import cache
    cache.clear() 
######################LISTS SCRAPER#################################

if action == 'lists2':
    from resources.lib.indexers import lists2
    lists2.indexer().root()

elif action == 'listsNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().lists()    

elif action == 'directory':
    from resources.lib.indexers import lists2
    lists2.indexer().get(url)

elif action == 'qdirectory':
    from resources.lib.indexers import lists2
    lists2.indexer().getq(url)

elif action == 'xdirectory':
    from resources.lib.indexers import lists2
    lists2.indexer().getx(url)

elif action == 'developer':
    from resources.lib.indexers import lists2
    lists2.indexer().developer()

elif action == 'tvtuner':
    from resources.lib.indexers import lists2
    lists2.indexer().tvtuner(url)

elif 'youtube' in str(action):
    from resources.lib.indexers import lists2
    lists2.indexer().youtube(url, action)

elif action == 'play2':
    from resources.lib.indexers import lists2
    lists2.player().play(url, content)

elif action == 'browser':
    from resources.lib.indexers import lists2
    lists2.resolver().browser(url)

elif action == 'queueItem':
    from resources.lib.modules import control
    control.queueItem()

elif action == 'openSettings':
    from resources.lib.modules import control
    control.openSettings()

elif action == 'urlresolverSettings':
    from resources.lib.modules import control
    control.openSettings(id='script.module.urlresolver')

elif action == 'addView':
    from resources.lib.modules import views
    views.addView(content)

elif action == 'downloader':
    from resources.lib.modules import downloader
    downloader.downloader()

elif action == 'addDownload':
    from resources.lib.modules import downloader
    downloader.addDownload(name,url,image)

elif action == 'removeDownload':
    from resources.lib.modules import downloader
    downloader.removeDownload(url)

elif action == 'startDownload':
    from resources.lib.modules import downloader
    downloader.startDownload()

elif action == 'startDownloadThread':
    from resources.lib.modules import downloader
    downloader.startDownloadThread()

elif action == 'stopDownload':
    from resources.lib.modules import downloader
    downloader.stopDownload()

elif action == 'statusDownload':
    from resources.lib.modules import downloader
    downloader.statusDownload()

elif action == 'trailer':
    from resources.lib.modules import trailer
    trailer.trailer().play(name)

elif action == 'clearCache1':
    from resources.lib.modules import cache
    cache.clear()   

######################LISTS3 SCRAPER#################################

if action == 'lists3':
    from resources.lib.indexers import lists3
    lists3.indexer().root()   

elif action == 'tvnav':
    from resources.lib.indexers import navigator
    navigator.navigator().tns()

elif action == 'directory':
    from resources.lib.indexers import lists3
    lists3.indexer().get(url)

elif action == 'qdirectory':
    from resources.lib.indexers import lists3
    lists3.indexer().getq(url)

elif action == 'xdirectory':
    from resources.lib.indexers import lists3
    lists3.indexer().getx(url)

elif action == 'developer':
    from resources.lib.indexers import lists3
    lists3.indexer().developer()

elif action == 'tvtuner':
    from resources.lib.indexers import lists3
    lists3.indexer().tvtuner(url)

elif 'youtube' in str(action):
    from resources.lib.indexers import lists3
    lists3.indexer().youtube(url, action)

elif action == 'play2':
    from resources.lib.indexers import lists3
    lists3.player().play(url, content)

elif action == 'browser':
    from resources.lib.indexers import lists3
    lists3.resolver().browser(url)


elif action == 'queueItem':
    from resources.lib.modules import control
    control.queueItem()

elif action == 'openSettings':
    from resources.lib.modules import control
    control.openSettings()

elif action == 'urlresolverSettings':
    from resources.lib.modules import control
    control.openSettings(id='script.module.urlresolver')

elif action == 'addView':
    from resources.lib.modules import views
    views.addView(content)

elif action == 'downloader':
    from resources.lib.modules import downloader
    downloader.downloader()

elif action == 'addDownload':
    from resources.lib.modules import downloader
    downloader.addDownload(name,url,image)

elif action == 'removeDownload':
    from resources.lib.modules import downloader
    downloader.removeDownload(url)

elif action == 'startDownload':
    from resources.lib.modules import downloader
    downloader.startDownload()

elif action == 'startDownloadThread':
    from resources.lib.modules import downloader
    downloader.startDownloadThread()

elif action == 'stopDownload':
    from resources.lib.modules import downloader
    downloader.stopDownload()

elif action == 'statusDownload':
    from resources.lib.modules import downloader
    downloader.statusDownload()

elif action == 'trailer':
    from resources.lib.modules import trailer
    trailer.trailer().play(name)

elif action == 'clearCache1':
    from resources.lib.modules import cache
    cache.clear()   	

######################sports SCRAPER#################################
if action == 'lists4':
    from resources.lib.indexers import lists4
    lists4.indexer().root()   

elif action == 'directory':
    from resources.lib.indexers import lists4
    lists4.indexer().get(url)

elif action == 'qdirectory':
    from resources.lib.indexers import lists4
    lists4.indexer().getq(url)

elif action == 'xdirectory':
    from resources.lib.indexers import lists4
    lists4.indexer().getx(url)

elif action == 'developer':
    from resources.lib.indexers import lists4
    lists4.indexer().developer()

elif action == 'tvtuner':
    from resources.lib.indexers import lists4
    lists4.indexer().tvtuner(url)

elif 'youtube' in str(action):
    from resources.lib.indexers import lists4
    lists4.indexer().youtube(url, action)

elif action == 'play3':
    from resources.lib.indexers import lists4
    lists4.player().play(url, content)

elif action == 'browser':
    from resources.lib.indexers import lists4
    lists4.resolver().browser(url)


elif action == 'queueItem':
    from resources.lib.modules import control
    control.queueItem()

elif action == 'openSettings':
    from resources.lib.modules import control
    control.openSettings()

elif action == 'urlresolverSettings':
    from resources.lib.modules import control
    control.openSettings(id='script.module.urlresolver')

elif action == 'addView':
    from resources.lib.modules import views
    views.addView(content)

elif action == 'downloader':
    from resources.lib.modules import downloader
    downloader.downloader()

elif action == 'addDownload':
    from resources.lib.modules import downloader
    downloader.addDownload(name,url,image)

elif action == 'removeDownload':
    from resources.lib.modules import downloader
    downloader.removeDownload(url)

elif action == 'startDownload':
    from resources.lib.modules import downloader
    downloader.startDownload()

elif action == 'startDownloadThread':
    from resources.lib.modules import downloader
    downloader.startDownloadThread()

elif action == 'stopDownload':
    from resources.lib.modules import downloader
    downloader.stopDownload()

elif action == 'statusDownload':
    from resources.lib.modules import downloader
    downloader.statusDownload()

elif action == 'trailer':
    from resources.lib.modules import trailer
    trailer.trailer().play(name)

elif action == 'clearCache1':
    from resources.lib.modules import cache
    cache.clear()   
######################LISTS5 SCRAPER#################################

if action == 'lists5':
    from resources.lib.indexers import lists5
    lists5.indexer().root()
   

elif action == 'directory':
    from resources.lib.indexers import lists5
    lists5.indexer().get(url)

elif action == 'qdirectory':
    from resources.lib.indexers import lists5
    lists5.indexer().getq(url)

elif action == 'xdirectory':
    from resources.lib.indexers import lists5
    lists5.indexer().getx(url)

elif action == 'developer':
    from resources.lib.indexers import lists5
    lists5.indexer().developer()

elif action == 'tvtuner':
    from resources.lib.indexers import lists5
    lists5.indexer().tvtuner(url)

elif 'youtube' in str(action):
    from resources.lib.indexers import lists5
    lists5.indexer().youtube(url, action)

elif action == 'play4':
    from resources.lib.indexers import lists5
    lists5.player().play(url, content)

elif action == 'browser':
    from resources.lib.indexers import lists5
    lists5.resolver().browser(url)

elif action == 'queueItem':
    from resources.lib.modules import control
    control.queueItem()

elif action == 'openSettings':
    from resources.lib.modules import control
    control.openSettings()

elif action == 'urlresolverSettings':
    from resources.lib.modules import control
    control.openSettings(id='script.module.urlresolver')

elif action == 'addView':
    from resources.lib.modules import views
    views.addView(content)

elif action == 'downloader':
    from resources.lib.modules import downloader
    downloader.downloader()

elif action == 'addDownload':
    from resources.lib.modules import downloader
    downloader.addDownload(name,url,image)

elif action == 'removeDownload':
    from resources.lib.modules import downloader
    downloader.removeDownload(url)

elif action == 'startDownload':
    from resources.lib.modules import downloader
    downloader.startDownload()

elif action == 'startDownloadThread':
    from resources.lib.modules import downloader
    downloader.startDownloadThread()

elif action == 'stopDownload':
    from resources.lib.modules import downloader
    downloader.stopDownload()

elif action == 'statusDownload':
    from resources.lib.modules import downloader
    downloader.statusDownload()

elif action == 'trailer':
    from resources.lib.modules import trailer
    trailer.trailer().play(name)

elif action == 'clearCache1':
    from resources.lib.modules import cache
    cache.clear() 
######################LISTS SCRAPER#################################

if action == 'lists6':
    from resources.lib.indexers import lists6
    lists6.indexer().root()
 

elif action == 'directory':
    from resources.lib.indexers import lists6
    lists6.indexer().get(url)

elif action == 'qdirectory':
    from resources.lib.indexers import lists6
    lists6.indexer().getq(url)

elif action == 'xdirectory':
    from resources.lib.indexers import lists6
    lists6.indexer().getx(url)

elif action == 'developer':
    from resources.lib.indexers import lists6
    lists6.indexer().developer()

elif action == 'tvtuner':
    from resources.lib.indexers import lists6
    lists6.indexer().tvtuner(url)

elif 'youtube' in str(action):
    from resources.lib.indexers import lists6
    lists6.indexer().youtube(url, action)

elif action == 'play6':
    from resources.lib.indexers import lists6
    lists6.player().play(url, content)

elif action == 'browser':
    from resources.lib.indexers import lists6
    lists6.resolver().browser(url)

elif action == 'queueItem':
    from resources.lib.modules import control
    control.queueItem()

elif action == 'openSettings':
    from resources.lib.modules import control
    control.openSettings()

elif action == 'urlresolverSettings':
    from resources.lib.modules import control
    control.openSettings(id='script.module.urlresolver')

elif action == 'addView':
    from resources.lib.modules import views
    views.addView(content)

elif action == 'downloader':
    from resources.lib.modules import downloader
    downloader.downloader()

elif action == 'addDownload':
    from resources.lib.modules import downloader
    downloader.addDownload(name,url,image)

elif action == 'removeDownload':
    from resources.lib.modules import downloader
    downloader.removeDownload(url)

elif action == 'startDownload':
    from resources.lib.modules import downloader
    downloader.startDownload()

elif action == 'startDownloadThread':
    from resources.lib.modules import downloader
    downloader.startDownloadThread()

elif action == 'stopDownload':
    from resources.lib.modules import downloader
    downloader.stopDownload()

elif action == 'statusDownload':
    from resources.lib.modules import downloader
    downloader.statusDownload()

elif action == 'trailer':
    from resources.lib.modules import trailer
    trailer.trailer().play(name)

elif action == 'clearCache1':
    from resources.lib.modules import cache
    cache.clear()   
######################tunes player#################################
	
elif action == 'radios':
    from resources.lib.indexers import odintunes
    odintunes.radios()

elif action == 'radioResolve':
    from resources.lib.indexers import odintunes
    odintunes.radioResolve(url)

elif action == 'radio1fm':
    from resources.lib.indexers import odintunes
    odintunes.radio1fm()

elif action == 'radio181fm':
    from resources.lib.indexers import odintunes
    odintunes.radio181fm()

elif action == 'radiocast':
    from resources.lib.indexers import odintunes
    odintunes.kickinradio()

elif action == 'kickinradiocats':
    from resources.lib.indexers import odintunes
    odintunes.kickinradiocats(url)
######################IMDB SCRAPER#################################

if action == None:
    from resources.lib.indexers import navigator
    from resources.lib.modules import cache
    cache.cache_version_check()
    navigator.navigator().root()

elif action == "furkNavigator":
    from resources.lib.indexers import navigator
    navigator.navigator().furk()

elif action == "furkMetaSearch":
    from resources.lib.indexers import furk
    furk.furk().furk_meta_search(url)

elif action == "furkSearch":
    from resources.lib.indexers import furk
    furk.furk().search()

elif action == "furkUserFiles":
    from resources.lib.indexers import furk
    furk.furk().user_files()

elif action == "furkSearchNew":
    from resources.lib.indexers import furk
    furk.furk().search_new()

elif action == 'ruSettings':
    from resources.lib.modules import control
    control.openSettings(id='script.module.resolveurl')    

elif action == 'movieNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().movies()

elif action == 'movieliteNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().movies(lite=True)

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

elif action == 'paranormalNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().paranormal()

elif action == 'oneclickNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().oneclick()

elif action == 'oneclick2Navigator':
    from resources.lib.indexers import navigator
    navigator.navigator().oneclick2()            

elif action == 'libraryNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().library()

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

elif action == 'clearCacheSearch':
    from resources.lib.indexers import navigator
    navigator.navigator().clearCacheSearch()
    
elif action == 'infoCheck':
    from resources.lib.indexers import navigator
    navigator.navigator().infoCheck('')

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
    movies.movies().search_new()

elif action == 'movieSearchnew':
    from resources.lib.indexers import movies
    movies.movies().search_new()

elif action == 'movieSearchterm':
    from resources.lib.indexers import movies
    movies.movies().search_term(name)

elif action == 'moviePerson':
    from resources.lib.indexers import movies
    movies.movies().person()

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
    movies.movies().persons(url)

elif action == 'movieUserlists':
    from resources.lib.indexers import movies
    movies.movies().userlists()

elif action == 'channels':
    from resources.lib.indexers import channels
    channels.channels().get()

elif action == 'tvshows':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().get(url)

elif action == 'tvshowPage':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().get(url)

elif action == 'tvSearch':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().search_new()

elif action == 'tvSearchnew':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().search_new()

elif action == 'tvSearchterm':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().search_term(name)
    
elif action == 'tvPerson':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().person()

elif action == 'tvGenres':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().genres()

elif action == 'tvNetworks':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().networks()

elif action == 'tvLanguages':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().languages()

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

elif action == 'trailer':
    from resources.lib.modules import trailer
    trailer.trailer().play(name, url, windowedtrailer)

elif action == 'traktManager':
    from resources.lib.modules import trakt
    trakt.manager(name, imdb, tvdb, content)

elif action == 'authTrakt':
    from resources.lib.modules import trakt
    trakt.authTrakt()

elif action == 'smuSettings':
    try: import resolveurl
    except: pass
    resolveurl.display_settings()

elif action == 'download':
    import json
    from resources.lib.modules import sources
    from resources.lib.modules import downloader
    try: downloader.download(name, image, sources.sources().sourcesResolve(json.loads(source)[0], True))
    except: pass

elif action == 'play1':
    from resources.lib.modules import sources
    sources.sources().play(title, year, imdb, tvdb, season, episode, tvshowtitle, premiered, meta, select)

elif action == 'addItem':
    from resources.lib.modules import sources
    sources.sources().addItem(title)

elif action == 'playItem':
    from resources.lib.modules import sources
    sources.sources().playItem(title, source)

elif action == 'alterSources':
    from resources.lib.modules import sources
    sources.sources().alterSources(url, meta)

elif action == 'clearSources':
    from resources.lib.modules import sources
    sources.sources().clearSources()

elif action == 'random':
    rtype = params.get('rtype')
    if rtype == 'movie':
        from resources.lib.indexers import movies
        rlist = movies.movies().get(url, create_directory=False)
        r = sys.argv[0]+"?action=play"
    elif rtype == 'episode':
        from resources.lib.indexers import episodes
        rlist = episodes.episodes().get(tvshowtitle, year, imdb, tvdb, season, create_directory=False)
        r = sys.argv[0]+"?action=play"
    elif rtype == 'season':
        from resources.lib.indexers import episodes
        rlist = episodes.seasons().get(tvshowtitle, year, imdb, tvdb, create_directory=False)
        r = sys.argv[0]+"?action=random&rtype=episode"
    elif rtype == 'show':
        from resources.lib.indexers import tvshows
        rlist = tvshows.tvshows().get(url, create_directory=False)
        r = sys.argv[0]+"?action=random&rtype=season"
    from resources.lib.modules import control
    from random import randint
    import json
    try:
        rand = randint(1,len(rlist))-1
        for p in ['title','year','imdb','tvdb','season','episode','tvshowtitle','premiered','select']:
            if rtype == "show" and p == "tvshowtitle":
                try: r += '&'+p+'='+urllib.quote_plus(rlist[rand]['title'])
                except: pass
            else:
                try: r += '&'+p+'='+urllib.quote_plus(rlist[rand][p])
                except: pass
        try: r += '&meta='+urllib.quote_plus(json.dumps(rlist[rand]))
        except: r += '&meta='+urllib.quote_plus("{}")
        if rtype == "movie":
            try: control.infoDialog(rlist[rand]['title'], control.lang(32536).encode('utf-8'), time=30000)
            except: pass
        elif rtype == "episode":
            try: control.infoDialog(rlist[rand]['tvshowtitle']+" - Season "+rlist[rand]['season']+" - "+rlist[rand]['title'], control.lang(32536).encode('utf-8'), time=30000)
            except: pass
        control.execute('RunPlugin(%s)' % r)
    except:
        control.infoDialog(control.lang(32537).encode('utf-8'), time=8000)

elif action == 'movieToLibrary':
    from resources.lib.modules import libtools
    libtools.libmovies().add(name, title, year, imdb, tmdb)

elif action == 'moviesToLibrary':
    from resources.lib.modules import libtools
    libtools.libmovies().range(url)

elif action == 'moviesToLibrarySilent':
    from resources.lib.modules import libtools
    libtools.libmovies().silent(url)

elif action == 'tvshowToLibrary':
    from resources.lib.modules import libtools
    libtools.libtvshows().add(tvshowtitle, year, imdb, tvdb)

elif action == 'tvshowsToLibrary':
    from resources.lib.modules import libtools
    libtools.libtvshows().range(url)

elif action == 'tvshowsToLibrarySilent':
    from resources.lib.modules import libtools
    libtools.libtvshows().silent(url)

elif action == 'updateLibrary':
    from resources.lib.modules import libtools
    libtools.libepisodes().update(query)

elif action == 'service':
    from resources.lib.modules import libtools
    libtools.libepisodes().service()

##############################odintoons test ####################################################################
elif action == 'cartoon':
    from resources.lib.indexers import navigator
    navigator.navigator().toons()

elif action == 'toonmovieNavigator':
    from resources.lib.indexers import odintoons
    odintoons.movies().genres()

elif action == 'animemovieNavigator':
    from resources.lib.indexers import odintoons
    odintoons.movies().animegenres()

elif action == 'animetvNavigator':
    from resources.lib.indexers import odintvtoons
    odintvtoons.tvshows().animegenres()

elif action == 'toonstvNavigator':
    from resources.lib.indexers import odintvtoons
    odintvtoons.tvshows().genres()
##################################action packed###################################3

elif action == 'apacked':
    from resources.lib.indexers import navigator
    navigator.navigator().apacked()

elif action == 'apmovies':
    from resources.lib.indexers import apmovies
    apmovies.movies().get(url)

elif action == 'apmovieGenres':
    from resources.lib.indexers import apmovies
    apmovies.movies().genres()
	
	
elif action == 'aptvshows':
    from resources.lib.indexers import aptvshows
    aptvshows.tvshows().get(url)

elif action == 'aptvGenres':
    from resources.lib.indexers import aptvshows
    aptvshows.tvshows().genres()
##############################laughing hour###################################

elif action == 'lhour':
    from resources.lib.indexers import navigator
    navigator.navigator().lhour()

elif action == 'lhmovies':
    from resources.lib.indexers import lhmovies
    lhmovies.movies().get(url)

elif action == 'lhmovieGenres':
    from resources.lib.indexers import lhmovies
    lhmovies.movies().genres()
	
elif action == 'lhtvshows':
    from resources.lib.indexers import lhtvshows
    lhtvshows.tvshows().get(url)

elif action == 'lhtvGenres':
    from resources.lib.indexers import lhtvshows
    lhtvshows.tvshows().genres()
############################3wild west####################

elif action == 'wild':
    from resources.lib.indexers import navigator
    navigator.navigator().wild()

elif action == 'wwmovies':
    from resources.lib.indexers import wwmovies
    wwmovies.movies().get(url)

elif action == 'wwmovieGenres':
    from resources.lib.indexers import wwmovies
    wwmovies.movies().genres()


elif action == 'wwtvshows':
    from resources.lib.indexers import wwtvshows
    wwtvshows.tvshows().get(url)


elif action == 'wwtvGenres':
    from resources.lib.indexers import wwtvshows
    wwtvshows.tvshows().genres()

