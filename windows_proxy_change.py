import ctypes
import winreg as winreg


def set_key(name, value):
    _, reg_type = winreg.QueryValueEx(INTERNET_SETTINGS, name)
    winreg.SetValueEx(INTERNET_SETTINGS, name, 0, reg_type, value)


INTERNET_SETTINGS = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
    r'Software\Microsoft\Windows\CurrentVersion\Internet Settings',
    0, winreg.KEY_ALL_ACCESS)

set_key('ProxyEnable', 1)
#set_key('ProxyOverride', u'*.local;<local>')  # Bypass the proxy for localhost
set_key('ProxyServer', u'222.124.130.197:4145')
INTERNET_OPTION_REFRESH = 37
INTERNET_OPTION_SETTINGS_CHANGED = 39

internet_set_option = ctypes.windll.Wininet.InternetSetOptionW

internet_set_option(0, INTERNET_OPTION_SETTINGS_CHANGED, 0, 0)
internet_set_option(0, INTERNET_OPTION_REFRESH, 0, 0)
