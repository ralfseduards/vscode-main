from selenium import webdriver
from selenium.webdriver.safari.options import Options
from selenium.webdriver.support.ui import WebDriverWait

# configure the webdriver
options = Options()
options.headless = True # hides the gui
options.add_argument("--window-size=1920,1080") # sets window size to the native gui size
options.add_argument("start-maximized") # ensures the window is fullscreen

# images and js are useless, so:
# safari_options = webdriver.r()

driver = webdriver.Safari(options=options) # activate the options
driver.get("https://www.twitch.tv/directory/game/Chess")