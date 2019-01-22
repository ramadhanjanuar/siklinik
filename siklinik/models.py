from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

from django.utils import timezone


class Role(models.Model):
    nama = models.CharField(max_length=25)

    def __str__(self):
        return self.nama

class Pekerjaan(models.Model):
    nama = models.CharField(max_length=90)

    def __str__(self):
        return self.nama


class Wilayah(models.Model):
    nama = models.CharField(max_length=90)
    kodepos = models.IntegerField()

    def __str__(self):
        return self.nama


class Agama(models.Model):
    nama = models.CharField(max_length=90)

    def __str__(self):
        return self.nama


class Kategori_Pegawai(models.Model):
    nama = models.CharField(max_length=90)

    def __str__(self):
        return self.nama


class Jenis_Kelamin(models.Model):
    nama = models.CharField(max_length=90)

    def __str__(self):
        return self.nama

class Pegawai(models.Model):
    nama = models.CharField(max_length=90)
    jk = models.ForeignKey(Jenis_Kelamin, on_delete=models.CASCADE)
    kp = models.ForeignKey(Kategori_Pegawai, on_delete=models.CASCADE)
    agama = models.ForeignKey(Agama, on_delete=models.CASCADE)
    tempat_lahir = models.CharField(max_length=25)
    tangal_lahir = models.DateField()
    alamat = models.TextField()
    rt = models.CharField(max_length=5)
    rw = models.CharField(max_length=5)
    kodepos = models.IntegerField()
    telepon = models.CharField(max_length=25)
    status_kawin = models.CharField(max_length=12)

    def __str__(self):
        return self.nama


class Rekam_Medis(models.Model):
    diagnosa = models.CharField(max_length=90)
    keterangan_diagnosa = models.TextField()


class Kategori_Barang(models.Model):
    nama = models.CharField(max_length=90)

    def __str__(self):
        return self.nama

class Obat(models.Model):
    kb = models.ForeignKey(Kategori_Barang, on_delete=models.CASCADE)
    nama = models.CharField(max_length=90)
    harga_dasar = models.DecimalField(max_digits=15, decimal_places=2)
    harga_beli = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return self.nama


class Alat_Kesehatan(models.Model):
    kb =models.ForeignKey(Obat, on_delete=models.CASCADE)
    nama = models.CharField(max_length=90)
    harga_dasar = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return self.nama


class Kelompok_Pasien(models.Model):
    nama = models.CharField(max_length=90)
    margin = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return self.nama


class Pasien(models.Model):
    jk = models.ForeignKey(Jenis_Kelamin, on_delete=models.CASCADE)
    kelpas = models.ForeignKey(Kelompok_Pasien, on_delete=models.CASCADE, default='')
    pekerjaan = models.ForeignKey(Pekerjaan, on_delete=models.CASCADE)
    agama = models.ForeignKey(Agama, on_delete=models.CASCADE)
    nama = models.CharField(max_length=90)
    tempat_lahir = models.CharField(max_length=25)
    tangal_lahir = models.DateField()
    alamat = models.TextField()
    rt = models.CharField(max_length=5)
    rw = models.CharField(max_length=5)
    kodepos = models.IntegerField()
    telepon = models.CharField(max_length=25)
    status_kawin = models.CharField(max_length=12)

    def __str__(self):
        return self.nama


class Registrasi(models.Model):
    kelpasien = models.ForeignKey(Kelompok_Pasien, on_delete=models.CASCADE, default='')
    pegawai = models.ForeignKey(Pegawai, on_delete=models.CASCADE)
    pasien = models.ForeignKey(Pasien, on_delete=models.CASCADE)
    tanggal = models.DateField()
    no_register = models.CharField(max_length=90)
    no_antrian = models.IntegerField()



class Harga_Jual(models.Model):
    alkes = models.ForeignKey(Alat_Kesehatan, on_delete=models.CASCADE)
    obat = models.ForeignKey(Obat, on_delete=models.CASCADE)
    kelpas = models.ForeignKey(Kelompok_Pasien, on_delete=models.CASCADE)
    harga = models.DecimalField(max_digits=15, decimal_places=2)
    harga_beli = models.DecimalField(max_digits=15, decimal_places=2)


class Farmasi(models.Model):
    registrasi = models.ForeignKey(Registrasi, on_delete=models.CASCADE)
    type = models.IntegerField()
    tanggal = models.DateField()
    no_transaksi = models.CharField(max_length=90)
    diskon = models.DecimalField(max_digits=3, decimal_places=2)
    total = models.DecimalField(max_digits=15, decimal_places=2)


class Farmasi_Detail(models.Model):
    farmasi = models.ForeignKey(Farmasi, on_delete=models.CASCADE)
    harga = models.DecimalField(max_digits=15, decimal_places=2)
    qty = models.IntegerField()
    diskon = models.DecimalField(max_digits=3, decimal_places=2)
    total = models.DecimalField(max_digits=3, decimal_places=2)


class Resep(models.Model):
    registrasi = models.ForeignKey(Registrasi, on_delete=models.CASCADE)
    tanggal = models.DateField()
    no_resep = models.CharField(max_length=90)


class Kasir(models.Model):
    registrasi = models.ForeignKey(Registrasi, on_delete=models.CASCADE)
    no_kwitansi = models.CharField(max_length=90)
    total = models.DecimalField(max_digits=15, decimal_places=2)


class Tindakan(models.Model):
    nama = models.CharField(max_length=90)
    harga = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return self.nama


class Transaksi(models.Model):
    obat = models.ForeignKey(Obat, on_delete=models.CASCADE)
    tindakan = models.ForeignKey(Tindakan, on_delete=models.CASCADE)
    registrasi = models.ForeignKey(Registrasi, on_delete=models.CASCADE)
    alkes = models.ForeignKey(Alat_Kesehatan, on_delete=models.CASCADE)
    qty = models.IntegerField()
    harga = models.DecimalField(max_digits=15, decimal_places=2)
    total = models.DecimalField(max_digits=15, decimal_places=2)
    jenis_tindakan = models.IntegerField()
    status = models.IntegerField()


class AuthUser(AbstractUser):
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True)
    pegawai = models.ForeignKey(Pegawai, on_delete=models.CASCADE, null=True)
