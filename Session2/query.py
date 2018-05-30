from models.service import *
import mlab

mlab.connect()

id_service = "5af5a7b29f880b0dc1b8803d"

# hera = Service.objects(id = id_service)
# hera2 = Service.objects.get(id = id_service)
hera3 = Service.objects.with_id(id_service)

if hera3 is not None:
    # hera3.delete()
    hera3.update(set__address = "Nguyễn Thị Định", set__name="Vũ Viết Cảnh")
    hera3.reload()
    print(hera3.address)
    print(hera3.name)
else:
    print("Không tìm thấy dữ liệu bạn cần xóa !")

# hera3.delete()

# print(hera3.to_mongo())

# all_service = Service.objects(gender=1) # Có thể filter dữ liệu tại đây !

# fist_service = all_service[0]

# for index, service in enumerate(all_service):
#     print(service["name"])
#     print(service["gender"])
#     if index == 9:
#         break
