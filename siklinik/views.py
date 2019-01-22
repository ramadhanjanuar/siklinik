from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.forms import modelform_factory
from django import forms
import datetime

from .models import Pasien, Kategori_Barang, Pasien, AuthUser, Role,//
Pegawai, Agama, Jenis_Kelamin, Pekerjaan, Kategori_Pegawai, Kelompok_Pasien
from .forms import LoginForm, UserForm, UmumForm, RoleForm, PasienForm, PegawaiForm


User = get_user_model()

# Create your views here.
def index(request):
    return HttpResponse("hai")

def dashboard(request):
    return render(request, 'siklinik/dashboard.html')

# USER
def loginform(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['username']
            passw = form.cleaned_data['password']
            user = authenticate(username=user, password=passw)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
    else:
        form = LoginForm()

    context = {'form':form}
    return render(request, 'siklinik/login.html', context)

def logout_views(request):
    logout(request)
    return redirect('login')



@login_required
def userview(request):
    users = AuthUser.objects.order_by()
    context = {'users' : users}
    return render(request,'siklinik/view_user.html', context)

@login_required
def adduser(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('user')
    else:
        form = UserForm()
    context = {'form':form}
    return render(request, 'siklinik/form_add_user.html', context)

@login_required
def edituser(request, id_user):
    user = AuthUser.objects.get(pk=id_user)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('user')

    elif request.method == 'GET':
        form = UserForm(instance = user)

    else:
        form = UserForm()

    contex = {'form':form}
    return render(request, 'siklinik/form_edit_user.html', contex)

def deleteuser(request, id_user):
    deluser = AuthUser.objects.get(pk=id_user)
    if id_user == '1':
        return redirect('user')
    else:
        deluser.delete()
    return redirect('user')


##############################################################
# ROLE

def roleview(request):
    form = RoleForm()
    roles = Role.objects.all()
    contex = {'form':form, 'roles':roles}
    return render(request, 'siklinik/view_role.html', contex)

def addrole(request):
    if request.method == 'POST':
        form = RoleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('role')
    else:
        form = RoleForm()

    contex = {'form':form,}
    return render(request, 'siklinik/form_add_role.html', contex)

def editrole(request, id_role):
    role = Role.objects.get(pk=id_role)
    if request.method == 'POST':
        form = RoleForm(request.POST, instance=role)
        if form.is_valid():
            form.save()
            return redirect('role')
    else:
        form = RoleForm(instance=role)

    contex = {'form': form, 'role':role}
    return render(request, 'siklinik/form_edit_role.html', contex)

def deleterole(request, id_role):
    role = Role.objects.get(pk=id_role)
    role.delete()
    return redirect('role')


##############################################################
# AGAMA

def agamaview(request):
    agamas = Agama.objects.all()
    contex = {'agamas' : agamas}
    return render(request, 'siklinik/view_agama.html', contex)

def addagama(request):
    if request.method == 'POST':
        Form = modelform_factory(Agama, form = UmumForm)
        form = Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agama')
    else:
        form = Form = modelform_factory(Agama, form = UmumForm)

    contex = {'form':form}
    return render(request, 'siklinik/form_add_agama.html', contex)

def editagama(request, id_agama):
    agama = Agama.objects.get(pk=id_agama)
    if request.method == 'POST':
        Form = modelform_factory(Agama, form = UmumForm)
        form = Form(request.POST, instance=agama)
        if form.is_valid():
            form.save()
            return redirect('agama')
    else:
        Form = modelform_factory(Agama, form = UmumForm)
        form = Form(instance=agama)

    contex = {'form': form, 'agama':agama}
    return render(request, 'siklinik/form_edit_agama.html', contex)

def deleteagama(request, id_agama):
    agama = Agama.objects.get(pk=id_agama)
    agama.delete()
    return redirect('agama')


##############################################################
# JENIS KELAMIN

def jeniskelaminview(request):
    jeniskelamin = Jenis_Kelamin.objects.all()
    contex = {'jeniskelamin' : jeniskelamin}
    return render(request, 'siklinik/view_jk.html', contex)

def addjeniskelamin(request):
    if request.method == 'POST':
        Form = modelform_factory(Jenis_Kelamin, fields=['nama'])
        form = Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('jeniskelamin')
    else:
        #form = modelform_factory(Jenis_Kelamin, fields=['nama'],widgets={'nama': forms.TextInput(attrs={'placeholder': 'Masukan Jenis Kelamin','class':'form-control'})})
        form = modelform_factory(Jenis_Kelamin, form=UmumForm)
    contex = {'form':form}
    return render(request, 'siklinik/form_add_jk.html', contex)

def editjeniskelamin(request, id_jk):
    jk = Jenis_Kelamin.objects.get(pk=id_jk)
    if request.method == 'POST':
        Form = modelform_factory(Jenis_Kelamin, form=UmumForm)
        form = Form(request.POST, instance=jk)
        if form.is_valid():
            form.save()
            return redirect('jeniskelamin')
    else:
        Form = modelform_factory(Jenis_Kelamin, form=UmumForm)
        form = Form(instance=jk)
        contex = {'form':form, 'jk':jk}
    return render(request,'siklinik/form_edit_jk.html', contex)

def deletejeniskelamin(request, id_jk):
    jk = Jenis_Kelamin.objects.get(pk=id_jk)
    jk.delete()
    return redirect('jeniskelamin')


##############################################################
# PEKERJAAN

def pekerjaanview(request):
    pekerjaan = Pekerjaan.objects.all()
    contex = {'pekerjaan':pekerjaan}
    return render(request, 'siklinik/view_pekerjaan.html', contex)

def addpekerjaan(request):
    if request.method == 'POST':
        Form = modelform_factory(Pekerjaan, form=UmumForm)
        form = Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pekerjaan')
    else:
        form = modelform_factory(Pekerjaan, form=UmumForm)

    contex = {'form':form}
    return render(request, 'siklinik/form_add_pekerjaan.html', contex)

def editpekerjaan(request, id_pekerja):
    pekerjaan = Pekerjaan.objects.get(pk=id_pekerja)
    if request.method == 'POST':
        Form = modelform_factory(Pekerjaan, form=UmumForm)
        form = Form(request.POST, instance=pekerjaan)
        if form.is_valid:
            form.save()
            return redirect('pekerjaan')
    else:
        Form = modelform_factory(Pekerjaan, form=UmumForm)
        form = Form(instance=pekerjaan)


    contex = {'pekerja':pekerjaan, 'form' : form}
    return render(request, 'siklinik/form_edit_pekerjaan.html', contex)

def deletepekerjaan(request, id_pekerja):
    pekerjaan = Pekerjaan.objects.get(pk=id_pekerja)
    pekerjaan.delete()
    return redirect('pekerjaan')



##############################################################
# PASIEN

def pasienview(request):
    pasiens = Pasien.objects.all()
    context = {'pasiens' : pasiens}
    return render(request, 'siklinik/view_pasien.html', context)

def addpasien(request):
    if request.method == 'POST':
        form = PasienForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pasien')
    else:
        form = PasienForm()

    context = {'form' : form}
    return render(request, 'siklinik/form_add_pasien.html', context)

def editpasien(request, id_pasien):
    pasien = Pasien.objects.get(pk=id_pasien)
    if request.method == 'POST':
        form = PasienForm(request.POST, instance=pasien)
        if form.is_valid():
            form.save()
            return redirect('pasien')
    else:
        form = PasienForm(instance=pasien)

    context = {'form' : form, 'pasien':pasien}
    return render(request, 'siklinik/form_edit_pasien.html', context)

def deletepasien(request, id_pasien):
    pasien = Pasien.objects.get(pk=id_pasien)
    pasien.delete()
    return redirect('pasien')




##############################################################
# KELOMPOK PASIEN

def kelompokpasienview(request):
    kelpas = Kelompok_Pasien.objects.all()
    context = {'kelpas' : kelpas}
    return render(request, 'siklinik/view_kelPasien.html', context)

def addkelompokpasien(request):
    if request.method == 'POST':
        Form = modelform_factory(Kelompok_Pasien, form=UmumForm)
        form = Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('kelompokpasien')
    else:
        form = modelform_factory(Kelompok_Pasien, form=UmumForm)

    context = {'form' : form}
    return render(request, 'siklinik/form_add_kelpasien.html', context)

def editkelompokpasien(request, id_kelpasien):
    kelpas = Kelompok_Pasien.objects.get(pk=id_kelpasien)
    if request.method == 'POST':
        Form = modelform_factory(Kelompok_Pasien, form = UmumForm)
        form = Form(request.POST, instance = kelpas)
        if form.is_valid():
            form.save()
            return redirect('kelompokpasien')
    else:
        form = modelform_factory(Kelompok_Pasien, form=UmumForm)
        form = form(instance=kelpas)

    context = {'form' : form, 'kelpas' : kelpas}
    return render(request, 'siklinik/form_edit_kelpasien.html', context)

def deletekelompokpasien(request, id_kelpasien):
    kelpas = Kelompok_Pasien.objects.get(pk=id_kelpasien)
    kelpas.delete()
    return redirect('kelompokpasien')



##############################################################
# PEGAWAI

def pegawaiview(request):
    pegawai = Pegawai.objects.all()
    context = {'pegawai':pegawai}

    return render(request, 'siklinik/view_pegawai.html',context)

def addpegawai(request):
    if request.method == 'POST':
        form = PegawaiForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pegawai')
    else:
        form = PegawaiForm()

    context = {'form':form}
    return render(request, 'siklinik/form_add_pegawai.html', context)

def editpegawai(request, id_pegawai):
    pegawai = Pegawai.objects.get(pk=id_pegawai)
    if request.method == 'POST':
        form = PegawaiForm(request.POST, instance = pegawai)
        if form.is_valid():
            form.save()
            return redirect('pegawai')
    else:
        form = PegawaiForm(instance=pegawai)

    context = {'form' : form, 'pegawai' : pegawai}
    return render(request, 'siklinik/form_edit_pegawai.html', context)

def deletepegawai(request, id_pegawai):
    pegawai = Pegawai.objects.get(pk=id_pegawai)
    pegawai.delete()
    return redirect('pegawai')




##############################################################
# KATEGORI PEGAWAI

def kategoripegawaiview(request):
    kpegawai = Kategori_Pegawai.objects.all()
    contex = {'kpegawai': kpegawai}
    return render(request, 'siklinik/view_ketPegawai.html', contex)

def addkategoripegawai(request):
    if request.method == 'POST':
        Form = modelform_factory(Kategori_Pegawai, form=UmumForm)
        form = Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('kategoripegawai')
    else:
        form = modelform_factory(Kategori_Pegawai, form=UmumForm)

    contex = {'form' : form}
    return render(request, 'siklinik/form_add_ketPegawai.html', contex)

def editkategoripegawai(request, id_kp):
    return render(request, 'siklinik/form_edit_ketPegawai.html')

def deletekategoripegawai(request, id_kp):
    kpegawai = Kategori_Pegawai.objects.get(pk=id_kp)
    kpegawai.delete()
    return redirect('kategoripegawai')


################################################################################
#kategori barang

def kategoribarangview(request):
    kbarang = Kategori_Barang.objects.all()
    context = {'kategoribarang':kbarang}
    return render(request, 'siklinik/view_katbarang.html', context)

def addkategoribarang(request):
    if request.method == 'POST':
        Form = modelform_factory(Kategori_Barang, form = UmumForm)
        form = Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('kategoribarang')
    else:
        form = modelform_factory(Kategori_Barang, form = UmumForm)

    context = {'form': form}
    return render(request, 'siklinik/form_add_katbarang.html', context)

def editkategoribarang(request, id_kb):
    kbarang = Kategori_Barang.objects.get(pk=id_kb)
    if request.method == 'POST':
        Form = modelform_factory(Kategori_Barang, form = UmumForm)
        form = Form(request.POST, instance = kbarang)
        if form.is_valid():
            form.save()
            return redirect('kategoribarang')
    else:
        Form = modelform_factory(Kategori_Barang, form = UmumForm)
        form = Form(instance=kbarang)

    context = {'form' : form, 'kbarang' : kbarang}
    return render(request, 'siklinik/form_edit_katbarang.html', context)

def deletekategoribarang(request, id_kb):
    kbarang = Kategori_Barang.objects.get(pk=id_kb)
    kbarang.delete()
    return redirect('kategoribarang')

################################################################################
#alat kesehatan

def alatkesehatanview(request):
    return render(request, 'siklinik/view_alkes.html')

def addalatkesehatan(request):
    return render(request, 'siklinik/form_add_alkes.html')

def editalatkesehatan(request):
    return render(request, 'siklinik/form_edit_alkes.html')

##########
#farmasi
def farmasipemesanan(request):
    return render(request, 'farmasi/pemesanan/form-create.html')

def farmasipemesananview(request):
    return render(request, 'farmasi/pemesanan/list.html')

def farmasipenerimaan(request):
    return render(request, 'farmasi/penerimaan/form-create.html')

def farmasipenerimaanview(request):
    return render(request, 'farmasi/penerimaan/list.html')

def farmasipenjualan(request):
    return render(request, 'farmasi/penjualan/form-create-non-resep.html')

def farmasipenjualanresep(request):
    return render(request, 'farmasi/penjualan/form-create.html')

def farmasipenjualanview(request):
    return render(request, 'farmasi/penjualan/list.html')

def kasir(request):
    return render(request, 'kasir/list.html')

def pemeriksaan(request):
    return render(request, 'pemeriksaan/list.html')

def addpemeriksaan(request):
    return render(request, 'pemeriksaan/form-create.html')

def registrasi(request):
    return render(request, 'registrasi/list.html')

def addregistrasi(request):
    return render(request, 'registrasi/form.html')
