from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URL = "mongodb+srv://sakethsampath2006:VUwCGTAePmacqJry@cluster0.vu1gvgg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
MONGO_DB_NAME = 'fastapipractice'

client = AsyncIOMotorClient(MONGO_URL)
db = client[MONGO_DB_NAME]['users']

