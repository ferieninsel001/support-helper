import os
import shutil
import psutil
import sys

BROWSER_PATHS = {
    'chrome': {
        'cache': r'C:\Users\{username}\AppData\Local\Google\Chrome\User Data\Default\Cache',
        'history': r'C:\Users\{username}\AppData\Local\Google\Chrome\User Data\Default\History',
        'process_name': 'chrome.exe'
    },
    'firefox': {
        'cache': r'C:\Users\{username}\AppData\Local\Mozilla\Firefox\Profiles\{profile}\cache2',
        'history': r'C:\Users\{username}\AppData\Roaming\Mozilla\Firefox\Profiles\{profile}\places.sqlite',
        'process_name': 'firefox.exe'
    },
    'edge': {
        'cache': r'C:\Users\{username}\AppData\Local\Microsoft\Edge\User Data\Default\Cache',
        'history': r'C:\Users\{username}\AppData\Local\Microsoft\Edge\User Data\Default\History',
        'process_name': ['msedge.exe', 'edge.exe']  # Edge can run under multiple process names
    },
    'opera': {
        'cache': r'C:\Users\{username}\AppData\Local\Opera Software\Opera Stable\Cache',
        'history': r'C:\Users\{username}\AppData\Roaming\Opera Software\Opera Stable\History',
        'process_name': 'opera.exe'
    },
    'brave': {
        'cache': r'C:\Users\{username}\AppData\Local\BraveSoftware\Brave-Browser\User Data\Default\Cache',
        'history': r'C:\Users\{username}\AppData\Local\BraveSoftware\Brave-Browser\User Data\Default\History',
        'process_name': 'brave.exe'
    },
}

def is_browser_open(browser_name):
    process_names = BROWSER_PATHS[browser_name]['process_name']
    if isinstance(process_names, str):
        process_names = [process_names]  # Ensure it's a list for consistency

    for proc in psutil.process_iter(['name']):
        if proc.info['name'].lower() in [name.lower() for name in process_names]:
            return True
    return False

def clear_cache(browser_name, username, profile=None):
    cache_path = BROWSER_PATHS[browser_name]['cache'].format(username=username, profile=profile or '')
    if os.path.exists(cache_path):
        shutil.rmtree(cache_path)
        print(f"{browser_name.capitalize()} cache cleared!")
    else:
        print(f"{browser_name.capitalize()} cache folder not found!")

def clear_history(browser_name, username, profile=None):
    history_path = BROWSER_PATHS[browser_name]['history'].format(username=username, profile=profile or '')
    if os.path.exists(history_path):
        os.remove(history_path)
        print(f"{browser_name.capitalize()} history cleared!")
    else:
        print(f"{browser_name.capitalize()} history file not found!")

def clear_browser_data(username):
    firefox_profiles_dir = f'C:\\Users\\{username}\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles'
    
    for browser in BROWSER_PATHS:
        if is_browser_open(browser):
            print(f"{browser.capitalize()} is currently open. Please close it before running this script.")
            continue
        if browser == 'firefox' and os.path.exists(firefox_profiles_dir):
            for profile in os.listdir(firefox_profiles_dir):
                if os.path.isdir(os.path.join(firefox_profiles_dir, profile)):
                    print(f"Clearing data for Firefox profile: {profile}")
                    clear_cache('firefox', username, profile)
                    clear_history('firefox', username, profile)
        else:
            clear_cache(browser, username)
            clear_history(browser, username)

username = os.getlogin()
clear_browser_data(username)
