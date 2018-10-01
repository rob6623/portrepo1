import time
import xbmc
import os
import xbmcgui
import urllib2
import webbrowser


def menuoptions():
    dialog = xbmcgui.Dialog()
    funcs = (
    function1,
    function2,
    function3,
	function4,
	function5
    )
        
    call = dialog.select('[B][COLOR=gold]Crucial Minds Pair Tool[/COLOR][/B]', [
    '[B][COLOR=gold]      vidup.me[/COLOR][/B]', 
    '[B][COLOR=gold]      tvad.me[/COLOR][/B]',
    '[B][COLOR=gold]      Olpair.com[/COLOR][/B]', 
    '[B][COLOR=gold]      vshare.eu[/COLOR][/B]',
    '[B][COLOR=gold]      thevideo.me[/COLOR][/B]'])
    # dialog.selectreturns
    #   0 -> escape pressed
    #   1 -> first item
    #   2 -> second item
    if call:
        # esc is not pressed
        if call < 0:
            return
        func = funcs[call-5]
        return func()
    else:
        func = funcs[call]
        return func()
    return 

def platform():
    if xbmc.getCondVisibility('system.platform.android'):
        return 'android'
    elif xbmc.getCondVisibility('system.platform.linux'):
        return 'linux'
    elif xbmc.getCondVisibility('system.platform.windows'):
        return 'windows'
    elif xbmc.getCondVisibility('system.platform.osx'):
        return 'osx'
    elif xbmc.getCondVisibility('system.platform.atv2'):
        return 'atv2'
    elif xbmc.getCondVisibility('system.platform.ios'):
        return 'ios'

myplatform = platform()
    
def function1():
    if myplatform == 'android': # Android 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( 'https://tvad.me/pair' ) )
    else:
        opensite = webbrowser . open('https://tvad.me/pair')


def function2():
    if myplatform == 'android': # Android 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( 'https://vidup.me/pair' ) )
    else:
        opensite = webbrowser . open('https://vidup.me/pair')

def function3():
    if myplatform == 'android': # Android 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( 'https://thevideo.me/pair' ) )
    else:
        opensite = webbrowser . open('https://thevideo.me/pair')

def function4():
    if myplatform == 'android': # Android 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( 'https://thevideo.me/pair' ) )
    else:
        opensite = webbrowser . open('https://thevideo.me/pair')

def function5():
    if myplatform == 'android': # Android 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( 'https://thevideo.me/pair' ) )
    else:
        opensite = webbrowser . open('https://thevideo.me/pair')		
     
menuoptions()
