'''Copy local browser headers and it in driver arguments and then make the request'''
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options=Options()
options.add_argument("accept=*/*")
options.add_argument("accept-encoding=gzip, deflate, br, zstd")
options.add_argument("accept-language=en-US,en;q=0.9")
options.add_argument("content-length=0")
options.add_argument("cookie=ar_debug=1")
options.add_argument("origin=https://www.health.mil")
options.add_argument("priority=u=1, i")
options.add_argument("referer=https://www.health.mil/")
options.add_argument('sec-ch-ua="Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"')
options.add_argument("sec-ch-ua-mobile=?0")
options.add_argument('sec-ch-ua-platform="Windows"')
options.add_argument("sec-fetch-dest=empty")
options.add_argument("sec-fetch-mode=no-cors")
options.add_argument("sec-fetch-site=cross-site")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36")

# Additional options to handle Google Analytics request (as an example)
options.add_argument("authority=www.google-analytics.com")
options.add_argument("method=POST")
options.add_argument("path=/g/collect?v=2&tid=G-CSLL4ZEK4L&gtm=45je4al0v9131934939za200&_p=1729749723213&gcd=13l3l3l3l1l1&npa=0&dma=0&tag_exp=101686685~101794737~101823848&cid=2043967838.1725874913&ul=en-us&sr=1536x864&uaa=x86&uab=64&uafvl=Chromium%3B130.0.6723.69%7CGoogle%2520Chrome%3B130.0.6723.69%7CNot%253FA_Brand%3B99.0.0.0&uamb=0&uam=&uap=Windows&uapv=10.0.0&uaw=0&are=1&frm=0&pscdl=noapi&_s=1&dl=https%3A%2F%2Fwww.health.mil%2Fabout-mhs%2Foasdha%2Fdefense-health-agency%2Fdha-office-of-the-inspector-general%2Ffraud-and-abuse%2Fexcluded-providers&dt=Excluded%20Providers%20%7C%20Health.mil&sid=1729749711&sct=11&seg=1&en=page_view&_ee=1&ep.agency=DOD&ep.subagency=MHS&ep.site_topic=unspecified%3Ahealth.mil&ep.site_platform=unspecified%3Ahealth.mil&ep.script_source=https%3A%2F%2Fdap.digitalgov.gov%2Funiversal-federated-analytics-min.js&ep.version=20240925%20v8.3%20-%20ga4&ep.protocol=https%3A&ep.using_parallel_tracker=no&tfd=8155")
options.add_argument("scheme=https")

# Set up the WebDriver with the configured options
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Example usage
driver.get('https://www.health.mil')
