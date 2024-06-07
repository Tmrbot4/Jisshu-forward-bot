from os import environ 

class Config:
    API_ID = environ.get("API_ID", "23171051")
    API_HASH = environ.get("API_HASH", "10331d5d712364f57ffdd23417f4513c")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7360215422:AAHUR79RpMmtCPxSjcR7PIUhRDUVibDzNto") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://tmr624062:Jishu123@cluster0.pvwfmfd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "Jishu")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '6987799874').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
