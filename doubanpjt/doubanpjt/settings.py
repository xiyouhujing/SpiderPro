# -*- coding: utf-8 -*-

# Scrapy settings for doubanpjt project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'doubanpjt'

SPIDER_MODULES = ['doubanpjt.spiders']
NEWSPIDER_MODULE = 'doubanpjt.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'doubanpjt (+http://www.yourdomain.com)'

# Obey robots.txt rules
# ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'Accept': '*/*',
  'Accept-Language': 'zh-CN,zh;q=0.9',
  'Connection': 'keep-alive',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
  'Cookie': 'bid=jCQXRC57Mc0; __yadk_uid=LAdA5sJpOS271mLClXuolpmXOEffkeCs; ll="118254"; __utmc=30149280; _ga=GA1.2.727909837.1513079734; _gid=GA1.2.1640583283.1514190543; ps=y; push_noty_num=0; push_doumail_num=0; __utmv=30149280.14502; __utmz=30149280.1514191906.4.4.utmcsr=so.com|utmccn=(organic)|utmcmd=organic|utmctr=%E8%B1%86%E7%93%A3%E7%99%BB%E9%99%86%E9%A6%96%E9%A1%B5; ap=1; dbcl2="145022450:+ug3uUlWbIQ"; ck=r77U; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1514204734%2C%22http%3A%2F%2Fwww.so.com%2Flink%3Fm%3DaA6zjJDEouUB10NQ2SWfwHkVnsV4kNJHn%252BsxX7O8wGV%252ByBAYrYHQZ%252Beezm4NT3%252FG5LiV4P4AGK%252BK4usDr2VhN6B89jy%252FD%252FATH%22%5D; _pk_id.100001.8cb4=1ec82cc93e7c78e1.1513079732.5.1514204734.1514196357.; _pk_ses.100001.8cb4=*; __utma=30149280.727909837.1513079734.1514195137.1514204734.6; __utmt=1; __utmb=30149280.2.10.1514204734',
}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'doubanpjt.middlewares.DoubanpjtSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'doubanpjt.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    'doubanpjt.pipelines.DoubanpjtPipeline': 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
