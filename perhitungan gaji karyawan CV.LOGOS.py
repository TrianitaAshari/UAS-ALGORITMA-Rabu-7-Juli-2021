# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 09:04:40 2021

@author: trianita ashari
"""

"""
Cek nilai Menggunakan Loop 
" Loop CEK Program perhitungan gaji karyawan CV.LOGOS
" loop run program (ok)
"""
#CEK Program 
ulangprog = "y"
while ulangprog=="y" or ulangprog=="Y":
    print("===============================================")
    print("<<    PERHITUNGAN GAJI KARYAWAN CV LOGOS     >>")
    print("<<      CEK PERHITUNGAN GAJI KARYAWAN        >>")
    print("===============================================")
    
    #input nama karyawan,jenis kelamin,dan status kawin/tidak kawin   
    Karyawan = input("Masukkan nama karyawan : ")
    
    #input gaji pokok
    ringajipokok = ['Golongan 1 = 2.500.000','Golongan 2 = 4.500.000','Golongan 3 = 6.500.000']
    golongan = ['Golongan 1','Golongan 2','Golongan 3']
    gajipokok = [2500000,4500000,6500000]
    
    pilihan = input(">> Masukkan Golongan = ")
    #identifikasi pilihan
    if pilihan=="1":
        idx = 0
        tunjanganistri = 2500000*0.01
    elif pilihan=="2":
        idx = 1
        tunjanganistri = 4500000*0.03
    elif pilihan=="3":
        idx = 2
        tunjanganistri = 6500000*0.05
    else:
        idx = 4
        print("----------------Golongan tidak terdaftar---------------------")
        
    #cetak gaji pokok
    print(">>> rincian gaji pokok = " + ringajipokok[idx])
    
    #tunjangan istri
    jeniskelamin = input("jenis kelamin      :" )
    statuskawin = input("status kawin / belum kawin : ")
    if jeniskelamin=="laki-laki" and statuskawin=="kawin":
        print(">>> Total tunjangan istri     = Rp " + str(tunjanganistri))
             
    #tunjangan anak
    gajipokok = gajipokok[idx]
    tunjangananak = gajipokok*0.02
    #tampilkan tunjangan anak
    mempunyaianak = input("punya anak / belum punya anak :")
    if statuskawin=="kawin" and mempunyaianak=="punya anak":
        print(">>> Total tunjangan anak     = Rp " + str(tunjangananak))
    
    #gaji bruto
    gajibruto = gajipokok+tunjangananak+tunjanganistri
    #tampilkan gaji bruto
    print(">>> gaji bruto     = Rp " + str(gajibruto))
    
    #biaya jabatan
    biayajabatan = gajibruto*0.005
    print(">>> biaya jabatan     = Rp " + str(biayajabatan))
    
    #iuran pensiun
    iuranpensiun = 15500
    print(">>> iuran pensiun karyawan    = Rp 15.500 " )
    
    #iuran organisasi
    iuranorganisasi = 3500
    print(">>> iuran organisasi    = Rp 3.500 " )
    
    #gaji netto
    gajinetto = gajibruto-biayajabatan-iuranpensiun-iuranorganisasi
    print(">>> gaji netto     = Rp " + str(gajinetto))
    
    print("--------------------------------------------")
    print("            SLIP GAJI KARYAWAN              ")
    import datetime
    x = datetime.datetime.now()
    print("        Tanggal : " + str(x))
    print("--------------------------------------------")
    print(" Nama karyawan   :" + Karyawan)  
    print(" Golongan        :" + golongan[idx])
    print(" Jenis kelamin   :" + jeniskelamin)
    print(" Status kawin    :" + statuskawin)
    print(" Gaji Pokok      : Rp " + str(gajipokok))
    if jeniskelamin=="laki-laki" and statuskawin=="kawin":
        print(" Tunjangan Istri : Rp " + str(tunjanganistri))
    if statuskawin=="kawin" and mempunyaianak=="punya anak":    
        print(" Tunjangan anak  : Rp " + str(tunjangananak))
    print(" >> Gaji Bruto   : Rp " + str(gajibruto))
    print("_______________________________________________")
    print(" Biaya jabatan    : Rp " + str(biayajabatan))
    print(" Iuran pensiun    : Rp 15.500 " )
    print(" Iuran organisasi : Rp 3.500 " )
    print(" >> Gaji Netto    : Rp " + str(gajinetto))
    
    ulangprog = input(">> Cek perhitungan gaji lagi ? y/t = ")  
    if ulangprog=="t" or ulangprog=="T":
        break 