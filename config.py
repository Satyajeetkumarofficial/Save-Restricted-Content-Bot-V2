# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# wtite up here insta cookies
"""

# YouTube cookies
YTUB_COOKIES = """# Netscape HTTP Cookie File
# https://curl.haxx.se/rfc/cookie_spec.html
# This is a generated file! Do not edit.

.youtube.com	TRUE	/	TRUE	1800759127	PREF	tz=Asia.Calcutta
.youtube.com	TRUE	/	TRUE	1797508493	__Secure-1PSIDTS	sidts-CjUBflaCdXGhRXOy9EA4BGxJn7p5ix3PT50hSlii6GsYTsMpyukzvcrlQqBFRd-VmnX8xwTEZxAA
.youtube.com	TRUE	/	TRUE	1797508493	__Secure-3PSIDTS	sidts-CjUBflaCdXGhRXOy9EA4BGxJn7p5ix3PT50hSlii6GsYTsMpyukzvcrlQqBFRd-VmnX8xwTEZxAA
.youtube.com	TRUE	/	FALSE	1800532493	HSID	AGFmUqtkswLwQU8wZ
.youtube.com	TRUE	/	TRUE	1800532493	SSID	ApgkP86RrWnN4ci7E
.youtube.com	TRUE	/	FALSE	1800532493	APISID	m7icKXv2LJuCd2AC/AYzmrXMV90Dmy3bIb
.youtube.com	TRUE	/	TRUE	1800532493	SAPISID	boTuDkSr5EKLqx-i/AHnzaEEwfMcIqGtYM
.youtube.com	TRUE	/	TRUE	1800532493	__Secure-1PAPISID	boTuDkSr5EKLqx-i/AHnzaEEwfMcIqGtYM
.youtube.com	TRUE	/	TRUE	1800532493	__Secure-3PAPISID	boTuDkSr5EKLqx-i/AHnzaEEwfMcIqGtYM
.youtube.com	TRUE	/	FALSE	1800532493	SID	g.a0004gj9jZNnWwgyuezKZiIyBO4LtO3KQZDQuctcbpY45hxwTr_r8vTR3eNhzAoeKgl5gD-psQACgYKARQSARYSFQHGX2Micn8b41cTiVTc_YMwOfYaxRoVAUF8yKpBsz8DOB_h-pG4BOpr9Ggs0076
.youtube.com	TRUE	/	TRUE	1800532493	__Secure-1PSID	g.a0004gj9jZNnWwgyuezKZiIyBO4LtO3KQZDQuctcbpY45hxwTr_r-L0HvsgweSStoGkhjW8xoQACgYKATQSARYSFQHGX2MiE1j6ITv0CFS6SX_R5AuMtBoVAUF8yKrWmx0yqno9g9eGlV4YCAGP0076
.youtube.com	TRUE	/	TRUE	1800532493	__Secure-3PSID	g.a0004gj9jZNnWwgyuezKZiIyBO4LtO3KQZDQuctcbpY45hxwTr_r3Tnsp_myrgZO8DgVDAPS9AACgYKAcISARYSFQHGX2MiiOxSSGYIUL9bm751gVPWahoVAUF8yKpGnNzqfKiKAzOMvDafTAeU0076
.youtube.com	TRUE	/	TRUE	1800532592	LOGIN_INFO	AFmmF2swRQIhAJgdCcarjQP5bUge1b9-30jGC0cPNIg1acKqVqli-Wk5AiBnHxA_iBX5VUU6UzzWVAzaq7AqA6qxU43fbYHKaDeG-Q:QUQ3MjNmeGxicno1OU5iem1FMG12ZS1lNVI2YUxCN0NzQkxVZHB1TWRlWjlmNUNvaTladmprT2RvTVZ4M1ZlM1IwVDJtcVE5Z1ZBYjNDbTlTSm56QlQ4SXcxWmJUdmlSV1hXaERpYWpXQnkyMXU0U1laUDg2aF9FeUtpRllkbC12czk2VDhNTmlEeHUtXzFtcEZZZlFjSmZsbFVNUi01RGpR
.youtube.com	TRUE	/	TRUE	1766199713	CONSISTENCY	APeVyi-vzFF4rs01YVxyO48ghQxcTx9If-Qd5hiIl0EI7ddmNVEctMBACuRtfRkMzsMBDkJuJ-vi6BED5_TB-793fpYFiYfyPSpC1xlllhb9L91S9KgEL2qjVUo
.youtube.com	TRUE	/	FALSE	1797735148	SIDCC	AKEyXzU7MbE-Wr5xjze86atRYuVUlsSSqC4TIwgMJ0Uzr04sTrVLGv6a04zSB5KuR3hQ6rZN
.youtube.com	TRUE	/	TRUE	1797735148	__Secure-1PSIDCC	AKEyXzXbzcDB_h2XFA3rsOETSOXBpfPbL-4HEs9Zc1bgTqTWZBnOuAqWdumsd-LzrgBq8zV2Ag
.youtube.com	TRUE	/	TRUE	1797735148	__Secure-3PSIDCC	AKEyXzV05WbXqiNmbCpaNM2tOAGR65SAZUpr-c4bbnNIEWO9lqA11c65Xk2YfRwe4yb1B21Y"""

API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH", "")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = list(map(int, getenv("OWNER_ID", "").split()))
MONGO_DB = getenv("MONGO_DB", "")
LOG_GROUP = getenv("LOG_GROUP", "")
CHANNEL_ID = int(getenv("CHANNEL_ID", ""))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "5"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "500"))
WEBSITE_URL = getenv("WEBSITE_URL", "")
AD_API = getenv("AD_API", "")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", YTUB_COOKIES)
DEFAULT_SESSION = getenv("DEFAUL_SESSION", None)  # added old method of invite link joining
INSTA_COOKIES = getenv("INSTA_COOKIES", INST_COOKIES)
