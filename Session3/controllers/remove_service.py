from configs.db_config import connect
from models.service import Service
connect()
all_service = Service.objects()

def xoa():
    all_service.delete()