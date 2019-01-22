from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Agama, AuthUser, Role, Pegawai, Pekerjaan, Pasien, Kategori_Pegawai, Kelompok_Pasien, Jenis_Kelamin, Agama
import datetime

class LoginForm(forms.Form):
    username = forms.CharField(max_length=40 , widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'username', 'name' : 'username', 'id' : 'id_username'}))
    password = forms.CharField(max_length=40 , widget=forms.PasswordInput(attrs={'class' : 'form-control', 'placeholder' : 'password','name' : 'password', 'id' : 'id_password'}))


class UserForm(UserCreationForm):

    pilihan_role = Role.objects.all()
    pilihan_pegawai = Pegawai.objects.all()

    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Masukan Username Anda', 'required': '', 'autofocus':''}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Masukan Nama Depan Anda', 'required': ''}), max_length=32)
    last_name=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Masukan Nama Belakang Anda', 'required': ''}), max_length=32)
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password Again'}))
    role = forms.ModelChoiceField(pilihan_role, widget=forms.Select(attrs={'class': 'form-control'}))
    pegawai = forms.ModelChoiceField(pilihan_pegawai,widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta(UserCreationForm.Meta):
        model = AuthUser
        # I've tried both of these 'fields' declaration, result is the same
        # fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'role', 'pegawai')


class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = ['nama']
        widgets = {
            'nama' : forms.TextInput(
                attrs={'class':'form-control', 'placeholder':'Masukan nama Role', 'required' : 'required'}
            )
        }

class UmumForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        widgets = {
            'nama' : forms.TextInput(
                attrs={'class':'form-control', 'placeholder':'Tulis disini', 'required' : 'required'}
            ),
            'margin' : forms.TextInput(
                attrs={'class':'form-control', 'placeholder':'Tulis disini', 'required' : 'required'}
            ),
        }

class PasienForm(forms.ModelForm):
    pilihan_agama = Agama.objects.all()
    pilihan_jk = Jenis_Kelamin.objects.all()
    pilihan_pekerjaan = Pekerjaan.objects.all()
    pilihan_kelpas = Kelompok_Pasien.objects.all()

    agama = forms.ModelChoiceField(pilihan_agama,widget=forms.Select(attrs={'class': 'form-control'}))
    jk = forms.ModelChoiceField(pilihan_jk,widget=forms.Select(attrs={'class': 'form-control'}))
    pekerjaan = forms.ModelChoiceField(pilihan_pekerjaan,widget=forms.Select(attrs={'class': 'form-control'}))
    kelpas = forms.ModelChoiceField(pilihan_kelpas,widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Pasien
        fields = '__all__'
        widgets = {
            'nama' : forms.TextInput(
                attrs={'class':'form-control', 'placeholder':'Tulis disini', 'required' : 'required'}
            ),
            'tempat_lahir' : forms.TextInput(
                attrs={'class':'form-control', 'placeholder':'Tulis disini', 'required' : 'required'}
            ),
            'alamat' : forms.TextInput(
                attrs={'class':'form-control', 'placeholder':'Tulis disini', 'required' : 'required'}
            ),
            'rt' : forms.TextInput(
                attrs={'class':'form-control', 'placeholder':'Tulis disini', 'required' : 'required'}
            ),
            'rw' : forms.TextInput(
                attrs={'class':'form-control', 'placeholder':'Tulis disini', 'required' : 'required'}
            ),
            'kodepos' : forms.TextInput(
                attrs={'class':'form-control', 'placeholder':'Tulis disini', 'required' : 'required'}
            ),
            'email' : forms.TextInput(
                attrs={'class':'form-control', 'placeholder':'Tulis disini', 'required' : 'required'}
            ),
            'telepon' : forms.TextInput(
                attrs={'class':'form-control', 'placeholder':'Tulis disini', 'required' : 'required'}
            ),
            'status_kawin' : forms.TextInput(
                attrs={'class':'form-control', 'placeholder':'Tulis disini', 'required' : 'required'}
            ),

        }



class PegawaiForm(forms.ModelForm):
    pilihan_agama = Agama.objects.all()
    pilihan_jk = Jenis_Kelamin.objects.all()
    pilihan_pekerjaan = Pekerjaan.objects.all()
    pilihan_kelpas = Kelompok_Pasien.objects.all()
    pilihan_kp = Kategori_Pegawai.objects.all()

    agama = forms.ModelChoiceField(pilihan_agama,widget=forms.Select(attrs={'class': 'form-control'}))
    jk = forms.ModelChoiceField(pilihan_jk,widget=forms.Select(attrs={'class': 'form-control'}))
    kp = forms.ModelChoiceField(pilihan_kp,widget=forms.Select(attrs={'class': 'form-control'}))
    tangal_lahir = forms.DateInput()

    class Meta:
        model = Pegawai
        fields = '__all__'
        widgets = {
            'nama' : forms.TextInput(
                attrs={'class':'form-control', 'placeholder':'Tulis disini', 'required' : 'required'}
            ),
            'tempat_lahir' : forms.TextInput(
                attrs={'class':'form-control', 'placeholder':'Tulis disini', 'required' : 'required'}
            ),
            'alamat' : forms.TextInput(
                attrs={'class':'form-control', 'placeholder':'Tulis disini', 'required' : 'required'}
            ),
            'rt' : forms.TextInput(
                attrs={'class':'form-control', 'placeholder':'Tulis disini', 'required' : 'required'}
            ),
            'rw' : forms.TextInput(
                attrs={'class':'form-control', 'placeholder':'Tulis disini', 'required' : 'required'}
            ),
            'kodepos' : forms.TextInput(
                attrs={'class':'form-control', 'placeholder':'Tulis disini', 'required' : 'required'}
            ),
            'telepon' : forms.TextInput(
                attrs={'class':'form-control', 'placeholder':'Tulis disini', 'required' : 'required'}
            ),
            'status_kawin' : forms.TextInput(
                attrs={'class':'form-control', 'placeholder':'Tulis disini', 'required' : 'required'}

            ),
        }
