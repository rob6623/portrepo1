# -*- coding: utf-8 -*-




import os,sys,urlparse

from resources.lib.modules import control
from resources.lib.modules import trakt
from resources.lib.modules import cache

sysaddon = sys.argv[0] ; syshandle = int(sys.argv[1])

artPath = control.artPath() ; addonFanart = control.addonFanart()

imdbCredentials = False if control.setting('imdb.user') == '' else True

traktCredentials = trakt.getTraktCredentialsInfo()

traktIndicators = trakt.getTraktIndicatorsInfo()

queueMenu = control.lang(32065).encode('utf-8')


class navigator:
    def root(self):
        self.addDirectoryItem('50s to 60s Movies', 'movieGenres50', 'movies.jpg', 'Defaultmovies.jpg')
        self.addDirectoryItem('60s to 70s Movies', 'movieGenres60', 'movies.jpg', 'Defaultmovies.jpg')
        self.addDirectoryItem('70s to 80s Movies', 'movieGenres70', 'movies.jpg', 'Defaultmovies.jpg')		
        self.addDirectoryItem('80s to 90s Movies', 'movieGenres80', 'movies.jpg', 'Defaultmovies.jpg')		
        self.addDirectoryItem('50s to 60s TV Shows', 'tvGenres50', 'tvshows.jpg', 'Defaultmovies.jpg')		
        self.addDirectoryItem('60s to 70s TV Shows', 'tvGenres60', 'tvshows.jpg', 'Defaultmovies.jpg')		
        self.addDirectoryItem('70s to 80s TV Shows', 'tvGenres70', 'tvshows.jpg', 'Defaultmovies.jpg')		
        self.addDirectoryItem('80s to 90s TV Shows', 'tvGenres80', 'tvshows.jpg', 'Defaultmovies.jpg')
        self.addDirectoryItem(32043, 'openSettings&query=0.0', 'icon.jpg', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32044, 'openSettings&query=3.1', 'icon.jpg', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32045, 'openSettings&query=1.0', 'icon.jpg', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32046, 'openSettings&query=5.0', 'icon.jpg', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32047, 'openSettings&query=2.0', 'icon.jpg', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32048, 'openSettings&query=4.0', 'icon.jpg', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32049, 'viewsNavigator', 'icon.jpg', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32050, 'clearSources', 'icon.jpg', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32052, 'clearCache', 'icon.jpg', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32073, 'infoCheck', 'icon.jpg', 'DefaultAddonProgram.png', isFolder=False)		
        self.endDirectory()


    def movies(self, lite=False):
        self.addDirectoryItem(32011, 'movieGenres', 'movies.jpg', 'Defaultmovies.jpg')
        self.addDirectoryItem(32012, 'movieYears', 'movies.jpg', 'Defaultmovies.jpg')
        self.addDirectoryItem(32013, 'moviePersons', 'movies.jpg', 'Defaultmovies.jpg')
        self.addDirectoryItem(32014, 'movieLanguages', 'movies.jpg', 'Defaultmovies.jpg')
        self.addDirectoryItem(32015, 'movieCertificates', 'movies.jpg', 'Defaultmovies.jpg')
        self.addDirectoryItem(32017, 'movies&url=trending', 'movies.jpg', 'DefaultRecentlyAddedmovies.jpg')
        self.addDirectoryItem(32018, 'movies&url=popular', 'movies.jpg', 'Defaultmovies.jpg')
        self.addDirectoryItem(32019, 'movies&url=views', 'movies.jpg', 'Defaultmovies.jpg')
        self.addDirectoryItem(32020, 'movies&url=boxoffice', 'movies.jpg', 'Defaultmovies.jpg')
        self.addDirectoryItem(32021, 'movies&url=oscars', 'movies.jpg', 'Defaultmovies.jpg')
        self.addDirectoryItem(32022, 'movies&url=theaters', 'movies.jpg', 'DefaultRecentlyAddedmovies.jpg')
        self.addDirectoryItem(32005, 'movies&url=featured', 'movies.jpg', 'DefaultRecentlyAddedmovies.jpg')

        if lite == False:
            if not control.setting('lists.widget') == '0':
                self.addDirectoryItem(32003, 'mymovieliteNavigator', 'movies.jpg', 'DefaultVideoPlaylists.png')

            self.addDirectoryItem(32028, 'moviePerson', 'movies.jpg', 'Defaultmovies.jpg')
            self.addDirectoryItem(32010, 'movieSearch', 'movies.jpg', 'Defaultmovies.jpg')

        self.endDirectory()


    def mymovies(self, lite=False):
        self.accountCheck()

        if traktCredentials == True and imdbCredentials == True:
            self.addDirectoryItem(32032, 'movies&url=traktcollection', 'movies.jpg', 'Defaultmovies.jpg', queue=True)
            self.addDirectoryItem(32033, 'movies&url=traktwatchlist', 'movies.jpg', 'Defaultmovies.jpg', queue=True)
            self.addDirectoryItem(32034, 'movies&url=imdbwatchlist', 'movies.jpg', 'Defaultmovies.jpg', queue=True)

        elif traktCredentials == True:
            self.addDirectoryItem(32032, 'movies&url=traktcollection', 'movies.jpg', 'Defaultmovies.jpg', queue=True)
            self.addDirectoryItem(32033, 'movies&url=traktwatchlist', 'movies.jpg', 'Defaultmovies.jpg', queue=True)

        elif imdbCredentials == True:
            self.addDirectoryItem(32032, 'movies&url=imdbwatchlist', 'movies.jpg', 'Defaultmovies.jpg', queue=True)
            self.addDirectoryItem(32033, 'movies&url=imdbwatchlist2', 'movies.jpg', 'Defaultmovies.jpg', queue=True)

        if traktCredentials == True:
            self.addDirectoryItem(32035, 'movies&url=traktfeatured', 'movies.jpg', 'Defaultmovies.jpg', queue=True)

        elif imdbCredentials == True:
            self.addDirectoryItem(32035, 'movies&url=featured', 'movies.jpg', 'Defaultmovies.jpg', queue=True)

        if traktIndicators == True:
            self.addDirectoryItem(32036, 'movies&url=trakthistory', 'movies.jpg', 'Defaultmovies.jpg', queue=True)

        self.addDirectoryItem(32039, 'movieUserlists', 'movies.jpg', 'Defaultmovies.jpg')

        if lite == False:
            self.addDirectoryItem(32031, 'movieliteNavigator', 'movies.jpg', 'Defaultmovies.jpg')
            self.addDirectoryItem(32028, 'moviePerson', 'movies.jpg', 'Defaultmovies.jpg')
            self.addDirectoryItem(32010, 'movieSearch', 'movies.jpg', 'Defaultmovies.jpg')

        self.endDirectory()


    def tvshows(self, lite=False):
        self.addDirectoryItem(32011, 'tvGenres', 'tvshows.jpg', 'Defaulttvshows.jpg')
        self.addDirectoryItem(32016, 'tvNetworks', 'tvshows.jpg', 'Defaulttvshows.jpg')
        self.addDirectoryItem(32014, 'tvLanguages', 'tvshows.jpg', 'Defaulttvshows.jpg')
        self.addDirectoryItem(32015, 'tvCertificates', 'tvshows.jpg', 'Defaulttvshows.jpg')
        self.addDirectoryItem(32017, 'tvshows&url=trending', 'tvshows.jpg', 'DefaultRecentlyAddedEpisodes.png')
        self.addDirectoryItem(32018, 'tvshows&url=popular', 'tvshows.jpg', 'Defaulttvshows.jpg')
        self.addDirectoryItem(32023, 'tvshows&url=rating', 'tvshows.jpg', 'Defaulttvshows.jpg')
        self.addDirectoryItem(32019, 'tvshows&url=views', 'tvshows.jpg', 'Defaulttvshows.jpg')
        self.addDirectoryItem(32024, 'tvshows&url=airing', 'tvshows.jpg', 'Defaulttvshows.jpg')
        #self.addDirectoryItem(32025, 'tvshows&url=active', 'tvshows.jpg', 'Defaulttvshows.jpg')
        self.addDirectoryItem(32026, 'tvshows&url=premiere', 'tvshows.jpg', 'Defaulttvshows.jpg')
        self.addDirectoryItem(32006, 'calendar&url=added', 'tvshows.jpg', 'DefaultRecentlyAddedEpisodes.png', queue=True)
        self.addDirectoryItem(32027, 'calendars', 'tvshows.jpg', 'DefaultRecentlyAddedEpisodes.png')

        if lite == False:
            if not control.setting('lists.widget') == '0':
                self.addDirectoryItem(32004, 'mytvliteNavigator', 'tvshows.jpg', 'DefaultVideoPlaylists.png')

            self.addDirectoryItem(32028, 'tvPerson', 'tvshows.jpg', 'Defaulttvshows.jpg')
            self.addDirectoryItem(32010, 'tvSearch', 'tvshows.jpg', 'Defaulttvshows.jpg')

        self.endDirectory()


    def mytvshows(self, lite=False):
        self.accountCheck()

        if traktCredentials == True and imdbCredentials == True:
            self.addDirectoryItem(32032, 'tvshows&url=traktcollection', 'tvshows.jpg', 'Defaulttvshows.jpg')
            self.addDirectoryItem(32033, 'tvshows&url=traktwatchlist', 'tvshows.jpg', 'Defaulttvshows.jpg')
            self.addDirectoryItem(32034, 'tvshows&url=imdbwatchlist', 'tvshows.jpg', 'Defaulttvshows.jpg')

        elif traktCredentials == True:
            self.addDirectoryItem(32032, 'tvshows&url=traktcollection', 'tvshows.jpg', 'Defaulttvshows.jpg')
            self.addDirectoryItem(32033, 'tvshows&url=traktwatchlist', 'tvshows.jpg', 'Defaulttvshows.jpg')

        elif imdbCredentials == True:
            self.addDirectoryItem(32032, 'tvshows&url=imdbwatchlist', 'tvshows.jpg', 'Defaulttvshows.jpg')
            self.addDirectoryItem(32033, 'tvshows&url=imdbwatchlist2', 'tvshows.jpg', 'Defaulttvshows.jpg')

        if traktCredentials == True:
            self.addDirectoryItem(32035, 'tvshows&url=traktfeatured', 'tvshows.jpg', 'Defaulttvshows.jpg')

        elif imdbCredentials == True:
            self.addDirectoryItem(32035, 'tvshows&url=trending', 'tvshows.jpg', 'Defaultmovies.jpg', queue=True)

        if traktIndicators == True:
            self.addDirectoryItem(32036, 'calendar&url=trakthistory', 'tvshows.jpg', 'Defaulttvshows.jpg', queue=True)
            self.addDirectoryItem(32037, 'calendar&url=progress', 'tvshows.jpg', 'DefaultRecentlyAddedEpisodes.png', queue=True)
            self.addDirectoryItem(32038, 'calendar&url=mycalendar', 'tvshows.jpg', 'DefaultRecentlyAddedEpisodes.png', queue=True)

        self.addDirectoryItem(32040, 'tvUserlists', 'tvshows.jpg', 'Defaulttvshows.jpg')

        if traktCredentials == True:
            self.addDirectoryItem(32041, 'episodeUserlists', 'tvshows.jpg', 'Defaulttvshows.jpg')

        if lite == False:
            self.addDirectoryItem(32031, 'tvliteNavigator', 'tvshows.jpg', 'Defaulttvshows.jpg')
            self.addDirectoryItem(32028, 'tvPerson', 'tvshows.jpg', 'Defaulttvshows.jpg')
            self.addDirectoryItem(32010, 'tvSearch', 'tvshows.jpg', 'Defaulttvshows.jpg')

        self.endDirectory()


    def tools(self):
        self.addDirectoryItem(32043, 'openSettings&query=0.0', 'icon.jpg', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32044, 'openSettings&query=3.1', 'icon.jpg', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32045, 'openSettings&query=1.0', 'icon.jpg', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32046, 'openSettings&query=5.0', 'icon.jpg', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32047, 'openSettings&query=2.0', 'icon.jpg', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32048, 'openSettings&query=4.0', 'icon.jpg', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32049, 'viewsNavigator', 'icon.jpg', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32050, 'clearSources', 'icon.jpg', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32052, 'clearCache', 'icon.jpg', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32073, 'infoCheck', 'icon.jpg', 'DefaultAddonProgram.png', isFolder=False)

        self.endDirectory()


    def downloads(self):
        movie_downloads = control.setting('movie.download.path')
        tv_downloads = control.setting('tv.download.path')

        if len(control.listDir(movie_downloads)[0]) > 0:
            self.addDirectoryItem(32001, movie_downloads, 'movies.jpg', 'Defaultmovies.jpg', isAction=False)
        if len(control.listDir(tv_downloads)[0]) > 0:
            self.addDirectoryItem(32002, tv_downloads, 'tvshows.jpg', 'Defaulttvshows.jpg', isAction=False)

        self.endDirectory()

    def search(self):
        self.addDirectoryItem(32001, 'movieSearch', 'search.png', 'DefaultMovies.png')
        self.addDirectoryItem(32002, 'tvSearch', 'search.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32029, 'moviePerson', 'people-search.png', 'DefaultMovies.png')
        self.addDirectoryItem(32030, 'tvPerson', 'people-search.png', 'DefaultTVShows.png')

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


    def infoCheck(self, version):
        try:
            control.infoDialog('', control.lang(32074).encode('utf-8'), time=5000, sound=False)
            return '1'
        except:
            return '1'


    def clearCache(self):
        control.idle()
        yes = control.yesnoDialog(control.lang(32056).encode('utf-8'), '', '')
        if not yes: return
        from resources.lib.modules import cache
        cache.cache_clear()
        control.infoDialog(control.lang(32057).encode('utf-8'), sound=True, icon='INFO')

    def clearCacheMeta(self):
        control.idle()
        yes = control.yesnoDialog(control.lang(32056).encode('utf-8'), '', '')
        if not yes: return
        from resources.lib.modules import cache
        cache.cache_clear_meta()
        control.infoDialog(control.lang(32057).encode('utf-8'), sound=True, icon='INFO')

    def clearCacheProviders(self):
        control.idle()
        yes = control.yesnoDialog(control.lang(32056).encode('utf-8'), '', '')
        if not yes: return
        from resources.lib.modules import cache
        cache.cache_clear_providers()
        control.infoDialog(control.lang(32057).encode('utf-8'), sound=True, icon='INFO')

    def clearCacheSearch(self):
        control.idle()
        yes = control.yesnoDialog(control.lang(32056).encode('utf-8'), '', '')
        if not yes: return
        from resources.lib.modules import cache
        cache.cache_clear_search()
        control.infoDialog(control.lang(32057).encode('utf-8'), sound=True, icon='INFO')

    def clearCacheAll(self):
        control.idle()
        yes = control.yesnoDialog(control.lang(32056).encode('utf-8'), '', '')
        if not yes: return
        from resources.lib.modules import cache
        cache.cache_clear_all()
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
