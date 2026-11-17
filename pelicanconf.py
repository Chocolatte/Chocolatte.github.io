AUTHOR = 'Zoltan Kubat'
SITENAME = 'Zoltan Kubat — Product Manager'
SITEURL = ''

PATH = 'content'
TIMEZONE = 'Europe/London'
DEFAULT_LANG = 'en'

THEME = 'themes/minimal'

# Pages in nav
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False

# No feeds for now
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 5

STATIC_PATHS = ['images']

SOCIAL = (
    ('LinkedIn', 'https://www.linkedin.com/in/zoltan-kubat-478461104'),
    ('Email', 'mailto:kubat.zoltan@icloud.com'),
)

# ── PM Toolkit membership ────────────────────────────────────────────────
# Paste your checkout links here once your payment account is set up
# (e.g. Lemon Squeezy or Gumroad subscription links). While they are empty,
# the buttons on the Toolkit page fall back to a "join the waitlist" email.
TOOLKIT_PRICE_MONTHLY = '€9'
TOOLKIT_PRICE_YEARLY = '€90'
TOOLKIT_CHECKOUT_MONTHLY = ''
TOOLKIT_CHECKOUT_YEARLY = ''
TOOLKIT_CONTACT_EMAIL = 'kubat.zoltan@icloud.com'
