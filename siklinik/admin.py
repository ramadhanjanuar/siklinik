from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import AuthUser, Role, Pegawai,Jenis_Kelamin, Wilayah, Pekerjaan, Agama, Kategori_Pegawai

# Register your models here.
admin.site.register(AuthUser, UserAdmin)
admin.site.register(Role)
admin.site.register(Pegawai)
admin.site.register(Jenis_Kelamin)
admin.site.register(Wilayah)
admin.site.register(Pekerjaan)
admin.site.register(Agama)
admin.site.register(Kategori_Pegawai)

