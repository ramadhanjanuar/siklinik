from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginform, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout', views.logout_views, name='logout'),
    path('user/', views.userview, name='user'),
    path('user/add', views.adduser, name='adduser'),
    path('user/edit/<id_user>', views.edituser, name='edituser'),
    path('user/delete/<id_user>', views.deleteuser , name='deleteuser'),
    path('role/', views.roleview, name='role'),
    path('role/add', views.addrole, name='addrole'),
    path('role/edit/<id_role>', views.editrole, name='editrole'),
    path('role/delete/<id_role>', views.deleterole, name='deleterole'),
    path('agama/', views.agamaview, name='agama'),
    path('agama/add', views.addagama, name='addagama'),
    path('agama/edit/<id_agama>', views.editagama, name='editagama'),
    path('agama/delete/<id_agama>', views.deleteagama, name='deleteagama'),
    path('jenis-kelamin/', views.jeniskelaminview, name='jeniskelamin'), #jeniskelamin
    path('jenis-kelamin/add', views.addjeniskelamin, name='addjeniskelamin'),
    path('jenis-kelamin/edit/<id_jk>', views.editjeniskelamin, name='editjeniskelamin'),
    path('jenis-kelamin/delete/<id_jk>', views.deletejeniskelamin, name='deletejeniskelamin'),
    path('pekerjaan/', views.pekerjaanview, name='pekerjaan'),
    path('pekerjaan/add', views.addpekerjaan, name='addpekerjaan'),
    path('pekerjaan/edit/<id_pekerja>', views.editpekerjaan, name='editpekerjaan'),
    path('pekerjaan/delete/<id_pekerja>', views.deletepekerjaan, name='deletepekerjaan'),
    path('pasien/', views.pasienview, name='pasien'),
    path('pasien/add', views.addpasien, name='addpasien'),
    path('pasien/edit/<id_pasien>', views.editpasien, name='editpasien'),
    path('pasien/delete/<id_pasien>', views.deletepasien, name='deletepasien'),
    path('kelompokpasien', views.kelompokpasienview, name='kelompokpasien'),#kelompokpasien
    path('kelompokpasien/add', views.addkelompokpasien, name='addkelompokpasien'),
    path('kelompokpasien/edit/<id_kelpasien>', views.editkelompokpasien, name='editkelompokpasien'),
    path('kelompokpasien/delete/<id_kelpasien>', views.deletekelompokpasien, name='deletekelompokpasien'),
    path('pegawai/', views.pegawaiview, name='pegawai'),
    path('pegawai/add', views.addpegawai, name='addpegawai'),
    path('pegawai/edit/<id_pegawai>', views.editpegawai, name='editpegawai'),
    path('pegawai/delete/<id_pegawai>', views.deletepegawai, name='deletepegawai'),
    path('kategori-pegawai/', views.kategoripegawaiview, name='kategoripegawai'), #kategori pegawai
    path('kategori-pegawai/add', views.addkategoripegawai, name='addkategoripegawai'),
    path('kategori-pegawai/edit/<id_kp>', views.editkategoripegawai, name='editkategoripegawai'),
    path('kategori-pegawai/delete/<id_kp>', views.deletekategoripegawai, name='deletekategoripegawai'),
    path('kategori-barang/', views.kategoribarangview, name='kategoribarang'),
    path('kategori-barang/add', views.addkategoribarang, name='addkategoribarang'),
    path('kategori-barang/edit/<id_kb>', views.editkategoribarang, name='editkategoribarang'),
    path('kategori-barang/delete/<id_kb>', views.deletekategoribarang, name='deletekategoribarang'),
    path('alatkesehatan', views.alatkesehatanview, name='alatkesehatan'),
    path('alatkesehatan/edit', views.editalatkesehatan, name='editalatkesehatan'),
    path('alatkesehatan/add', views.addalatkesehatan, name='addalatkesehatan'),
    path('farmasi/pemesanan/', views.farmasipemesananview, name='farmasipemesananview'),
    path('farmasi/pemesanan/form', views.farmasipemesanan, name='farmasipemesanan'),
    path('farmasi/penerimaan/', views.farmasipenerimaanview, name='farmasipenerimaanview'),
    path('farmasi/penerimaan/form', views.farmasipenerimaan, name='farmasipenerimaan'),
    path('farmasi/penjualan/', views.farmasipenjualanview, name='farmasipenjualanview'),
    path('farmasi/penjualan/form-non-resep', views.farmasipenjualan, name='farmasipenjualannonresep'),
    path('farmasi/penjualan/form', views.farmasipenjualanresep, name='farmasipenjualan'),
    path('kasir', views.kasir, name='kasir'),
    path('pemeriksaan', views.pemeriksaan, name='pemeriksaan'),
    path('pemeriksaan/add', views.addpemeriksaan, name='addpemeriksaan'),
    path('registrasi/', views.registrasi, name='registrasi'),
    path('registrasi/add', views.addregistrasi, name='addregistrasi'),
]
