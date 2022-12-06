# Script Program Buku Pengamatan Klimatologi
# Badan Meteorologi Klimatologi dan Geofisika
# Satsiun Klimatologi Kelas 1 Lombok Barat
# Written by Robiatul Adawia & Iyan Islamiyati, Program Studi Fisika FMIPA Universitas Mataram
# Last updated: September 2019
# Written in Python and Indonesian Language

# Modul GUI Python
from tkinter import*
from tkinter import ttk
import tkinter.messagebox
from PIL import ImageTk, Image

# Database
import pymysql

win = Tk()

win.iconbitmap('icon.ico')
win.title("Pengamatan Iklim")
win.geometry('1000x650')
win.resizable(False, False)

#-------------------------------------------------------------------------------------------------------------------------------------
img1 = ImageTk.PhotoImage(Image.open("hal1clean.png"))
img2 = ImageTk.PhotoImage(Image.open("hal2clean.png"))

#-------------------------------------------------------------------------------------------------------------------------------------

"""======================================== TAMPILAN HALAMAN AWAL ============================================"""
#Masukkan logo BMKG
img = ImageTk.PhotoImage(Image.open("logo.png"))
label1 = Label(image=img, bg="white").grid(column=0, row=0, pady=25)
img_logo = ImageTk.PhotoImage(Image.open("logo_unram.png"))
label_logo = Label(image=img_logo, bg="white").place(x=5, y=570)

#Judul di halaman awal
judul1 = Label(win, text="BADAN METEOROLOGI KLIMATOLOGI DAN GEOFISIKA", bg="white", fg="black", font="callibri 26")
judul1.grid(column=0, row=1, padx=40)

judul2 = Label(win, text="STASIUN KLIMATOLOGI KELAS I LOMBOK BARAT", bg="white", fg="black", font="callibri 24")
judul2.grid(column=0, row=2)

judul3 = Label(win, text="BUKU PENGAMATAN KLIMATOLOGI", bg="white", fg="black", font="callibri 34 bold")
judul3.grid(column=0, row=3, pady=100)

keluar = Button(win, text="KELUAR", bg="green", fg="white", width=8, bd=5, font="callibri 12 bold", command=quit)
keluar.place(x=850 , y=540)
"""========================================== AKHIR TAMPILAN HALAMAN AWAL ============================================"""

"""================================================ MEMBUAT LAPORAN ===================================================="""
def membuat_laporan():
	Frame(win, width=900, height=630, bg="cadet blue").place(x=0, y=0)
	Frame(win, width=30, height=630, bg="powder blue").place(x=865, y=0)
	Frame(win, width=130, height=630, bg="cadet blue").place(x=870, y=0)
	
	tahun_bulan_tanggal = StringVar()
	
	Label(win, text="BUAT LAPORAN", bg="cadet blue", fg="black", font="callibri 10 bold").place(x=875, y=10)
	Label(win, text="Masukkan:", bg="cadet blue", fg="black", font="callibri 10 bold").place(x=875, y=40)
	Label(win, text="Waktu (YYYYMMDD):", bg="cadet blue", fg="black", font="callibri 8 bold").place(x=875, y=60)
	Entry(win, width=10, bd=5, textvariable=tahun_bulan_tanggal).place(x=895, y=80)
	
	global TahunBulanTanggal
	TahunBulanTanggal = tahun_bulan_tanggal.get()
	
	"""------------------------------------------------- FUNGSI ANGIN -------------------------------------------------"""
	def angin():
		Frame(win, width=864, height=630, bg='cadet blue' ).place(x=0, y=0)
		
		#JUDUL ALAT ANGIN (A)
		Label(win, text=" ANGIN ", bg="black", fg="cadet blue", font="callibri 24 bold").place(x=30, y=30)
		
		#Pilihan Waktu Pengamatan (PWP)
		waktu_pengamatanAngin = StringVar()
		
		jam_07_15 = StringVar()
		jam_07_45 = StringVar()
		jam_13_45 = StringVar()
		jam_14_15 = StringVar()
		jam_17_45 = StringVar()
		jam_18_15 = StringVar()
		
		waktu = ["-- Pilih Waktu Pengamatan --", "07.15", "07.45", "13.45", "14.15", "17.45", "18.15"]
		pilihan_waktu = ttk.Combobox(win, values = waktu, width = 22, font="callibri 12", textvariable=waktu_pengamatanAngin, state='readonly')
		pilihan_waktu.place(x=30, y=120)
		pilihan_waktu.current(0)
		
		#TABEL TEMPAT PENGISIAN NILAI
		cupCounter_0koma5m = StringVar()
		cupCounter_2m = StringVar()
		
		arah_4m = StringVar()
		arah_7m = StringVar()
		arah_10m = StringVar()
		
		kecepatan_4m = StringVar()
		kecepatan_7m = StringVar()
		kecepatan_10m = StringVar()
		
		#Baris 1
		Label(win, text="Ketinggian Anemometer", bg="cadet blue", font="callibri 12").place(x=30, y=170)
		Label(win, text="0.5 m", bg="cadet blue", font="callibri 12").place(x=250, y=170)
		Label(win, text="2 m", bg="cadet blue", font="callibri 12").place(x=350, y=170)
		
		#Baris 2 dan Entry
		Label(win, text="Cup Counter", bg="cadet blue", font="callibri 12").place(x=110, y=210)
		Entry(win, width=10, bd=10, textvariable=cupCounter_0koma5m).place(x=230, y=200)
		Entry(win, width=10, bd=10, textvariable=cupCounter_2m).place(x=330, y=200)
		
		#Baris 3
		Label(win, text="Ketinggian Anemometer", bg="cadet blue", font="callibri 12").place(x=30, y=242)
		Label(win, text="4 m", bg="cadet blue", font="callibri 12").place(x=250, y=242)
		Label(win, text="7 m", bg="cadet blue", font="callibri 12").place(x=350, y=242)
		Label(win, text="10 m", bg="cadet blue", font="callibri 12").place(x=450, y=242)
		
		#Baris 4 dan Entry
		Label(win, text="Arah", bg="cadet blue", font="callibri 12").place(x=160, y=280)
		Entry(win, width=10, bd=10, textvariable=arah_4m).place(x=230, y=270)
		Entry(win, width=10, bd=10, textvariable=arah_7m).place(x=330, y=270)
		Entry(win, width=10, bd=10, textvariable=arah_10m).place(x=430, y=270)
		
		#Baris 5 dan Entry
		Label(win, text="Kecepatan", bg="cadet blue", font="callibri 12").place(x=120, y=340)
		Entry(win, width=10, bd=10, textvariable=kecepatan_4m).place(x=230, y=330)
		Entry(win, width=10, bd=10, textvariable=kecepatan_7m).place(x=330, y=330)
		Entry(win, width=10, bd=10, textvariable=kecepatan_10m).place(x=430, y=330)
		
		#SAVE DAN EXIT
		def save():
			#simpan entry ke variabel
			wp = (waktu_pengamatanAngin.get())
			if (wp == "07.15"):
				jam_07_15 = wp
				
				CupCounter_0koma5m_07_15=cupCounter_0koma5m.get()
				CupCounter_2m_07_15=cupCounter_2m.get()
				
				
				Arah_4m_07_15=arah_4m.get()
				Arah_7m_07_15=arah_7m.get()
				Arah_10m_07_15=arah_10m.get()
				
				Kecepatan_4m_07_15=kecepatan_4m.get()
				Kecepatan_7m_07_15=kecepatan_7m.get()
				Kecepatan_10m_07_15=kecepatan_10m.get()
				
				#simpan ke database
				con = pymysql.connect("localhost", "root", "12345", "Buku_Klimatologi_BMKG")
				#with con.cursor() as cursor:
				#	cursor.execute("CREATE TABLE Angin0715_1 (Waktu text, cup0_5_07_15 text, cup2_0_07_15 text, arah4m_07_15 text, kecepatan4m_07_15 text, arah7m_07_15 text, kecepatan7m_07_15 text, arah10m_07_15 text, kecepatan10m_07_15 text)")
				with con.cursor() as cursor:
					sql1 = "INSERT INTO Angin0715_1(Waktu, cup0_5_07_15, cup2_0_07_15, arah4m_07_15, kecepatan4m_07_15, arah7m_07_15,kecepatan7m_07_15,arah10m_07_15,kecepatan10m_07_15)\
							VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')"%(TahunBulanTanggal, CupCounter_0koma5m_07_15, CupCounter_2m_07_15, Arah_4m_07_15, Kecepatan_4m_07_15, Arah_7m_07_15, Kecepatan_7m_07_15,\
							Arah_10m_07_15, Kecepatan_10m_07_15)
					cursor.execute(sql1)
					con.commit()
					
			elif (wp == "07.45"):
				jam_07_45 = wp

				CupCounter_0koma5m_07_45=cupCounter_0koma5m.get()
				CupCounter_2m_07_45=cupCounter_2m.get()
				
				Arah_4m_07_45=arah_4m.get()
				Arah_7m_07_45=arah_7m.get()
				Arah_10m_07_45=arah_10m.get()
				
				Kecepatan_4m_07_45=kecepatan_4m.get()
				Kecepatan_7m_07_45=kecepatan_7m.get()
				Kecepatan_10m_07_45=kecepatan_10m.get()
				
				#simpan ke database
				con = pymysql.connect("localhost", "root", "12345", "Buku_Klimatologi_BMKG")
				#with con.cursor() as cursor:
				#	cursor.execute("CREATE TABLE Angin0745_1 (Waktu text, cup0_5_07_45 text, cup2_0_07_45 text, arah4m_07_45 text, kecepatan4m_07_45 text, arah7m_07_45 text, kecepatan7m_07_45 text, arah10m_07_45 text,kecepatan10m_07_45 text)")
				with con.cursor() as cursor:
					sql2 = "INSERT INTO Angin0745_1(Waktu, cup0_5_07_45, cup2_0_07_45, arah4m_07_45, kecepatan4m_07_45, arah7m_07_45,kecepatan7m_07_45,arah10m_07_45,kecepatan10m_07_45)\
							VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')"%(TahunBulanTanggal, CupCounter_0koma5m_07_45, CupCounter_2m_07_45, Arah_4m_07_45, Kecepatan_4m_07_45, Arah_7m_07_45, Kecepatan_7m_07_45,\
							Arah_10m_07_45, Kecepatan_10m_07_45)
					cursor.execute(sql2)
					con.commit()

			elif (wp == str(13.45)):
				jam_13_45 = wp
				
				CupCounter_0koma5m_13_45=cupCounter_0koma5m.get()
				CupCounter_2m_13_45=cupCounter_2m.get()
				
				Arah_4m_13_45=arah_4m.get()
				Arah_7m_13_45=arah_7m.get()
				Arah_10m_13_45=arah_10m.get()
				
				Kecepatan_4m_13_45=kecepatan_4m.get()
				Kecepatan_7m_13_45=kecepatan_7m.get()
				Kecepatan_10m_13_45=kecepatan_10m.get()
				
				#simpan ke database
				con = pymysql.connect("localhost", "root", "12345", "Buku_Klimatologi_BMKG")
				#with con.cursor() as cursor:
				#	cursor.execute("CREATE TABLE Angin1345_1 (Waktu text, cup0_5_13_45 text, cup2_0_13_45 text, arah4m_13_45 text, kecepatan4m_13_45 text, arah7m_13_45 text, kecepatan7m_13_45 text, arah10m_13_45 text, kecepatan10m_13_45 text)")
				with con.cursor() as cursor:
					sql3 = "INSERT INTO Angin1345_1(Waktu, cup0_5_13_45, cup2_0_13_45, arah4m_13_45, kecepatan4m_13_45, arah7m_13_45, kecepatan7m_13_45, arah10m_13_45, kecepatan10m_13_45)\
							VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')"%(TahunBulanTanggal, CupCounter_0koma5m_13_45, CupCounter_2m_13_45, Arah_4m_13_45, Kecepatan_4m_13_45, Arah_7m_13_45, Kecepatan_7m_13_45,\
							Arah_10m_13_45, Kecepatan_10m_13_45)
					cursor.execute(sql3)
					con.commit()
				
			elif (wp == str(14.15)):
				jam_14_15 = wp
				
				CupCounter_0koma5m_14_15=cupCounter_0koma5m.get()
				CupCounter_2m_14_15=cupCounter_2m.get()
				
				Arah_4m_14_15=arah_4m.get()
				Arah_7m_14_15=arah_7m.get()
				Arah_10m_14_15=arah_10m.get()
				
				Kecepatan_4m_14_15=kecepatan_4m.get()
				Kecepatan_7m_14_15=kecepatan_7m.get()
				Kecepatan_10m_14_15=kecepatan_10m.get()
				
				#simpan ke database
				con = pymysql.connect("localhost", "root", "12345", "Buku_Klimatologi_BMKG")
				#with con.cursor() as cursor:
				#	cursor.execute("CREATE TABLE Angin1415_1 (Waktu text, cup0_5_14_15 text, cup2_0_14_15 text, arah4m_14_15 text, kecepatan4m_14_15 text, arah7m_14_15 text, kecepatan7m_14_15 text, arah10m_14_15 text, kecepatan10m_14_15 text)")
				with con.cursor() as cursor:
					sql4 = "INSERT INTO Angin1415_1 (Waktu, cup0_5_14_15, cup2_0_14_15, arah4m_14_15, kecepatan4m_14_15, arah7m_14_15, kecepatan7m_14_15, arah10m_14_15, kecepatan10m_14_15)\
							VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')"%(TahunBulanTanggal, CupCounter_0koma5m_14_15, CupCounter_2m_14_15, Arah_4m_14_15, Kecepatan_4m_14_15, Arah_7m_14_15, Kecepatan_7m_14_15,\
							Arah_10m_14_15, Kecepatan_10m_14_15)
					cursor.execute(sql4)
					con.commit()
				
			elif (wp == str(17.45)):
				jam_17_45 = wp
				
				CupCounter_0koma5m_17_45=cupCounter_0koma5m.get()
				CupCounter_2m_17_45=cupCounter_2m.get()
				
				Arah_4m_17_45=arah_4m.get()
				Arah_7m_17_45=arah_7m.get()
				Arah_10m_17_45=arah_10m.get()
				
				Kecepatan_4m_17_45=kecepatan_4m.get()
				Kecepatan_7m_17_45=kecepatan_7m.get()
				Kecepatan_10m_17_45=kecepatan_10m.get()
				
				#simpan ke database
				con = pymysql.connect("localhost", "root", "12345", "Buku_Klimatologi_BMKG")
				#with con.cursor() as cursor:
				#	cursor.execute("CREATE TABLE Angin1745_1 (Waktu text, cup0_5_17_45 text, cup2_0_17_45 text, arah4m_17_45 text, kecepatan4m_17_45 text, arah7m_17_45 text, kecepatan7m_17_45 text, arah10m_17_45 text, kecepatan10m_17_45 text)")
				with con.cursor() as cursor:
					sql5 = "INSERT INTO Angin1745_1 (Waktu, cup0_5_17_45, cup2_0_17_45, arah4m_17_45, kecepatan4m_17_45, arah7m_17_45, kecepatan7m_17_45, arah10m_17_45, kecepatan10m_17_45)\
							VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')"%(TahunBulanTanggal, CupCounter_0koma5m_17_45, CupCounter_2m_17_45, Arah_4m_17_45, Kecepatan_4m_17_45, Arah_7m_17_45, Kecepatan_7m_17_45,\
							Arah_10m_17_45, Kecepatan_10m_17_45)
					cursor.execute(sql5)
					con.commit()
				
			elif (wp == str(18.15)):
				jam_18_15 = wp
				
				CupCounter_0koma5m_18_15=cupCounter_0koma5m.get()
				CupCounter_2m_18_15=cupCounter_2m.get()
				
				Arah_4m_18_15=arah_4m.get()
				Arah_7m_18_15=arah_7m.get()
				Arah_10m_18_15=arah_10m.get()
				
				Kecepatan_4m_18_15=kecepatan_4m.get()
				Kecepatan_7m_18_15=kecepatan_7m.get()
				Kecepatan_10m_18_15=kecepatan_10m.get()
				
				#simpan ke database
				con = pymysql.connect("localhost", "root", "12345", "Buku_Klimatologi_BMKG")
				#with con.cursor() as cursor:
				#	cursor.execute("CREATE TABLE Angin1815_1 (Waktu text, cup0_5_18_15 text, cup2_0_18_15 text, arah4m_18_15 text, kecepatan4m_18_15 text, arah7m_18_15 text, kecepatan7m_18_15 text, arah10m_18_15 text, kecepatan10m_18_15 text)")
				with con.cursor() as cursor:
					sql6 = "INSERT INTO Angin1815_1 (Waktu, cup0_5_18_15, cup2_0_18_15, arah4m_18_15, kecepatan4m_18_15, arah7m_18_15, kecepatan7m_18_15, arah10m_18_15, kecepatan10m_18_15)\
							VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')"%(TahunBulanTanggal, CupCounter_0koma5m_18_15, CupCounter_2m_18_15, Arah_4m_18_15, Kecepatan_4m_18_15, Arah_7m_18_15, Kecepatan_7m_18_15,\
							Arah_10m_18_15, Kecepatan_10m_18_15)
					cursor.execute(sql6)
					con.commit()

			else:
				tkinter.messagebox.showwarning("Peringatan", "Anda belum memilih Waktu Pengamatan")
						
			
			#bersihkan entry
			waktu_pengamatanAngin.set("-- Pilih Waktu Pengamatan --")
			
			cupCounter_0koma5m.set("")
			cupCounter_2m.set("")
			
			arah_4m.set("")
			arah_7m.set("")
			arah_10m.set("")
			
			kecepatan_4m.set("")
			kecepatan_7m.set("")
			kecepatan_10m.set("")
			
		
		simpan = Button(win, text="SIMPAN", bg="blue", fg="white", width=8, bd=5, font="callibri 12 bold", command=save)
		simpan.place(x=700 , y=540)
		

		
	"""------------------------------------------------- AKHIR FUNGSI ANGIN -------------------------------------------"""
	
	"""-------------------------------------------------- FUNGSI BAROMETER ---------------------------------------------"""
	def barometer():
		Frame(win, width=864, height=630, bg='cadet blue' ).place(x=0, y=0)
		
		#JUDUL ALAT BAROMETER (B)
		b = Label(win, text=" BAROMETER ", bg="black", fg="cadet blue", font="callibri 24 bold")
		b.place(x=30, y=30)
		
		#TABEL TEMPAT PENGISIAN NILAI
		barometer_suhu = StringVar()
		barometer_barometer = StringVar()
		barometer_QFF = StringVar()
		barometer_QFE = StringVar()
		
		#kolom1
		Label(win, text="Waktu", bg="cadet blue", font="callibri 12").place(x=30, y=140)
		Label(win, text="Suhu", bg="cadet blue", font="callibri 12").place(x=30, y=200)
		Label(win, text="Barometer", bg="cadet blue", font="callibri 12").place(x=30, y=260)
		Label(win, text="QFF", bg="cadet blue", font="callibri 12").place(x=30, y=320)
		Label(win, text="QFE", bg="cadet blue", font="callibri 12").place(x=30, y=380)
		#Kolom 2 dan Entry
		Label(win, text="00.00 UTC", bg="cadet blue", font="callibri 12").place(x=200, y=140)
		Entry(win, width=10, bd=10, textvariable=barometer_suhu).place(x=205, y=200)
		Entry(win, width=10, bd=10, textvariable=barometer_barometer).place(x=205, y=260)
		Entry(win, width=10, bd=10, textvariable=barometer_QFF).place(x=205, y=320)
		Entry(win, width=10, bd=10, textvariable=barometer_QFE).place(x=205, y=380)
		
		def save():
			#simpan entry ke variabel
			Barometer_suhu=barometer_suhu.get()
			Barometer_barometer=barometer_barometer.get()
			Barometer_QFF=barometer_QFF.get()
			Barometer_QFE=barometer_QFE.get()
			
			# simpan ke database
			con = pymysql.connect("localhost", "root", "12345", "Buku_Klimatologi_BMKG")
			#with con.cursor() as cursor:
			#	cursor.execute("CREATE TABLE Barometer_5(Waktu text, suhu00_00UTC text, barometer00_00UTC text, QFF00_00UTC text, QFE00_00UTC text)")
			with con.cursor() as cursor:
				sql7 = "INSERT INTO Barometer_5(Waktu, suhu00_00UTC, barometer00_00UTC, QFF00_00UTC, QFE00_00UTC) VALUES ('%s', '%s', '%s', '%s', '%s')"\
					%(TahunBulanTanggal, Barometer_suhu, Barometer_barometer, Barometer_QFF, Barometer_QFE)
				cursor.execute(sql7)
				con.commit()
				
			#bersihkan entry
			barometer_suhu.set("")
			barometer_barometer.set("")
			barometer_QFF.set("")
			barometer_QFE.set("")
		
		#SAVE DAN EXIT
		simpan = Button(win, text="SIMPAN", bg="blue", fg="white", width=8, bd=5, font="callibri 12 bold", command=save)
		simpan.place(x=700 , y=540)
	"""------------------------------------------- AKHIR FUNGSI BAROMETER -------------------------------------------"""
	
	"""------------------------------------------- FUNGSI KONDISI CUACA DAN TANAH -----------------------------------"""
	def kondisi_cuacaTanah():
		Frame(win, width=700, height=630, bg='cadet blue' ).place(x=0, y=0)
		#JUDUL ALAT KONDISI CUACA DAN TANAH (KCT)
		kct = Label(win, text=" KONDISI CUACA DAN TANAH ", bg="black", fg="cadet blue", font="callibri 24 bold")
		kct.place(x=30, y=30)
		
		#Pilihan Waktu Pengamatan (PWP)
		waktu_pengamatanCuacaTanah = StringVar()
		jam_07_15 = StringVar()
		jam_14_15 = StringVar()
		
		waktu = ["-- Pilih Waktu Pengamatan --", "07.15", "14.15"]
		pilihan_waktu = ttk.Combobox(win, values = waktu, width = 22, font="callibri 12", textvariable=waktu_pengamatanCuacaTanah, state='readonly')
		pilihan_waktu.place(x=30, y=120)
		pilihan_waktu.current(0)
		
		#TABEL TEMPAT PENGISIAN NILAI
		cuacaTanah_kodeTanah = StringVar()
		cuacaTanah_kodeCuaca = StringVar()
		
		#Baris 1 dan Entry
		Label(win, text="Kode Tanah", bg="cadet blue", font="callibri 12").place(x=30, y=240)
		Entry(win, width=10, bd=10, textvariable=cuacaTanah_kodeTanah).place(x=150, y=240)
		#Baris 2 dan Entry
		Label(win, text="Kode Cuaca", bg="cadet blue", font="callibri 12").place(x=30, y=300)
		Entry(win, width=10, bd=10, textvariable=cuacaTanah_kodeCuaca).place(x=150, y=300)
		
		def save():
			#simpan entry ke variabel
			wp = (waktu_pengamatanCuacaTanah.get())
			if (wp == "07.15"):
				jam_07_15 = wp
				CuacaTanah_kodeTanah_07_15=cuacaTanah_kodeTanah.get()
				CuacaTanah_kodeCuaca_07_15=cuacaTanah_kodeCuaca.get()
				
				#simpan ke database
				con = pymysql.connect("localhost", "root", "12345", "Buku_Klimatologi_BMKG")
				#with con.cursor() as cursor:
				#	cursor.execute("CREATE TABLE Kondisi_Cuaca_Tanah0715_1 (Waktu text, kodetanah_07_15 text, kodecuaca_07_15 text)")
				with con.cursor() as cursor:
					sql8 = "INSERT INTO Kondisi_Cuaca_Tanah0715_1 (Waktu, kodetanah_07_15, kodecuaca_07_15) VALUES('%s', '%s', '%s')"\
							%(TahunBulanTanggal, CuacaTanah_kodeTanah_07_15, CuacaTanah_kodeCuaca_07_15)
					cursor.execute(sql8)
					con.commit()

			elif (wp == str(14.15)):
				jam_14_15 = wp
				CuacaTanah_kodeTanah_14_15=cuacaTanah_kodeTanah.get()
				CuacaTanah_kodeCuaca_14_15=cuacaTanah_kodeCuaca.get()
				
				#simpan ke database
				con = pymysql.connect("localhost", "root", "12345", "Buku_Klimatologi_BMKG")
				#with con.cursor() as cursor:
				#	cursor.execute("CREATE TABLE Kondisi_Cuaca_Tanah1415_1 (Waktu text, kodetanah_14_15 text, kodecuaca_14_15 text)")
				with con.cursor() as cursor:
					sql9 = "INSERT INTO Kondisi_Cuaca_Tanah1415_1 (Waktu, kodetanah_14_15, kodecuaca_14_15) VALUES('%s', '%s', '%s')"\
							%(TahunBulanTanggal,CuacaTanah_kodeTanah_14_15, CuacaTanah_kodeCuaca_14_15)
					cursor.execute(sql9)
					con.commit()
				
			else:
				tkinter.messagebox.showwarning("Peringatan", "Anda belum memilih Waktu Pengamatan")
						
			#bersihkan entry
			waktu_pengamatanCuacaTanah.set("-- Pilih Waktu Pengamatan --")
			cuacaTanah_kodeTanah.set("")
			cuacaTanah_kodeCuaca.set("")
		
		#SAVE DAN EXIT
		simpan = Button(win, text="SIMPAN", bg="blue", fg="white", width=8, bd=5, font="callibri 12 bold", command=save)
		simpan.place(x=700 , y=540)
	"""------------------------------------ AKHIR FUNGSI KONDISI CUACA DAN TANAH ---------------------------------"""
	
	def lama_penyinaran():
		Frame(win, width=864, height=630, bg='cadet blue' ).place(x=0, y=0)
		
		#JUDUL ALAT LAMA PENYINARAN (LP)
		lp = Label(win, text=" LAMA PENYINARAN ", bg="black", fg="cadet blue", font="callibri 24 bold")
		lp.place(x=30, y=30)
		
		#TABEL TEMPAT PENGISIAN NILAI
		lamaPenyinaran12jam_jam = StringVar()
		lamaPenyinaran12jam_persen = StringVar()
		lama_penyinaran8jam_jam = StringVar()
		lama_penyinaran8jam_persen = StringVar()
		#Baris
		Label(win, text="Waktu", bg="cadet blue", font="callibri 12").place(x=40, y=150)
		Label(win, text="12 Jam", bg="cadet blue", font="callibri 12").place(x=30, y=210)
		Label(win, text="8 Jam", bg="cadet blue", font="callibri 12").place(x=40, y=270)
		
		#Kolom
		Label(win, text="Jam", bg="cadet blue", font="callibri 12").place(x=180, y=150)
		Label(win, text="%", bg="cadet blue", font="callibri 12").place(x=370, y=150)
		
		#Entry
		Entry(win, width=10, bd=10, textvariable=lamaPenyinaran12jam_jam).place(x=170, y=215)
		Entry(win, width=10, bd=10, textvariable=lama_penyinaran8jam_jam).place(x=170, y=275)
		Entry(win, width=10, bd=10, textvariable=lamaPenyinaran12jam_persen).place(x=350, y=215)
		Entry(win, width=10, bd=10, textvariable=lama_penyinaran8jam_persen).place(x=350, y=275)
		
		def save():
			#simpan entry ke variabel
			LamaPenyinaran12jam_jam=lamaPenyinaran12jam_jam.get()
			LamaPenyinaran12jam_persen=lamaPenyinaran12jam_persen.get()
			LamaPenyinaran8jam_jam=lama_penyinaran8jam_jam.get()
			LamaPenyinaran8jam_persen=lama_penyinaran8jam_persen.get()
			
			#simpan ke database
			con  = pymysql.connect("localhost", "root", "12345", "Buku_Klimatologi_BMKG")
			#with con.cursor() as cursor:
			#	cursor.execute("CREATE TABLE Lama_Penyinaran_1(Waktu text, lamapenyinaran12jam_jam text, lamapenyinaran12jam_persen text, lamapenyinaran8jam_jam text, lamapenyinaran8jam_persen text)")
			with con.cursor() as cursor:
				sql10 = "INSERT INTO Lama_Penyinaran_1(Waktu, lamapenyinaran12jam_jam, lamapenyinaran12jam_persen, lamapenyinaran8jam_jam, lamapenyinaran8jam_persen) VALUES('%s', '%s', '%s', '%s', '%s')"\
						%(TahunBulanTanggal, LamaPenyinaran12jam_jam, LamaPenyinaran12jam_persen, LamaPenyinaran8jam_jam, LamaPenyinaran8jam_persen)
				cursor.execute(sql10)
				con.commit()
				
			#bersihkan entry
			lamaPenyinaran12jam_jam.set("")
			lamaPenyinaran12jam_persen.set("")
			lama_penyinaran8jam_jam.set("")
			lama_penyinaran8jam_persen.set("")
		
		#SAVE DAN EXIT
		simpan = Button(win, text="SIMPAN", bg="blue", fg="white", width=8, bd=5, font="callibri 12 bold", command=save)
		simpan.place(x=700 , y=540)
	"""----------------------------------------- AKHIR FUNGSI LAMA PENYINARAN --------------------------------------"""
	
	def lysimeter():
		Frame(win, width=864, height=630, bg='cadet blue' ).place(x=0, y=0)
		
		#JUDUL ALAT LYSIMETER (lys)
		lys = Label(win, text=" LYSIMETER ", bg="black", fg="cadet blue", font="callibri 24 bold")
		lys.place(x=30, y=30)
		
		#TABEL TEMPAT PENGISIAN NILAI
		tanahGundul_siram = StringVar()
		tanahGundul_keluar = StringVar()

		tanahBerumput_siram = StringVar()
		tanahBerumput_keluar = StringVar()

		tanahTanamanKomoditi_siram = StringVar()
		tanahTanamanKomoditi_keluar = StringVar()

		lain2_curahHujanPerJam = StringVar()
		lain2_namaTanamanKomoditi = StringVar()
		lain2_keteranganFase_atas = StringVar()
		lain2_keteranganFase_bawah = StringVar()
		lain2_keteranganFase_hasil = StringVar()
		lain2_display = StringVar()

		#TIGA JENIS TANAH
		Label(win, text="Tanah Gundul", bg="cadet blue", font="callibri 12").place(x=90, y=160)
		Label(win, text="Siram", bg="cadet blue", font="callibri 12").place(x=40, y=190)
		Label(win, text="Keluar", bg="cadet blue", font="callibri 12").place(x=40, y=230)
		Entry(win, width=10, bd=10, textvariable=tanahGundul_siram).place(x=100, y=185)
		Entry(win, width=10, bd=10, textvariable=tanahGundul_keluar).place(x=100, y=225)

		Label(win, text="Tanaman Komoditi", bg="cadet blue", font="callibri 12").place(x=200, y=160)
		Entry(win, width=10, bd=10, textvariable=tanahTanamanKomoditi_siram).place(x=220, y=185)
		Entry(win, width=10, bd=10, textvariable=tanahTanamanKomoditi_keluar).place(x=220, y=225)

		Label(win, text="Tanah Berumput", bg="cadet blue", font="callibri 12").place(x=340, y=160)
		Entry(win, width=10, bd=10, textvariable=tanahBerumput_siram).place(x=355, y=185)
		Entry(win, width=10, bd=10, textvariable=tanahBerumput_keluar).place(x=355, y=225)

		#LAIN-LAIN
		Label(win, text="Lain-lain:", bg="cadet blue", font="callibri 12 bold").place(x=110, y=300)
		Label(win, text="Jumlah Curah Hujan", bg="cadet blue", font="callibri 12").place(x=40, y=330)
		Label(win, text="Per jam", bg="cadet blue", font="callibri 12").place(x=120, y=350)
		Entry(win, width=10, bd=10, textvariable=lain2_curahHujanPerJam).place(x=200, y=330)

		Label(win, text="Nama Tanaman", bg="cadet blue", font="callibri 12").place(x=65, y=380)
		Label(win, text="Komoditi", bg="cadet blue", font="callibri 12").place(x=113, y=400)
		Entry(win, width=30, bd=10, textvariable=lain2_namaTanamanKomoditi).place(x=200, y=380)

		Label(win, text="Keterangan", bg="cadet blue", font="callibri 12").place(x=430, y=300)
		Label(win, text="Fase:", bg="cadet blue", font="callibri 12").place(x=475, y=320)
		Frame(win, width=300, height=150, bg='powder blue').place(x=530, y=300)
		Entry(win, width=10, bd=3, textvariable=lain2_keteranganFase_atas).place(x=550, y=310)
		Entry(win, width=10, bd=3, textvariable=lain2_keteranganFase_bawah).place(x=550, y=335)
		Frame(win, width=10, height=2, bg='black').place(x=630, y=355)
		Frame(win, width=90, height=3, bg='black').place(x=540, y=360)
		Label(win, text="mm", bg="powder blue", font="callibri 12").place(x=620, y=365)
		Entry(win, width=5, bd=3, textvariable=lain2_keteranganFase_hasil).place(x=580, y=365)

		Label(win, text="Display:", bg="cadet blue", font="callibri 12").place(x=460, y=405)
		Entry(win, width=10, bd=3, textvariable=lain2_display).place(x=550, y=410)

		def save():
			#simpan entry ke variabel
			TanahGundul_siram=tanahGundul_siram.get()
			TanahaGundul_keluar=tanahGundul_keluar.get()
			TanahTanamanKomoditi_siram=tanahTanamanKomoditi_siram.get()
			TanahTanamanKomoditi_keluar=tanahTanamanKomoditi_keluar.get()
			TanahBerumput_siram=tanahBerumput_siram.get()
			TanahBerumput_keluar=tanahBerumput_keluar.get()
			
			
			Lain2_curahHujanPerJam=lain2_curahHujanPerJam.get()
			Lain2_namaTanamanKomoditi=lain2_namaTanamanKomoditi.get()
			Lain2_keteranganFase_atas=lain2_keteranganFase_atas.get()
			Lain2_keteranganFase_bawah=lain2_keteranganFase_bawah.get()
			Lain2_keteranganFase_hasil=lain2_keteranganFase_hasil.get()
			Lain2_display=lain2_display.get()
			
			#simpan ke database
			con = pymysql.connect("localhost", "root", "12345", "Buku_Klimatologi_BMKG")
			#with con.cursor() as cursor:
			#	cursor.execute("CREATE TABLE Lysimeter_11 (Waktu text, tanahgundul_siram text, tanahgundul_keluar text, tanahtanamankomoditi_siram text, tanahtanamankomoditi_keluar text,\
			#	tanahberumput_siram text, tanahberumput_keluar text, lain2_curahhujanperjam17_15 text, lain2_namatanamankomoditi varchar(20), lain2_keteranganfase_atas varchar(20),\
			#	lain2_keteranganfase_bawah varchar(20), lain2_keteranganfase_hasil varchar(20), lain2_display varchar(20))")
			with con.cursor() as cursor:
				sql11 = "INSERT INTO Lysimeter_11 (Waktu, tanahgundul_siram, tanahgundul_keluar, tanahtanamankomoditi_siram, tanahtanamankomoditi_keluar,\
						tanahberumput_siram, tanahberumput_keluar, lain2_curahhujanperjam17_15, lain2_namatanamankomoditi, lain2_keteranganfase_atas, lain2_keteranganfase_bawah,\
						lain2_keteranganfase_hasil, lain2_display) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (TahunBulanTanggal, TanahGundul_siram, TanahaGundul_keluar,\
						TanahTanamanKomoditi_siram, TanahTanamanKomoditi_keluar,TanahBerumput_siram, TanahBerumput_keluar, Lain2_curahHujanPerJam, Lain2_namaTanamanKomoditi, Lain2_keteranganFase_atas,\
						Lain2_keteranganFase_bawah, Lain2_keteranganFase_hasil, Lain2_display)
				cursor.execute(sql11)
				con.commit()
			
			#bersihkan entry
			tanahGundul_siram.set("")
			tanahGundul_keluar.set("")
			tanahBerumput_siram.set("")
			tanahBerumput_keluar.set("")
			tanahTanamanKomoditi_siram.set("")
			tanahTanamanKomoditi_keluar.set("")
			
			lain2_curahHujanPerJam.set("")
			lain2_namaTanamanKomoditi.set("")
			lain2_curahHujanPerJam.set("")
			lain2_namaTanamanKomoditi.set("")
			lain2_keteranganFase_atas.set("")
			lain2_keteranganFase_bawah.set("")
			lain2_keteranganFase_hasil.set("")
			lain2_display.set("")

		#SAVE DAN EXIT
		simpan = Button(win, text="SIMPAN", bg="blue", fg="white", width=8, bd=5, font="callibri 12 bold", command=save)
		simpan.place(x=700 , y=540)
	"""-------------------------------------------- AKHIR FUNGSI LYSIMETER ------------------------------------------"""

	"""------------------------------------------------ FUNGSI OPEN PAN -----------------------------------------------"""
	def open_pan():
		Frame(win, width=864, height=630, bg='cadet blue' ).place(x=0, y=0)
		
		#JUDUL OPEN PAN (OP)
		op = Label(win, text=" OPEN PAN ", bg="black", fg="cadet blue", font="callibri 24 bold")
		op.place(x=30, y=30)
		
		#Pilihan Waktu Pengamatan (PWP)
		waktu_pengamatanOpenPan = StringVar()
		jam_07_15 = StringVar()
		jam_07_45 = StringVar()
		jam_13_45 = StringVar()
		jam_17_45 = StringVar()
		
		waktu = ["-- Pilih Waktu Pengamatan --", "07.15", "07.45", "13.45", "17.45"]
		pilihan_waktu = ttk.Combobox(win, values = waktu, width = 22, font="callibri 12", state='readonly', textvariable=waktu_pengamatanOpenPan)
		pilihan_waktu.place(x=30, y=120)
		pilihan_waktu.current(0)
		
		#TABEL TEMPAT PENGISIAN NILAI
		hujan_13_5jam = StringVar()
		hujan_24jam = StringVar()
		hujan_30menit = StringVar()
		hujan_6jam = StringVar()
		hujan_4jam = StringVar()
		
		penguapan_24jam = StringVar()
		penguapan_13_5jam = StringVar()
		penguapan_6jam = StringVar()
		penguapan_4jam = StringVar()
		
		ketinggianAirPanci = StringVar()
		suhuAirMax = StringVar()
		suhuAirMin = StringVar()

		#Area kiri
		Label(win, text="Ketinggian Air di Panci:", bg="cadet blue", font="callibri 12").place(x=30, y=240)
		Entry(win, width=10, bd=10, textvariable=ketinggianAirPanci).place(x=220, y=235)
		Label(win, text="Suhu Air", bg="cadet blue", font="callibri 12").place(x=30, y=280)
		Label(win, text="Maksimum:", bg="cadet blue", font="callibri 12").place(x=30, y=320)
		Label(win, text="Minimum:", bg="cadet blue", font="callibri 12").place(x=150, y=320)
		Entry(win, width=10, bd=10, textvariable=suhuAirMax).place(x=30, y=360)
		Entry(win, width=10, bd=10, textvariable=suhuAirMin).place(x=150, y=360)
		
		#Area kanan
		def Buka():
			wp = (waktu_pengamatanOpenPan.get())
			if (wp == "07.15"):
				Frame(win, width=200, height=220, bg='powder blue' ).place(x=340, y=230)
				#Waktu 07.15
				Label(win, text="Hujan", bg="powder blue", font="callibri 12").place(x=350, y=240)
				Label(win, text="13.5 jam:", bg="powder blue", font="callibri 12").place(x=350, y=280)
				Entry(win, width=10, bd=10, textvariable=hujan_13_5jam).place(x=440, y=275)
				Label(win, text="24 jam:", bg="powder blue", font="callibri 12").place(x=350, y=320)
				Entry(win, width=10, bd=10, textvariable=hujan_24jam).place(x=440, y=315)
				Label(win, text="Penguapan", bg="powder blue", font="callibri 12").place(x=350, y=360)
				Label(win, text="24 jam:", bg="powder blue", font="callibri 12").place(x=350, y=400)
				Entry(win, width=10, bd=10, textvariable=penguapan_24jam).place(x=440, y=395)
			elif (wp == "07.45"):
				Frame(win, width=200, height=220, bg='powder blue' ).place(x=340, y=230)
				#Waktu 07.45
				Label(win, text="Hujan", bg="powder blue", font="callibri 12").place(x=350, y=240)
				Label(win, text="30 menit:", bg="powder blue", font="callibri 12").place(x=350, y=280)
				Entry(win, width=10, bd=10, textvariable=hujan_30menit).place(x=440, y=275)
				Label(win, text="Penguapan", bg="powder blue", font="callibri 12").place(x=350, y=320)
				Label(win, text="13.5 jam:", bg="powder blue", font="callibri 12").place(x=350, y=360)
				Entry(win, width=10, bd=10, textvariable=penguapan_13_5jam).place(x=440, y=355)
			elif (wp == str(13.45)):
				Frame(win, width=200, height=220, bg='powder blue' ).place(x=340, y=230)
				#Waktu 13.45
				Label(win, text="Hujan", bg="powder blue", font="callibri 12").place(x=350, y=240)
				Label(win, text="6 jam:", bg="powder blue", font="callibri 12").place(x=350, y=280)
				Entry(win, width=10, bd=10, textvariable=hujan_6jam).place(x=440, y=275)
				Label(win, text="Penguapan", bg="powder blue", font="callibri 12").place(x=350, y=320)
				Label(win, text="6 jam:", bg="powder blue", font="callibri 12").place(x=350, y=360)
				Entry(win, width=10, bd=10, textvariable=penguapan_6jam).place(x=440, y=355)
			elif (wp == str(17.45)):
				Frame(win, width=200, height=220, bg='powder blue' ).place(x=340, y=230)
				#Waktu 17.45
				Label(win, text="Hujan", bg="powder blue", font="callibri 12").place(x=350, y=240)
				Label(win, text="4 jam:", bg="powder blue", font="callibri 12").place(x=350, y=280)
				Entry(win, width=10, bd=10, textvariable=hujan_4jam).place(x=440, y=275)
				Label(win, text="Penguapan", bg="powder blue", font="callibri 12").place(x=350, y=320)
				Label(win, text="4 jam:", bg="powder blue", font="callibri 12").place(x=350, y=360)
				Entry(win, width=10, bd=10, textvariable=penguapan_4jam).place(x=440, y=355)
			else :
				Frame(win, width=200, height=220, bg='cadet blue' ).place(x=340, y=230)
				#tktexter.messagebox.showwarning("Peringatan", "Anda belum memilih Waktu Pengamatan")
		
		buka = Button(win, text="Buka", bg="green", fg="white", width=8, bd=10, font="callibri 12 bold", command=Buka)
		buka.place(x=390, y=175)
		
		def save():
			wp = (waktu_pengamatanOpenPan.get())
			if (wp == "07.15"):
				#simpan entry ke variabel
				jam_07_15 = wp
				
				KetinggianAirPanci_07_15=ketinggianAirPanci.get()
				SuhuAirMax_07_15=suhuAirMax.get()
				SuhuAirMin_07_15=suhuAirMin.get()
				
				Hujan_13_5jam_07_15=hujan_13_5jam.get()
				Hujan_24jam_07_15=hujan_24jam.get()
				Penguapan_24jam_07_15=penguapan_24jam.get()
				
				#simpan ke database
				con = pymysql.connect("localhost", "root", "12345", "Buku_Klimatologi_BMKG")
				#with con.cursor() as cursor:
				#	cursor.execute("CREATE TABLE Open_Pan_0715_1 (Waktu text, ketinggian_airpanci07_15 text, suhu_airmax07_15 text, suhu_airmin07_15 text, hujan_13_5jam07_15 text, hujan_24jam_07_15 text, penguapan_24jam_07_15 text)")
				with con.cursor() as cursor:
					sql12 = "INSERT INTO Open_Pan_0715_1 (Waktu, ketinggian_airpanci07_15, suhu_airmax07_15, suhu_airmin07_15, hujan_13_5jam07_15, hujan_24jam_07_15, penguapan_24jam_07_15)\
							VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (TahunBulanTanggal, KetinggianAirPanci_07_15, SuhuAirMax_07_15, SuhuAirMin_07_15, Hujan_13_5jam_07_15, Hujan_24jam_07_15, Penguapan_24jam_07_15)
					cursor.execute(sql12)
					con.commit()
				
				#bersihkan entry
				hujan_13_5jam.set("")
				hujan_24jam.set("")
				penguapan_24jam.set("")
				
			elif (wp == "07.45"):
				#simpan entry ke variabel
				jam_07_45 = wp
				
				KetinggianAirPanci_07_45=ketinggianAirPanci.get()
				SuhuAirMax_07_45=suhuAirMax.get()
				SuhuAirMin_07_45=suhuAirMin.get()				
				
				Hujan_30menit_07_45=hujan_30menit.get()
				Penguapan_13_5jam_07_45=penguapan_13_5jam.get()
				
				#simpan ke database
				con = pymysql.connect("localhost", "root", "12345", "Buku_Klimatologi_BMKG")
				#with con.cursor() as cursor:
				#	cursor.execute("CREATE TABLE Open_Pan_0745_2 (Waktu text, ketinggian_airpanci07_45 text, suhu_airmax07_45 text, suhu_airmin07_45 text, hujan_30menit07_45 text, penguapan_13_5jam07_45 text)")
				with con.cursor() as cursor:
					sql13 = "INSERT INTO Open_Pan_0745_2 (Waktu, ketinggian_airpanci07_45, suhu_airmax07_45, suhu_airmin07_45, hujan_30menit07_45, penguapan_13_5jam07_45)\
							VALUES('%s', '%s', '%s', '%s', '%s', '%s')" % (TahunBulanTanggal, KetinggianAirPanci_07_45, SuhuAirMax_07_45, SuhuAirMin_07_45, Hujan_30menit_07_45, Penguapan_13_5jam_07_45)
					cursor.execute(sql13)
					con.commit()
				
				#bersihkan entry
				hujan_30menit.set("")
				penguapan_13_5jam.set("")
 			
			elif (wp == str(13.45)):
				#simpan entry ke variabel
				jam_13_15 = wp
				
				KetinggianAirPanci_13_45=ketinggianAirPanci.get()
				SuhuAirMax_13_45=suhuAirMax.get()
				SuhuAirMin_13_45=suhuAirMin.get()
				
				Hujan_6jam_13_45=hujan_6jam.get()
				Penguapan_6jam_13_45=penguapan_6jam.get()
				
				#simpan ke database
				con = pymysql.connect("localhost", "root", "12345", "Buku_Klimatologi_BMKG")
				#with con.cursor() as cursor:
				#	cursor.execute("CREATE TABLE Open_Pan_1345_1 (Waktu text, ketinggian_airpanci13_45 text, suhu_airmax13_45 text, suhu_airmin13_45 text, hujan_6jam_13_45 text, penguapan_6jam_13_45 text)")
				with con.cursor() as cursor:
					sql14 = "INSERT INTO Open_Pan_1345_1 (Waktu, ketinggian_airpanci13_45, suhu_airmax13_45, suhu_airmin13_45, hujan_6jam_13_45, penguapan_6jam_13_45)\
						VALUES('%s', '%s', '%s', '%s', '%s', '%s')" % (TahunBulanTanggal, KetinggianAirPanci_13_45, SuhuAirMax_13_45, SuhuAirMin_13_45, Hujan_6jam_13_45, Penguapan_6jam_13_45)
					cursor.execute(sql14)
					con.commit()
		
				#bersihkan entry
				hujan_6jam.set("")
				penguapan_6jam.set("")
			
			elif (wp == str(17.45)):
				#simpan entry ke variabel
				jam_17_15 = wp
				
				KetinggianAirPanci_17_45=ketinggianAirPanci.get()
				SuhuAirMax_17_45=suhuAirMax.get()
				SuhuAirMin_17_45=suhuAirMin.get()
				
				Hujan_4jam_17_45=hujan_4jam.get()
				Penguapan_4jam_17_45=penguapan_4jam.get()
				
				#simpan ke database
				con = pymysql.connect("localhost", "root", "12345", "Buku_Klimatologi_BMKG")
				#with con.cursor() as cursor:
				#	cursor.execute("CREATE TABLE Open_Pan_1745_1 (Waktu text, ketinggian_airpanci17_45 text, suhu_airmax17_45 text, suhu_airmin17_45 text, hujan_4jam_17_45 text, penguapan_4jam_17_45 text)")
				with con.cursor() as cursor:
					sql14 = "INSERT INTO Open_Pan_1745_1 (Waktu, ketinggian_airpanci17_45, suhu_airmax17_45, suhu_airmin17_45, hujan_4jam_17_45, penguapan_4jam_17_45)\
						VALUES('%s', '%s', '%s', '%s', '%s', '%s')" % (TahunBulanTanggal, KetinggianAirPanci_17_45, SuhuAirMax_17_45, SuhuAirMin_17_45, Hujan_4jam_17_45, Penguapan_4jam_17_45)
					cursor.execute(sql14)
					con.commit()
					
				#bersihkan entry
				hujan_4jam.set("")
				penguapan_4jam.set("")
			else:
				tkinter.messagebox.showwarning("Peringatan", "Anda belum memilih Waktu Pengamatan")			
			
			waktu_pengamatanOpenPan.set("-- Pilih Waktu Pengamatan --")
			ketinggianAirPanci.set("")
			suhuAirMax.set("")
			suhuAirMin.set("")
			
		#SAVE DAN EXIT
		simpan = Button(win, text="SIMPAN", bg="blue", fg="white", width=8, bd=5, font="callibri 12 bold", command=save)
		simpan.place(x=700 , y=540)
	"""--------------------------------------------- AKHIR FUNGSI OPEN PAN -------------------------------------------"""
	
	"""----------------------------------------------- FUNGSI PICHE EVAPORATOR ------------------------------------------"""
	def piche_evaporator():
		Frame(win, width=864, height=630, bg='cadet blue' ).place(x=0, y=0)
	
		#JUDUL ALAT PICHE EVAPORATOR (PE)
		pe = Label(win, text=" PICHE EVAPORIMETER ", bg="black", fg="cadet blue", font="callibri 24 bold")
		pe.place(x=30, y=30)
		
		#TABEL TEMPAT PENGISIAN NILAI
		picheEvaporator_07_45_1 = StringVar()
		picheEvaporator_07_45_2 = StringVar()
		picheEvaporator_13_45_1 = StringVar()
		picheEvaporator_13_45_2 = StringVar()
		picheEvaporator_17_45_1 = StringVar()
		picheEvaporator_17_45_2 = StringVar()
		
		#Baris 1
		Label(win, text="Waktu", bg="cadet blue", font="callibri 12").place(x=90, y=140)
		Label(win, text="Ketinggian Air di Piche 1.2 m", bg="cadet blue", font="callibri 12").place(x=150, y=140)
		
		#Baris 2 dan Entry
		Label(win, text="07.45", bg="cadet blue", font="callibri 12").place(x=90, y=210)
		Entry(win, width=10, bd=10, textvariable=picheEvaporator_07_45_1).place(x=210, y=180)
		Entry(win, width=10, bd=10, textvariable=picheEvaporator_07_45_2).place(x=210, y=210)
		
		#Baris 2 dan Entry
		Label(win, text="13.45", bg="cadet blue", font="callibri 12").place(x=90, y=290)
		Entry(win, width=10, bd=10, textvariable=picheEvaporator_13_45_1).place(x=210, y=260)
		Entry(win, width=10, bd=10, textvariable=picheEvaporator_13_45_2).place(x=210, y=290)
		
		#Baris 3 dan Entry
		Label(win, text="17.45", bg="cadet blue", font="callibri 12").place(x=90, y=370)
		Entry(win, width=10, bd=10, textvariable=picheEvaporator_17_45_1).place(x=210, y=340)
		Entry(win, width=10, bd=10, textvariable=picheEvaporator_17_45_2).place(x=210, y=370)
		
		def save():
			#simpan entry ke variabel sementara
			Piche_Evaporimeter1_0745 = picheEvaporator_07_45_1.get()
			Piche_Evaporimeter2_0745 = picheEvaporator_07_45_2.get()
			Piche_Evaporimeter1_1345 = picheEvaporator_13_45_1.get()
			Piche_Evaporimeter2_1345 = picheEvaporator_13_45_2.get()
			Piche_Evaporimeter1_1745 = picheEvaporator_17_45_1.get()
			Piche_Evaporimeter2_1745 = picheEvaporator_17_45_2.get()
			
			#simpan ke database
			con =  pymysql.connect("localhost", "root", "12345", "Buku_Klimatologi_BMKG")
			#with con.cursor() as cursor:
			#	cursor.execute("CREATE TABLE Piche_Evaporimeter_1(Waktu text, piche_evaporimeter1_07_45 text, piche_evaporimeter2_07_45 text, piche_evaporimeter1_13_45 text,\
			#		piche_evaporimeter2_13_45 text, piche_evaporimeter1_17_45 text,piche_evaporimeter2_17_45 text)")
			with con.cursor() as cursor:
				sql16 = "INSERT INTO Piche_Evaporimeter_1(Waktu, piche_evaporimeter1_07_45, piche_evaporimeter2_07_45, piche_evaporimeter1_13_45, piche_evaporimeter2_13_45,\
						piche_evaporimeter1_17_45, piche_evaporimeter2_17_45) VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (TahunBulanTanggal, Piche_Evaporimeter1_0745, Piche_Evaporimeter2_0745,\
						Piche_Evaporimeter1_1345, Piche_Evaporimeter2_1345, Piche_Evaporimeter1_1745, Piche_Evaporimeter2_1745)
				cursor.execute(sql16)
				con.commit()
			
			#bersihkan entry
			picheEvaporator_07_45_1.set("")
			picheEvaporator_07_45_2.set("")
			picheEvaporator_13_45_1.set("")
			picheEvaporator_13_45_2.set("")
			picheEvaporator_17_45_1.set("")
			picheEvaporator_17_45_2.set("")
		
		#SAVE DAN EXIT
		simpan = Button(win, text="SIMPAN", bg="blue", fg="white", width=8, bd=5, font="callibri 12 bold", command=save)
		simpan.place(x=700 , y=540)
	"""------------------------------------------- AKHIR FUNGSI PICHE EVAPORATOR ------------------------------------------"""
	
	"""-------------------------------------------- FUNGSI PSYCHROMETER ASSMANN ------------------------------------------"""
	def psychrometer_assmann():
		Frame(win, width=864, height=630, bg='cadet blue' ).place(x=0, y=0)

		#JUDUL ALAT PSYCHROMETER ASSMANN (PA)
		pa = Label(win, text="PSYCHROMETER ASSMANN", bg="cadet blue", fg="black", font="callibri 24 bold")
		pa.place(x=30, y=30)
		
		#Pilihan Waktu Pengamatan (PWP)
		waktu_pengamatanPsychrometerAssmann = StringVar()
		jam_07_45 = StringVar()
		jam_13_45 = StringVar()
		jam_17_45 = StringVar()
		
		waktu = ["-- Pilih Waktu Pengamatan --", "07.45", "13.45", "17.45"]
		pilihan_waktu = ttk.Combobox(win, values = waktu, width = 22, font="callibri 12", state='readonly', textvariable=waktu_pengamatanPsychrometerAssmann)
		pilihan_waktu.place(x=30, y=120)
		pilihan_waktu.current(0)
		
		#TABEL TEMPAT PENGISIAN NILAI
		
		psyAssmann_BK5cm = StringVar()
		psyAssmann_BK10cm = StringVar()
		psyAssmann_BK20cm = StringVar()
		psyAssmann_BK50cm = StringVar()
		psyAssmann_BK100cm = StringVar()
		psyAssmann_BK150cm = StringVar()
		psyAssmann_BK200cm = StringVar()
		
		psyAssmann_BB5cm = StringVar()
		psyAssmann_BB10cm = StringVar()
		psyAssmann_BB20cm = StringVar()
		psyAssmann_BB50cm = StringVar()
		psyAssmann_BB100cm = StringVar()
		psyAssmann_BB150cm = StringVar()
		psyAssmann_BB200cm = StringVar()
		
		psyAssmann_RH5cm = StringVar()
		psyAssmann_RH10cm = StringVar()
		psyAssmann_RH20cm = StringVar()
		psyAssmann_RH50cm = StringVar()
		psyAssmann_RH100cm = StringVar()
		psyAssmann_RH150cm = StringVar()
		psyAssmann_RH200cm = StringVar()
	
		#Kolom 1
		Label(win, text="Tinggi", bg="cadet blue", font="callibri 12").place(x=30, y=260)
		Label(win, text="5 cm", bg="cadet blue", font="callibri 12").place(x=50, y=300)
		Label(win, text="10 cm", bg="cadet blue", font="callibri 12").place(x=40, y=340)
		Label(win, text="20 cm", bg="cadet blue", font="callibri 12").place(x=40, y=380)
		Label(win, text="50 cm", bg="cadet blue", font="callibri 12").place(x=40, y=420)
		Label(win, text="100 cm", bg="cadet blue", font="callibri 12").place(x=30, y=460)
		Label(win, text="150 cm", bg="cadet blue", font="callibri 12").place(x=30, y=500)
		Label(win, text="200 cm", bg="cadet blue", font="callibri 12").place(x=30, y=540)
		
		#Kolom 2 dan Entry
		Label(win, text="BK", bg="cadet blue", font="callibri 12").place(x=200, y=260)
		Entry(win, width=10, bd=10, textvariable=psyAssmann_BK5cm).place(x=185, y=300)
		Entry(win, width=10, bd=10, textvariable=psyAssmann_BK10cm).place(x=185, y=340)
		Entry(win, width=10, bd=10, textvariable=psyAssmann_BK20cm).place(x=185, y=380)
		Entry(win, width=10, bd=10, textvariable=psyAssmann_BK50cm).place(x=185, y=420)
		Entry(win, width=10, bd=10, textvariable=psyAssmann_BK100cm).place(x=185, y=460)
		Entry(win, width=10, bd=10, textvariable=psyAssmann_BK150cm).place(x=185, y=500)
		Entry(win, width=10, bd=10, textvariable=psyAssmann_BK200cm).place(x=185, y=540)
		
		#Kolom 3 dan Entry
		Label(win, text="BB", bg="cadet blue", font="callibri 12").place(x=360, y=260)
		Entry(win, width=10, bd=10, textvariable=psyAssmann_BB5cm).place(x=335, y=300)
		Entry(win, width=10, bd=10, textvariable=psyAssmann_BB10cm).place(x=335, y=340)
		Entry(win, width=10, bd=10, textvariable=psyAssmann_BB20cm).place(x=335, y=380)
		Entry(win, width=10, bd=10, textvariable=psyAssmann_BB50cm).place(x=335, y=420)
		Entry(win, width=10, bd=10, textvariable=psyAssmann_BB100cm).place(x=335, y=460)
		Entry(win, width=10, bd=10, textvariable=psyAssmann_BB150cm).place(x=335, y=500)
		Entry(win, width=10, bd=10, textvariable=psyAssmann_BB200cm).place(x=335, y=540)
		
		#Kolom 4 dan Entry
		Label(win, text="RH", bg="cadet blue", font="callibri 12").place(x=520, y=260)
		Entry(win, width=10, bd=10, textvariable=psyAssmann_RH5cm).place(x=495, y=300)
		Entry(win, width=10, bd=10, textvariable=psyAssmann_RH10cm).place(x=495, y=340)
		Entry(win, width=10, bd=10, textvariable=psyAssmann_RH20cm).place(x=495, y=380)
		Entry(win, width=10, bd=10, textvariable=psyAssmann_RH50cm).place(x=495, y=420)
		Entry(win, width=10, bd=10, textvariable=psyAssmann_RH100cm).place(x=495, y=460)
		Entry(win, width=10, bd=10, textvariable=psyAssmann_RH150cm).place(x=495, y=500)
		Entry(win, width=10, bd=10, textvariable=psyAssmann_RH200cm).place(x=495, y=540)
		
		def save():
			#simpan entry ke variabel
			wp = (waktu_pengamatanPsychrometerAssmann.get())
			if (wp == "07.45"):
				jam_07_45 = wp
				
				#ambil nilai dari entry
				PsyAssmann_BK5cm_07_45=psyAssmann_BK5cm.get()
				PsyAssmann_BK10cm_07_45=psyAssmann_BK10cm.get()
				PsyAssmann_BK20cm_07_45=psyAssmann_BK20cm.get()
				PsyAssmann_BK50cm_07_45=psyAssmann_BK50cm.get()
				PsyAssmann_BK100cm_07_45=psyAssmann_BK100cm.get()
				PsyAssmann_BK150cm_07_45=psyAssmann_BK150cm.get()
				PsyAssmann_BK200cm_07_45=psyAssmann_BK200cm.get()
				
				PsyAssmann_BB5cm_07_45=psyAssmann_BB5cm.get()
				PsyAssmann_BB10cm_07_45=psyAssmann_BB10cm.get()
				PsyAssmann_BB20cm_07_45=psyAssmann_BB20cm.get()
				PsyAssmann_BB50cm_07_45=psyAssmann_BB50cm.get()
				PsyAssmann_BB100cm_07_45=psyAssmann_BB100cm.get()
				PsyAssmann_BB150cm_07_45=psyAssmann_BB150cm.get()
				PsyAssmann_BB200cm_07_45=psyAssmann_BB200cm.get()
				
				PsyAssmann_RH5cm_07_45=psyAssmann_RH5cm.get()
				PsyAssmann_RH10cm_07_45=psyAssmann_RH10cm.get()
				PsyAssmann_RH20cm_07_45=psyAssmann_RH20cm.get()
				PsyAssmann_RH50cm_07_45=psyAssmann_RH50cm.get()
				PsyAssmann_RH100cm_07_45=psyAssmann_RH100cm.get()
				PsyAssmann_RH150cm_07_45=psyAssmann_RH150cm.get()
				PsyAssmann_RH200cm_07_45=psyAssmann_RH200cm.get()
				
				#simpan ke database
				con = pymysql.connect("localhost", "root", "12345", "Buku_Klimatologi_BMKG")
				#with con.cursor() as cursor:
				#	cursor.execute("CREATE TABLE Psychrometer_Assmann0745_1(Waktu text, passmannBK5_0745 text, passmannBB5_0745 text, passmannRH5_0745 text,\
				#		passmannBK10_0745 text, passmannBB10_0745 text, passmannRH10_0745 text,passmannBK20_0745 text, passmannBB20_0745 text, passmannRH20_0745 text,\
				#		passmannBK50_0745 text, passmannBB50_0745 text, passmannRH50_0745 text,passmannBK100_0745 text, passmannBB100_0745 text, passmannRH100_0745 text,\
				#		passmannBK150_0745 text, passmannBB150_0745 text, passmannRH150_0745 text,passmannBK200_0745 text, passmannBB200_0745 text, passmannRH200_0745 text)")
				with con.cursor() as cursor:
					sql17 = "INSERT INTO Psychrometer_Assmann0745_1(Waktu, passmannBK5_0745, passmannBB5_0745, passmannRH5_0745,\
							passmannBK10_0745, passmannBB10_0745, passmannRH10_0745, passmannBK20_0745, passmannBB20_0745, passmannRH20_0745,\
							passmannBK50_0745, passmannBB50_0745, passmannRH50_0745, passmannBK100_0745, passmannBB100_0745, passmannRH100_0745,\
							passmannBK150_0745, passmannBB150_0745, passmannRH150_0745, passmannBK200_0745, passmannBB200_0745, passmannRH200_0745)\
							VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')"\
							% (TahunBulanTanggal, PsyAssmann_BK5cm_07_45, PsyAssmann_BB5cm_07_45, PsyAssmann_RH5cm_07_45, PsyAssmann_BK10cm_07_45, PsyAssmann_BB10cm_07_45, PsyAssmann_RH10cm_07_45,\
							PsyAssmann_BK20cm_07_45, PsyAssmann_BB20cm_07_45, PsyAssmann_RH20cm_07_45, PsyAssmann_BK50cm_07_45, PsyAssmann_BB50cm_07_45, PsyAssmann_RH50cm_07_45,\
							PsyAssmann_BK100cm_07_45, PsyAssmann_BB100cm_07_45, PsyAssmann_RH100cm_07_45, PsyAssmann_BK150cm_07_45, PsyAssmann_BB150cm_07_45, PsyAssmann_RH150cm_07_45,\
							PsyAssmann_BK200cm_07_45, PsyAssmann_BB200cm_07_45, PsyAssmann_RH200cm_07_45)
					cursor.execute(sql17)
					con.commit()
					
			elif (wp == str(13.45)):
				jam_13_45 = wp
				
				#ambil nilai dari entry
				PsyAssmann_BK5cm_13_45=psyAssmann_BK5cm.get()
				PsyAssmann_BK10cm_13_45=psyAssmann_BK10cm.get()
				PsyAssmann_BK20cm_13_45=psyAssmann_BK20cm.get()
				PsyAssmann_BK50cm_13_45=psyAssmann_BK50cm.get()
				PsyAssmann_BK100cm_13_45=psyAssmann_BK100cm.get()
				PsyAssmann_BK150cm_13_45=psyAssmann_BK150cm.get()
				PsyAssmann_BK200cm_13_45=psyAssmann_BK200cm.get()
				
				PsyAssmann_BB5cm_13_45=psyAssmann_BB5cm.get()
				PsyAssmann_BB10cm_13_45=psyAssmann_BB10cm.get()
				PsyAssmann_BB20cm_13_45=psyAssmann_BB20cm.get()
				PsyAssmann_BB50cm_13_45=psyAssmann_BB50cm.get()
				PsyAssmann_BB100cm_13_45=psyAssmann_BB100cm.get()
				PsyAssmann_BB150cm_13_45=psyAssmann_BB150cm.get()
				PsyAssmann_BB200cm_13_45=psyAssmann_BB200cm.get()
				
				PsyAssmann_RH5cm_13_45=psyAssmann_RH5cm.get()
				PsyAssmann_RH10cm_13_45=psyAssmann_RH10cm.get()
				PsyAssmann_RH20cm_13_45=psyAssmann_RH20cm.get()
				PsyAssmann_RH50cm_13_45=psyAssmann_RH50cm.get()
				PsyAssmann_RH100cm_13_45=psyAssmann_RH100cm.get()
				PsyAssmann_RH150cm_13_45=psyAssmann_RH150cm.get()
				PsyAssmann_RH200cm_13_45=psyAssmann_RH200cm.get()
				
				con = pymysql.connect("localhost", "root", "12345", "Buku_Klimatologi_BMKG")
				#with con.cursor() as cursor:
				#	cursor.execute("CREATE TABLE Psychrometer_Assmann1345_1(Waktu text, passmannBK5_1345 text, passmannBB5_1345 text, passmannRH5_1345 text,\
				#		passmannBK10_1345 text, passmannBB10_1345 text, passmannRH10_1345 text,passmannBK20_1345 text, passmannBB20_1345 text, passmannRH20_1345 text,\
				#		passmannBK50_1345 text, passmannBB50_1345 text, passmannRH50_1345 text,passmannBK100_1345 text, passmannBB100_1345 text, passmannRH100_1345 text,\
				#		passmannBK150_1345 text, passmannBB150_1345 text, passmannRH150_1345 text,passmannBK200_1345 text, passmannBB200_1345 text, passmannRH200_1345 text)")
				with con.cursor() as cursor:
					sql18 = "INSERT INTO Psychrometer_Assmann1345_1(Waktu, passmannBK5_1345, passmannBB5_1345, passmannRH5_1345,\
							passmannBK10_1345, passmannBB10_1345, passmannRH10_1345, passmannBK20_1345, passmannBB20_1345, passmannRH20_1345,\
							passmannBK50_1345, passmannBB50_1345, passmannRH50_1345, passmannBK100_1345, passmannBB100_1345, passmannRH100_1345,\
							passmannBK150_1345, passmannBB150_1345, passmannRH150_1345, passmannBK200_1345, passmannBB200_1345, passmannRH200_1345)\
							VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')"\
							% (TahunBulanTanggal, PsyAssmann_BK5cm_13_45, PsyAssmann_BB5cm_13_45, PsyAssmann_RH5cm_13_45, PsyAssmann_BK10cm_13_45, PsyAssmann_BB10cm_13_45, PsyAssmann_RH10cm_13_45,\
							PsyAssmann_BK20cm_13_45, PsyAssmann_BB20cm_13_45, PsyAssmann_RH20cm_13_45, PsyAssmann_BK50cm_13_45, PsyAssmann_BB50cm_13_45, PsyAssmann_RH50cm_13_45,\
							PsyAssmann_BK100cm_13_45, PsyAssmann_BB100cm_13_45, PsyAssmann_RH100cm_13_45, PsyAssmann_BK150cm_13_45, PsyAssmann_BB150cm_13_45, PsyAssmann_RH150cm_13_45,\
							PsyAssmann_BK200cm_13_45, PsyAssmann_BB200cm_13_45, PsyAssmann_RH200cm_13_45)
					cursor.execute(sql18)
					con.commit()
				
				
			elif (wp == str(17.45)):
				jam_17_45 = wp
				
				#ambil nilai dari entry
				PsyAssmann_BK5cm_17_45=psyAssmann_BK5cm.get()
				PsyAssmann_BK10cm_17_45=psyAssmann_BK10cm.get()
				PsyAssmann_BK20cm_17_45=psyAssmann_BK20cm.get()
				PsyAssmann_BK50cm_17_45=psyAssmann_BK50cm.get()
				PsyAssmann_BK100cm_17_45=psyAssmann_BK100cm.get()
				PsyAssmann_BK150cm_17_45=psyAssmann_BK150cm.get()
				PsyAssmann_BK200cm_17_45=psyAssmann_BK200cm.get()
				
				PsyAssmann_BB5cm_17_45=psyAssmann_BB5cm.get()
				PsyAssmann_BB10cm_17_45=psyAssmann_BB10cm.get()
				PsyAssmann_BB20cm_17_45=psyAssmann_BB20cm.get()
				PsyAssmann_BB50cm_17_45=psyAssmann_BB50cm.get()
				PsyAssmann_BB100cm_17_45=psyAssmann_BB100cm.get()
				PsyAssmann_BB150cm_17_45=psyAssmann_BB150cm.get()
				PsyAssmann_BB200cm_17_45=psyAssmann_BB200cm.get()
				
				PsyAssmann_RH5cm_17_45=psyAssmann_RH5cm.get()
				PsyAssmann_RH10cm_17_45=psyAssmann_RH10cm.get()
				PsyAssmann_RH20cm_17_45=psyAssmann_RH20cm.get()
				PsyAssmann_RH50cm_17_45=psyAssmann_RH50cm.get()
				PsyAssmann_RH100cm_17_45=psyAssmann_RH100cm.get()
				PsyAssmann_RH150cm_17_45=psyAssmann_RH150cm.get()
				PsyAssmann_RH200cm_17_45=psyAssmann_RH200cm.get()		

				con = pymysql.connect("localhost", "root", "12345", "Buku_Klimatologi_BMKG")
				#with con.cursor() as cursor:
				#	cursor.execute("CREATE TABLE Psychrometer_Assmann1745_2 (Waktu text, passmannBK5_1745 text, passmannBB5_1745 text, passmannRH5_1745 text,\
				#		passmannBK10_1745 text, passmannBB10_1745 text, passmannRH10_1745 text,passmannBK20_1745 text, passmannBB20_1745 text, passmannRH20_1745 text,\
				#		passmannBK50_1745 text, passmannBB50_1745 text, passmannRH50_1745 text,passmannBK100_1745 text, passmannBB100_1745 text, passmannRH100_1745 text,\
				#		passmannBK150_1745 text, passmannBB150_1745 text, passmannRH150_1745 text,passmannBK200_1745 text, passmannBB200_1745 text, passmannRH200_1745 text)")
				with con.cursor() as cursor:
					sql19 = "INSERT INTO Psychrometer_Assmann1745_2(Waktu, passmannBK5_1745, passmannBB5_1745, passmannRH5_1745,\
							passmannBK10_1745, passmannBB10_1745, passmannRH10_1745, passmannBK20_1745, passmannBB20_1745, passmannRH20_1745,\
							passmannBK50_1745, passmannBB50_1745, passmannRH50_1745, passmannBK100_1745, passmannBB100_1745, passmannRH100_1745,\
							passmannBK150_1745, passmannBB150_1745, passmannRH150_1745, passmannBK200_1745, passmannBB200_1745, passmannRH200_1745)\
							VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')"\
							% (TahunBulanTanggal, PsyAssmann_BK5cm_17_45, PsyAssmann_BB5cm_17_45, PsyAssmann_RH5cm_17_45, PsyAssmann_BK10cm_17_45, PsyAssmann_BB10cm_17_45, PsyAssmann_RH10cm_17_45,\
							PsyAssmann_BK20cm_17_45, PsyAssmann_BB20cm_17_45, PsyAssmann_RH20cm_17_45, PsyAssmann_BK50cm_17_45, PsyAssmann_BB50cm_17_45, PsyAssmann_RH50cm_17_45,\
							PsyAssmann_BK100cm_17_45, PsyAssmann_BB100cm_17_45, PsyAssmann_RH100cm_17_45, PsyAssmann_BK150cm_17_45, PsyAssmann_BB150cm_17_45, PsyAssmann_RH150cm_17_45,\
							PsyAssmann_BK200cm_17_45, PsyAssmann_BB200cm_17_45, PsyAssmann_RH200cm_17_45)
					cursor.execute(sql19)
					con.commit()
				
			else:
				tkinter.messagebox.showwarning("Peringatan", "Anda belum memilih Waktu Pengamatan")	
				
			#bersihkan entry
			waktu_pengamatanPsychrometerAssmann.set("-- Pilih Waktu Pengamatan --")
			
			psyAssmann_BK5cm.set("")
			psyAssmann_BK10cm.set("")
			psyAssmann_BK20cm.set("")
			psyAssmann_BK50cm.set("")
			psyAssmann_BK100cm.set("")
			psyAssmann_BK150cm.set("")
			psyAssmann_BK200cm.set("")
			
			psyAssmann_BB5cm.set("")
			psyAssmann_BB10cm.set("")
			psyAssmann_BB20cm.set("")
			psyAssmann_BB50cm.set("")
			psyAssmann_BB100cm.set("")
			psyAssmann_BB150cm.set("")
			psyAssmann_BB200cm.set("")
			
			psyAssmann_RH5cm.set("")
			psyAssmann_RH10cm.set("")
			psyAssmann_RH20cm.set("")
			psyAssmann_RH50cm.set("")
			psyAssmann_RH100cm.set("")
			psyAssmann_RH150cm.set("")
			psyAssmann_RH200cm.set("")
			
		#SAVE DAN EXIT
		simpan = Button(win, text="SIMPAN", bg="blue", fg="white", width=8, bd=5, font="callibri 12 bold", command=save)
		simpan.place(x=700 , y=540)
	"""------------------------------------------- AKHIR FUNGSI PSYCHROMETER ASSMANN -----------------------------------"""
	
	"""---------------------------------------- FUNGSI PSYCHROMETER SANGKAR METEOROLOGI --------------------------------"""
	def psychrometer_sangkarMeteorologi():
		Frame(win, width=864, height=630, bg='cadet blue' ).place(x=0, y=0)
		
		#JUDUL ALAT PSYCHROMETER SANGKAR METEOROLOGI (PSM)
		psm = Label(win, text=" PSYCHROMETER SANGKAR METEOROLOGI ", bg="black", fg="cadet blue", font="callibri 24 bold")
		psm.place(x=30, y=30)
		
		#Pilihan Waktu Pengamatan (PWP)
		waktu_pengamatanPsychrometerSangkar = StringVar()
		jam_07_15 = StringVar()
		jam_07_45 = StringVar()
		jam_13_15 = StringVar()
		jam_13_45 = StringVar()
		jam_14_15 = StringVar()
		jam_17_45 = StringVar()
		jam_18_15 = StringVar()
		
		waktu = ["-- Pilih Waktu Pengamatan --", "07.15", "07.45", "13.15", "13.45", "14.15", "17.45", "18.15"]
		pilihan_waktu = ttk.Combobox(win, values = waktu, width = 22, font="callibri 12", state='readonly', textvariable=waktu_pengamatanPsychrometerSangkar)
		pilihan_waktu.place(x=30, y=120)
		pilihan_waktu.current(0)
		
		#TABEL TEMPAT PENGISIAN NILAI
		psychrometer_Tbk1_2m = StringVar()
		psychrometer_Tbk4m = StringVar()
		psychrometer_Tbk7m = StringVar()
		psychrometer_Tbk10m = StringVar()
		
		psychrometer_Tbb1_2m = StringVar()
		psychrometer_Tbb4m = StringVar()
		psychrometer_Tbb7m = StringVar()
		psychrometer_Tbb10m = StringVar()
		
		psychrometer_RH1_2m = StringVar()
		psychrometer_RH4m = StringVar()
		psychrometer_RH7m = StringVar()
		psychrometer_RH10m = StringVar()
			
		#kolom
		Label(win, text="1.2 m", bg="cadet blue", font="callibri 12").place(x=120, y=350)
		Label(win, text="4 m", bg="cadet blue", font="callibri 12").place(x=240, y=350)
		Label(win, text="7 m", bg="cadet blue", font="callibri 12").place(x=360, y=350)
		Label(win, text="10 m", bg="cadet blue", font="callibri 12").place(x=480, y=350)
		
		#baris
		Label(win, text="Tbk", bg="cadet blue", font="callibri 12").place(x=30, y=400)
		Label(win, text="Tbb", bg="cadet blue", font="callibri 12").place(x=30, y=460)
		Label(win, text="RH", bg="cadet blue", font="callibri 12").place(x=30, y=520)
		
		#Kotak Entry kolom 1
		Entry(win, width=10, bd=10, textvariable=psychrometer_Tbk1_2m).place(x=110, y=400)
		Entry(win, width=10, bd=10, textvariable=psychrometer_Tbb1_2m).place(x=110, y=460)
		Entry(win, width=10, bd=10, textvariable=psychrometer_RH1_2m).place(x=110, y=520)
		#Kotak Entry kolom 2
		Entry(win, width=10, bd=10, textvariable=psychrometer_Tbk4m).place(x=230, y=400)
		Entry(win, width=10, bd=10, textvariable=psychrometer_Tbb4m).place(x=230, y=460)
		Entry(win, width=10, bd=10, textvariable=psychrometer_RH4m).place(x=230, y=520)
		#Kotak Entry kolom 3
		Entry(win, width=10, bd=10, textvariable=psychrometer_Tbk7m).place(x=350, y=400)
		Entry(win, width=10, bd=10, textvariable=psychrometer_Tbb7m).place(x=350, y=460)
		Entry(win, width=10, bd=10, textvariable=psychrometer_RH7m).place(x=350, y=520)
		#Kotak Entry kolom 4
		Entry(win, width=10, bd=10, textvariable=psychrometer_Tbk10m).place(x=470, y=400)
		Entry(win, width=10, bd=10, textvariable=psychrometer_Tbb10m).place(x=470, y=460)
		Entry(win, width=10, bd=10, textvariable=psychrometer_RH10m).place(x=470, y=520)
		
		def save():
			#simpan entry ke variabel
			wp = (waktu_pengamatanPsychrometerSangkar.get())
			
			if (wp == "07.15"):
				jam_07_15 = wp
				
				Psychrometer_Tbk1_2m_07_15=psychrometer_Tbk1_2m.get()
				Psychrometer_Tbk4m_07_15=psychrometer_Tbk4m.get()
				Psychrometer_Tbk7m_07_15=psychrometer_Tbk7m.get()
				Psychrometer_Tbk10m_07_15=psychrometer_Tbk10m.get()
				
				Psychrometer_Tbb1_2m_07_15=psychrometer_Tbb1_2m.get()
				Psychrometer_Tbb4m_07_15=psychrometer_Tbb4m.get()
				Psychrometer_Tbb7m_07_15=psychrometer_Tbb7m.get()
				Psychrometer_Tbb10m_07_15=psychrometer_Tbb10m.get()
				
				Psychrometer_RH1_2m_07_15=psychrometer_RH1_2m.get()
				Psychrometer_RH4m_07_15=psychrometer_RH4m.get()
				Psychrometer_RH7m_07_15=psychrometer_RH7m.get()
				Psychrometer_RH10m_07_15=psychrometer_RH10m.get()
				
				#simpan ke database
				con = pymysql.connect("localhost", "root", "12345", "Buku_Klimatologi_BMKG")
				#with con.cursor() as cursor:
				#	cursor.execute("CREATE TABLE Psychrometer_Sangkar_Meteo0715_1 (Waktu text, psmeteoTbk1_2_0715 text, psmeteoTbk4_0715 text, psmeteoTbk7_0715 text, psmeteoTbk10_0715 text,\
				#		psmeteoTbb1_2_0715 text, psmeteoTbb4_0715 text, psmeteoTbb7_0715 text, psmeteoTbb10_0715 text, psmeteoRH1_2_0715 text, psmeteoRH4_0715 text, psmeteoRH7_0715 text, psmeteoRH10_0715 text)")
				with con.cursor() as cursor:
					sql20 = "INSERT INTO Psychrometer_Sangkar_Meteo0715_1 (Waktu, psmeteoTbk1_2_0715, psmeteoTbk4_0715, psmeteoTbk7_0715, psmeteoTbk10_0715, psmeteoTbb1_2_0715, psmeteoTbb4_0715,\
							psmeteoTbb7_0715, psmeteoTbb10_0715, psmeteoRH1_2_0715, psmeteoRH4_0715, psmeteoRH7_0715, psmeteoRH10_0715) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')"\
							% (TahunBulanTanggal, Psychrometer_Tbk1_2m_07_15, Psychrometer_Tbk4m_07_15, Psychrometer_Tbk7m_07_15, Psychrometer_Tbk10m_07_15, Psychrometer_Tbb1_2m_07_15,\
							Psychrometer_Tbb4m_07_15, Psychrometer_Tbb7m_07_15, Psychrometer_Tbb10m_07_15, Psychrometer_RH1_2m_07_15, Psychrometer_RH4m_07_15, Psychrometer_RH7m_07_15,\
							Psychrometer_RH10m_07_15)
					cursor.execute(sql20)
					con.commit()
				
			elif (wp == "07.45"):
				jam_07_45 = wp
				
				Psychrometer_Tbk1_2m_07_45=psychrometer_Tbk1_2m.get()
				Psychrometer_Tbk4m_07_45=psychrometer_Tbk4m.get()
				Psychrometer_Tbk7m_07_45=psychrometer_Tbk7m.get()
				Psychrometer_Tbk10m_07_45=psychrometer_Tbk10m.get()
				
				Psychrometer_Tbb1_2m_07_45=psychrometer_Tbb1_2m.get()
				Psychrometer_Tbb4m_07_45=psychrometer_Tbb4m.get()
				Psychrometer_Tbb7m_07_45=psychrometer_Tbb7m.get()
				Psychrometer_Tbb10m_07_45=psychrometer_Tbb10m.get()
				
				Psychrometer_RH1_2m_07_45=psychrometer_RH1_2m.get()
				Psychrometer_RH4m_07_45=psychrometer_RH4m.get()
				Psychrometer_RH7m_07_45=psychrometer_RH7m.get()
				Psychrometer_RH10m_07_45=psychrometer_RH10m.get()
				
				#simpan ke database
				con = pymysql.connect("localhost", "root", "12345", "Buku_Klimatologi_BMKG")
				#with con.cursor() as cursor:
				#	cursor.execute("CREATE TABLE Psychrometer_Sangkar_Meteo0745_1 (Waktu text, psmeteoTbk1_2_0745 text, psmeteoTbk4_0745 text, psmeteoTbk7_0745 text, psmeteoTbk10_0745 text,\
				#		psmeteoTbb1_2_0745 text, psmeteoTbb4_0745 text, psmeteoTbb7_0745 text, psmeteoTbb10_0745 text, psmeteoRH1_2_0745 text, psmeteoRH4_0745 text, psmeteoRH7_0745 text, psmeteoRH10_0745 text)")
				with con.cursor() as cursor:
					sql21 = "INSERT INTO Psychrometer_Sangkar_Meteo0745_1 (Waktu, psmeteoTbk1_2_0745, psmeteoTbk4_0745, psmeteoTbk7_0745, psmeteoTbk10_0745, psmeteoTbb1_2_0745, psmeteoTbb4_0745,\
							psmeteoTbb7_0745, psmeteoTbb10_0745, psmeteoRH1_2_0745, psmeteoRH4_0745, psmeteoRH7_0745, psmeteoRH10_0745) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')"\
							% (TahunBulanTanggal, Psychrometer_Tbk1_2m_07_45, Psychrometer_Tbk4m_07_45, Psychrometer_Tbk7m_07_45, Psychrometer_Tbk10m_07_45, Psychrometer_Tbb1_2m_07_45,\
							Psychrometer_Tbb4m_07_45, Psychrometer_Tbb7m_07_45, Psychrometer_Tbb10m_07_45, Psychrometer_RH1_2m_07_45, Psychrometer_RH4m_07_45, Psychrometer_RH7m_07_45,\
							Psychrometer_RH10m_07_45)
					cursor.execute(sql21)
					con.commit()
				
			elif (wp == str(13.15)):
				jam_13_15 = wp
				
				Psychrometer_Tbk1_2m_13_15=psychrometer_Tbk1_2m.get()
				Psychrometer_Tbk4m_13_15=psychrometer_Tbk4m.get()
				Psychrometer_Tbk7m_13_15=psychrometer_Tbk7m.get()
				Psychrometer_Tbk10m_13_15=psychrometer_Tbk10m.get()
				
				Psychrometer_Tbb1_2m_13_15=psychrometer_Tbb1_2m.get()
				Psychrometer_Tbb4m_13_15=psychrometer_Tbb4m.get()
				Psychrometer_Tbb7m_13_15=psychrometer_Tbb7m.get()
				Psychrometer_Tbb10m_13_15=psychrometer_Tbb10m.get()
				
				Psychrometer_RH1_2m_13_15=psychrometer_RH1_2m.get()
				Psychrometer_RH4m_13_15=psychrometer_RH4m.get()
				Psychrometer_RH7m_13_15=psychrometer_RH7m.get()
				Psychrometer_RH10m_13_15=psychrometer_RH10m.get()
				
				#simpan ke database
				con = pymysql.connect("localhost", "root", "12345", "Buku_Klimatologi_BMKG")
				#with con.cursor() as cursor:
				#	cursor.execute("CREATE TABLE Psychrometer_Sangkar_Meteo1315_1 (Waktu text, psmeteoTbk1_2_1315 text, psmeteoTbk4_1315 text, psmeteoTbk7_1315 text, psmeteoTbk10_1315 text,\
				#		psmeteoTbb1_2_1315 text, psmeteoTbb4_1315 text, psmeteoTbb7_1315 text, psmeteoTbb10_1315 text, psmeteoRH1_2_1315 text, psmeteoRH4_1315 text, psmeteoRH7_1315 text, psmeteoRH10_1315 text)")
				with con.cursor() as cursor:
					sql22 = "INSERT INTO Psychrometer_Sangkar_Meteo1315_1 (Waktu, psmeteoTbk1_2_1315, psmeteoTbk4_1315, psmeteoTbk7_1315, psmeteoTbk10_1315, psmeteoTbb1_2_1315, psmeteoTbb4_1315,\
							psmeteoTbb7_1315, psmeteoTbb10_1315, psmeteoRH1_2_1315, psmeteoRH4_1315, psmeteoRH7_1315, psmeteoRH10_1315) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')"\
							% (TahunBulanTanggal, Psychrometer_Tbk1_2m_13_15, Psychrometer_Tbk4m_13_15, Psychrometer_Tbk7m_13_15, Psychrometer_Tbk10m_13_15, Psychrometer_Tbb1_2m_13_15,\
							Psychrometer_Tbb4m_13_15, Psychrometer_Tbb7m_13_15, Psychrometer_Tbb10m_13_15, Psychrometer_RH1_2m_13_15, Psychrometer_RH4m_13_15, Psychrometer_RH7m_13_15,\
							Psychrometer_RH10m_13_15)
					cursor.execute(sql22)
					con.commit()
				
			elif (wp == str(13.45)):
				jam_13_45 = wp
				
				Psychrometer_Tbk1_2m_13_45=psychrometer_Tbk1_2m.get()
				Psychrometer_Tbk4m_13_45=psychrometer_Tbk4m.get()
				Psychrometer_Tbk7m_13_45=psychrometer_Tbk7m.get()
				Psychrometer_Tbk10m_13_45=psychrometer_Tbk10m.get()
				
				Psychrometer_Tbb1_2m_13_45=psychrometer_Tbb1_2m.get()
				Psychrometer_Tbb4m_13_45=psychrometer_Tbb4m.get()
				Psychrometer_Tbb7m_13_45=psychrometer_Tbb7m.get()
				Psychrometer_Tbb10m_13_45=psychrometer_Tbb10m.get()
				
				Psychrometer_RH1_2m_13_45=psychrometer_RH1_2m.get()
				Psychrometer_RH4m_13_45=psychrometer_RH4m.get()
				Psychrometer_RH7m_13_45=psychrometer_RH7m.get()
				Psychrometer_RH10m_13_45=psychrometer_RH10m.get()
				
				#simpan ke database
				con = pymysql.connect("localhost", "root", "12345", "Buku_Klimatologi_BMKG")
				#with con.cursor() as cursor:
				#	cursor.execute("CREATE TABLE Psychrometer_Sangkar_Meteo1345_1 (Waktu text, psmeteoTbk1_2_1345 text, psmeteoTbk4_1345 text, psmeteoTbk7_1345 text, psmeteoTbk10_1345 text,\
				#		psmeteoTbb1_2_1345 text, psmeteoTbb4_1345 text, psmeteoTbb7_1345 text, psmeteoTbb10_1345 text, psmeteoRH1_2_1345 text, psmeteoRH4_1345 text, psmeteoRH7_1345 text, psmeteoRH10_1345 text)")
				with con.cursor() as cursor:
					sql23 = "INSERT INTO Psychrometer_Sangkar_Meteo1345_1 (Waktu, psmeteoTbk1_2_1345, psmeteoTbk4_1345, psmeteoTbk7_1345, psmeteoTbk10_1345, psmeteoTbb1_2_1345, psmeteoTbb4_1345,\
							psmeteoTbb7_1345, psmeteoTbb10_1345, psmeteoRH1_2_1345, psmeteoRH4_1345, psmeteoRH7_1345, psmeteoRH10_1345) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')"\
							% (TahunBulanTanggal, Psychrometer_Tbk1_2m_13_45, Psychrometer_Tbk4m_13_45, Psychrometer_Tbk7m_13_45, Psychrometer_Tbk10m_13_45, Psychrometer_Tbb1_2m_13_45,\
							Psychrometer_Tbb4m_13_45, Psychrometer_Tbb7m_13_45, Psychrometer_Tbb10m_13_45, Psychrometer_RH1_2m_13_45, Psychrometer_RH4m_13_45, Psychrometer_RH7m_13_45,\
							Psychrometer_RH10m_13_45)
					cursor.execute(sql23)
					con.commit()

			elif (wp == str(14.15)):
				jam_14_15 = wp
				
				Psychrometer_Tbk1_2m_14_15=psychrometer_Tbk1_2m.get()
				Psychrometer_Tbk4m_14_15=psychrometer_Tbk4m.get()
				Psychrometer_Tbk7m_14_15=psychrometer_Tbk7m.get()
				Psychrometer_Tbk10m_14_15=psychrometer_Tbk10m.get()
				
				Psychrometer_Tbb1_2m_14_15=psychrometer_Tbb1_2m.get()
				Psychrometer_Tbb4m_14_15=psychrometer_Tbb4m.get()
				Psychrometer_Tbb7m_14_15=psychrometer_Tbb7m.get()
				Psychrometer_Tbb10m_14_15=psychrometer_Tbb10m.get()
				
				Psychrometer_RH1_2m_14_15=psychrometer_RH1_2m.get()
				Psychrometer_RH4m_14_15=psychrometer_RH4m.get()
				Psychrometer_RH7m_14_15=psychrometer_RH7m.get()
				Psychrometer_RH10m_14_15=psychrometer_RH10m.get()
				
				#simpan ke database
				con = pymysql.connect("localhost", "root", "12345", "Buku_Klimatologi_BMKG")
				#with con.cursor() as cursor:
				#	cursor.execute("CREATE TABLE Psychrometer_Sangkar_Meteo1415_1 (Waktu text, psmeteoTbk1_2_1415 text, psmeteoTbk4_1415 text, psmeteoTbk7_1415 text, psmeteoTbk10_1415 text,\
				#		psmeteoTbb1_2_1415 text, psmeteoTbb4_1415 text, psmeteoTbb7_1415 text, psmeteoTbb10_1415 text, psmeteoRH1_2_1415 text, psmeteoRH4_1415 text, psmeteoRH7_1415 text, psmeteoRH10_1415 text)")
				with con.cursor() as cursor:
					sql24 = "INSERT INTO Psychrometer_Sangkar_Meteo1415_1 (Waktu, psmeteoTbk1_2_1415, psmeteoTbk4_1415, psmeteoTbk7_1415, psmeteoTbk10_1415, psmeteoTbb1_2_1415, psmeteoTbb4_1415,\
							psmeteoTbb7_1415, psmeteoTbb10_1415, psmeteoRH1_2_1415, psmeteoRH4_1415, psmeteoRH7_1415, psmeteoRH10_1415) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')"\
							% (TahunBulanTanggal, Psychrometer_Tbk1_2m_14_15, Psychrometer_Tbk4m_14_15, Psychrometer_Tbk7m_14_15, Psychrometer_Tbk10m_14_15, Psychrometer_Tbb1_2m_14_15,\
							Psychrometer_Tbb4m_14_15, Psychrometer_Tbb7m_14_15, Psychrometer_Tbb10m_14_15, Psychrometer_RH1_2m_14_15, Psychrometer_RH4m_14_15, Psychrometer_RH7m_14_15,\
							Psychrometer_RH10m_14_15)
					cursor.execute(sql24)
					con.commit()

			elif (wp == str(17.45)):
				jam_17_45 = wp
				
				Psychrometer_Tbk1_2m_17_45=psychrometer_Tbk1_2m.get()
				Psychrometer_Tbk4m_17_45=psychrometer_Tbk4m.get()
				Psychrometer_Tbk7m_17_45=psychrometer_Tbk7m.get()
				Psychrometer_Tbk10m_17_45=psychrometer_Tbk10m.get()
				
				Psychrometer_Tbb1_2m_17_45=psychrometer_Tbb1_2m.get()
				Psychrometer_Tbb4m_17_45=psychrometer_Tbb4m.get()
				Psychrometer_Tbb7m_17_45=psychrometer_Tbb7m.get()
				Psychrometer_Tbb10m_17_45=psychrometer_Tbb10m.get()
				
				Psychrometer_RH1_2m_17_45=psychrometer_RH1_2m.get()
				Psychrometer_RH4m_17_45=psychrometer_RH4m.get()
				Psychrometer_RH7m_17_45=psychrometer_RH7m.get()
				Psychrometer_RH10m_17_45=psychrometer_RH10m.get()
				
				#simpan ke database
				con = pymysql.connect("localhost", "root", "12345", "Buku_Klimatologi_BMKG")
				#with con.cursor() as cursor:
				#	cursor.execute("CREATE TABLE Psychrometer_Sangkar_Meteo1745_1 (Waktu text, psmeteoTbk1_2_1745 text, psmeteoTbk4_1745 text, psmeteoTbk7_1745 text, psmeteoTbk10_1745 text,\
				#		psmeteoTbb1_2_1745 text, psmeteoTbb4_1745 text, psmeteoTbb7_1745 text, psmeteoTbb10_1745 text, psmeteoRH1_2_1745 text, psmeteoRH4_1745 text, psmeteoRH7_1745 text, psmeteoRH10_1745 text)")
				with con.cursor() as cursor:
					sql25 = "INSERT INTO Psychrometer_Sangkar_Meteo1745_1 (Waktu, psmeteoTbk1_2_1745, psmeteoTbk4_1745, psmeteoTbk7_1745, psmeteoTbk10_1745, psmeteoTbb1_2_1745, psmeteoTbb4_1745,\
							psmeteoTbb7_1745, psmeteoTbb10_1745, psmeteoRH1_2_1745, psmeteoRH4_1745, psmeteoRH7_1745, psmeteoRH10_1745) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')"\
							% (TahunBulanTanggal, Psychrometer_Tbk1_2m_17_45, Psychrometer_Tbk4m_17_45, Psychrometer_Tbk7m_17_45, Psychrometer_Tbk10m_17_45, Psychrometer_Tbb1_2m_17_45,\
							Psychrometer_Tbb4m_17_45, Psychrometer_Tbb7m_17_45, Psychrometer_Tbb10m_17_45, Psychrometer_RH1_2m_17_45, Psychrometer_RH4m_17_45, Psychrometer_RH7m_17_45,\
							Psychrometer_RH10m_17_45)
					cursor.execute(sql25)
					con.commit()

			elif (wp == str(18.15)):
				jam_18_15 = wp
				
				Psychrometer_Tbk1_2m_18_15=psychrometer_Tbk1_2m.get()
				Psychrometer_Tbk4m_18_15=psychrometer_Tbk4m.get()
				Psychrometer_Tbk7m_18_15=psychrometer_Tbk7m.get()
				Psychrometer_Tbk10m_18_15=psychrometer_Tbk10m.get()
				
				Psychrometer_Tbb1_2m_18_15=psychrometer_Tbb1_2m.get()
				Psychrometer_Tbb4m_18_15=psychrometer_Tbb4m.get()
				Psychrometer_Tbb7m_18_15=psychrometer_Tbb7m.get()
				Psychrometer_Tbb10m_18_15=psychrometer_Tbb10m.get()
				
				Psychrometer_RH1_2m_18_15=psychrometer_RH1_2m.get()
				Psychrometer_RH4m_18_15=psychrometer_RH4m.get()
				Psychrometer_RH7m_18_15=psychrometer_RH7m.get()
				Psychrometer_RH10m_18_15=psychrometer_RH10m.get()
				
				#simpan ke database
				con = pymysql.connect("localhost", "root", "12345", "Buku_Klimatologi_BMKG")
				#with con.cursor() as cursor:
				#	cursor.execute("CREATE TABLE Psychrometer_Sangkar_Meteo1815_1 (Waktu text, psmeteoTbk1_2_1815 text, psmeteoTbk4_1815 text, psmeteoTbk7_1815 text, psmeteoTbk10_1815 text,\
				#		psmeteoTbb1_2_1815 text, psmeteoTbb4_1815 text, psmeteoTbb7_1815 text, psmeteoTbb10_1815 text, psmeteoRH1_2_1815 text, psmeteoRH4_1815 text, psmeteoRH7_1815 text, psmeteoRH10_1815 text)")
				with con.cursor() as cursor:
					sql26 = "INSERT INTO Psychrometer_Sangkar_Meteo1815_1 (Waktu, psmeteoTbk1_2_1815, psmeteoTbk4_1815, psmeteoTbk7_1815, psmeteoTbk10_1815, psmeteoTbb1_2_1815, psmeteoTbb4_1815,\
							psmeteoTbb7_1815, psmeteoTbb10_1815, psmeteoRH1_2_1815, psmeteoRH4_1815, psmeteoRH7_1815, psmeteoRH10_1815) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')"\
							% (TahunBulanTanggal, Psychrometer_Tbk1_2m_18_15, Psychrometer_Tbk4m_18_15, Psychrometer_Tbk7m_18_15, Psychrometer_Tbk10m_18_15, Psychrometer_Tbb1_2m_18_15,\
							Psychrometer_Tbb4m_18_15, Psychrometer_Tbb7m_18_15, Psychrometer_Tbb10m_18_15, Psychrometer_RH1_2m_18_15, Psychrometer_RH4m_18_15, Psychrometer_RH7m_18_15,\
							Psychrometer_RH10m_18_15)
					cursor.execute(sql26)
					con.commit()

			else:
				tkinter.messagebox.showwarning("Peringatan", "Anda belum memilih Waktu Pengamatan")
			
			#bersihkan entry
			waktu_pengamatanPsychrometerSangkar.set("-- Pilih Waktu Pengamatan --")
			
			psychrometer_Tbk1_2m.set("")
			psychrometer_Tbk4m.set("")
			psychrometer_Tbk7m.set("")
			psychrometer_Tbk10m.set("")
			
			psychrometer_Tbb1_2m.set("")
			psychrometer_Tbb4m.set("")
			psychrometer_Tbb7m.set("")
			psychrometer_Tbb10m.set("")
			
			psychrometer_RH1_2m.set("")
			psychrometer_RH4m.set("")
			psychrometer_RH7m.set("")
			psychrometer_RH10m.set("")
		
		#SAVE DAN EXIT
		simpan = Button(win, text="SIMPAN", bg="blue", fg="white", width=8, bd=5, font="callibri 12 bold", command=save)
		simpan.place(x=700 , y=540)
	"""-------------------------------------- AKHIR FUNGSI PSYCHROMETER SANGKAR METEOROLOGI --------------------------------"""
	
	"""--------------------------------------------------- FUNGSI RADIASI ------------------------------------------------"""
	def radiasi():
		Frame(win, width=864, height=630, bg='cadet blue' ).place(x=0, y=0)
		
		#JUDUL ALAT RADIASI (R)
		r = Label(win, text=" RADIASI ", bg="black", fg="cadet blue", font="callibri 24 bold")
		r.place(x=30, y=30)
		
		#TABEL TEMPAT PENGISIAN NILAI
		intensitas_radiasi = StringVar()
		
		#Baris 1
		Label(win, text="Waktu", bg="cadet blue", font="callibri 12").place(x=30, y=140)
		Label(win, text="Intensitas", bg="cadet blue", font="callibri 12").place(x=150, y=140)
		#Baris 2 dan Entry
		Label(win, text="07.15", bg="cadet blue", font="callibri 12").place(x=30, y=190)
		Entry(win, width=10, bd=10, textvariable=intensitas_radiasi).place(x=155, y=190)
		
		def save():
			#simpan entry ke variabel
			Intensitas_radiasi=intensitas_radiasi.get()
			
			#simpan ke database
			con = pymysql.connect("localhost", "root", "12345", "Buku_Klimatologi_BMKG")
			#with con.cursor() as cursor:
			#	cursor.execute("CREATE TABLE Radiasi_2 (Waktu text, intensitas text)")
			with con.cursor() as cursor:
				sql27 = "INSERT INTO Radiasi_2 (Waktu, intensitas) VALUES ('%s', '%s')" % (TahunBulanTanggal, Intensitas_radiasi)
				cursor.execute(sql27)
				con.commit()
			
			#bersihkan entry
			intensitas_radiasi.set("")
		
		#SAVE DAN EXIT
		simpan = Button(win, text="SIMPAN", bg="blue", fg="white", width=8, bd=5, font="callibri 12 bold", command=save)
		simpan.place(x=700 , y=540)
	"""----------------------------------------------- AKHIR FUNGSI RADIASI ------------------------------------------------"""
	
	"""------------------------------------------------- FUNGSI SUHU MIN RUMPUT ------------------------------------------"""
	def suhu_minRumput():
		Frame(win, width=864, height=630, bg='cadet blue' ).place(x=0, y=0)
		
		#JUDUL ALAT SUHU MIN RUMPUT (SMR)
		smr = Label(win, text=" SUHU MIN RUMPUT ", bg="black", fg="cadet blue", font="callibri 24 bold")
		smr.place(x=30, y=30)
		
		#TABEL TEMPAT PENGISIAN NILAI
		suhuMinRumput_pembacaan = StringVar()
		suhuMinRumput_reseting = StringVar()
		
		#Baris 1
		Label(win, text="Waktu", bg="cadet blue", font="callibri 12").place(x=30, y=140)
		Label(win, text="07.15", bg="cadet blue", font="callibri 12").place(x=220, y=140)
		#Baris 2 dan Entry
		Label(win, text="Pembacaan", bg="cadet blue", font="callibri 12").place(x=30, y=190)
		Entry(win, width=10, bd=10, textvariable=suhuMinRumput_pembacaan).place(x=210, y=190)
		#Baris 3 dan Entry
		Label(win, text="Reseting", bg="cadet blue", font="callibri 12").place(x=30, y=240)
		Entry(win, width=10, bd=10, textvariable=suhuMinRumput_reseting).place(x=210, y=240)
		
		def save():
			#simpan entry ke variabel
			SuhuMinRumput_pembacaan=suhuMinRumput_pembacaan.get()
			SuhuMinRumput_reseting=suhuMinRumput_reseting.get()
			
			#simpan ke database
			con  = pymysql.connect("localhost", "root", "12345", "Buku_Klimatologi_BMKG")
			#with con.cursor() as cursor:
			#	cursor.execute("CREATE TABLE Suhu_Minimum_Rumput_2 (Waktu text, suhumin_rumput0715 text, suhumin_rumput0715_reset text)")
			with con.cursor() as cursor:
				sql28 = "INSERT INTO Suhu_Minimum_Rumput_2(Waktu, suhumin_rumput0715, suhumin_rumput0715_reset) VALUES('%s', '%s', '%s')"\
						% (TahunBulanTanggal, SuhuMinRumput_pembacaan, SuhuMinRumput_reseting)
				cursor.execute(sql28)
				con.commit()				
			
			#bersihkan entry
			suhuMinRumput_pembacaan.set("")
			suhuMinRumput_reseting.set("")
		
		#SAVE DAN EXIT
		simpan = Button(win, text="SIMPAN", bg="blue", fg="white", width=8, bd=5, font="callibri 12 bold", command=save)
		simpan.place(x=700 , y=540)
	"""------------------------------------------- AKHIR FUNGSI SUHU MIN RUMPUT ------------------------------------------"""
	
	"""-------------------------------------------------- FUNGSI SUHU TANAH ----------------------------------------------"""
	def suhu_tanah():
		Frame(win, width=864, height=630, bg='cadet blue' ).place(x=0, y=0)
		
		#JUDUL SUHU TANAH (ST)
		st = Label(win, text=" SUHU TANAH ", bg="black", fg="cadet blue", font="callibri 24 bold")
		st.place(x=30, y=30)
		
		#Pilihan Waktu Pengamatan (PWP)
		waktu_pengamatanSuhuTanah = StringVar()
		jam_07_45 = StringVar()
		jam_13_45 = StringVar()
		jam_14_15 = StringVar()
		jam_17_45 = StringVar()
			
		waktu = ["-- Pilih Waktu Pengamatan --", "07.45", "13.45", "14.15", "17.45"]
		pilihan_waktu = ttk.Combobox(win, values = waktu, width = 22, font="callibri 12", state='readonly', textvariable=waktu_pengamatanSuhuTanah)
		pilihan_waktu.place(x=30, y=120)
		pilihan_waktu.current(0)

		#TABEL TEMPAT PENGISIAN NILAI
		suhuTanah_berumput0cm = StringVar()
		suhuTanah_berumput2cm = StringVar()
		suhuTanah_berumput5cm = StringVar()
		suhuTanah_berumput10cm = StringVar()
		suhuTanah_berumput20cm = StringVar()
		suhuTanah_berumput50cm = StringVar()
		suhuTanah_berumput100cm = StringVar()
		
		suhuTanah_gundul0cm = StringVar()
		suhuTanah_gundul2cm = StringVar()
		suhuTanah_gundul5cm = StringVar()
		suhuTanah_gundul10cm = StringVar()
		suhuTanah_gundul20cm = StringVar()
		suhuTanah_gundul50cm = StringVar()
		suhuTanah_gundul100cm = StringVar()
		
		#Kolom 1
		Label(win, text="Kedalaman", bg="cadet blue", font="callibri 12").place(x=30, y=260)
		Label(win, text="0 cm", bg="cadet blue", font="callibri 12").place(x=50, y=300)
		Label(win, text="2 cm", bg="cadet blue", font="callibri 12").place(x=50, y=340)
		Label(win, text="5 cm", bg="cadet blue", font="callibri 12").place(x=50, y=380)
		Label(win, text="10 cm", bg="cadet blue", font="callibri 12").place(x=50, y=420)
		Label(win, text="20 cm", bg="cadet blue", font="callibri 12").place(x=50, y=460)
		Label(win, text="50 cm", bg="cadet blue", font="callibri 12").place(x=50, y=500)
		Label(win, text="100 cm", bg="cadet blue", font="callibri 12").place(x=40, y=540)
		
		#Kolom 2 (Berumput) dan Entry
		Label(win, text="Berumput", bg="cadet blue", font="callibri 12").place(x=180, y=260)
		Entry(win, width=10, bd=10, textvariable=suhuTanah_berumput0cm).place(x=185, y=300)
		Entry(win, width=10, bd=10, textvariable=suhuTanah_berumput2cm).place(x=185, y=340)
		Entry(win, width=10, bd=10, textvariable=suhuTanah_berumput5cm).place(x=185, y=380)
		Entry(win, width=10, bd=10, textvariable=suhuTanah_berumput10cm).place(x=185, y=420)
		Entry(win, width=10, bd=10, textvariable=suhuTanah_berumput20cm).place(x=185, y=460)
		Entry(win, width=10, bd=10, textvariable=suhuTanah_berumput50cm).place(x=185, y=500)
		Entry(win, width=10, bd=10, textvariable=suhuTanah_berumput100cm).place(x=185, y=540)
		
		#Kolom 3 dan Entry
		Label(win, text="Gundul", bg="cadet blue", font="callibri 12").place(x=340, y=260)
		Entry(win, width=10, bd=10, textvariable=suhuTanah_gundul0cm).place(x=335, y=300)
		Entry(win, width=10, bd=10, textvariable=suhuTanah_gundul2cm).place(x=335, y=340)
		Entry(win, width=10, bd=10, textvariable=suhuTanah_gundul5cm).place(x=335, y=380)
		Entry(win, width=10, bd=10, textvariable=suhuTanah_gundul10cm).place(x=335, y=420)
		Entry(win, width=10, bd=10, textvariable=suhuTanah_gundul20cm).place(x=335, y=460)
		Entry(win, width=10, bd=10, textvariable=suhuTanah_gundul50cm).place(x=335, y=500)
		Entry(win, width=10, bd=10, textvariable=suhuTanah_gundul100cm).place(x=335, y=540)
		
		def save():
			#simpan entry ke variabel
			wp = (waktu_pengamatanSuhuTanah.get())
			if (wp == "07.45"):
				jam_07_45 = wp
				
				SuhuTanah_berumput0cm_07_45=suhuTanah_berumput0cm.get()
				SuhuTanah_berumput2cm_07_45=suhuTanah_berumput2cm.get()
				SuhuTanah_berumput5cm_07_45=suhuTanah_berumput5cm.get()
				SuhuTanah_berumput10cm_07_45=suhuTanah_berumput10cm.get()
				SuhuTanah_berumput20cm_07_45=suhuTanah_berumput20cm.get()
				SuhuTanah_berumput50cm_07_45=suhuTanah_berumput50cm.get()
				SuhuTanah_berumput100cm_07_45=suhuTanah_berumput100cm.get()
				
				SuhuTanah_gundul0cm_07_45=suhuTanah_gundul0cm.get()
				SuhuTanah_gundul2cm_07_45=suhuTanah_gundul2cm.get()
				SuhuTanah_gundul5cm_07_45=suhuTanah_gundul5cm.get()
				SuhuTanah_gundul10cm_07_45=suhuTanah_gundul10cm.get()
				SuhuTanah_gundul20cm_07_45=suhuTanah_gundul20cm.get()
				SuhuTanah_gundul50cm_07_45=suhuTanah_gundul50cm.get()
				SuhuTanah_gundul100cm_07_45=suhuTanah_gundul100cm.get()
				
				#simpan ke database
				con = pymysql.connect("localhost", "root", "12345", "Buku_Klimatologi_BMKG")
				#with con.cursor() as cursor:
				#	cursor.execute("CREATE TABLE Suhu_Tanah0745_1 (Waktu text, suhutanah_berumput0_0745 text, suhutanah_gundul0_0745 text, suhutanah_berumput2_0745 text, suhutanah_gundul2_0745 text,\
				#	suhutanah_berumput5_0745 text, suhutanah_gundul5_0745 text, suhutanah_berumput10_0745 text, suhutanah_gundul10_0745 text, suhutanah_berumput20_0745 text, suhutanah_gundul20_0745 text)")
				with con.cursor() as cursor:
					sql29 = "INSERT INTO Suhu_Tanah0745_1 (Waktu, suhutanah_berumput0_0745, suhutanah_gundul0_0745, suhutanah_berumput2_0745, suhutanah_gundul2_0745,\
							suhutanah_berumput5_0745, suhutanah_gundul5_0745,  suhutanah_berumput10_0745, suhutanah_gundul10_0745,  suhutanah_berumput20_0745, suhutanah_gundul20_0745)\
							VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (TahunBulanTanggal, SuhuTanah_berumput0cm_07_45, SuhuTanah_gundul0cm_07_45, SuhuTanah_berumput2cm_07_45,\
							SuhuTanah_gundul2cm_07_45, SuhuTanah_berumput5cm_07_45, SuhuTanah_gundul5cm_07_45, SuhuTanah_berumput10cm_07_45, SuhuTanah_gundul10cm_07_45, SuhuTanah_berumput20cm_07_45,\
							SuhuTanah_gundul20cm_07_45)
					cursor.execute(sql29)
					con.commit()
					
			elif (wp == str(13.45)):
				jam_13_45 = wp
				
				SuhuTanah_berumput0cm_13_45=suhuTanah_berumput0cm.get()
				SuhuTanah_berumput2cm_13_45=suhuTanah_berumput2cm.get()
				SuhuTanah_berumput5cm_13_45=suhuTanah_berumput5cm.get()
				SuhuTanah_berumput10cm_13_45=suhuTanah_berumput10cm.get()
				SuhuTanah_berumput20cm_13_45=suhuTanah_berumput20cm.get()
				SuhuTanah_berumput50cm_13_45=suhuTanah_berumput50cm.get()
				SuhuTanah_berumput100cm_13_45=suhuTanah_berumput100cm.get()
				
				SuhuTanah_gundul0cm_13_45=suhuTanah_gundul0cm.get()
				SuhuTanah_gundul2cm_13_45=suhuTanah_gundul2cm.get()
				SuhuTanah_gundul5cm_13_45=suhuTanah_gundul5cm.get()
				SuhuTanah_gundul10cm_13_45=suhuTanah_gundul10cm.get()
				SuhuTanah_gundul20cm_13_45=suhuTanah_gundul20cm.get()
				SuhuTanah_gundul50cm_13_45=suhuTanah_gundul50cm.get()
				SuhuTanah_gundul100cm_13_45=suhuTanah_gundul100cm.get()
				
				#simpan ke database
				con = pymysql.connect("localhost", "root", "12345", "Buku_Klimatologi_BMKG")
				#with con.cursor() as cursor:
				#	cursor.execute("CREATE TABLE Suhu_Tanah1345_1 (Waktu text, suhutanah_berumput0_1345 text, suhutanah_gundul0_1345 text, suhutanah_berumput2_1345 text, suhutanah_gundul2_1345 text,\
				#	suhutanah_berumput5_1345 text, suhutanah_gundul5_1345 text, suhutanah_berumput10_1345 text, suhutanah_gundul10_1345 text, suhutanah_berumput20_1345 text, suhutanah_gundul20_1345 text)")
				with con.cursor() as cursor:
					sql30 = "INSERT INTO Suhu_Tanah1345_1 (Waktu, suhutanah_berumput0_1345, suhutanah_gundul0_1345, suhutanah_berumput2_1345, suhutanah_gundul2_1345,\
							suhutanah_berumput5_1345, suhutanah_gundul5_1345,  suhutanah_berumput10_1345, suhutanah_gundul10_1345,  suhutanah_berumput20_1345, suhutanah_gundul20_1345)\
							VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (TahunBulanTanggal, SuhuTanah_berumput0cm_13_45, SuhuTanah_gundul0cm_13_45, SuhuTanah_berumput2cm_13_45,\
							SuhuTanah_gundul2cm_13_45, SuhuTanah_berumput5cm_13_45, SuhuTanah_gundul5cm_13_45, SuhuTanah_berumput10cm_13_45, SuhuTanah_gundul10cm_13_45, SuhuTanah_berumput20cm_13_45,\
							SuhuTanah_gundul20cm_13_45)
					cursor.execute(sql30)
					con.commit()

			elif (wp == str(14.15)):
				jam_14_15 = wp
				
				SuhuTanah_berumput0cm_14_15=suhuTanah_berumput0cm.get()
				SuhuTanah_berumput2cm_14_15=suhuTanah_berumput2cm.get()
				SuhuTanah_berumput5cm_14_15=suhuTanah_berumput5cm.get()
				SuhuTanah_berumput10cm_14_15=suhuTanah_berumput10cm.get()
				SuhuTanah_berumput20cm_14_15=suhuTanah_berumput20cm.get()
				SuhuTanah_berumput50cm_14_15=suhuTanah_berumput50cm.get()
				SuhuTanah_berumput100cm_14_15=suhuTanah_berumput100cm.get()
				
				SuhuTanah_gundul0cm_14_15=suhuTanah_gundul0cm.get()
				SuhuTanah_gundul2cm_14_15=suhuTanah_gundul2cm.get()
				SuhuTanah_gundul5cm_14_15=suhuTanah_gundul5cm.get()
				SuhuTanah_gundul10cm_14_15=suhuTanah_gundul10cm.get()
				SuhuTanah_gundul20cm_14_15=suhuTanah_gundul20cm.get()
				SuhuTanah_gundul50cm_14_15=suhuTanah_gundul50cm.get()
				SuhuTanah_gundul100cm_14_15=suhuTanah_gundul100cm.get()
				
				#simpan ke database
				con = pymysql.connect("localhost", "root", "12345", "Buku_Klimatologi_BMKG")
				#with con.cursor() as cursor:
				#	cursor.execute("CREATE TABLE Suhu_Tanah1415_1 (Waktu text, suhutanah_berumput0_1415 text, suhutanah_gundul0_1415 text, suhutanah_berumput2_1415 text, suhutanah_gundul2_1415 text,\
				#	suhutanah_berumput5_1415 text, suhutanah_gundul5_1415 text, suhutanah_berumput10_1415 text, suhutanah_gundul10_1415 text, suhutanah_berumput20_1415 text, suhutanah_gundul20_1415 text)")
				with con.cursor() as cursor:
					sql31 = "INSERT INTO Suhu_Tanah1415_1 (Waktu, suhutanah_berumput0_1415, suhutanah_gundul0_1415, suhutanah_berumput2_1415, suhutanah_gundul2_1415,\
							suhutanah_berumput5_1415, suhutanah_gundul5_1415,  suhutanah_berumput10_1415, suhutanah_gundul10_1415,  suhutanah_berumput20_1415, suhutanah_gundul20_1415)\
							VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (TahunBulanTanggal, SuhuTanah_berumput0cm_14_15, SuhuTanah_gundul0cm_14_15, SuhuTanah_berumput2cm_14_15,\
							SuhuTanah_gundul2cm_14_15, SuhuTanah_berumput5cm_14_15, SuhuTanah_gundul5cm_14_15, SuhuTanah_berumput10cm_14_15, SuhuTanah_gundul10cm_14_15, SuhuTanah_berumput20cm_14_15,\
							SuhuTanah_gundul20cm_14_15)
					cursor.execute(sql31)
					con.commit()

			elif (wp == str(17.45)):
				jam_17_45 = wp
				
				SuhuTanah_berumput0cm_17_45=suhuTanah_berumput0cm.get()
				SuhuTanah_berumput2cm_17_45=suhuTanah_berumput2cm.get()
				SuhuTanah_berumput5cm_17_45=suhuTanah_berumput5cm.get()
				SuhuTanah_berumput10cm_17_45=suhuTanah_berumput10cm.get()
				SuhuTanah_berumput20cm_17_45=suhuTanah_berumput20cm.get()
				SuhuTanah_berumput50cm_17_45=suhuTanah_berumput50cm.get()
				SuhuTanah_berumput100cm_17_45=suhuTanah_berumput100cm.get()
				
				SuhuTanah_gundul0cm_17_45=suhuTanah_gundul0cm.get()
				SuhuTanah_gundul2cm_17_45=suhuTanah_gundul2cm.get()
				SuhuTanah_gundul5cm_17_45=suhuTanah_gundul5cm.get()
				SuhuTanah_gundul10cm_17_45=suhuTanah_gundul10cm.get()
				SuhuTanah_gundul20cm_17_45=suhuTanah_gundul20cm.get()
				SuhuTanah_gundul50cm_17_45=suhuTanah_gundul50cm.get()
				SuhuTanah_gundul100cm_17_45=suhuTanah_gundul100cm.get()
				
				#simpan ke database
				con = pymysql.connect("localhost", "root", "12345", "Buku_Klimatologi_BMKG")
				#with con.cursor() as cursor:
				#	cursor.execute("CREATE TABLE Suhu_Tanah1745_4 (Waktu text, suhutanah_berumput0_1745 text, suhutanah_gundul0_1745 text, suhutanah_berumput2_1745 text, suhutanah_gundul2_1745 text,\
				#	suhutanah_berumput5_1745 text, suhutanah_gundul5_1745 text, suhutanah_berumput10_1745 text, suhutanah_gundul10_1745 text, suhutanah_berumput20_1745 text, suhutanah_gundul20_1745 text,\
				#	suhutanah_berumput50_1745 text, suhutanah_gundul50_1745 text, suhutanah_berumput100_1745 text, suhutanah_gundul100_1745 text)")
				with con.cursor() as cursor:
					sql32 = "INSERT INTO Suhu_Tanah1745_4 (Waktu, suhutanah_berumput0_1745, suhutanah_gundul0_1745, suhutanah_berumput2_1745, suhutanah_gundul2_1745,\
							suhutanah_berumput5_1745, suhutanah_gundul5_1745,  suhutanah_berumput10_1745, suhutanah_gundul10_1745,  suhutanah_berumput20_1745, suhutanah_gundul20_1745,\
							suhutanah_berumput50_1745, suhutanah_gundul50_1745, suhutanah_berumput100_1745, suhutanah_gundul100_1745)\
							VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (TahunBulanTanggal, SuhuTanah_berumput0cm_17_45, SuhuTanah_gundul0cm_17_45, SuhuTanah_berumput2cm_17_45,\
							SuhuTanah_gundul2cm_17_45, SuhuTanah_berumput5cm_17_45, SuhuTanah_gundul5cm_17_45, SuhuTanah_berumput10cm_17_45, SuhuTanah_gundul10cm_17_45, SuhuTanah_berumput20cm_17_45,\
							SuhuTanah_gundul20cm_17_45, SuhuTanah_berumput50cm_17_45, SuhuTanah_gundul50cm_17_45, SuhuTanah_berumput100cm_17_45, SuhuTanah_gundul100cm_17_45)
					cursor.execute(sql32)
					con.commit()
					
			else:
				tkinter.messagebox.showwarning("Peringatan", "Anda belum memilih Waktu Pengamatan")
						
			#bersihkan entry
			waktu_pengamatanSuhuTanah.set("-- Pilih Waktu Pengamatan --")
			
			suhuTanah_berumput0cm.set("")
			suhuTanah_berumput2cm.set("")
			suhuTanah_berumput5cm.set("")
			suhuTanah_berumput10cm.set("")
			suhuTanah_berumput20cm.set("")
			suhuTanah_berumput50cm.set("")
			suhuTanah_berumput100cm.set("")
			
			suhuTanah_gundul0cm.set("")
			suhuTanah_gundul2cm.set("")
			suhuTanah_gundul5cm.set("")
			suhuTanah_gundul10cm.set("")
			suhuTanah_gundul20cm.set("")
			suhuTanah_gundul50cm.set("")
			suhuTanah_gundul100cm.set("")
			
		#SAVE DAN EXIT
		simpan = Button(win, text="SIMPAN", bg="blue", fg="white", width=8, bd=5, font="callibri 12 bold", command=save)
		simpan.place(x=700 , y=540)
	"""------------------------------------------------ AKHIR FUNGSI SUHU TANAH --------------------------------"""
	
	"""-------------------------------------------- FUNGSI TERMOMETER MAKSIMUM & MINIMUM --------------------------------"""
	def termometer_maxMin():
		Frame(win, width=864, height=630, bg='cadet blue' ).place(x=0, y=0)
		
		#JUDUL ALAT TERMOMETER MAKSIMUM & MINIMUM (TMM)
		tmm = Label(win, text=" TERMOMETER MAKSIMUM & MINIMUM ",bg="black", fg="cadet blue", font="callibri 24 bold")
		tmm.place(x=30, y=30)
		
		#Pilihan Waktu Pengamatan (PWP)
		waktu_pengamatanTermometerMaxMin = StringVar()
		jam_14_15 = StringVar()
		jam_18_15 = StringVar()
		
		waktu = ["-- Pilih Waktu Pengamatan --", "14.15", "18.15"]
		pilihan_waktu = ttk.Combobox(win, values = waktu, width = 22, font="callibri 12", state='readonly', textvariable=waktu_pengamatanTermometerMaxMin)
		pilihan_waktu.place(x=30, y=120)
		pilihan_waktu.current(0)
		
		#TABEL TEMPAT PENGISIAN NILAI
		termoMaxMin_maxMin = StringVar()
		termoMaxMin_reset = StringVar()
		
		#Baris 1
		Label(win, text="Ketinggian", bg="cadet blue", font="callibri 12").place(x=30, y=240)
		Label(win, text="1.2 m", bg="cadet blue", font="callibri 12").place(x=200, y=240)
		#Baris 2
		Label(win, text="Max/Min", bg="cadet blue", font="callibri 12").place(x=30, y=300)
		Label(win, text="Reset", bg="cadet blue", font="callibri 12").place(x=200, y=300)
		#Entry
		Entry(win, width=10, bd=10, textvariable=termoMaxMin_maxMin).place(x=30, y=360)
		Entry(win, width=10, bd=10, textvariable=termoMaxMin_reset).place(x=200, y=360)
		
		def save():
			#simpan entry ke variabel
			wp = (waktu_pengamatanTermometerMaxMin.get())
			if (wp == str(14.15)):
				jam_14_15 = wp
				
				TermoMaxMin_maxMin_14_15=termoMaxMin_maxMin.get()
				TermoMaxMin_reset_14_15=termoMaxMin_reset.get()
				
				#simpan ke database
				con = pymysql.connect("localhost", "root", "12345", "Buku_Klimatologi_BMKG")
				#with con.cursor() as cursor:
				#	cursor.execute("CREATE TABLE Termo_Max_Min1415_1 (Waktu text, termoMM_min_1415 text, termoMM_reset_1415 text)")
				with con.cursor() as cursor:
					sql33 = "INSERT INTO Termo_Max_Min1415_1 (Waktu, termoMM_min_1415, termoMM_reset_1415) VALUES ('%s', '%s', '%s')" % (TahunBulanTanggal, TermoMaxMin_maxMin_14_15, TermoMaxMin_reset_14_15)
					cursor.execute(sql33)
					con.commit()
								
			elif (wp == str(18.15)):
				jam_18_15 = wp
				
				TermoMaxMin_maxMin_18_15=termoMaxMin_maxMin.get()
				TermoMaxMin_reset_18_15=termoMaxMin_reset.get()
				
				#simpan ke database
				con = pymysql.connect("localhost", "root", "12345", "Buku_Klimatologi_BMKG")
				#with con.cursor() as cursor:
				#	cursor.execute("CREATE TABLE Termo_Max_Min1815_1 (Waktu text, termoMM_max_1815 text, termoMM_reset_1815 text)")
				with con.cursor() as cursor:
					sql34 = "INSERT INTO Termo_Max_Min1815_1 (Waktu, termoMM_max_1815, termoMM_reset_1815) VALUES ('%s', '%s', '%s')" % (TahunBulanTanggal, TermoMaxMin_maxMin_18_15, TermoMaxMin_reset_18_15)
					cursor.execute(sql34)
					con.commit()

			else:
				tkinter.messagebox.showwarning("Peringatan", "Anda belum memilih Waktu Pengamatan")
						
			#bersihkan variabel
			waktu_pengamatanTermometerMaxMin.set("-- Pilih Waktu Pengamatan --")
			termoMaxMin_maxMin.set("")
			termoMaxMin_reset.set("")
		
		#SAVE DAN EXIT
		simpan = Button(win, text="SIMPAN", bg="blue", fg="white", width=8, bd=5, font="callibri 12 bold", command=save)
		simpan.place(x=700, y=540)
		
	"""------------------------------------ AKHIR FUNGSI TERMOMETER MAKSIMUM & MINIMMUM -----------------------------"""
	
	"""----------------------------------------- AWAL FUNGSI PMG ON DUTY & CATATAN ----------------------------------"""
	def PMGonDuty_Catatan():
		Frame(win, width=864, height=630, bg='cadet blue' ).place(x=0, y=0)

		#JUDUL PMG ON DUTY (pmg)
		Label(win, text=" PMG ON DUTY DAN CATATAN ", bg="black", fg="cadet blue", font="callibri 24 bold").place(x=30, y=30)

		#VARIABEL
		hari = StringVar()
		tgl = StringVar()

		pmg_pagi = StringVar()
		pmg_siang = StringVar()

		catatan1 = StringVar()
		#catatan2 = StringVar()
		#catatan3 = StringVar()

		Label(win, text="Hari:", bg="cadet blue", font="callibri 12").place(x=80, y=90)
		Entry(win, width=14, bd=10, textvariable=hari).place(x=150, y=90)
		Label(win, text="Tanggal:", bg="cadet blue", font="callibri 12").place(x=50, y=130)
		Entry(win, width=14, bd=10, textvariable=tgl).place(x=150, y=130)
		Label(win, text="Ket. Penulisan:", bg="cadet blue", font="callibri 9").place(x=260, y=130)
		Label(win, text="(tanggal-bulan-tahun) = (DD-MM-YYYY)", bg="cadet blue", font="callibri 9").place(x=260, y=145)


		Label(win, text="NAMA", bg="cadet blue", font="callibri 12 bold").place(x=175, y=195)
		Label(win, text="DUTY ON", bg="cadet blue", font="callibri 12 bold").place(x=50, y=195)
		Label(win, text="Pagi:", bg="cadet blue", font="callibri 12").place(x=75, y=225)
		Entry(win, width=14, bd=10, textvariable=pmg_pagi).place(x=150, y=220)
		Label(win, text="Siang:", bg="cadet blue", font="callibri 12").place(x=70, y=265)
		Entry(win, width=14, bd=10, textvariable=pmg_siang).place(x=150, y=260)

		#CATATAN
		Label(win, text="CATATAN:", bg="cadet blue", font="callibri 12 bold").place(x=50, y=315)
		Entry(win, width=40, bd=3, font="callibri 12", textvariable=catatan1).place(x=50, y=340)
		#Entry(win, width=40, bd=3, font="callibri 12", textvariable=catatan2).place(x=50, y=365)
		#Entry(win, width=40, bd=3, font="callibri 12", textvariable=catatan3).place(x=50, y=390)

		def save():
			Hari = hari.get()
			Tgl = tgl.get()
			Pmg_pagi = pmg_pagi.get()
			Pmg_siang = pmg_siang.get()
			Catatan1 = catatan1.get()
			#Catatan2 = catatan2.get()
			#Catatan3 = catatan3.get()
			#Catatan = Catatan1 + ' ' + Catatan2 + ' ' + Catatan3
			#print(Catatan)
			
			#simpan ke database
			#tipe data text dan varchar
			con = pymysql.connect("localhost", "root", "12345", "Buku_Klimatologi_BMKG")
			#with con.cursor() as cursor:
			#	cursor.execute("CREATE TABLE PMGonDuty_Catatan_4 (Waktu text, hari varchar(20), tanggal varchar(20), pmg_pagi text, pmg_siang text, catatan1 text)")
			with con.cursor() as cursor:
				sql35 = "INSERT INTO PMGonDuty_Catatan_4 (Waktu, hari, tanggal, pmg_pagi, pmg_siang, catatan1) VALUES ('%s', '%s', '%s', '%s', '%s', '%s')"\
						% (TahunBulanTanggal, Hari, Tgl, Pmg_pagi, Pmg_siang, Catatan1)
				cursor.execute(sql35)
				con.commit()
			
			hari.set("")
			tgl.set("")
			pmg_pagi.set("")
			pmg_siang.set("")
			catatan1.set("")
			#catatan2.set("")
			#catatan3.set("")

		#SAVE DAN EXIT
		simpan = Button(win, text="SIMPAN", bg="blue", fg="white", width=8, bd=5, font="callibri 12 bold", command=save)
		simpan.place(x=700 , y=540)

	"""----------------------------------------- AKHIR FUNGSI PMG ON DUTY & CATATAN ----------------------------------"""
	
	def o_k():
	
		global TahunBulanTanggal
		TahunBulanTanggal = tahun_bulan_tanggal.get()

		Frame(win, width=120, height=490, bg="powder blue").place(x=875, y=150)
		Button(win, text="Angin", bg="gray", fg="black", width=15, bd=5, font="callibri 7", 
			command=angin).place(x=882, y=154)
		Button(win, text="Barometer", bg="gray", fg="black", width=15, bd=5, font="callibri 7", 
			command=barometer).place(x=882, y=180)
		Button(win, text="Kondisi Cuaca\ndan Tanah", bg="gray", fg="black", width=15, bd=5, 
			font="callibri 7", command=kondisi_cuacaTanah).place(x=882, y=205)
		Button(win, text="Lama\nPenyinaran", bg="gray", fg="black", width=15, bd=5, font="callibri 7",
			command=lama_penyinaran).place(x=882, y=240)
		Button(win, text="Lysimeter", bg="gray", fg="black", width=15, bd=5, font="callibri 7", 
			command=lysimeter).place(x=882, y=275)
		Button(win, text="Open Pan", bg="gray", fg="black", width=15, bd=5, font="callibri 7", 
			command=open_pan).place(x=882, y=300)
		Button(win, text="Piche\nEvaporimeter", bg="gray", fg="black", width=15, bd=5, 
			font="callibri 7", command=piche_evaporator).place(x=882, y=325)
		Button(win, text="Psychrometer\nAssmann", bg="gray", fg="black", width=15, bd=5, 
			font="callibri 7", command=psychrometer_assmann).place(x=882, y=360)
		Button(win, text="Psychrometer\nSangkar\nMeteorologi", bg="gray", fg="black", width=15, bd=5, 
			font="callibri 7", command=psychrometer_sangkarMeteorologi).place(x=882, y=395)
		Button(win, text="Radiasi", bg="gray", fg="black", width=15, bd=5, font="callibri 7", 
			command=radiasi).place(x=882, y=445)
		Button(win, text="Suhu Min Rumput", bg="gray", fg="black", width=15, bd=5, font="callibri 7", 
			command=suhu_minRumput).place(x=882, y=470)
		Button(win, text="Suhu Tanah", bg="gray", fg="black", width=15, bd=5, font="callibri 7", 
			command=suhu_tanah).place(x=882, y=495)
		Button(win, text="Termometer Maksimum\ndan Minimum", bg="gray", fg="black", width=15, bd=5, 
			font="callibri 7", command=termometer_maxMin).place(x=882, y=520)
		Button(win, text="PMG dan Catatan", bg="gray", fg="black", width=15, bd=5,
			font="callibri 7", command=PMGonDuty_Catatan).place(x=882, y=556)
		Button(win, text="Buat Laporan", bg="green", fg="black", bd=5, font="callibri 8 bold").place(x=889, y=590)
		
	Button(win, text="OK", bg="green", fg="black", width=8, bd=5, font="callibri 10 bold", command=o_k).place(x=893, y=110)
	
	
	Button(win, text="Buat Laporan", bg="green", fg="black", bd=5, font="callibri 8 bold").place(x=889, y=570)		
	
	
"""================================================ AKHIR MEMBUAT LAPORAN ===================================================="""

"""================================================= MENAMPILKAN LAPORAN ====================================================="""
def tampilkan_laporan():
	Frame(win, width=865, height=630, bg="white").place(x=0, y=0)
	Frame(win, width=30, height=630, bg="powder blue").place(x=865, y=0)
	Frame(win, width=130, height=630, bg="cadet blue").place(x=870, y=0)
	Frame(win, width=100, height=80, bg="powder blue").place(x=885, y=280)

	#deklarasi variabel waktu: tanggal bulan tahun dalam integer
	input_tahun_bulan_tanggal = StringVar()

	Label(win, text="CARI LAPORAN", bg="cadet blue", fg="white", font="callibri 10 bold").place(x=880, y=20)
	Label(win, text="Masukkan:", bg="cadet blue", fg="white", font="callibri 10 bold").place(x=880, y=50)
	Label(win, text="Waktu (YYYYMMDD):", bg="cadet blue", fg="white", font="callibri 9 bold").place(x=875, y=80)
	Entry(win, width=10, bd=5, textvariable=input_tahun_bulan_tanggal).place(x=895, y=100)

	def halaman1():
		Frame(win, width=864, height=630, bg="white").place(x=0, y=0)
		foto1 = Label(image=img1).place(x=3, y=7)
		
		"""================================================ MYSQL START HERE ====================================================="""
		#Psychrometer Sangkar Meteorologi
		con = pymysql.connect("localhost", "root", "12345", "Buku_Klimatologi_BMKG")
		with con.cursor() as cursor:
			dis1 = "SELECT psmeteoTbk1_2_0715 FROM Psychrometer_Sangkar_Meteo0715_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis1)
			result1 = cursor.fetchone()
			
			dis2 = "SELECT psmeteoTbb1_2_0715 FROM Psychrometer_Sangkar_Meteo0715_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis2)
			result2 = cursor.fetchone()
			
			dis3 = "SELECT psmeteoRH1_2_0715 FROM Psychrometer_Sangkar_Meteo0715_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis3)
			result3 = cursor.fetchone()

			dis4 = "SELECT psmeteoTbk4_0715 FROM Psychrometer_Sangkar_Meteo0715_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis4)
			result4 = cursor.fetchone()
			
			dis5 = "SELECT psmeteoTbb4_0715 FROM Psychrometer_Sangkar_Meteo0715_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis5)
			result5 = cursor.fetchone()
			
			dis6 = "SELECT psmeteoRH4_0715 FROM Psychrometer_Sangkar_Meteo0715_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis6)
			result6 = cursor.fetchone()
			
			dis7 = "SELECT psmeteoTbk7_0715 FROM Psychrometer_Sangkar_Meteo0715_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis7)
			result7 = cursor.fetchone()
			
			dis8 = "SELECT psmeteoTbb7_0715 FROM Psychrometer_Sangkar_Meteo0715_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis8)
			result8 = cursor.fetchone()
			
			dis9 = "SELECT psmeteoRH7_0715 FROM Psychrometer_Sangkar_Meteo0715_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis9)
			result9 = cursor.fetchone()
			
			dis10 = "SELECT psmeteoTbk10_0715 FROM Psychrometer_Sangkar_Meteo0715_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis10)
			result10 = cursor.fetchone()
			
			dis11 = "SELECT psmeteoTbb10_0715 FROM Psychrometer_Sangkar_Meteo0715_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis11)
			result11 = cursor.fetchone()
			
			dis12 = "SELECT psmeteoRH1_2_0715 FROM Psychrometer_Sangkar_Meteo0715_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis12)
			result12 = cursor.fetchone()
			
			dis13 = "SELECT psmeteoTbk1_2_0745 FROM Psychrometer_Sangkar_Meteo0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis13)
			result13 = cursor.fetchone()
			
			dis14 = "SELECT psmeteoTbb1_2_0745 FROM Psychrometer_Sangkar_Meteo0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis14)
			result14 = cursor.fetchone()
			
			dis15 = "SELECT psmeteoRH1_2_0745 FROM Psychrometer_Sangkar_Meteo0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis15)
			result15 = cursor.fetchone()
			
			dis16 = "SELECT psmeteoTbk4_0745 FROM Psychrometer_Sangkar_Meteo0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis16)
			result16 = cursor.fetchone()
			
			dis17 = "SELECT psmeteoTbb4_0745 FROM Psychrometer_Sangkar_Meteo0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis17)
			result17 = cursor.fetchone()
			
			dis18 = "SELECT psmeteoRH4_0745 FROM Psychrometer_Sangkar_Meteo0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis18)
			result18 = cursor.fetchone()
			
			dis19 = "SELECT psmeteoTbk7_0745 FROM Psychrometer_Sangkar_Meteo0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis19)
			result19 = cursor.fetchone()
			
			dis20 = "SELECT psmeteoTbb7_0745 FROM Psychrometer_Sangkar_Meteo0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis20)
			result20 = cursor.fetchone()
			
			dis21 = "SELECT psmeteoRH7_0745 FROM Psychrometer_Sangkar_Meteo0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis21)
			result21 = cursor.fetchone()

			dis22 = "SELECT psmeteoTbk10_0745 FROM Psychrometer_Sangkar_Meteo0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis22)
			result22 = cursor.fetchone()
			
			dis23 = "SELECT psmeteoTbb10_0745 FROM Psychrometer_Sangkar_Meteo0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis23)
			result23 = cursor.fetchone()
			
			dis24 = "SELECT psmeteoRH10_0745 FROM Psychrometer_Sangkar_Meteo0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis24)
			result24 = cursor.fetchone()
			
			dis25 = "SELECT psmeteoTbk1_2_1315 FROM Psychrometer_Sangkar_Meteo1315_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis25)
			result25 = cursor.fetchone()
			
			dis26 = "SELECT psmeteoTbb1_2_1315 FROM Psychrometer_Sangkar_Meteo1315_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis26)
			result26 = cursor.fetchone()
			
			dis27 = "SELECT psmeteoRH1_2_1315 FROM Psychrometer_Sangkar_Meteo1315_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis27)
			result27 = cursor.fetchone()

			dis28 = "SELECT psmeteoTbk4_1315 FROM Psychrometer_Sangkar_Meteo1315_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis28)
			result28 = cursor.fetchone()
			
			dis29 = "SELECT psmeteoTbb4_1315 FROM Psychrometer_Sangkar_Meteo1315_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis29)
			result29 = cursor.fetchone()
			
			dis30 = "SELECT psmeteoRH4_1315 FROM Psychrometer_Sangkar_Meteo1315_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis30)
			result30 = cursor.fetchone()
			
			dis31 = "SELECT psmeteoTbk7_1315 FROM Psychrometer_Sangkar_Meteo1315_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis31)
			result31 = cursor.fetchone()
			
			dis32 = "SELECT psmeteoTbb7_1315 FROM Psychrometer_Sangkar_Meteo1315_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis32)
			result32 = cursor.fetchone()
			
			dis33 = "SELECT psmeteoRH7_1315 FROM Psychrometer_Sangkar_Meteo1315_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis33)
			result33 = cursor.fetchone()
			
			dis34 = "SELECT psmeteoTbk10_1315 FROM Psychrometer_Sangkar_Meteo1315_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis34)
			result34 = cursor.fetchone()
			
			dis35 = "SELECT psmeteoTbb10_1315 FROM Psychrometer_Sangkar_Meteo1315_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis35)
			result35 = cursor.fetchone()
			
			dis36 = "SELECT psmeteoRH10_1315 FROM Psychrometer_Sangkar_Meteo1315_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis36)
			result36 = cursor.fetchone()
			
			dis37 = "SELECT psmeteoTbk1_2_1345 FROM Psychrometer_Sangkar_Meteo1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis37)
			result37 = cursor.fetchone()
			
			dis38 = "SELECT psmeteoTbb1_2_1345 FROM Psychrometer_Sangkar_Meteo1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis38)
			result38 = cursor.fetchone()
			
			dis39 = "SELECT psmeteoRH1_2_1345 FROM Psychrometer_Sangkar_Meteo1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis39)
			result39 = cursor.fetchone()

			dis40 = "SELECT psmeteoTbk4_1345 FROM Psychrometer_Sangkar_Meteo1345_1 WHERE Waktu = '%s'"  % input_tahun_bulan_tanggal.get()
			cursor.execute(dis40)
			result40 = cursor.fetchone()
			
			dis41 = "SELECT psmeteoTbb4_1345 FROM Psychrometer_Sangkar_Meteo1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis41)
			result41 = cursor.fetchone()
			
			dis42 = "SELECT psmeteoRH4_1345 FROM Psychrometer_Sangkar_Meteo1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis42)
			result42 = cursor.fetchone()
			
			dis43 = "SELECT psmeteoTbk7_1345 FROM Psychrometer_Sangkar_Meteo1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis43)
			result43 = cursor.fetchone()
			
			dis44 = "SELECT psmeteoTbb7_1345 FROM Psychrometer_Sangkar_Meteo1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis44)
			result44 = cursor.fetchone()
			
			dis45 = "SELECT psmeteoRH7_1345 FROM Psychrometer_Sangkar_Meteo1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis45)
			result45 = cursor.fetchone()
			
			dis46 = "SELECT psmeteoTbk10_1345 FROM Psychrometer_Sangkar_Meteo1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis46)
			result46 = cursor.fetchone()
			
			dis47 = "SELECT psmeteoTbb10_1345 FROM Psychrometer_Sangkar_Meteo1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis47)
			result47 = cursor.fetchone()
			
			dis48 = "SELECT psmeteoRH10_1345 FROM Psychrometer_Sangkar_Meteo1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis48)
			result48 = cursor.fetchone()
			
			dis49 = "SELECT psmeteoTbk1_2_1415 FROM Psychrometer_Sangkar_Meteo1415_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis49)
			result49 = cursor.fetchone()
			
			dis50 = "SELECT psmeteoTbb1_2_1415 FROM Psychrometer_Sangkar_Meteo1415_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis50)
			result50 = cursor.fetchone()
			
			dis51 = "SELECT psmeteoRH1_2_1415 FROM Psychrometer_Sangkar_Meteo1415_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis51)
			result51 = cursor.fetchone()
			
			dis52 = "SELECT psmeteoTbk4_1415 FROM Psychrometer_Sangkar_Meteo1415_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis52)
			result52 = cursor.fetchone()
			
			dis53 = "SELECT psmeteoTbb4_1415 FROM Psychrometer_Sangkar_Meteo1415_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis52)
			result53 = cursor.fetchone()
			
			dis54 = "SELECT psmeteoRH4_1415 FROM Psychrometer_Sangkar_Meteo1415_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis54)
			result54 = cursor.fetchone()
			
			dis55 = "SELECT psmeteoTbk7_1415 FROM Psychrometer_Sangkar_Meteo1415_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis55)
			result55 = cursor.fetchone()
			
			dis56 = "SELECT psmeteoTbb7_1415 FROM Psychrometer_Sangkar_Meteo1415_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis56)
			result56 = cursor.fetchone()
			
			dis57 = "SELECT psmeteoRH7_1415 FROM Psychrometer_Sangkar_Meteo1415_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis57)
			result57 = cursor.fetchone()
			
			dis58 = "SELECT psmeteoTbk10_1415 FROM Psychrometer_Sangkar_Meteo1415_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis58)
			result58 = cursor.fetchone()
			
			dis59 = "SELECT psmeteoTbb10_1415 FROM Psychrometer_Sangkar_Meteo1415_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis59)
			result59 = cursor.fetchone()
			
			dis60 = "SELECT psmeteoRH10_1415 FROM Psychrometer_Sangkar_Meteo1415_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis60)
			result60 = cursor.fetchone()
			
			dis61 = "SELECT psmeteoTbk1_2_1745 FROM Psychrometer_Sangkar_Meteo1745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis61)
			result61 = cursor.fetchone()
			
			dis62 = "SELECT psmeteoTbb1_2_1745 FROM Psychrometer_Sangkar_Meteo1745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis62)
			result62 = cursor.fetchone()
			
			dis63 = "SELECT psmeteoRH1_2_1745 FROM Psychrometer_Sangkar_Meteo1745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis63)
			result63 = cursor.fetchone()
			
			dis64 = "SELECT psmeteoTbk4_1745 FROM Psychrometer_Sangkar_Meteo1745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis64)
			result64 = cursor.fetchone()
			
			dis65 = "SELECT psmeteoTbb4_1745 FROM Psychrometer_Sangkar_Meteo1745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis65)
			result65 = cursor.fetchone()
			
			dis66 = "SELECT psmeteoRH4_1745 FROM Psychrometer_Sangkar_Meteo1745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis66)
			result66 = cursor.fetchone()
				
			dis67 = "SELECT psmeteoTbk7_1745 FROM Psychrometer_Sangkar_Meteo1745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis67)
			result67 = cursor.fetchone()
			
			dis68 = "SELECT psmeteoTbb7_1745 FROM Psychrometer_Sangkar_Meteo1745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis68)
			result68 = cursor.fetchone()
			
			dis69 = "SELECT psmeteoRH7_1745 FROM Psychrometer_Sangkar_Meteo1745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis69)
			result69 = cursor.fetchone()

			dis70 = "SELECT psmeteoTbk10_1745 FROM Psychrometer_Sangkar_Meteo1745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis70)
			result70 = cursor.fetchone()
			
			dis71 = "SELECT psmeteoTbb10_1745 FROM Psychrometer_Sangkar_Meteo1745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis71)
			result71 = cursor.fetchone()
			
			dis72 = "SELECT psmeteoRH10_1745 FROM Psychrometer_Sangkar_Meteo1745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis72)
			result72 = cursor.fetchone()	

			dis73 = "SELECT psmeteoTbk1_2_1815 FROM Psychrometer_Sangkar_Meteo1815_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis73)
			result73 = cursor.fetchone()
			
			dis74 = "SELECT psmeteoTbb1_2_1815 FROM Psychrometer_Sangkar_Meteo1815_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis74)
			result74 = cursor.fetchone()
			
			dis75 = "SELECT psmeteoRH1_2_1815 FROM Psychrometer_Sangkar_Meteo1815_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis75)
			result75 = cursor.fetchone()
			
			dis76 = "SELECT psmeteoTbk4_1815 FROM Psychrometer_Sangkar_Meteo1815_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis76)
			result76 = cursor.fetchone()
			
			dis77 = "SELECT psmeteoTbb4_1815 FROM Psychrometer_Sangkar_Meteo1815_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis77)
			result77 = cursor.fetchone()
			
			dis78 = "SELECT psmeteoRH4_1815 FROM Psychrometer_Sangkar_Meteo1815_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis78)
			result78 = cursor.fetchone()
			
			dis79 = "SELECT psmeteoTbk7_1815 FROM Psychrometer_Sangkar_Meteo1815_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis79)
			result79 = cursor.fetchone()
			
			dis80 = "SELECT psmeteoTbb7_1815 FROM Psychrometer_Sangkar_Meteo1815_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis80)
			result80 = cursor.fetchone()
			
			dis81 = "SELECT psmeteoRH7_1815 FROM Psychrometer_Sangkar_Meteo1815_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis81)
			result81 = cursor.fetchone()

			dis82 = "SELECT psmeteoTbk10_1815 FROM Psychrometer_Sangkar_Meteo1815_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis82)
			result82 = cursor.fetchone()
			
			dis83 = "SELECT psmeteoTbb10_1815 FROM Psychrometer_Sangkar_Meteo1815_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis83)
			result83 = cursor.fetchone()
			
			dis84 = "SELECT psmeteoRH10_1815 FROM Psychrometer_Sangkar_Meteo1815_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis84)
			result84 = cursor.fetchone()
			
		# Lama Penyinaran	
		with con.cursor() as cursor:
			dis85 = "SELECT lamapenyinaran12jam_jam FROM Lama_Penyinaran_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis85)
			result85 = cursor.fetchone()
			
			dis86 = "SELECT lamapenyinaran8jam_jam FROM Lama_Penyinaran_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis86)
			result86 = cursor.fetchone()

			dis87 = "SELECT lamapenyinaran12jam_persen FROM Lama_Penyinaran_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis87)
			result87 = cursor.fetchone()
			
			dis88 = "SELECT lamapenyinaran8jam_persen FROM Lama_Penyinaran_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis88)
			result88 = cursor.fetchone()
			
		#Termometer Maksimum dan Minimum
		with con.cursor() as cursor:
			dis89 = "SELECT termoMM_max_1815 FROM Termo_Max_Min1815_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis89)
			result89 = cursor.fetchone()
			
			dis90 = "SELECT termoMM_reset_1815 FROM Termo_Max_Min1815_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis90)
			result90 = cursor.fetchone()

			dis91 = "SELECT termoMM_min_1415 FROM Termo_Max_Min1415_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis91)
			result91 = cursor.fetchone()

			dis92 = "SELECT termoMM_reset_1415 FROM Termo_Max_Min1415_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis92)
			result92 = cursor.fetchone()	

		# Piche Evaporimeter
		with con.cursor() as cursor:
			dis93 = "SELECT piche_evaporimeter1_07_45 FROM Piche_Evaporimeter_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis93)
			result93 = cursor.fetchone()
			
			dis94 = "SELECT piche_evaporimeter2_07_45 FROM Piche_Evaporimeter_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis94)
			result94 = cursor.fetchone()
			
			dis95 = "SELECT piche_evaporimeter1_13_45 FROM Piche_Evaporimeter_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis95)
			result95 = cursor.fetchone()
			
			dis96 = "SELECT piche_evaporimeter2_13_45 FROM Piche_Evaporimeter_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis96)
			result96 = cursor.fetchone()

			dis97 = "SELECT piche_evaporimeter1_17_45 FROM Piche_Evaporimeter_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis97)
			result97 = cursor.fetchone()
			
			dis98 = "SELECT piche_evaporimeter2_17_45 FROM Piche_Evaporimeter_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis98)
			result98 = cursor.fetchone()
			
		# Radiasi
		with con.cursor() as cursor:
			dis99 = "SELECT intensitas FROM Radiasi_2 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis99)
			result99 = cursor.fetchone()
			
		# Suhu Minimum Rumput
		with con.cursor() as cursor:
			dis100 = "SELECT suhumin_rumput0715 FROM Suhu_Minimum_Rumput_2 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis100)
			result100 = cursor.fetchone()
				
			dis101 = "SELECT suhumin_rumput0715_reset FROM Suhu_Minimum_Rumput_2 WHERE Waktu = '%s'"  % input_tahun_bulan_tanggal.get()
			cursor.execute(dis101)
			result101 = cursor.fetchone()	

		# Kondisi Cuaca dan Tanah
		with con.cursor() as cursor:
			dis102 = "SELECT kodetanah_07_15 FROM Kondisi_Cuaca_Tanah0715_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis102)
			result102 = cursor.fetchone()
			
			dis103 = "SELECT kodetanah_14_15 FROM Kondisi_Cuaca_Tanah1415_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis103)
			result103 = cursor.fetchone()
			
			dis104 = "SELECT kodecuaca_07_15 FROM Kondisi_Cuaca_Tanah0715_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis104)
			result104 = cursor.fetchone()
			
			dis105 = "SELECT kodecuaca_14_15 FROM Kondisi_Cuaca_Tanah1415_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis105)
			result105 = cursor.fetchone()
			
		# Open Pan
		with con.cursor() as cursor:
			dis106 = "SELECT ketinggian_airpanci07_15 FROM Open_Pan_0715_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis106)
			result106 = cursor.fetchone()
			
			dis107 = "SELECT ketinggian_airpanci07_45 FROM Open_Pan_0745_2 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis107)
			result107 = cursor.fetchone()
			
			dis108 = "SELECT ketinggian_airpanci13_45 FROM Open_Pan_1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis108)
			result108 = cursor.fetchone()
			
			dis109 = "SELECT ketinggian_airpanci17_45 FROM Open_Pan_1745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis109)
			result109 = cursor.fetchone()
			
			dis110 = "SELECT suhu_airmax07_15 FROM Open_Pan_0715_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis110)
			result110 = cursor.fetchone()
			
			dis111 = "SELECT suhu_airmax07_45 FROM Open_Pan_0745_2 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis111)
			result111 = cursor.fetchone()

			dis112 = "SELECT suhu_airmax13_45 FROM Open_Pan_1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis112)
			result112 = cursor.fetchone()
			
			dis113 = "SELECT suhu_airmax17_45 FROM Open_Pan_1745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis113)
			result113 = cursor.fetchone()
			
			dis114 = "SELECT suhu_airmin07_15 FROM Open_Pan_0715_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis114)
			result114 = cursor.fetchone()
			
			dis115 = "SELECT suhu_airmin07_45 FROM Open_Pan_0745_2 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis115)
			result115 = cursor.fetchone()
			
			dis116 = "SELECT suhu_airmin13_45 FROM Open_Pan_1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis116)
			result116 = cursor.fetchone()
			
			dis117 = "SELECT suhu_airmin17_45 FROM Open_Pan_1745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis117)
			result117 = cursor.fetchone()
			
			dis118 = "SELECT hujan_13_5jam07_15 FROM Open_Pan_0715_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis118)
			result118 = cursor.fetchone()
			
			dis119 = "SELECT hujan_24jam_07_15 FROM Open_Pan_0715_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis119)
			result119 = cursor.fetchone()
			
			dis120 = "SELECT hujan_30menit07_45 FROM Open_Pan_0745_2 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis120)
			result120 = cursor.fetchone()
			
			dis121 = "SELECT hujan_6jam_13_45 FROM Open_Pan_1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis121)
			result121 = cursor.fetchone()
			
			dis122 = "SELECT hujan_4jam_17_45 FROM Open_Pan_1745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis122)
			result122 = cursor.fetchone()
			
			dis123 = "SELECT penguapan_24jam_07_15 FROM Open_Pan_0715_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis123)
			result123 = cursor.fetchone()
			
			dis124 = "SELECT penguapan_13_5jam07_45 FROM Open_Pan_0745_2 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis124)
			result124 = cursor.fetchone()
			
			dis125 = "SELECT penguapan_6jam_13_45 FROM Open_Pan_1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis125)
			result125 = cursor.fetchone()
			
			dis126 = "SELECT penguapan_4jam_17_45 FROM Open_Pan_1745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis126)
			result126 = cursor.fetchone()
			
		# Barometer
		with con.cursor() as cursor:
			dis127 = "SELECT suhu00_00UTC FROM Barometer_5 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis127)
			result127 = cursor.fetchone()
			
			dis128 = "SELECT barometer00_00UTC FROM Barometer_5 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis128)
			result128 = cursor.fetchone()
			
			dis129 = "SELECT QFF00_00UTC FROM Barometer_5 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis129)
			result129 = cursor.fetchone()
			
			dis130 = "SELECT QFE00_00UTC FROM Barometer_5 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis130)
			result130 = cursor.fetchone()
			
		# Catatan
		with con.cursor() as cursor:
			dis302 = "SELECT catatan1 FROM PMGonDuty_Catatan_4 WHERE Waktu = '%s' " % input_tahun_bulan_tanggal.get()
			cursor.execute(dis302)
			result302 = cursor.fetchone()
			
		
		"""===================================================== MYSQL ENDS HERE ========================================================"""
		
		"""-------------------------------------- TABEL PERTAMA - PSYCHROMETER SANGKAR METEOROLOGI ---------------------------------------"""
		#kolom1 PSYCHROMETER SANGKAR
		#kolom2 PSYCHROMETER SANGKAR 07.15
		#entry psychro sangkar kolom2 1.2m
		Label(win, text=result1, bg="white", font="callibri 7").place(x=87, y=84)
		Label(win, text=result2, bg="white", font="callibri 7").place(x=87, y=103)
		Label(win, text=result3, bg="white", font="callibri 7").place(x=91, y=122)
		#entry psychro sangkar kolom2 4m
		Label(win, text=result4, bg="white", font="callibri 7").place(x=122, y=84)
		Label(win, text=result5, bg="white", font="callibri 7").place(x=122, y=103)
		Label(win, text=result6, bg="white", font="callibri 7").place(x=126, y=122)
		#entry psychro sangkar kolom2 7m
		Label(win, text=result7, bg="white", font="callibri 7").place(x=157, y=84)
		Label(win, text=result8, bg="white", font="callibri 7").place(x=157, y=103)
		Label(win, text=result9, bg="white", font="callibri 7").place(x=161, y=122)
		#entry psychro sangkar kolom2 10m
		Label(win, text=result10, bg="white", font="callibri 7").place(x=192, y=84)
		Label(win, text=result11, bg="white", font="callibri 7").place(x=192, y=103)
		Label(win, text=result12, bg="white", font="callibri 7").place(x=196, y=122)

		#kolom3 PSYCHROMETER SANGKAR 07.45
		#entry psychro sangkar kolom3 1.2m
		Label(win, text=result13, bg="white", font="callibri 7").place(x=228, y=84)
		Label(win, text=result14, bg="white", font="callibri 7").place(x=228, y=103)
		Label(win, text=result15, bg="white", font="callibri 7").place(x=232, y=122)
		#entry psychro sangkar kolom3 4m
		Label(win, text=result16, bg="white", font="callibri 7").place(x=263, y=84)
		Label(win, text=result17, bg="white", font="callibri 7").place(x=263, y=103)
		Label(win, text=result18, bg="white", font="callibri 7").place(x=267, y=122)
		#entry psychro sangkar kolom3 7m
		Label(win, text=result19, bg="white", font="callibri 7").place(x=298, y=84)
		Label(win, text=result20, bg="white", font="callibri 7").place(x=298, y=103)
		Label(win, text=result21, bg="white", font="callibri 7").place(x=302, y=122)
		#entry psychro sangkar kolom3 10m
		Label(win, text=result22, bg="white", font="callibri 7").place(x=333, y=84)
		Label(win, text=result23, bg="white", font="callibri 7").place(x=333, y=103)
		Label(win, text=result24, bg="white", font="callibri 7").place(x=337, y=122)

		#kolom4 PSYCHROMETER SANGKAR 13.15
		#entry psychro sangkar kolom4 1.2m
		Label(win, text=result25, bg="white", font="callibri 7").place(x=369, y=84)
		Label(win, text=result26, bg="white", font="callibri 7").place(x=369, y=103)
		Label(win, text=result27, bg="white", font="callibri 7").place(x=373, y=122)
		#entry psychro sangkar kolom4 4m
		Label(win, text=result28, bg="white", font="callibri 7").place(x=404, y=84)
		Label(win, text=result29, bg="white", font="callibri 7").place(x=404, y=103)
		Label(win, text=result30, bg="white", font="callibri 7").place(x=408, y=122)
		#entry psychro sangkar kolom4 7m
		Label(win, text=result31, bg="white", font="callibri 7").place(x=439, y=84)
		Label(win, text=result32, bg="white", font="callibri 7").place(x=439, y=103)
		Label(win, text=result33, bg="white", font="callibri 7").place(x=443, y=122)
		#entry psychro sangkar kolom4 10m
		Label(win, text=result34, bg="white", font="callibri 7").place(x=474, y=84)
		Label(win, text=result35, bg="white", font="callibri 7").place(x=474, y=103)
		Label(win, text=result36, bg="white", font="callibri 7").place(x=478, y=122)

		#kolom5 PSYCHROMETER SANGKAR 13.45
		#entry psychro sangkar kolom5 1.2m
		Label(win, text=result37, bg="white", font="callibri 7").place(x=510, y=84)
		Label(win, text=result38, bg="white", font="callibri 7").place(x=510, y=103)
		Label(win, text=result39, bg="white", font="callibri 7").place(x=514, y=122)
		#entry psychro sangkar kolom5 4m
		Label(win, text=result40, bg="white", font="callibri 7").place(x=545, y=84)
		Label(win, text=result41, bg="white", font="callibri 7").place(x=545, y=103)
		Label(win, text=result42, bg="white", font="callibri 7").place(x=549, y=122)
		#entry psychro sangkar kolom5 7m
		Label(win, text=result43, bg="white", font="callibri 7").place(x=580, y=84)
		Label(win, text=result44, bg="white", font="callibri 7").place(x=580, y=103)
		Label(win, text=result45, bg="white", font="callibri 7").place(x=584, y=122)
		#entry psychro sangkar kolom5 10m
		Label(win, text=result46, bg="white", font="callibri 7").place(x=615, y=84)
		Label(win, text=result47, bg="white", font="callibri 7").place(x=615, y=103)
		Label(win, text=result48, bg="white", font="callibri 7").place(x=619, y=122)

		#kolom6 PSYCHROMETER SANGKAR 14.15
		#entry psychro sangkar kolom6 1.2m
		Label(win, text=result49, bg="white", font="callibri 7").place(x=651, y=84)
		Label(win, text=result50, bg="white", font="callibri 7").place(x=651, y=103)
		Label(win, text=result51, bg="white", font="callibri 7").place(x=655, y=122)
		#entry psychro sangkar kolom6 4m
		Label(win, text=result52, bg="white", font="callibri 7").place(x=686, y=84)
		Label(win, text=result53, bg="white", font="callibri 7").place(x=686, y=103)
		Label(win, text=result54, bg="white", font="callibri 7").place(x=690, y=122)
		#entry psychro sangkar kolom6 7m
		Label(win, text=result55, bg="white", font="callibri 7").place(x=721, y=84)
		Label(win, text=result56, bg="white", font="callibri 7").place(x=721, y=103)
		Label(win, text=result57, bg="white", font="callibri 7").place(x=725, y=122)
		#entry psychro sangkar kolom6 10m
		Label(win, text=result58, bg="white", font="callibri 7").place(x=791, y=84)
		Label(win, text=result59, bg="white", font="callibri 7").place(x=791, y=103)
		Label(win, text=result60, bg="white", font="callibri 7").place(x=795, y=122)
		"""--------------------------- AKHIR TABEL PERTAMA - PSYCHROMETER SANGKAR METEOROLOGI --------------------------------"""

		"""--------------------------- TABEL KEDUA - LANJUTAN PSYCHROMETER SANGKAR METEOROLOGI -------------------------------"""

		#kolom1 PSYCHROMETER SANGKAR TABEL 2
		#kolom2 PSYCHROMETER SANGKAR TABEL 2 17.45
		#entry psychro sangkar tabel2 kolom2 1.2m
		Label(win, text=result61, bg="white", font="callibri 7").place(x=87, y=219)
		Label(win, text=result62, bg="white", font="callibri 7").place(x=87, y=238)
		Label(win, text=result63, bg="white", font="callibri 7").place(x=91, y=257)
		#entry psychro sangkar tabel2 kolom2 4m
		Label(win, text=result64, bg="white", font="callibri 7").place(x=122, y=219)
		Label(win, text=result65, bg="white", font="callibri 7").place(x=122, y=238)
		Label(win, text=result66, bg="white", font="callibri 7").place(x=126, y=257)
		#entry psychro sangkar tabel2 kolom2 7m
		Label(win, text=result67, bg="white", font="callibri 7").place(x=157, y=219)
		Label(win, text=result68, bg="white", font="callibri 7").place(x=157, y=238)
		Label(win, text=result69, bg="white", font="callibri 7").place(x=161, y=257)
		#entry psychro sangkar tabel2 kolom2 10m
		Label(win, text=result70, bg="white", font="callibri 7").place(x=192, y=219)
		Label(win, text=result71, bg="white", font="callibri 7").place(x=192, y=238)
		Label(win, text=result72, bg="white", font="callibri 7").place(x=196, y=257)

		#kolom3 PSYCHROMETER SANGKAR TABEL 2 18.15
		#entry psychro sangkar tabel2 kolom3 1.2m
		Label(win, text=result73, bg="white", font="callibri 7").place(x=228, y=219)
		Label(win, text=result74, bg="white", font="callibri 7").place(x=228, y=238)
		Label(win, text=result75, bg="white", font="callibri 7").place(x=232, y=257)
		#entry psychro sangkar tabel2 kolom3 4m
		Label(win, text=result76, bg="white", font="callibri 7").place(x=263, y=219)
		Label(win, text=result77, bg="white", font="callibri 7").place(x=263, y=238)
		Label(win, text=result78, bg="white", font="callibri 7").place(x=267, y=257)
		#entry psychro sangkar tabel2 kolom3 7m
		Label(win, text=result79, bg="white", font="callibri 7").place(x=298, y=219)
		Label(win, text=result80, bg="white", font="callibri 7").place(x=298, y=238)
		Label(win, text=result81, bg="white", font="callibri 7").place(x=312, y=257)
		#entry psychro sangkar tabel2 kolom3 10m
		Label(win, text=result82, bg="white", font="callibri 7").place(x=333, y=219)
		Label(win, text=result73, bg="white", font="callibri 7").place(x=333, y=238)
		Label(win, text=result84, bg="white", font="callibri 7").place(x=337, y=257)
		"""---------------------------- AKHIR TABEL KEDUA - LANJUTAN PSYCHROMETER SANGKAR METEOROLOGI ------------------------"""

		"""-------------------------------------------- TABEL KETIGA - LAMA PENYINARAN ---------------------------------------"""
		#kolom1 lama penyinaran
		#kolom2 lama penyinaran jam
		Label(win, text=result85, bg="white", font="callibri 7").place(x=441, y=209)
		Label(win, text=result86, bg="white", font="callibri 7").place(x=441, y=247)
		#kolom3 lama penyinaran %
		Label(win, text=result87, bg="white", font="callibri 7").place(x=476 , y=209)
		Label(win, text=result88, bg="white", font="callibri 7").place(x=476 , y=247)
		"""------------------------------------------ AKHIR TABEL KETIGA - LAMA PENYINARAN -----------------------------------"""

		"""----------------------------------- TABEL KEEMPAT - TERMOMETER MAKSIMUM DAN MINIMUM -------------------------------"""
		#kolom2 termometer maksimum dan minimum 18.15
		Label(win, text=result89, bg="white", fg="black", font="callibri 7").place(x=688, y=238)
		Label(win, text=result90, bg="white", fg="black", font="callibri 7").place(x=723, y=238)
		#kolom3 termometer maksimum dan minimum 14.15
		Label(win, text=result91, bg="white", fg="black", font="callibri 7").place(x=758, y=238)
		Label(win, text=result92, bg="white", fg="black", font="callibri 7").place(x=809, y=238)
		"""------------------------------- AKHIR TABEL KEEMPAT - TERMOMETER MAKSIMUM DAN MINIMUM --------------------------------"""

		"""---------------------------------------- TABEL KELIMA - PICHE EVAPORIMETER--------------------------------------------"""
		#kolom1 EVAPORIMETER
		#kolom2 evaporimeter
		Label(win, text=result93, bg="white", font="callibri 7").place(x=124, y=357)
		Label(win, text=result94, bg="white", font="callibri 7").place(x=124, y=376)
		Label(win, text=result95, bg="white", font="callibri 7").place(x=124, y=395)
		Label(win, text=result96, bg="white", font="callibri 7").place(x=124, y=414)
		Label(win, text=result97, bg="white", font="callibri 7").place(x=124, y=433)
		Label(win, text=result98, bg="white", font="callibri 7").place(x=124, y=452)
		"""------------------------------------- AKHIR TABEL KELIMA - PICHE EVAPORIMETER ---------------------------------------"""

		"""---------------------------------------------- TABEL KEENAM - RADIASI -----------------------------------------------"""
		#kolom1 radiasi
		#kolom2 radiasi
		Label(win, text=result99, bg="white", font="callibri 7").place(x=322, y=343)
		"""----------------------------------------- AKHIR TABEL KEENAM - RADIASI ----------------------------------------------"""

		"""---------------------------------------- TABEL KETUJUH - SUHU MIN RUMPUT --------------------------------------------"""
		#KOLOM1 suhu min rumput
		#KOLOM2 suhu min rumput pembacaan
		Label(win, text=result100, bg="white", font="callibri 7").place(x=442, y=346)
		#KOLOM3 suhu min rumput reseting
		Label(win, text=result101, bg="white", font="callibri 7").place(x=477, y=346)
		"""--------------------------------------- AKHIR TABEL KETUJUH - SUHU MIN RUMPUT ----------------------------------------"""

		"""------------------------------------- TABEL KEDELAPAN - KONDISI CUACA DAN TANAH --------------------------------------"""
		#kolom1 kondisi cuaca tanah
		#kolom2 kondisi cuaca tanah kode tanah
		Label(win, text=result102, bg="white", font="callibri 7").place(x=324, y=434)
		Label(win, text=result103, bg="white", font="callibri 7").place(x=324, y=453)
		#kolom3 kondisi cuaca tanah kode cuaca
		Label(win, text=result104, bg="white", font="callibri 7").place(x=390, y=434)
		Label(win, text=result105, bg="white", font="callibri 7").place(x=390, y=453)
		"""---------------------------------- AKHIR TABEL KEDELAPAN - KONDISI CUACA DAN TANAH ----------------------------------"""

		"""--------------------------------------------- TABEL KESEMBILAN - OPEN PAN -------------------------------------------"""
		#kolom1 open pan
		#kolom2 open pan ketinggian air di panci
		Label(win, text=result106, bg="white", font="callibri 7").place(x=593, y=354)
		Label(win, text="-", bg="white", font="callibri 7").place(x=593, y=373)
		Label(win, text=result107, bg="white", font="callibri 7").place(x=593, y=392)
		Label(win, text="-", bg="white", font="callibri 7").place(x=593, y=411)
		Label(win, text=result108, bg="white", font="callibri 7").place(x=593, y=430)
		Label(win, text="-", bg="white", font="callibri 7").place(x=593, y=449)
		Label(win, text=result109, bg="white", font="callibri 7").place(x=593, y=468)
		Label(win, text="-", bg="white", font="callibri 7").place(x=593, y=487)

		#kolom3 open pan suhu air
		#kolom3 open pan suhu air MAX
		Label(win, text=result110, bg="white", font="callibri 7").place(x=650, y=364)
		Label(win, text=result111, bg="white", font="callibri 7").place(x=650, y=402)
		Label(win, text=result112, bg="white", font="callibri 7").place(x=650, y=440)
		Label(win, text=result113, bg="white", font="callibri 7").place(x=650, y=478)
		#kolom3 open pan suhu air MIN
		Label(win, text=result114, bg="white", font="callibri 7").place(x=685, y=364)
		Label(win, text=result115, bg="white", font="callibri 7").place(x=685, y=402)
		Label(win, text=result116, bg="white", font="callibri 7").place(x=685, y=440)
		Label(win, text=result117, bg="white", font="callibri 7").place(x=685, y=478)

		#kolom4 Hujan
		Label(win, text=result118, bg="white", font="callibri 7").place(x=720, y=373) #13.5 Jam
		Label(win, text=result119, bg="white", font="callibri 7").place(x=755, y=373) #24 Jam
		Label(win, text=result120, bg="white", font="callibri 7").place(x=740, y=411)
		Label(win, text=result121, bg="white", font="callibri 7").place(x=740, y=449)
		Label(win, text=result122, bg="white", font="callibri 7").place(x=740, y=487)

		#kolom5 Penguapan
		Label(win, text=result123, bg="white", font="callibri 7").place(x=803, y=373)
		Label(win, text=result124, bg="white", font="callibri 7").place(x=803, y=411)
		Label(win, text=result125, bg="white", font="callibri 7").place(x=803, y=449)
		Label(win, text=result126, bg="white", font="callibri 7").place(x=803, y=487)
		"""------------------------------------------- AKHIR TABEL KESEMBILAN - OPEN PAN --------------------------------------"""

		"""---------------------------------------------- TABEL KESEPULUH - BAROMETER -----------------------------------------"""
		#kolom1 barometer
		#kolom2 barometer
		#print(result127)
		Label(win, text= result127, bg="white", font="callibri 7").place(x=123, y=532)
		Label(win, text= result128, bg="white", font="callibri 7").place(x=123, y=551)
		Label(win, text= result129, bg="white", font="callibri 7").place(x=118, y=570)
		Label(win, text= result130, bg="white", font="callibri 7").place(x=118, y=589)
				
		"""------------------------------------------- AKHIR TABEL KESEPULUH - BAROMETER --------------------------------------"""
		
		"""----------------------------------------- TABEL KESEBELAS - CATATAN DAN TANGGAL ------------------------------------"""
		with con.cursor() as cursor:
			dis299 = "SELECT tanggal FROM PMGonDuty_Catatan_4 WHERE Waktu = '%s' " % input_tahun_bulan_tanggal.get()
			cursor.execute(dis299)
			result299 = cursor.fetchone()
		
		hitung3 = result299[0]
		Hitung3 = hitung3[3]
		Hitung4 = hitung3[4]

		if (Hitung3==str(0)):
			if(Hitung4=="1"):
				Tanggal_pmg_on_duty = hitung3[0] + hitung3[1] + " JANUARI " + hitung3[6] + hitung3[7] + hitung3[8] + hitung3[9]
			elif(Hitung4=="2"):
				Tanggal_pmg_on_duty = hitung3[0] + hitung3[1] + " FEBRUARI " + hitung3[6] + hitung3[7] + hitung3[8] + hitung3[9]
			elif(Hitung4=="3"):
				Tanggal_pmg_on_duty = hitung3[0] + hitung3[1] + " MARET " + hitung3[6] + hitung3[7] + hitung3[8] + hitung3[9]
			elif(Hitung4=="4"):
				Tanggal_pmg_on_duty = hitung3[0] + hitung3[1] + " APRIL " + hitung3[6] + hitung3[7] + hitung3[8] + hitung3[9]
			elif(Hitung4=="5"):
				Tanggal_pmg_on_duty = hitung3[0] + hitung3[1] + " MEI " + hitung3[6] + hitung3[7] + hitung3[8] + hitung3[9]
			elif(Hitung4=="6"):
				Tanggal_pmg_on_duty = hitung3[0] + hitung3[1] + " JUNI " + hitung3[6] + hitung3[7] + hitung3[8] + hitung3[9]
			elif(Hitung4=="7"):
				Tanggal_pmg_on_duty = hitung3[0] + hitung3[1] + " JULI " + hitung3[6] + hitung3[7] + hitung3[8] + hitung3[9]
			elif(Hitung4=="8"):
				Tanggal_pmg_on_duty = hitung3[0] + hitung3[1] + " AGUSTUS " + hitung3[6] + hitung3[7] + hitung3[8] + hitung3[9]
			elif(Hitung4=="9"):
				Tanggal_pmg_on_duty = hitung3[0] + hitung3[1] + " SEPTEMBER " + hitung3[6] + hitung3[7] + hitung3[8] + hitung3[9]
		elif(Hitung3=="1"):
			if(Hitung4==str(0)):
				Tanggal_pmg_on_duty = hitung3[0] + hitung3[1] + " OKTOBER " + hitung3[6] + hitung3[7] + hitung3[8] + hitung3[9]
			elif(Hitung4=="1"):
				Tanggal_pmg_on_duty = hitung3[0] + hitung3[1] + " NOVEMBER " + hitung3[6] + hitung3[7] + hitung3[8] + hitung3[9]
			elif(Hitung4=="2"):
				Tanggal_pmg_on_duty = hitung3[0] + hitung3[1] + " DESEMBER " + hitung3[6] + hitung3[7] + hitung3[8] + hitung3[9]
		else:
			Tanggal_pmg_on_duty = "Tanggal Salah"

		Label(win, text=result302, bg="white", font="callibri 7").place(x=229, y=525)
		Label(win, text=Tanggal_pmg_on_duty, bg="white", font="callibri 9 bold").place(x=725, y=569)
		"""---------------------------------------- AKHIR TABEL KESEBELAS - CATATAN DAN TANGGAL -------------------------------"""
		
		#"""#################################################### HALAMAN KEDUA #################################################"""
	def halaman2():
		Frame(win, width=864, height=630, bg="white").place(x=0, y=0)
		label2 = Label(image=img2).place(x=3, y=0)
		"""----------------------------------------------- TABEL KEDUA BELAS - ANGIN ------------------------------------"""
		# Angin
		con = pymysql.connect("localhost", "root", "12345", "Buku_Klimatologi_BMKG")
		with con.cursor() as cursor:
			dis131 ="SELECT cup0_5_07_15 FROM Angin0715_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis131)
			result131 = cursor.fetchone()
			
			dis132 ="SELECT cup0_5_07_45 FROM Angin0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis132)
			result132 = cursor.fetchone()

			dis133 ="SELECT cup0_5_13_45 FROM Angin1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis133)
			result133 = cursor.fetchone()
			
			dis134 ="SELECT cup0_5_14_15 FROM Angin1415_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis134)
			result134 = cursor.fetchone()
			
			dis135 ="SELECT cup0_5_17_45 FROM Angin1745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis135)
			result135 = cursor.fetchone()
			
			dis136 ="SELECT cup0_5_18_15 FROM Angin1815_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis136)
			result136 = cursor.fetchone()
			
			dis137 ="SELECT cup2_0_07_15 FROM Angin0715_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis137)
			result137 = cursor.fetchone()
			
			dis138 ="SELECT cup2_0_07_45 FROM Angin0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis138)
			result138 = cursor.fetchone()
			
			dis139 ="SELECT cup2_0_13_45 FROM Angin1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis139)
			result139 = cursor.fetchone()
			
			dis140 ="SELECT cup2_0_14_15 FROM Angin1415_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis140)
			result140 = cursor.fetchone()
			
			dis141 ="SELECT cup2_0_17_45 FROM Angin1745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis141)
			result141 = cursor.fetchone()
			
			dis142 ="SELECT cup2_0_18_15 FROM Angin1815_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis142)
			result142 = cursor.fetchone()
			
			dis143 ="SELECT arah4m_07_15 FROM Angin0715_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis143)
			result143 = cursor.fetchone()
			
			dis144 ="SELECT arah4m_07_45 FROM Angin0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis144)
			result144 = cursor.fetchone()
			
			dis145 ="SELECT arah4m_13_45 FROM Angin1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis145)
			result145 = cursor.fetchone()
			
			dis146 ="SELECT arah4m_14_15 FROM Angin1415_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis146)
			result146 = cursor.fetchone()
			
			dis147 ="SELECT arah4m_17_45 FROM Angin1745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis147)
			result147 = cursor.fetchone()
			
			dis148 ="SELECT arah4m_18_15 FROM Angin1815_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis148)
			result148 = cursor.fetchone()
			
			dis149 ="SELECT kecepatan4m_07_15 FROM Angin0715_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis149)
			result149 = cursor.fetchone()
			
			dis150 ="SELECT kecepatan4m_07_45 FROM Angin0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis150)
			result150 = cursor.fetchone()
			
			dis151 ="SELECT kecepatan4m_13_45 FROM Angin1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis151)
			result151 = cursor.fetchone()
			
			dis152 ="SELECT kecepatan4m_14_15 FROM Angin1415_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis152)
			result152 = cursor.fetchone()
			
			dis153 ="SELECT kecepatan4m_17_45 FROM Angin1745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis153)
			result153 = cursor.fetchone()
			
			dis154 ="SELECT kecepatan4m_18_15 FROM Angin1815_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis154)
			result154 = cursor.fetchone()
			
			dis155 ="SELECT arah7m_07_15 FROM Angin0715_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis155)
			result155 = cursor.fetchone()
			
			dis156 ="SELECT arah7m_07_45 FROM Angin0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis156)
			result156 = cursor.fetchone()
			
			dis157 ="SELECT arah7m_13_45 FROM Angin1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis157)
			result157 = cursor.fetchone()
			
			dis158 ="SELECT arah7m_14_15 FROM Angin1415_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis158)
			result158 = cursor.fetchone()
			
			dis159 ="SELECT arah7m_17_45 FROM Angin1745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis159)
			result159 = cursor.fetchone()
			
			dis160 ="SELECT arah7m_18_15 FROM Angin1815_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis160)
			result160 = cursor.fetchone()
			
			dis161 ="SELECT kecepatan7m_07_15 FROM Angin0715_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis161)
			result161 = cursor.fetchone()
			
			dis162 ="SELECT kecepatan7m_07_45 FROM Angin0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis162)
			result162 = cursor.fetchone()
			
			dis163 ="SELECT kecepatan7m_13_45 FROM Angin1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis163)
			result163 = cursor.fetchone()
			
			dis164 ="SELECT kecepatan7m_14_15 FROM Angin1415_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis164)
			result164 = cursor.fetchone()
			
			dis165 ="SELECT kecepatan7m_17_45 FROM Angin1745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis165)
			result165 = cursor.fetchone()
			
			dis166 ="SELECT kecepatan7m_18_15 FROM Angin1815_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis166)
			result166 = cursor.fetchone()
			
			dis167 ="SELECT arah10m_07_15 FROM Angin0715_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis167)
			result167 = cursor.fetchone()
			
			dis168 ="SELECT arah10m_07_45 FROM Angin0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis168)
			result168 = cursor.fetchone()
			
			dis169 ="SELECT arah10m_13_45 FROM Angin1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis169)
			result169 = cursor.fetchone()
			
			dis170 ="SELECT arah10m_14_15 FROM Angin1415_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis170)
			result170 = cursor.fetchone()
			
			dis171 ="SELECT arah10m_17_45 FROM Angin1745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis171)
			result171 = cursor.fetchone()
			
			dis172 ="SELECT arah10m_18_15 FROM Angin1815_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis172)
			result172 = cursor.fetchone()
			
			dis173 ="SELECT kecepatan10m_07_15 FROM Angin0715_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis173)
			result173 = cursor.fetchone()
			
			dis174 ="SELECT kecepatan10m_07_45 FROM Angin0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis174)
			result174 = cursor.fetchone()
			
			dis175 ="SELECT kecepatan10m_13_45 FROM Angin1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis175)
			result175 = cursor.fetchone()
			
			dis176 ="SELECT kecepatan10m_14_15 FROM Angin1415_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis176)
			result176 = cursor.fetchone()
			
			dis177 ="SELECT kecepatan10m_17_45 FROM Angin1745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis177)
			result177 = cursor.fetchone()
			
			dis178 ="SELECT kecepatan10m_18_15 FROM Angin1815_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis178)
			result178 = cursor.fetchone()
			
		# Suhu Tanah
		with con.cursor() as cursor:
			dis179 = "SELECT suhutanah_berumput0_0745 FROM Suhu_Tanah0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis179)
			result179 = cursor.fetchone()
			
			dis180 = "SELECT suhutanah_berumput2_0745 FROM Suhu_Tanah0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis180)
			result180 = cursor.fetchone()
			
			dis181 = "SELECT suhutanah_berumput5_0745 FROM Suhu_Tanah0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis181)
			result181 = cursor.fetchone()
			
			dis182 = "SELECT suhutanah_berumput10_0745 FROM Suhu_Tanah0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis182)
			result182 = cursor.fetchone()
			
			dis183 = "SELECT suhutanah_berumput20_0745 FROM Suhu_Tanah0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis183)
			result183 = cursor.fetchone()
			
			dis184 = "SELECT suhutanah_gundul0_0745 FROM Suhu_Tanah0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis184)
			result184 = cursor.fetchone()
			
			dis185 = "SELECT suhutanah_gundul2_0745 FROM Suhu_Tanah0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis185)
			result185 = cursor.fetchone()
			
			dis186 = "SELECT suhutanah_gundul5_0745 FROM Suhu_Tanah0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis186)
			result186 = cursor.fetchone()
			
			dis187 = "SELECT suhutanah_gundul10_0745 FROM Suhu_Tanah0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis187)
			result187 = cursor.fetchone()
			
			dis188 = "SELECT suhutanah_gundul20_0745 FROM Suhu_Tanah0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis188)
			result188 = cursor.fetchone()
			
			dis189 = "SELECT suhutanah_berumput0_1345 FROM Suhu_Tanah1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis189)
			result189 = cursor.fetchone()
			
			dis190 = "SELECT suhutanah_berumput2_1345 FROM Suhu_Tanah1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis190)
			result190 = cursor.fetchone()
			
			dis191 = "SELECT suhutanah_berumput5_1345 FROM Suhu_Tanah1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis191)
			result191 = cursor.fetchone()
			
			dis192 = "SELECT suhutanah_berumput10_1345 FROM Suhu_Tanah1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis192)
			result192 = cursor.fetchone()
			
			dis193 = "SELECT suhutanah_berumput20_1345 FROM Suhu_Tanah1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis193)
			result193 = cursor.fetchone()
			
			dis194 = "SELECT suhutanah_gundul0_1345 FROM Suhu_Tanah1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis194)
			result194 = cursor.fetchone()
			
			dis195 = "SELECT suhutanah_gundul2_1345 FROM Suhu_Tanah1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis195)
			result195 = cursor.fetchone()
			
			dis196 = "SELECT suhutanah_gundul5_1345 FROM Suhu_Tanah1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis196)
			result196 = cursor.fetchone()
			
			dis197 = "SELECT suhutanah_gundul10_1345 FROM Suhu_Tanah1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis197)
			result197 = cursor.fetchone()
			
			dis198 = "SELECT suhutanah_gundul20_1345 FROM Suhu_Tanah1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis198)
			result198 = cursor.fetchone()
			
			dis199 = "SELECT suhutanah_berumput0_1415 FROM Suhu_Tanah1415_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis199)
			result199 = cursor.fetchone()
			
			dis200 = "SELECT suhutanah_berumput2_1415 FROM Suhu_Tanah1415_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis200)
			result200 = cursor.fetchone()
			
			dis201 = "SELECT suhutanah_berumput5_1415 FROM Suhu_Tanah1415_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis201)
			result201 = cursor.fetchone()
			
			dis202 = "SELECT suhutanah_berumput10_1415 FROM Suhu_Tanah1415_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis202)
			result202 = cursor.fetchone()
			
			dis203 = "SELECT suhutanah_berumput20_1415 FROM Suhu_Tanah1415_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis203)
			result203 = cursor.fetchone()
			
			dis204 = "SELECT suhutanah_gundul0_1415 FROM Suhu_Tanah1415_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis204)
			result204 = cursor.fetchone()
			
			dis205 = "SELECT suhutanah_gundul2_1415 FROM Suhu_Tanah1415_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis205)
			result205 = cursor.fetchone()
			
			dis206 = "SELECT suhutanah_gundul5_1415 FROM Suhu_Tanah1415_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis206)
			result206 = cursor.fetchone()
			
			dis207 = "SELECT suhutanah_gundul10_1415 FROM Suhu_Tanah1415_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis207)
			result207 = cursor.fetchone()
			
			dis208 = "SELECT suhutanah_gundul20_1415 FROM Suhu_Tanah1415_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis208)
			result208 = cursor.fetchone()
			
			dis209 = "SELECT suhutanah_berumput0_1745 FROM Suhu_Tanah1745_4 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis209)
			result209 = cursor.fetchone()
			
			dis210 = "SELECT suhutanah_berumput2_1745 FROM Suhu_Tanah1745_4 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis210)
			result210 = cursor.fetchone()
			
			dis211 = "SELECT suhutanah_berumput5_1745 FROM Suhu_Tanah1745_4 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis211)
			result211 = cursor.fetchone()
			
			dis212 = "SELECT suhutanah_berumput10_1745 FROM Suhu_Tanah1745_4 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get() 
			cursor.execute(dis212)
			result212 = cursor.fetchone()
			
			dis213 = "SELECT suhutanah_berumput20_1745 FROM Suhu_Tanah1745_4 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis213)
			result213 = cursor.fetchone()
			
			dis214 = "SELECT suhutanah_berumput50_1745 FROM Suhu_Tanah1745_4 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis214)
			result214 = cursor.fetchone()
			
			dis215 = "SELECT suhutanah_berumput100_1745 FROM Suhu_Tanah1745_4 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis215)
			result215 = cursor.fetchone()
			
			dis216 = "SELECT suhutanah_gundul0_1745 FROM Suhu_Tanah1745_4 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis216)
			result216 = cursor.fetchone()
			
			dis217 = "SELECT suhutanah_gundul2_1745 FROM Suhu_Tanah1745_4 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis217)
			result217 = cursor.fetchone()
			
			dis218 = "SELECT suhutanah_gundul5_1745 FROM Suhu_Tanah1745_4 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis218)
			result218 = cursor.fetchone()
			
			dis219 = "SELECT suhutanah_gundul10_1745 FROM Suhu_Tanah1745_4 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis219)
			result219 = cursor.fetchone()
			
			dis220 = "SELECT suhutanah_gundul20_1745 FROM Suhu_Tanah1745_4 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis220)
			result220 = cursor.fetchone()
			
			dis221 = "SELECT suhutanah_gundul50_1745 FROM Suhu_Tanah1745_4 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis221)
			result221 = cursor.fetchone()
			
			dis222 = "SELECT suhutanah_gundul100_1745 FROM Suhu_Tanah1745_4 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis222)
			result222 = cursor.fetchone()

		# Lysimeter
		with con.cursor() as cursor:
			dis223 = "SELECT tanahgundul_siram FROM Lysimeter_11 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis223)
			result223 = cursor.fetchone()
			
			dis224 = "SELECT tanahgundul_keluar FROM Lysimeter_11 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis224)
			result224 = cursor.fetchone()
			
			dis225 = "SELECT tanahtanamankomoditi_siram FROM Lysimeter_11 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis225)
			result225 = cursor.fetchone()
			
			dis226 = "SELECT tanahtanamankomoditi_keluar FROM Lysimeter_11 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis226)
			result226 = cursor.fetchone()
			
			dis227 = "SELECT tanahberumput_siram FROM Lysimeter_11 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis227)
			result227 = cursor.fetchone()
			
			dis228 = "SELECT tanahberumput_keluar FROM Lysimeter_11 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis228)
			result228 = cursor.fetchone()
			
			dis229 = "SELECT lain2_curahhujanperjam17_15 FROM Lysimeter_11 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis229)
			result229 = cursor.fetchone()
			
			dis230 = "SELECT lain2_namatanamankomoditi FROM Lysimeter_11 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis230)
			result230 = cursor.fetchone()
			
			dis231 = "SELECT lain2_keteranganfase_atas FROM Lysimeter_11 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis231)
			result231 = cursor.fetchone()
			
			dis295 = "SELECT lain2_keteranganfase_bawah FROM Lysimeter_11 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis295)
			result295 = cursor.fetchone()
			
			dis296 = "SELECT lain2_keteranganfase_hasil FROM Lysimeter_11 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis296)
			result296 = cursor.fetchone()
			
			dis297 = "SELECT lain2_display FROM Lysimeter_11 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis297)
			result297 = cursor.fetchone()
			
		# Psychrometer Assmann
		with con.cursor() as cursor:
			dis232 = "SELECT passmannBK5_0745 FROM Psychrometer_Assmann0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis232)
			result232 = cursor.fetchone()
			
			dis233 = "SELECT passmannBK10_0745 FROM Psychrometer_Assmann0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis233)
			result233 = cursor.fetchone()
			
			dis234 = "SELECT passmannBK20_0745 FROM Psychrometer_Assmann0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis234)
			result234 = cursor.fetchone()
			
			dis235 = "SELECT passmannBK50_0745 FROM Psychrometer_Assmann0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis235)
			result235 = cursor.fetchone()
			
			dis236 = "SELECT passmannBK100_0745 FROM Psychrometer_Assmann0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis236)
			result236 = cursor.fetchone()
			
			dis237 = "SELECT passmannBK150_0745 FROM Psychrometer_Assmann0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get() 
			cursor.execute(dis237)
			result237 = cursor.fetchone()
			
			dis238 = "SELECT passmannBK200_0745 FROM Psychrometer_Assmann0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis238)
			result238 = cursor.fetchone()
			
			dis239 = "SELECT passmannBB5_0745 FROM Psychrometer_Assmann0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis239)
			result239 = cursor.fetchone()
			
			dis240 = "SELECT passmannBB10_0745 FROM Psychrometer_Assmann0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis240)
			result240 = cursor.fetchone()
			
			dis241 = "SELECT passmannBB20_0745 FROM Psychrometer_Assmann0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis241)
			result241 = cursor.fetchone()
			
			dis242 = "SELECT passmannBB50_0745 FROM Psychrometer_Assmann0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis242)
			result242 = cursor.fetchone()
			
			dis243 = "SELECT passmannBB100_0745 FROM Psychrometer_Assmann0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis243)
			result243 = cursor.fetchone()
			
			dis244 = "SELECT passmannBB150_0745 FROM Psychrometer_Assmann0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis244)
			result244 = cursor.fetchone()
			
			dis245 = "SELECT passmannBB200_0745 FROM Psychrometer_Assmann0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis245)
			result245 = cursor.fetchone()
			
			dis246 = "SELECT passmannRH5_0745 FROM Psychrometer_Assmann0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis246)
			result246 = cursor.fetchone()
			
			dis247 = "SELECT passmannRH10_0745 FROM Psychrometer_Assmann0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis247)
			result247 = cursor.fetchone()
			
			dis248 = "SELECT passmannRH20_0745 FROM Psychrometer_Assmann0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis248)
			result248 = cursor.fetchone()
			
			dis249 = "SELECT passmannRH50_0745 FROM Psychrometer_Assmann0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis249)
			result249 = cursor.fetchone()
			
			dis250 = "SELECT passmannRH100_0745 FROM Psychrometer_Assmann0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis250)
			result250 = cursor.fetchone()
			
			dis251 = "SELECT passmannRH150_0745 FROM Psychrometer_Assmann0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis251)
			result251 = cursor.fetchone()
			
			dis252 = "SELECT passmannRH200_0745 FROM Psychrometer_Assmann0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis252)
			result252 = cursor.fetchone()
			
			dis253 = "SELECT passmannBK5_1345 FROM Psychrometer_Assmann1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis253)
			result253 = cursor.fetchone()
			
			dis254 = "SELECT passmannBK10_1345 FROM Psychrometer_Assmann1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis254)
			result254 = cursor.fetchone()
			
			dis255 = "SELECT passmannBK20_1345 FROM Psychrometer_Assmann1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis255)
			result255 = cursor.fetchone()
			
			dis256 = "SELECT passmannBK50_1345 FROM Psychrometer_Assmann1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis256)
			result256 = cursor.fetchone()
			
			dis257 = "SELECT passmannBK100_1345 FROM Psychrometer_Assmann1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis257)
			result257 = cursor.fetchone()
			
			dis258 = "SELECT passmannBK150_1345 FROM Psychrometer_Assmann1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis258)
			result258 = cursor.fetchone()
			
			dis259 = "SELECT passmannBK200_1345 FROM Psychrometer_Assmann1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis259)
			result259 = cursor.fetchone()
			
			dis260 = "SELECT passmannBB5_1345 FROM Psychrometer_Assmann1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis260)
			result260 = cursor.fetchone()
			
			dis261 = "SELECT passmannBB10_1345 FROM Psychrometer_Assmann1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis261)
			result261 = cursor.fetchone()
			
			dis262 = "SELECT passmannBB20_1345 FROM Psychrometer_Assmann1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis262)
			result262 = cursor.fetchone()
			
			dis263 = "SELECT passmannBB50_1345 FROM Psychrometer_Assmann1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis263)
			result263 = cursor.fetchone()
			
			dis264 = "SELECT passmannBB100_1345 FROM Psychrometer_Assmann1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis264)
			result264 = cursor.fetchone()
			
			dis265 = "SELECT passmannBB150_1345 FROM Psychrometer_Assmann1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis265)
			result265 = cursor.fetchone()
			
			dis266 = "SELECT passmannBB200_1345 FROM Psychrometer_Assmann1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis266)
			result266 = cursor.fetchone()
			
			dis267 = "SELECT passmannRH5_1345 FROM Psychrometer_Assmann1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis267)
			result267 = cursor.fetchone()
			
			dis268 = "SELECT passmannRH10_1345 FROM Psychrometer_Assmann1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis268)
			result268 = cursor.fetchone()
			
			dis269 = "SELECT passmannRH20_1345 FROM Psychrometer_Assmann1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis269)
			result269 = cursor.fetchone()
			
			dis270 = "SELECT passmannRH50_1345 FROM Psychrometer_Assmann1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis270)
			result270 = cursor.fetchone()
			
			dis271 = "SELECT passmannRH100_1345 FROM Psychrometer_Assmann1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis271)
			result271 = cursor.fetchone()
			
			dis272 = "SELECT passmannRH150_1345 FROM Psychrometer_Assmann1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis272)
			result272 = cursor.fetchone()
			
			dis273 = "SELECT passmannRH200_1345 FROM Psychrometer_Assmann1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis273)
			result273 = cursor.fetchone()
			
			dis274 = "SELECT passmannBK5_1745 FROM Psychrometer_Assmann1745_2 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis274)
			result274 = cursor.fetchone()
			
			dis275 = "SELECT passmannBK10_1745 FROM Psychrometer_Assmann1745_2 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis275)
			result275 = cursor.fetchone()
			
			dis276 = "SELECT passmannBK20_1745 FROM Psychrometer_Assmann1745_2 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis276)
			result276 = cursor.fetchone()
			
			dis277 = "SELECT passmannBK50_1745 FROM Psychrometer_Assmann1745_2 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis277)
			result277 = cursor.fetchone()
			
			dis278 = "SELECT passmannBK100_1745 FROM Psychrometer_Assmann1745_2 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis278)
			result278 = cursor.fetchone()
			
			dis279 = "SELECT passmannBK150_1745 FROM Psychrometer_Assmann1745_2 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis279)
			result279 = cursor.fetchone()
			
			dis280 = "SELECT passmannBK200_1745 FROM Psychrometer_Assmann1745_2 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis280)
			result280 = cursor.fetchone()
			
			dis281 = "SELECT passmannBB5_1745 FROM Psychrometer_Assmann1745_2 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis281)
			result281 = cursor.fetchone()
			
			dis282 = "SELECT passmannBB10_1745 FROM Psychrometer_Assmann1745_2 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis282)
			result282 = cursor.fetchone()
			
			dis283 = "SELECT passmannBB20_1745 FROM Psychrometer_Assmann1745_2 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis283)
			result283 = cursor.fetchone()
			
			dis284 = "SELECT passmannBB50_1745 FROM Psychrometer_Assmann1745_2 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis284)
			result284 = cursor.fetchone()
			
			dis285 = "SELECT passmannBB100_1745 FROM Psychrometer_Assmann1745_2 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis285)
			result285 = cursor.fetchone()
			
			dis286 = "SELECT passmannBB150_1745 FROM Psychrometer_Assmann1745_2 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis286)
			result286 = cursor.fetchone()
			
			dis287 = "SELECT passmannBB200_1745 FROM Psychrometer_Assmann1745_2 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis287)
			result287 = cursor.fetchone()
			
			dis288 = "SELECT passmannRH5_1745 FROM Psychrometer_Assmann1745_2 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis288)
			result288 = cursor.fetchone()
			
			dis289 = "SELECT passmannRH10_1745 FROM Psychrometer_Assmann1745_2 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis289)
			result289 = cursor.fetchone()
			
			dis290 = "SELECT passmannRH20_1745 FROM Psychrometer_Assmann1745_2 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis290)
			result290 = cursor.fetchone()
			
			dis291 = "SELECT passmannRH50_1745 FROM Psychrometer_Assmann1745_2 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis291)
			result291 = cursor.fetchone()
			
			dis292 = "SELECT passmannRH100_1745 FROM Psychrometer_Assmann1745_2 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis292)
			result292 = cursor.fetchone()
			
			dis293 = "SELECT passmannRH150_1745 FROM Psychrometer_Assmann1745_2 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis293)
			result293 = cursor.fetchone()
			
			dis294 = "SELECT passmannRH200_1745 FROM Psychrometer_Assmann1745_2 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis294)
			result294 = cursor.fetchone()
			
		#PMG on Duty
		with con.cursor() as cursor:
			dis298 = "SELECT hari FROM PMGonDuty_Catatan_4 WHERE Waktu = '%s' " % input_tahun_bulan_tanggal.get()
			cursor.execute(dis298)
			result298 = cursor.fetchone()
			
			dis299 = "SELECT tanggal FROM PMGonDuty_Catatan_4 WHERE Waktu = '%s' " % input_tahun_bulan_tanggal.get()
			cursor.execute(dis299)
			result299 = cursor.fetchone()
			
			dis300 = "SELECT pmg_pagi FROM PMGonDuty_Catatan_4 WHERE Waktu = '%s' " % input_tahun_bulan_tanggal.get()
			cursor.execute(dis300)
			result300 = cursor.fetchone()
			
			dis301 = "SELECT pmg_siang FROM PMGonDuty_Catatan_4 WHERE Waktu = '%s' " % input_tahun_bulan_tanggal.get()
			cursor.execute(dis301)
			result301 = cursor.fetchone()
			
		#KOLOM1 ANGIN
		#KOLOM2 ANGIN CUP COUNTER 0.5m
		Label(win, text=result131, bg="white", font="callibri 7").place(x=115, y=97)
		Label(win, text=result132, bg="white", font="callibri 7").place(x=115, y=116)
		Label(win, text=result133, bg="white", font="callibri 7").place(x=115, y=135)
		Label(win, text=result134, bg="white", font="callibri 7").place(x=115, y=154)
		Label(win, text=result135, bg="white", font="callibri 7").place(x=115, y=173)
		Label(win, text=result136, bg="white", font="callibri 7").place(x=115, y=192)
		
		#KOLOM3 ANGIN CUP COUNTER 2m
		Label(win, text=result137, bg="white", font="callibri 7").place(x=222, y=97)
		Label(win, text=result138, bg="white", font="callibri 7").place(x=222, y=116)
		Label(win, text=result139, bg="white", font="callibri 7").place(x=222, y=135)
		Label(win, text=result140, bg="white", font="callibri 7").place(x=222, y=154)
		Label(win, text=result141, bg="white", font="callibri 7").place(x=222, y=173)
		Label(win, text=result142, bg="white", font="callibri 7").place(x=222, y=192)

		#KOLOM4 ANGIN 4m
		#kolom4 angin 4m arah
		Label(win, text=result143, bg="white", font="callibri 7").place(x=320, y=97)
		Label(win, text=result144, bg="white", font="callibri 7").place(x=320, y=116)
		Label(win, text=result145, bg="white", font="callibri 7").place(x=320, y=135)
		Label(win, text=result146, bg="white", font="callibri 7").place(x=320, y=154)
		Label(win, text=result147, bg="white", font="callibri 7").place(x=320, y=173)
		Label(win, text=result148, bg="white", font="callibri 7").place(x=320, y=192)
		#kolom4 angin 4m kecepatan
		Label(win, text=result149, bg="white", font="callibri 7").place(x=400, y=97)
		Label(win, text=result150, bg="white", font="callibri 7").place(x=400, y=116)
		Label(win, text=result151, bg="white", font="callibri 7").place(x=400, y=135)
		Label(win, text=result152, bg="white", font="callibri 7").place(x=400, y=154)
		Label(win, text=result153, bg="white", font="callibri 7").place(x=400, y=173)
		Label(win, text=result154, bg="white", font="callibri 7").place(x=400, y=192)

		#KOLOM5 ANGIN 7m
		#kolom5 angin 7m arah 
		Label(win, text=result155, bg="white", font="callibri 7").place(x=497, y=97)
		Label(win, text=result156, bg="white", font="callibri 7").place(x=497, y=116)
		Label(win, text=result157, bg="white", font="callibri 7").place(x=497, y=135)
		Label(win, text=result158, bg="white", font="callibri 7").place(x=497, y=154)
		Label(win, text=result159, bg="white", font="callibri 7").place(x=497, y=173)
		Label(win, text=result160, bg="white", font="callibri 7").place(x=497, y=192)
		#kolom5 angin 7m kecepatan
		Label(win, text=result161, bg="white", font="callibri 7").place(x=577, y=97)
		Label(win, text=result162, bg="white", font="callibri 7").place(x=577, y=116)
		Label(win, text=result163, bg="white", font="callibri 7").place(x=577, y=135)
		Label(win, text=result164, bg="white", font="callibri 7").place(x=577, y=154)
		Label(win, text=result165, bg="white", font="callibri 7").place(x=577, y=173)
		Label(win, text=result166, bg="white", font="callibri 7").place(x=577, y=192)

		#KOLOM6 ANGIN 10m
		#kolom6 angin 10m arah
		Label(win, text=result167, bg="white", font="callibri 7").place(x=674, y=97)
		Label(win, text=result168, bg="white", font="callibri 7").place(x=674, y=116)
		Label(win, text=result169, bg="white", font="callibri 7").place(x=674, y=135)
		Label(win, text=result170, bg="white", font="callibri 7").place(x=674, y=154)
		Label(win, text=result171, bg="white", font="callibri 7").place(x=674, y=173)
		Label(win, text=result172, bg="white", font="callibri 7").place(x=674, y=192)
		#kolom6 angin 10m kecepatan
		Label(win, text=result173, bg="white", font="callibri 7").place(x=754, y=97)
		Label(win, text=result174, bg="white", font="callibri 7").place(x=754, y=116)
		Label(win, text=result175, bg="white", font="callibri 7").place(x=754, y=135)
		Label(win, text=result176, bg="white", font="callibri 7").place(x=754, y=154)
		Label(win, text=result177, bg="white", font="callibri 7").place(x=754, y=173)
		Label(win, text=result178, bg="white", font="callibri 7").place(x=754, y=192)
		"""--------------------------------------------- AKHIR TABEL KEDUA BELAS - ANGIN --------------------------------"""
		
		"""--------------------------------------------- TABEL KETIGA BELAS - SUHU TANAH --------------------------------"""
		#kolom1 suhu tanah
		#kolom2 suhu tanah
		#kolom2 berumput
		Label(win, text=result179, bg="white", font="callibri 7").place(x=105, y=286)
		Label(win, text=result180, bg="white", font="callibri 7").place(x=105, y=305)
		Label(win, text=result181, bg="white", font="callibri 7").place(x=105, y=324)
		Label(win, text=result182, bg="white", font="callibri 7").place(x=105, y=343)
		Label(win, text=result183, bg="white", font="callibri 7").place(x=105, y=362)
		#kolom2 gundul
		Label(win, text=result184, bg="white", font="callibri 7").place(x=178, y=286)
		Label(win, text=result185, bg="white", font="callibri 7").place(x=178, y=305)
		Label(win, text=result186, bg="white", font="callibri 7").place(x=178, y=324)
		Label(win, text=result187, bg="white", font="callibri 7").place(x=178, y=343)
		Label(win, text=result188, bg="white", font="callibri 7").place(x=178, y=362)

		#kolom3 suhu tanah
		#kolom3 berumput
		Label(win, text=result189, bg="white", font="callibri 7").place(x=249, y=286)
		Label(win, text=result190, bg="white", font="callibri 7").place(x=249, y=305)
		Label(win, text=result191, bg="white", font="callibri 7").place(x=249, y=324)
		Label(win, text=result192, bg="white", font="callibri 7").place(x=249, y=343)
		Label(win, text=result193, bg="white", font="callibri 7").place(x=249, y=362)
		#kolom3 gundul
		Label(win, text=result194, bg="white", font="callibri 7").place(x=315, y=286)
		Label(win, text=result195, bg="white", font="callibri 7").place(x=315, y=305)
		Label(win, text=result196, bg="white", font="callibri 7").place(x=315, y=324)
		Label(win, text=result197, bg="white", font="callibri 7").place(x=315, y=343)
		Label(win, text=result198, bg="white", font="callibri 7").place(x=315, y=362)

		#kolom4 suhu tanah
		#kolom4 berumput
		Label(win, text=result199, bg="white", font="callibri 7").place(x=385, y=286)
		Label(win, text=result200, bg="white", font="callibri 7").place(x=385, y=305)
		Label(win, text=result201, bg="white", font="callibri 7").place(x=385, y=324)
		Label(win, text=result202, bg="white", font="callibri 7").place(x=385, y=343)
		Label(win, text=result203, bg="white", font="callibri 7").place(x=385, y=362)
		#kolom4 gundul
		Label(win, text=result204, bg="white", font="callibri 7").place(x=455, y=286)
		Label(win, text=result205, bg="white", font="callibri 7").place(x=455, y=305)
		Label(win, text=result206, bg="white", font="callibri 7").place(x=455, y=324)
		Label(win, text=result207, bg="white", font="callibri 7").place(x=455, y=343)
		Label(win, text=result208, bg="white", font="callibri 7").place(x=455, y=362)

		#kolom5
		#kolom5 berumput
		Label(win, text=result209, bg="white", font="callibri 7").place(x=512, y=286)
		Label(win, text=result210, bg="white", font="callibri 7").place(x=512, y=305)
		Label(win, text=result211, bg="white", font="callibri 7").place(x=512, y=324)
		Label(win, text=result212, bg="white", font="callibri 7").place(x=512, y=343)
		Label(win, text=result213, bg="white", font="callibri 7").place(x=512, y=362)
		Label(win, text=result214, bg="white", font="callibri 7").place(x=512, y=381)
		Label(win, text=result215, bg="white", font="callibri 7").place(x=512, y=400)
		#kolom5 gundul
		Label(win, text=result216, bg="white", font="callibri 7").place(x=551, y=286)
		Label(win, text=result217, bg="white", font="callibri 7").place(x=551, y=305)
		Label(win, text=result218, bg="white", font="callibri 7").place(x=551, y=324)
		Label(win, text=result219, bg="white", font="callibri 7").place(x=551, y=343)
		Label(win, text=result220, bg="white", font="callibri 7").place(x=551, y=362)
		Label(win, text=result221, bg="white", font="callibri 7").place(x=551, y=381)
		Label(win, text=result222, bg="white", font="callibri 7").place(x=551, y=400)
		"""------------------------------------------ AKHIR TABEL KETIGA BELAS - SUHU TANAH -----------------------------"""
		
		"""--------------------------------------------- TABEL KEEMPAT BELAS - LYSIMETER --------------------------------"""
		#KOLOM1 LYSIMETER TANAH GUNDUL
		Label(win, text=result223, bg="lightgray", font="callibri 7").place(x=622, y=286) #siram
		Label(win, text=result224, bg="lightgray", font="callibri 7").place(x=657, y=286) #keluar

		#KOLOM2 LYSIMETER TANAMAN KOMODITI
		Label(win, text=result225, bg="lightgray", font="callibri 7").place(x=693, y=286) #siram
		Label(win, text=result226, bg="lightgray", font="callibri 7").place(x=728, y=286) #keluar

		#KOLOM3 LYSIMETER TANAH BERUMPUT
		Label(win, text=result227, bg="white", font="callibri 7").place(x=764, y=286) #siram
		Label(win, text=result228, bg="white", font="callibri 7").place(x=799, y=286) #keluar

		#BARIS LYSIMETER BAWAH1: Jumlah Curah Hujan per Jam 17.15
		Label(win, text=result229, bg="white", font="callibri 7").place(x=773, y=305)

		#BARIS LYSIMETER BAWAH2
		#Nama Tanaman Komoditi
		Label(win, text=result230, bg="white", font="callibri 7").place(x=731, y=325)
		#Keterangan Fase
		Label(win, text=result231, bg="white", font="callibri 7").place(x=731, y=345) #atas
		Label(win, text=result295, bg="white", font="callibri 7").place(x=731, y=362) #bawah
		Label(win, text=result296, bg="white", font="callibri 7").place(x=750, y=384) #hasil pengurangan

		#BARIS LYSIMETER BAWAH3 :Digital - dilaporan yang baru, pengisiannya cuma ada satu aja
		Label(win, text=result297, bg="white", font="callibri 7").place(x=685, y=389)
		"""------------------------------------------ AKHIR TABEL KEEMPAT BELAS - LYSIMETER -----------------------------"""

		"""---------------------------------------- TABEL KELIMA BELAS - PSYCHROMETER ASSMANN ---------------------------"""
		#KOLOM1 PSYCHRO ASSMANN
		#KOLOM2 PSYCHRO ASSMANN
		#kolom2 psychro assmann BK
		Label(win, text=result232, bg="white", font="callibri 7").place(x=87, y=495) #5 cm
		Label(win, text=result233, bg="white", font="callibri 7").place(x=87, y=514) #10 cm
		Label(win, text=result234, bg="white", font="callibri 7").place(x=87, y=533) #20 cm
		Label(win, text=result235, bg="white", font="callibri 7").place(x=87, y=552) #50 cm
		Label(win, text=result236, bg="white", font="callibri 7").place(x=87, y=571) #100 cm
		Label(win, text=result237, bg="white", font="callibri 7").place(x=87, y=590) #150 cm
		Label(win, text=result238, bg="white", font="callibri 7").place(x=87, y=609) #200 cm
		#kolom2 psychro assmann BB
		Label(win, text=result239, bg="white", font="callibri 7").place(x=122, y=495)
		Label(win, text=result240, bg="white", font="callibri 7").place(x=122, y=514)
		Label(win, text=result241, bg="white", font="callibri 7").place(x=122, y=533)
		Label(win, text=result242, bg="white", font="callibri 7").place(x=122, y=552)
		Label(win, text=result243, bg="white", font="callibri 7").place(x=122, y=571)
		Label(win, text=result244, bg="white", font="callibri 7").place(x=122, y=590)
		Label(win, text=result245, bg="white", font="callibri 7").place(x=122, y=609)
		#kolom2 psychro assmann RH
		Label(win, text=result246, bg="white", font="callibri 7").place(x=179, y=495)
		Label(win, text=result247, bg="white", font="callibri 7").place(x=179, y=514)
		Label(win, text=result248, bg="white", font="callibri 7").place(x=179, y=533)
		Label(win, text=result249, bg="white", font="callibri 7").place(x=179, y=552)
		Label(win, text=result250, bg="white", font="callibri 7").place(x=179, y=571)
		Label(win, text=result251, bg="white", font="callibri 7").place(x=179, y=590)
		Label(win, text=result252, bg="white", font="callibri 7").place(x=179, y=609)

		#KOLOM3 PSYCHRO ASSMANN
		#kolom3 psychro assmann BK
		Label(win, text=result253, bg="white", font="callibri 7").place(x=228, y=495)
		Label(win, text=result254, bg="white", font="callibri 7").place(x=228, y=514)
		Label(win, text=result255, bg="white", font="callibri 7").place(x=228, y=533)
		Label(win, text=result256, bg="white", font="callibri 7").place(x=228, y=552)
		Label(win, text=result257, bg="white", font="callibri 7").place(x=228, y=571)
		Label(win, text=result258, bg="white", font="callibri 7").place(x=228, y=590)
		Label(win, text=result259, bg="white", font="callibri 7").place(x=228, y=609)
		#kolom3 psychro assmann BB
		Label(win, text=result260, bg="white", font="callibri 7").place(x=263, y=495)
		Label(win, text=result261, bg="white", font="callibri 7").place(x=263, y=514)
		Label(win, text=result262, bg="white", font="callibri 7").place(x=263, y=533)
		Label(win, text=result263, bg="white", font="callibri 7").place(x=263, y=552)
		Label(win, text=result264, bg="white", font="callibri 7").place(x=263, y=571)
		Label(win, text=result265, bg="white", font="callibri 7").place(x=263, y=590)
		Label(win, text=result266, bg="white", font="callibri 7").place(x=263, y=609)
		#kolom3 psychro assmann RH
		Label(win, text=result267, bg="white", font="callibri 7").place(x=340, y=495)
		Label(win, text=result268, bg="white", font="callibri 7").place(x=340, y=514)
		Label(win, text=result269, bg="white", font="callibri 7").place(x=340, y=533)
		Label(win, text=result270, bg="white", font="callibri 7").place(x=340, y=552)
		Label(win, text=result271, bg="white", font="callibri 7").place(x=340, y=571)
		Label(win, text=result272, bg="white", font="callibri 7").place(x=340, y=590)
		Label(win, text=result273, bg="white", font="callibri 7").place(x=340, y=609)

		#KOLOM4 PSYCHRO ASSMANN
		#kolom4 psychro assmann BK
		Label(win, text=result274, bg="white", font="callibri 7").place(x=409, y=495)
		Label(win, text=result275, bg="white", font="callibri 7").place(x=409, y=514)
		Label(win, text=result276, bg="white", font="callibri 7").place(x=409, y=533)
		Label(win, text=result277, bg="white", font="callibri 7").place(x=409, y=552)
		Label(win, text=result278, bg="white", font="callibri 7").place(x=409, y=571)
		Label(win, text=result279, bg="white", font="callibri 7").place(x=409, y=590)
		Label(win, text=result280, bg="white", font="callibri 7").place(x=409, y=609)
		#kolom4 psychro assmann BB
		Label(win, text=result281, bg="white", font="callibri 7").place(x=444, y=495)
		Label(win, text=result282, bg="white", font="callibri 7").place(x=444, y=514)
		Label(win, text=result283, bg="white", font="callibri 7").place(x=444, y=533)
		Label(win, text=result284, bg="white", font="callibri 7").place(x=444, y=552)
		Label(win, text=result285, bg="white", font="callibri 7").place(x=444, y=571)
		Label(win, text=result286, bg="white", font="callibri 7").place(x=444, y=590)
		Label(win, text=result287, bg="white", font="callibri 7").place(x=444, y=609)

		#kolom4 psychro assmann RH
		Label(win, text=result288, bg="white", font="callibri 7").place(x=521, y=495)
		Label(win, text=result289, bg="white", font="callibri 7").place(x=521, y=514)
		Label(win, text=result290, bg="white", font="callibri 7").place(x=521, y=533)
		Label(win, text=result291, bg="white", font="callibri 7").place(x=521, y=552)
		Label(win, text=result292, bg="white", font="callibri 7").place(x=521, y=571)
		Label(win, text=result293, bg="white", font="callibri 7").place(x=521, y=590)
		Label(win, text=result294, bg="white", font="callibri 7").place(x=521, y=609)
		"""------------------------------------- AKHIR TABEL KELIMA BELAS - PSYCHROMETER ASSMANN ------------------------"""

		"""---------------------------------------------- TABEL KEENAM BELAS - PMG ON DUTY ------------------------------"""
		#baris1 pmg on duty
		Label(win, text=result298, bg="white", font="callibri 7").place(x=640, y=439) #hari
		Label(win, text=result299, bg="white", font="callibri 7").place(x=760, y=439) #tanggal
		#baris2 pmg on duty
		#baris3 pmg on duty
		#baris4 pmg on duty
		Label(win, text=result300, bg="white", font="callibri 7 bold").place(x=700, y=515) #nama pmg pagi
		#baris5 pmg on duty
		Label(win, text=result301, bg="white", font="callibri 7 bold").place(x=700, y=577) #nama pmg siang
		"""------------------------------------------- AKHIR TABEL KEENAM BELAS - PMG ON DUTY ---------------------------"""
	"""################################################ AKHIR HALAMAN KEDUA ###########################################"""
	"""################################################ EXPORT FILE INTO PDF ##########################################"""
	def export_file():
		from reportlab.pdfgen import canvas
		from reportlab.lib.pagesizes import A4, landscape
		from reportlab.lib.units import mm, inch, cm
		from reportlab.lib import colors
		from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
		import string

		from reportlab.pdfbase import pdfmetrics
		from reportlab.pdfbase.ttfonts import TTFont

		pdfmetrics.registerFont(TTFont('Calibri', 'Calibri.ttf'))

		InputTahunBulanTanggal = input_tahun_bulan_tanggal.get()
		
		alpa = InputTahunBulanTanggal
		beta = alpa + ".pdf"

		doc = SimpleDocTemplate(beta, pagesize=(landscape(A4)), topMargin=1.1*cm, bottomMargin=0.5*cm, rightMargin=0.5*cm, leftMargin=2.5*cm)
		width, height = A4
		#container for the 'Flowable' objects
		elements = []
		
		"""================================================ MYSQL START HERE ====================================================="""
		#Psychrometer Sangkar Meteorologi
		con = pymysql.connect("localhost", "root", "12345", "Buku_Klimatologi_BMKG")
		with con.cursor() as cursor:
			dis1 = "SELECT psmeteoTbk1_2_0715 FROM Psychrometer_Sangkar_Meteo0715_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis1)
			result1 = cursor.fetchone()
			
			for r in result1:
				row1 = r
		
			dis2 = "SELECT psmeteoTbb1_2_0715 FROM Psychrometer_Sangkar_Meteo0715_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis2)
			result2 = cursor.fetchone()
			
			for r in result2:
				row2 = r
			
			dis3 = "SELECT psmeteoRH1_2_0715 FROM Psychrometer_Sangkar_Meteo0715_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis3)
			result3 = cursor.fetchone()
			
			for r in result3:
				row3 = r

			dis4 = "SELECT psmeteoTbk4_0715 FROM Psychrometer_Sangkar_Meteo0715_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis4)
			result4 = cursor.fetchone()
			
			for r in result4:
				row4 = r
			
			dis5 = "SELECT psmeteoTbb4_0715 FROM Psychrometer_Sangkar_Meteo0715_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis5)
			result5 = cursor.fetchone()
			
			for r in result5:
				row5 = r
			
			dis6 = "SELECT psmeteoRH4_0715 FROM Psychrometer_Sangkar_Meteo0715_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis6)
			result6 = cursor.fetchone()
			
			for r in result6:
				row6 = r
			
			dis7 = "SELECT psmeteoTbk7_0715 FROM Psychrometer_Sangkar_Meteo0715_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis7)
			result7 = cursor.fetchone()
			
			for r in result7:
				row7 = r
			
			dis8 = "SELECT psmeteoTbb7_0715 FROM Psychrometer_Sangkar_Meteo0715_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis8)
			result8 = cursor.fetchone()
			
			for r in result8:
				row8 = r
			
			dis9 = "SELECT psmeteoRH7_0715 FROM Psychrometer_Sangkar_Meteo0715_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis9)
			result9 = cursor.fetchone()
			
			for r in result9:
				row9 = r
			
			dis10 = "SELECT psmeteoTbk10_0715 FROM Psychrometer_Sangkar_Meteo0715_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis10)
			result10 = cursor.fetchone()
			
			for r in result10:
				row10 = r
			
			dis11 = "SELECT psmeteoTbb10_0715 FROM Psychrometer_Sangkar_Meteo0715_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis11)
			result11 = cursor.fetchone()
			
			for r in result11:
				row11 = r
			
			dis12 = "SELECT psmeteoRH1_2_0715 FROM Psychrometer_Sangkar_Meteo0715_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis12)
			result12 = cursor.fetchone()
			
			for r in result12:
				row12 = r
			
			dis13 = "SELECT psmeteoTbk1_2_0745 FROM Psychrometer_Sangkar_Meteo0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis13)
			result13 = cursor.fetchone()
			
			for r in result13:
				row13 = r
			
			dis14 = "SELECT psmeteoTbb1_2_0745 FROM Psychrometer_Sangkar_Meteo0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis14)
			result14 = cursor.fetchone()
			
			for r in result14:
				row14 = r
			
			dis15 = "SELECT psmeteoRH1_2_0745 FROM Psychrometer_Sangkar_Meteo0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis15)
			result15 = cursor.fetchone()
			
			for r in result15:
				row15 = r
			
			dis16 = "SELECT psmeteoTbk4_0745 FROM Psychrometer_Sangkar_Meteo0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis16)
			result16 = cursor.fetchone()
			
			for r in result16:
				row16 = r
			
			dis17 = "SELECT psmeteoTbb4_0745 FROM Psychrometer_Sangkar_Meteo0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis17)
			result17 = cursor.fetchone()
			
			for r in result17:
				row17 = r
			
			dis18 = "SELECT psmeteoRH4_0745 FROM Psychrometer_Sangkar_Meteo0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis18)
			result18 = cursor.fetchone()
			
			for r in result18:
				row18 = r
			
			dis19 = "SELECT psmeteoTbk7_0745 FROM Psychrometer_Sangkar_Meteo0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis19)
			result19 = cursor.fetchone()
			
			for r in result19:
				row19 = r
			
			dis20 = "SELECT psmeteoTbb7_0745 FROM Psychrometer_Sangkar_Meteo0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis20)
			result20 = cursor.fetchone()
			
			for r in result20:
				row20 = r
			
			dis21 = "SELECT psmeteoRH7_0745 FROM Psychrometer_Sangkar_Meteo0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis21)
			result21 = cursor.fetchone()
			
			for r in result21:
				row21 = r
			
			dis22 = "SELECT psmeteoTbk10_0745 FROM Psychrometer_Sangkar_Meteo0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis22)
			result22 = cursor.fetchone()
			
			for r in result22:
				row22 = r
			
			dis23 = "SELECT psmeteoTbb10_0745 FROM Psychrometer_Sangkar_Meteo0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis23)
			result23 = cursor.fetchone()
			
			for r in result23:
				row23 = r
			
			dis24 = "SELECT psmeteoRH10_0745 FROM Psychrometer_Sangkar_Meteo0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis24)
			result24 = cursor.fetchone()
			
			for r in result24:
				row24 = r
			
			dis25 = "SELECT psmeteoTbk1_2_1315 FROM Psychrometer_Sangkar_Meteo1315_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis25)
			result25 = cursor.fetchone()
			
			for r in result25:
				row25 = r
			
			dis26 = "SELECT psmeteoTbb1_2_1315 FROM Psychrometer_Sangkar_Meteo1315_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis26)
			result26 = cursor.fetchone()
			
			for r in result26:
				row26 = r
			
			dis27 = "SELECT psmeteoRH1_2_1315 FROM Psychrometer_Sangkar_Meteo1315_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis27)
			result27 = cursor.fetchone()

			for r in result27:
				row27 = r
			
			dis28 = "SELECT psmeteoTbk4_1315 FROM Psychrometer_Sangkar_Meteo1315_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis28)
			result28 = cursor.fetchone()
			
			for r in result28:
				row28 = r
			
			dis29 = "SELECT psmeteoTbb4_1315 FROM Psychrometer_Sangkar_Meteo1315_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis29)
			result29 = cursor.fetchone()
			
			for r in result29:
				row29 = r
			
			dis30 = "SELECT psmeteoRH4_1315 FROM Psychrometer_Sangkar_Meteo1315_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis30)
			result30 = cursor.fetchone()
			
			for r in result30:
				row30 = r
			
			dis31 = "SELECT psmeteoTbk7_1315 FROM Psychrometer_Sangkar_Meteo1315_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis31)
			result31 = cursor.fetchone()
			
			for r in result31:
				row31 = r
			
			dis32 = "SELECT psmeteoTbb7_1315 FROM Psychrometer_Sangkar_Meteo1315_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis32)
			result32 = cursor.fetchone()
			
			for r in result32:
				row32 = r
			
			dis33 = "SELECT psmeteoRH7_1315 FROM Psychrometer_Sangkar_Meteo1315_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis33)
			result33 = cursor.fetchone()
			
			for r in result33:
				row33 = r
			
			dis34 = "SELECT psmeteoTbk10_1315 FROM Psychrometer_Sangkar_Meteo1315_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis34)
			result34 = cursor.fetchone()
			
			for r in result34:
				row34 = r
			
			dis35 = "SELECT psmeteoTbb10_1315 FROM Psychrometer_Sangkar_Meteo1315_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis35)
			result35 = cursor.fetchone()
			
			for r in result35:
				row35 = r
			
			dis36 = "SELECT psmeteoRH10_1315 FROM Psychrometer_Sangkar_Meteo1315_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis36)
			result36 = cursor.fetchone()
			
			for r in result36:
				row36 = r
			
			dis37 = "SELECT psmeteoTbk1_2_1345 FROM Psychrometer_Sangkar_Meteo1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis37)
			result37 = cursor.fetchone()
			
			for r in result37:
				row37 = r
			
			dis38 = "SELECT psmeteoTbb1_2_1345 FROM Psychrometer_Sangkar_Meteo1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis38)
			result38 = cursor.fetchone()
			
			for r in result38:
				row38 = r
			
			dis39 = "SELECT psmeteoRH1_2_1345 FROM Psychrometer_Sangkar_Meteo1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis39)
			result39 = cursor.fetchone()
			
			for r in result39:	
				row39 = r
			
			dis40 = "SELECT psmeteoTbk4_1345 FROM Psychrometer_Sangkar_Meteo1345_1 WHERE Waktu = '%s'"  % input_tahun_bulan_tanggal.get()
			cursor.execute(dis40)
			result40 = cursor.fetchone()
			
			for r in result40:
				row40 = r
			
			dis41 = "SELECT psmeteoTbb4_1345 FROM Psychrometer_Sangkar_Meteo1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis41)
			result41 = cursor.fetchone()
			
			for r in result41:
				row41 = r
			
			dis42 = "SELECT psmeteoRH4_1345 FROM Psychrometer_Sangkar_Meteo1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis42)
			result42 = cursor.fetchone()
			
			for r in result42:
				row42 = r
			
			dis43 = "SELECT psmeteoTbk7_1345 FROM Psychrometer_Sangkar_Meteo1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis43)
			result43 = cursor.fetchone()
			
			for r in result43:	
				row43 = r
			
			dis44 = "SELECT psmeteoTbb7_1345 FROM Psychrometer_Sangkar_Meteo1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis44)
			result44 = cursor.fetchone()
			
			for r in result44:
				row44 = r
			
			dis45 = "SELECT psmeteoRH7_1345 FROM Psychrometer_Sangkar_Meteo1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis45)
			result45 = cursor.fetchone()
			
			for r in result45:
				row45 = r
			
			dis46 = "SELECT psmeteoTbk10_1345 FROM Psychrometer_Sangkar_Meteo1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis46)
			result46 = cursor.fetchone()
			
			for r in result46:	
				row46 = r
			
			dis47 = "SELECT psmeteoTbb10_1345 FROM Psychrometer_Sangkar_Meteo1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis47)
			result47 = cursor.fetchone()
			
			for r in result47:
				row47 = r
			
			dis48 = "SELECT psmeteoRH10_1345 FROM Psychrometer_Sangkar_Meteo1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis48)
			result48 = cursor.fetchone()
			
			for r in result48:
				row48 = r
			
			dis49 = "SELECT psmeteoTbk1_2_1415 FROM Psychrometer_Sangkar_Meteo1415_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis49)
			result49 = cursor.fetchone()
			
			for r in result49:
				row49 = r
			
			dis50 = "SELECT psmeteoTbb1_2_1415 FROM Psychrometer_Sangkar_Meteo1415_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis50)
			result50 = cursor.fetchone()
			
			for r in result50:
				row50 = r
			
			dis51 = "SELECT psmeteoRH1_2_1415 FROM Psychrometer_Sangkar_Meteo1415_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis51)
			result51 = cursor.fetchone()
			
			for r in result51:
				row51 = r
			
			dis52 = "SELECT psmeteoTbk4_1415 FROM Psychrometer_Sangkar_Meteo1415_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis52)
			result52 = cursor.fetchone()
			
			for r in result52:
				row52 = r
			
			dis53 = "SELECT psmeteoTbb4_1415 FROM Psychrometer_Sangkar_Meteo1415_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis52)
			result53 = cursor.fetchone()
			
			for r in result53:
				row53 = r
			
			dis54 = "SELECT psmeteoRH4_1415 FROM Psychrometer_Sangkar_Meteo1415_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis54)
			result54 = cursor.fetchone()
			
			for r in result54:
				row54 = r
			
			dis55 = "SELECT psmeteoTbk7_1415 FROM Psychrometer_Sangkar_Meteo1415_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis55)
			result55 = cursor.fetchone()
			
			for r in result55:
				row55 = r
			
			dis56 = "SELECT psmeteoTbb7_1415 FROM Psychrometer_Sangkar_Meteo1415_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis56)
			result56 = cursor.fetchone()
			
			for r in result56:
				row56 = r
			
			dis57 = "SELECT psmeteoRH7_1415 FROM Psychrometer_Sangkar_Meteo1415_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis57)
			result57 = cursor.fetchone()
			
			for r in result57:
				row57 = r
			
			dis58 = "SELECT psmeteoTbk10_1415 FROM Psychrometer_Sangkar_Meteo1415_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis58)
			result58 = cursor.fetchone()
			
			for r in result58:
				row58 = r
			
			dis59 = "SELECT psmeteoTbb10_1415 FROM Psychrometer_Sangkar_Meteo1415_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis59)
			result59 = cursor.fetchone()
			
			for r in result59:
				row59 = r
			
			dis60 = "SELECT psmeteoRH10_1415 FROM Psychrometer_Sangkar_Meteo1415_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis60)
			result60 = cursor.fetchone()
			
			for r in result60:
				row60 = r
			
			dis61 = "SELECT psmeteoTbk1_2_1745 FROM Psychrometer_Sangkar_Meteo1745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis61)
			result61 = cursor.fetchone()
			
			for r in result61:
				row61 = r
			
			dis62 = "SELECT psmeteoTbb1_2_1745 FROM Psychrometer_Sangkar_Meteo1745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis62)
			result62 = cursor.fetchone()
			
			for r in result62:
				row62 = r
			
			dis63 = "SELECT psmeteoRH1_2_1745 FROM Psychrometer_Sangkar_Meteo1745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis63)
			result63 = cursor.fetchone()
			
			for r in result63:
				row63 = r
			
			dis64 = "SELECT psmeteoTbk4_1745 FROM Psychrometer_Sangkar_Meteo1745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis64)
			result64 = cursor.fetchone()
			
			for r in result64:
				row64 = r
			
			dis65 = "SELECT psmeteoTbb4_1745 FROM Psychrometer_Sangkar_Meteo1745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis65)
			result65 = cursor.fetchone()
			
			for r in result65:
				row65 = r
			
			dis66 = "SELECT psmeteoRH4_1745 FROM Psychrometer_Sangkar_Meteo1745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis66)
			result66 = cursor.fetchone()
			
			for r in result66:
				row66 = r
			
			dis67 = "SELECT psmeteoTbk7_1745 FROM Psychrometer_Sangkar_Meteo1745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis67)
			result67 = cursor.fetchone()
			
			for r in result67:
				row67 = r
			
			dis68 = "SELECT psmeteoTbb7_1745 FROM Psychrometer_Sangkar_Meteo1745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis68)
			result68 = cursor.fetchone()
			
			for r in result68:
				row68 = r
			
			dis69 = "SELECT psmeteoRH7_1745 FROM Psychrometer_Sangkar_Meteo1745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis69)
			result69 = cursor.fetchone()
			
			for r in result69:
				row69 = r
			
			dis70 = "SELECT psmeteoTbk10_1745 FROM Psychrometer_Sangkar_Meteo1745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis70)
			result70 = cursor.fetchone()
			
			for r in result70:
				row70 = r
			
			dis71 = "SELECT psmeteoTbb10_1745 FROM Psychrometer_Sangkar_Meteo1745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis71)
			result71 = cursor.fetchone()
			
			for r in result71:
				row71 = r
			
			dis72 = "SELECT psmeteoRH10_1745 FROM Psychrometer_Sangkar_Meteo1745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis72)
			result72 = cursor.fetchone()	
			
			for r in result72:
				row72 = r
			
			dis73 = "SELECT psmeteoTbk1_2_1815 FROM Psychrometer_Sangkar_Meteo1815_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis73)
			result73 = cursor.fetchone()
			
			for r in result73:
				row73 = r
			
			dis74 = "SELECT psmeteoTbb1_2_1815 FROM Psychrometer_Sangkar_Meteo1815_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis74)
			result74 = cursor.fetchone()
			
			for r in result74:
				row74 = r
			
			dis75 = "SELECT psmeteoRH1_2_1815 FROM Psychrometer_Sangkar_Meteo1815_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis75)
			result75 = cursor.fetchone()
			
			for r in result75:
				row75 = r
			
			dis76 = "SELECT psmeteoTbk4_1815 FROM Psychrometer_Sangkar_Meteo1815_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis76)
			result76 = cursor.fetchone()
			
			for r in result76:
				row76 = r
			
			dis77 = "SELECT psmeteoTbb4_1815 FROM Psychrometer_Sangkar_Meteo1815_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis77)
			result77 = cursor.fetchone()
			
			for r in result77:
				row77 = r
			
			dis78 = "SELECT psmeteoRH4_1815 FROM Psychrometer_Sangkar_Meteo1815_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis78)
			result78 = cursor.fetchone()
			
			for r in result78:
				row78 = r
			
			dis79 = "SELECT psmeteoTbk7_1815 FROM Psychrometer_Sangkar_Meteo1815_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis79)
			result79 = cursor.fetchone()
			
			for r in result79:
				row79 = r
			
			dis80 = "SELECT psmeteoTbb7_1815 FROM Psychrometer_Sangkar_Meteo1815_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis80)
			result80 = cursor.fetchone()
			
			for r in result80:
				row80 = r
			
			dis81 = "SELECT psmeteoRH7_1815 FROM Psychrometer_Sangkar_Meteo1815_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis81)
			result81 = cursor.fetchone()
			
			for r in result81:
				row81 = r
			
			dis82 = "SELECT psmeteoTbk10_1815 FROM Psychrometer_Sangkar_Meteo1815_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis82)
			result82 = cursor.fetchone()
			
			for r in result82:
				row82 = r
			
			dis83 = "SELECT psmeteoTbb10_1815 FROM Psychrometer_Sangkar_Meteo1815_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis83)
			result83 = cursor.fetchone()
			
			for r in result83:
				row83 = r
			
			dis84 = "SELECT psmeteoRH10_1815 FROM Psychrometer_Sangkar_Meteo1815_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis84)
			result84 = cursor.fetchone()
			
			for r in result84:
				row84 = r
			
		# Lama Penyinaran	
		with con.cursor() as cursor:
			dis85 = "SELECT lamapenyinaran12jam_jam FROM Lama_Penyinaran_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis85)
			result85 = cursor.fetchone()
			
			for r in result85:
				row85 = r
			
			dis86 = "SELECT lamapenyinaran8jam_jam FROM Lama_Penyinaran_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis86)
			result86 = cursor.fetchone()
			
			for r in result86:
				row86 = r
			
			dis87 = "SELECT lamapenyinaran12jam_persen FROM Lama_Penyinaran_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis87)
			result87 = cursor.fetchone()
			
			for r in result87:
				row87 = r
			
			dis88 = "SELECT lamapenyinaran8jam_persen FROM Lama_Penyinaran_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis88)
			result88 = cursor.fetchone()
			
			for r in result88:
				row88 = r
			
		#Termometer Maksimum dan Minimum
		with con.cursor() as cursor:
			dis89 = "SELECT termoMM_max_1815 FROM Termo_Max_Min1815_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis89)
			result89 = cursor.fetchone()
			
			for r in result89:
				row89 = r
			
			dis90 = "SELECT termoMM_reset_1815 FROM Termo_Max_Min1815_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis90)
			result90 = cursor.fetchone()
			
			for r in result90:
				row90 = r
			
			dis91 = "SELECT termoMM_min_1415 FROM Termo_Max_Min1415_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis91)
			result91 = cursor.fetchone()
			
			for r in result91:
				row91 = r
			
			dis92 = "SELECT termoMM_reset_1415 FROM Termo_Max_Min1415_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis92)
			result92 = cursor.fetchone()	
			
			for r in result92:
				row92 = r
			
		# Piche Evaporimeter
		with con.cursor() as cursor:
			dis93 = "SELECT piche_evaporimeter1_07_45 FROM Piche_Evaporimeter_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis93)
			result93 = cursor.fetchone()
			
			for r in result93:
				row93 = r
			
			dis94 = "SELECT piche_evaporimeter2_07_45 FROM Piche_Evaporimeter_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis94)
			result94 = cursor.fetchone()
			
			for r in result94:
				row94 = r
			
			dis95 = "SELECT piche_evaporimeter1_13_45 FROM Piche_Evaporimeter_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis95)
			result95 = cursor.fetchone()
			
			for r in result95:
				row95 = r
			
			dis96 = "SELECT piche_evaporimeter2_13_45 FROM Piche_Evaporimeter_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis96)
			result96 = cursor.fetchone()
			
			for r in result96:
				row96 = r
			
			dis97 = "SELECT piche_evaporimeter1_17_45 FROM Piche_Evaporimeter_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis97)
			result97 = cursor.fetchone()
			
			for r in result97:
				row97 = r
			
			dis98 = "SELECT piche_evaporimeter2_17_45 FROM Piche_Evaporimeter_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis98)
			result98 = cursor.fetchone()
			
			for r in result98:
				row98 = r
			
		# Radiasi
		with con.cursor() as cursor:
			dis99 = "SELECT intensitas FROM Radiasi_2 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis99)
			result99 = cursor.fetchone()
			
			for r in result99:
				row99 = r
			
		# Suhu Minimum Rumput
		with con.cursor() as cursor:
			dis100 = "SELECT suhumin_rumput0715 FROM Suhu_Minimum_Rumput_2 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis100)
			result100 = cursor.fetchone()
			
			for r in result100:
				row100 = r
			
			dis101 = "SELECT suhumin_rumput0715_reset FROM Suhu_Minimum_Rumput_2 WHERE Waktu = '%s'"  % input_tahun_bulan_tanggal.get()
			cursor.execute(dis101)
			result101 = cursor.fetchone()	

			for r in result101:
				row101 = r
				
		# Kondisi Cuaca dan Tanah
		with con.cursor() as cursor:
			dis102 = "SELECT kodetanah_07_15 FROM Kondisi_Cuaca_Tanah0715_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis102)
			result102 = cursor.fetchone()
			
			for r in result102:
				row102 = r
			
			dis103 = "SELECT kodetanah_14_15 FROM Kondisi_Cuaca_Tanah1415_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis103)
			result103 = cursor.fetchone()
			
			for r in result103:
				row103 = r
			
			dis104 = "SELECT kodecuaca_07_15 FROM Kondisi_Cuaca_Tanah0715_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis104)
			result104 = cursor.fetchone()
			
			for r in result104:
				row104 = r
			
			dis105 = "SELECT kodecuaca_14_15 FROM Kondisi_Cuaca_Tanah1415_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis105)
			result105 = cursor.fetchone()
			
			for r in result105:
				row105 = r
			
		# Open Pan
		with con.cursor() as cursor:
			dis106 = "SELECT ketinggian_airpanci07_15 FROM Open_Pan_0715_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis106)
			result106 = cursor.fetchone()
			
			for r in result106:
				row106 = r
			
			dis107 = "SELECT ketinggian_airpanci07_45 FROM Open_Pan_0745_2 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis107)
			result107 = cursor.fetchone()
			
			for r in result107:
				row107 = r
			
			dis108 = "SELECT ketinggian_airpanci13_45 FROM Open_Pan_1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis108)
			result108 = cursor.fetchone()
			
			for r in result108:
				row108 = r
			
			dis109 = "SELECT ketinggian_airpanci17_45 FROM Open_Pan_1745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis109)
			result109 = cursor.fetchone()
			
			for r in result109:
				row109 = r
			
			dis110 = "SELECT suhu_airmax07_15 FROM Open_Pan_0715_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis110)
			result110 = cursor.fetchone()
			
			for r in result110:
				row110 = r
			
			dis111 = "SELECT suhu_airmax07_45 FROM Open_Pan_0745_2 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis111)
			result111 = cursor.fetchone()

			for r in result111:
				row111 = r
		
			dis112 = "SELECT suhu_airmax13_45 FROM Open_Pan_1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis112)
			result112 = cursor.fetchone()
			
			for r in result112:
				row112 = r
			
			dis113 = "SELECT suhu_airmax17_45 FROM Open_Pan_1745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis113)
			result113 = cursor.fetchone()
			
			for r in result113:
				row113 = r
			
			dis114 = "SELECT suhu_airmin07_15 FROM Open_Pan_0715_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis114)
			result114 = cursor.fetchone()
			
			for r in result114:
				row114 = r
			
			dis115 = "SELECT suhu_airmin07_45 FROM Open_Pan_0745_2 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis115)
			result115 = cursor.fetchone()
			
			for r in result115:
				row115 = r
			
			dis116 = "SELECT suhu_airmin13_45 FROM Open_Pan_1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis116)
			result116 = cursor.fetchone()
			
			for r in result116:
				row116 = r
			
			dis117 = "SELECT suhu_airmin17_45 FROM Open_Pan_1745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis117)
			result117 = cursor.fetchone()
			
			for r in result117:
				row117 = r
			
			dis118 = "SELECT hujan_13_5jam07_15 FROM Open_Pan_0715_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis118)
			result118 = cursor.fetchone()
			
			for r in result118:
				row118 = r
			
			dis119 = "SELECT hujan_24jam_07_15 FROM Open_Pan_0715_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis119)
			result119 = cursor.fetchone()
			
			for r in result119:
				row119 = r
			
			dis120 = "SELECT hujan_30menit07_45 FROM Open_Pan_0745_2 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis120)
			result120 = cursor.fetchone()
			
			for r in result120:
				row120 = r
			
			dis121 = "SELECT hujan_6jam_13_45 FROM Open_Pan_1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis121)
			result121 = cursor.fetchone()
			
			for r in result121:
				row121 = r
			
			dis122 = "SELECT hujan_4jam_17_45 FROM Open_Pan_1745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis122)
			result122 = cursor.fetchone()
			
			for r in result122:
				row122 = r
			
			dis123 = "SELECT penguapan_24jam_07_15 FROM Open_Pan_0715_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis123)
			result123 = cursor.fetchone()
			
			for r in result123:
				row123 = r
			
			dis124 = "SELECT penguapan_13_5jam07_45 FROM Open_Pan_0745_2 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis124)
			result124 = cursor.fetchone()
			
			for r in result124:
				row124 = r
			
			dis125 = "SELECT penguapan_6jam_13_45 FROM Open_Pan_1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis125)
			result125 = cursor.fetchone()
			
			for r in result125:
				row125 = r
			
			dis126 = "SELECT penguapan_4jam_17_45 FROM Open_Pan_1745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis126)
			result126 = cursor.fetchone()
			
			for r in result126:
				row126 = r
			
		# Barometer
		with con.cursor() as cursor:
			dis127 = "SELECT suhu00_00UTC FROM Barometer_5 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis127)
			result127 = cursor.fetchone()
			
			for r in result127:
				row127 = r		
			
			dis128 = "SELECT barometer00_00UTC FROM Barometer_5 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis128)
			result128 = cursor.fetchone()
			
			for r in result128:
				row128 = r
	
			dis129 = "SELECT QFF00_00UTC FROM Barometer_5 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis129)
			result129 = cursor.fetchone()
			
			for r in result129:
				row129 = r
			
			dis130 = "SELECT QFE00_00UTC FROM Barometer_5 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis130)
			result130 = cursor.fetchone()
			
			for r in result130:
				row130 = r
			
		# Catatan
		with con.cursor() as cursor:
			dis302 = "SELECT catatan1 FROM PMGonDuty_Catatan_4 WHERE Waktu = '%s' " % input_tahun_bulan_tanggal.get()
			cursor.execute(dis302)
			result302 = cursor.fetchone()
			
			for r in result302:
				row302 = r
			
		# Angin
		with con.cursor() as cursor:
			dis131 ="SELECT cup0_5_07_15 FROM Angin0715_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis131)
			result131 = cursor.fetchone()
			
			for r in result131:
				row131 = r
			
			dis132 ="SELECT cup0_5_07_45 FROM Angin0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis132)
			result132 = cursor.fetchone()
			
			for r in result132:
				row132 = r
			
			dis133 ="SELECT cup0_5_13_45 FROM Angin1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis133)
			result133 = cursor.fetchone()
			
			for r in result133:
				row133 = r
			
			dis134 ="SELECT cup0_5_14_15 FROM Angin1415_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis134)
			result134 = cursor.fetchone()
			
			for r in result134:
				row134 = r
			
			dis135 ="SELECT cup0_5_17_45 FROM Angin1745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis135)
			result135 = cursor.fetchone()
			
			for r in result135:
				row135 = r
			
			dis136 ="SELECT cup0_5_18_15 FROM Angin1815_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis136)
			result136 = cursor.fetchone()
			
			for r in result136:
				row136 = r
			
			dis137 ="SELECT cup2_0_07_15 FROM Angin0715_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis137)
			result137 = cursor.fetchone()
			
			for r in result137:
				row137 = r
			
			dis138 ="SELECT cup2_0_07_45 FROM Angin0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis138)
			result138 = cursor.fetchone()
			
			for r in result138:
				row138 = r
			
			dis139 ="SELECT cup2_0_13_45 FROM Angin1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis139)
			result139 = cursor.fetchone()
			
			for r in result139:
				row139 = r

			dis140 ="SELECT cup2_0_14_15 FROM Angin1415_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis140)
			result140 = cursor.fetchone()
			
			for r in result140:
				row140 = r
			
			dis141 ="SELECT cup2_0_17_45 FROM Angin1745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis141)
			result141 = cursor.fetchone()
			
			for r in result141:
				row141 = r
			
			dis142 ="SELECT cup2_0_18_15 FROM Angin1815_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis142)
			result142 = cursor.fetchone()
			
			for r in result142:
				row142 = r
			
			dis143 ="SELECT arah4m_07_15 FROM Angin0715_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis143)
			result143 = cursor.fetchone()
			
			for r in result143:
				row143 = r
			
			dis144 ="SELECT arah4m_07_45 FROM Angin0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis144)
			result144 = cursor.fetchone()
			
			for r in result144:
				row144 = r
			
			dis145 ="SELECT arah4m_13_45 FROM Angin1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis145)
			result145 = cursor.fetchone()
			
			for r in result145:
				row145 = r
			
			dis146 ="SELECT arah4m_14_15 FROM Angin1415_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis146)
			result146 = cursor.fetchone()
			
			for r in result146:
				row146 = r
	
			dis147 ="SELECT arah4m_17_45 FROM Angin1745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis147)
			result147 = cursor.fetchone()
			
			for r in result147:
				row147 = r
			
			dis148 ="SELECT arah4m_18_15 FROM Angin1815_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis148)
			result148 = cursor.fetchone()
			
			for r in result148:
				row148 = r
			
			dis149 ="SELECT kecepatan4m_07_15 FROM Angin0715_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis149)
			result149 = cursor.fetchone()
			
			for r in result149:
				row149 = r
			
			dis150 ="SELECT kecepatan4m_07_45 FROM Angin0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis150)
			result150 = cursor.fetchone()
			
			for r in result150:
				row150 = r
			
			dis151 ="SELECT kecepatan4m_13_45 FROM Angin1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis151)
			result151 = cursor.fetchone()
			
			for r in result151:
				row151 = r
			
			dis152 ="SELECT kecepatan4m_14_15 FROM Angin1415_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis152)
			result152 = cursor.fetchone()
			
			for r in result152:
				row152 = r
			
			dis153 ="SELECT kecepatan4m_17_45 FROM Angin1745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis153)
			result153 = cursor.fetchone()
			
			for r in result153:
				row153 = r
			
			dis154 ="SELECT kecepatan4m_18_15 FROM Angin1815_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis154)
			result154 = cursor.fetchone()
			
			for r in result154:
				row154 = r
			
			dis155 ="SELECT arah7m_07_15 FROM Angin0715_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis155)
			result155 = cursor.fetchone()
			
			for r in result155:
				row155 = r
			
			dis156 ="SELECT arah7m_07_45 FROM Angin0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis156)
			result156 = cursor.fetchone()
			
			for r in result156:
				row156 = r
			
			dis157 ="SELECT arah7m_13_45 FROM Angin1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis157)
			result157 = cursor.fetchone()
			
			for r in result157:
				row157 = r
			
			dis158 ="SELECT arah7m_14_15 FROM Angin1415_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis158)
			result158 = cursor.fetchone()
			
			for r in result158:
				row158 = r
			
			dis159 ="SELECT arah7m_17_45 FROM Angin1745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis159)
			result159 = cursor.fetchone()
			
			for r in result159:
				row159 = r
			
			dis160 ="SELECT arah7m_18_15 FROM Angin1815_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis160)
			result160 = cursor.fetchone()
			
			for r in result160:
				row160 = r
			
			dis161 ="SELECT kecepatan7m_07_15 FROM Angin0715_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis161)
			result161 = cursor.fetchone()
			
			for r in result161:
				row161 = r
			
			dis162 ="SELECT kecepatan7m_07_45 FROM Angin0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis162)
			result162 = cursor.fetchone()
			
			for r in result162:
				row162 = r
			
			dis163 ="SELECT kecepatan7m_13_45 FROM Angin1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis163)
			result163 = cursor.fetchone()
			
			for r in result163:
				row163 = r
			
			dis164 ="SELECT kecepatan7m_14_15 FROM Angin1415_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis164)
			result164 = cursor.fetchone()
			
			for r in result164:
				row164 = r
			
			dis165 ="SELECT kecepatan7m_17_45 FROM Angin1745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis165)
			result165 = cursor.fetchone()
			
			for r in result165:
				row165 = r
			
			dis166 ="SELECT kecepatan7m_18_15 FROM Angin1815_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis166)
			result166 = cursor.fetchone()
			
			
			for r in result166:
				row166 = r
			
			dis167 ="SELECT arah10m_07_15 FROM Angin0715_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis167)
			result167 = cursor.fetchone()
			
			for r in result167:
				row167 = r
			
			dis168 ="SELECT arah10m_07_45 FROM Angin0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis168)
			result168 = cursor.fetchone()
			
			for r in result168:
				row168 = r
			
			dis169 ="SELECT arah10m_13_45 FROM Angin1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis169)
			result169 = cursor.fetchone()
			
			for r in result169:
				row169 = r
			
			dis170 ="SELECT arah10m_14_15 FROM Angin1415_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis170)
			result170 = cursor.fetchone()
			
			for r in result170:
				row170 = r
			
			dis171 ="SELECT arah10m_17_45 FROM Angin1745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis171)
			result171 = cursor.fetchone()
			
			for r in result171:
				row171 = r
			
			dis172 ="SELECT arah10m_18_15 FROM Angin1815_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis172)
			result172 = cursor.fetchone()
			
			for r in result172:
				row172 = r
			
			dis173 ="SELECT kecepatan10m_07_15 FROM Angin0715_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis173)
			result173 = cursor.fetchone()
			
			for r in result173:
				row173 = r
			
			dis174 ="SELECT kecepatan10m_07_45 FROM Angin0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis174)
			result174 = cursor.fetchone()
			
			for r in result174:
				row174 = r
			
			dis175 ="SELECT kecepatan10m_13_45 FROM Angin1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis175)
			result175 = cursor.fetchone()
			
			for r in result175:
				row175 = r
			
			dis176 ="SELECT kecepatan10m_14_15 FROM Angin1415_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis176)
			result176 = cursor.fetchone()
			
			for r in result176:
				row176 = r
			
			dis177 ="SELECT kecepatan10m_17_45 FROM Angin1745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis177)
			result177 = cursor.fetchone()
			
			for r in result177:
				row177 = r
			
			dis178 ="SELECT kecepatan10m_18_15 FROM Angin1815_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis178)
			result178 = cursor.fetchone()
			
			for r in result178:
				row178 = r
			
		# Suhu Tanah
		with con.cursor() as cursor:
			dis179 = "SELECT suhutanah_berumput0_0745 FROM Suhu_Tanah0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis179)
			result179 = cursor.fetchone()
			
			for r in result179:
				row179 = r
			
			dis180 = "SELECT suhutanah_berumput2_0745 FROM Suhu_Tanah0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis180)
			result180 = cursor.fetchone()
			
			for r in result180:
				row180 = r
			
			dis181 = "SELECT suhutanah_berumput5_0745 FROM Suhu_Tanah0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis181)
			result181 = cursor.fetchone()
			
			for r in result181:
				row181 = r
			
			dis182 = "SELECT suhutanah_berumput10_0745 FROM Suhu_Tanah0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis182)
			result182 = cursor.fetchone()
			
			for r in result182:
				row182 = r
			
			dis183 = "SELECT suhutanah_berumput20_0745 FROM Suhu_Tanah0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis183)
			result183 = cursor.fetchone()
			
			for r in result183:
				row183 = r
			
			dis184 = "SELECT suhutanah_gundul0_0745 FROM Suhu_Tanah0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis184)
			result184 = cursor.fetchone()
			
			for r in result184:
				row184 = r
			
			dis185 = "SELECT suhutanah_gundul2_0745 FROM Suhu_Tanah0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis185)
			result185 = cursor.fetchone()
			
			for r in result185:
				row185 = r
			
			dis186 = "SELECT suhutanah_gundul5_0745 FROM Suhu_Tanah0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis186)
			result186 = cursor.fetchone()
			
			for r in result186:
				row186 = r
			
			dis187 = "SELECT suhutanah_gundul10_0745 FROM Suhu_Tanah0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis187)
			result187 = cursor.fetchone()
			
			for r in result187:
				row187 = r
			
			dis188 = "SELECT suhutanah_gundul20_0745 FROM Suhu_Tanah0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis188)
			result188 = cursor.fetchone()
			
			for r in result188:
				row188 = r
			
			dis189 = "SELECT suhutanah_berumput0_1345 FROM Suhu_Tanah1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis189)
			result189 = cursor.fetchone()
			
			for r in result189:
				row189 = r
			
			dis190 = "SELECT suhutanah_berumput2_1345 FROM Suhu_Tanah1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis190)
			result190 = cursor.fetchone()
			
			for r in result190:
				row190 = r
			
			dis191 = "SELECT suhutanah_berumput5_1345 FROM Suhu_Tanah1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis191)
			result191 = cursor.fetchone()
			
			for r in result191:
				row191 = r
			
			dis192 = "SELECT suhutanah_berumput10_1345 FROM Suhu_Tanah1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis192)
			result192 = cursor.fetchone()
			
			for r in result192:
				row192 = r
			
			dis193 = "SELECT suhutanah_berumput20_1345 FROM Suhu_Tanah1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis193)
			result193 = cursor.fetchone()
			
			for r in result193:
				row193 = r
			
			dis194 = "SELECT suhutanah_gundul0_1345 FROM Suhu_Tanah1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis194)
			result194 = cursor.fetchone()
			
			for r in result194:
				row194 = r
			
			dis195 = "SELECT suhutanah_gundul2_1345 FROM Suhu_Tanah1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis195)
			result195 = cursor.fetchone()
			
			for r in result195:
				row195 = r
			
			dis196 = "SELECT suhutanah_gundul5_1345 FROM Suhu_Tanah1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis196)
			result196 = cursor.fetchone()
			
			for r in result196:
				row196 = r
			
			dis197 = "SELECT suhutanah_gundul10_1345 FROM Suhu_Tanah1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis197)
			result197 = cursor.fetchone()
			
			for r in result197:
				row197 = r
			
			dis198 = "SELECT suhutanah_gundul20_1345 FROM Suhu_Tanah1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis198)
			result198 = cursor.fetchone()
			
			for r in result198:
				row198 = r
			
			dis199 = "SELECT suhutanah_berumput0_1415 FROM Suhu_Tanah1415_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis199)
			result199 = cursor.fetchone()
			
			for r in result199:
				row199 = r
			
			dis200 = "SELECT suhutanah_berumput2_1415 FROM Suhu_Tanah1415_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis200)
			result200 = cursor.fetchone()
			
			for r in result200:
				row200 = r
			
			dis201 = "SELECT suhutanah_berumput5_1415 FROM Suhu_Tanah1415_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis201)
			result201 = cursor.fetchone()
			
			for r in result201:
				row201 = r
				
			dis202 = "SELECT suhutanah_berumput10_1415 FROM Suhu_Tanah1415_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis202)
			result202 = cursor.fetchone()
			
			for r in result202:
				row202 = r
			
			dis203 = "SELECT suhutanah_berumput20_1415 FROM Suhu_Tanah1415_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis203)
			result203 = cursor.fetchone()
			
			for r in result203:
				row203 = r
			
			dis204 = "SELECT suhutanah_gundul0_1415 FROM Suhu_Tanah1415_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis204)
			result204 = cursor.fetchone()
			
			for r in result204:
				row204 = r
			
			dis205 = "SELECT suhutanah_gundul2_1415 FROM Suhu_Tanah1415_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis205)
			result205 = cursor.fetchone()
			
			for r in result205:
				row205 = r
			
			dis206 = "SELECT suhutanah_gundul5_1415 FROM Suhu_Tanah1415_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis206)
			result206 = cursor.fetchone()
			
			for r in result206:
				row206 = r
			
			dis207 = "SELECT suhutanah_gundul10_1415 FROM Suhu_Tanah1415_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis207)
			result207 = cursor.fetchone()
			
			for r in result207:
				row207 = r
			
			dis208 = "SELECT suhutanah_gundul20_1415 FROM Suhu_Tanah1415_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis208)
			result208 = cursor.fetchone()
			
			for r in result208:
				row208 = r
			
			dis209 = "SELECT suhutanah_berumput0_1745 FROM Suhu_Tanah1745_4 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis209)
			result209 = cursor.fetchone()
			
			for r in result209:
				row209 = r
			
			dis210 = "SELECT suhutanah_berumput2_1745 FROM Suhu_Tanah1745_4 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis210)
			result210 = cursor.fetchone()
			
			for r in result210:
				row210 = r
			
			dis211 = "SELECT suhutanah_berumput5_1745 FROM Suhu_Tanah1745_4 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis211)
			result211 = cursor.fetchone()
			
			for r in result211:
				row211 = r
			
			dis212 = "SELECT suhutanah_berumput10_1745 FROM Suhu_Tanah1745_4 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get() 
			cursor.execute(dis212)
			result212 = cursor.fetchone()
			
			for r in result212:
				row212 = r
			
			dis213 = "SELECT suhutanah_berumput20_1745 FROM Suhu_Tanah1745_4 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis213)
			result213 = cursor.fetchone()
			
			for r in result213:
				row213 = r
			
			dis214 = "SELECT suhutanah_berumput50_1745 FROM Suhu_Tanah1745_4 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis214)
			result214 = cursor.fetchone()
			
			for r in result214:
				row214 = r
			
			dis215 = "SELECT suhutanah_berumput100_1745 FROM Suhu_Tanah1745_4 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis215)
			result215 = cursor.fetchone()
			
			for r in result215:
				row215 = r
			
			dis216 = "SELECT suhutanah_gundul0_1745 FROM Suhu_Tanah1745_4 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis216)
			result216 = cursor.fetchone()
			
			for r in result216:
				row216 = r
			
			dis217 = "SELECT suhutanah_gundul2_1745 FROM Suhu_Tanah1745_4 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis217)
			result217 = cursor.fetchone()
			
			for r in result217:
				row217 = r
			
			dis218 = "SELECT suhutanah_gundul5_1745 FROM Suhu_Tanah1745_4 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis218)
			result218 = cursor.fetchone()
			
			for r in result218:
				row218 = r
			
			dis219 = "SELECT suhutanah_gundul10_1745 FROM Suhu_Tanah1745_4 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis219)
			result219 = cursor.fetchone()
			
			for r in result219:
				row219 = r
			
			dis220 = "SELECT suhutanah_gundul20_1745 FROM Suhu_Tanah1745_4 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis220)
			result220 = cursor.fetchone()
			
			for r in result220:
				row220 = r
			
			dis221 = "SELECT suhutanah_gundul50_1745 FROM Suhu_Tanah1745_4 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis221)
			result221 = cursor.fetchone()
			
			for r in result221:
				row221 = r
			
			dis222 = "SELECT suhutanah_gundul100_1745 FROM Suhu_Tanah1745_4 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis222)
			result222 = cursor.fetchone()
			
			for r in result222:
				row222 = r

		# Lysimeter
		with con.cursor() as cursor:
			dis223 = "SELECT tanahgundul_siram FROM Lysimeter_11 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis223)
			result223 = cursor.fetchone()
			
			for r in result223:
				row223 = r
			
			dis224 = "SELECT tanahgundul_keluar FROM Lysimeter_11 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis224)
			result224 = cursor.fetchone()
			
			for r in result224:
				row224 = r
			
			dis225 = "SELECT tanahtanamankomoditi_siram FROM Lysimeter_11 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis225)
			result225 = cursor.fetchone()
			
			for r in result225:
				row225 = r
			
			dis226 = "SELECT tanahtanamankomoditi_keluar FROM Lysimeter_11 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis226)
			result226 = cursor.fetchone()
			
			for r in result226:
				row226 = r
			
			dis227 = "SELECT tanahberumput_siram FROM Lysimeter_11 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis227)
			result227 = cursor.fetchone()
			
			for r in result227:
				row227 = r
			
			dis228 = "SELECT tanahberumput_keluar FROM Lysimeter_11 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis228)
			result228 = cursor.fetchone()
			
			for r in result228:
				row228 = r
			
			dis229 = "SELECT lain2_curahhujanperjam17_15 FROM Lysimeter_11 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis229)
			result229 = cursor.fetchone()
			
			for r in result229:
				row229 = r
			
			dis230 = "SELECT lain2_namatanamankomoditi FROM Lysimeter_11 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis230)
			result230 = cursor.fetchone()
			
			for r in result230:
				row230 = r
			
			dis231 = "SELECT lain2_keteranganfase_atas FROM Lysimeter_11 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis231)
			result231 = cursor.fetchone()
			
			for r in result231:
				row231 = r
			
			dis295 = "SELECT lain2_keteranganfase_bawah FROM Lysimeter_11 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis295)
			result295 = cursor.fetchone()
			
			for r in result295:
				row295 = r

			dis296 = "SELECT lain2_keteranganfase_hasil FROM Lysimeter_11 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis296)
			result296 = cursor.fetchone()
			
			for r in result296:
				row296 = r
			
			dis297 = "SELECT lain2_display FROM Lysimeter_11 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis297)
			result297 = cursor.fetchone()
			
			for r in result297:
				row297 = r
			
		# Psychrometer Assmann
		with con.cursor() as cursor:
			dis232 = "SELECT passmannBK5_0745 FROM Psychrometer_Assmann0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis232)
			result232 = cursor.fetchone()
			
			for r in result232:
				row232 = r
			
			dis233 = "SELECT passmannBK10_0745 FROM Psychrometer_Assmann0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis233)
			result233 = cursor.fetchone()
			
			for r in result233:
				row233 = r
			
			dis234 = "SELECT passmannBK20_0745 FROM Psychrometer_Assmann0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis234)
			result234 = cursor.fetchone()
			
			for r in result234:
				row234 = r
			
			dis235 = "SELECT passmannBK50_0745 FROM Psychrometer_Assmann0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis235)
			result235 = cursor.fetchone()
			
			for r in result235:
				row235 = r
			
			dis236 = "SELECT passmannBK100_0745 FROM Psychrometer_Assmann0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis236)
			result236 = cursor.fetchone()
			
			for r in result236:
				row236 = r
			
			dis237 = "SELECT passmannBK150_0745 FROM Psychrometer_Assmann0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get() 
			cursor.execute(dis237)
			result237 = cursor.fetchone()
			
			for r in result237:
				row237 = r
			
			dis238 = "SELECT passmannBK200_0745 FROM Psychrometer_Assmann0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis238)
			result238 = cursor.fetchone()
			
			for r in result238:
				row238 = r
			
			dis239 = "SELECT passmannBB5_0745 FROM Psychrometer_Assmann0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis239)
			result239 = cursor.fetchone()
			
			for r in result239:
				row239 = r
			
			dis240 = "SELECT passmannBB10_0745 FROM Psychrometer_Assmann0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis240)
			result240 = cursor.fetchone()
			
			for r in result240:
				row240 = r
			
			dis241 = "SELECT passmannBB20_0745 FROM Psychrometer_Assmann0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis241)
			result241 = cursor.fetchone()
			
			for r in result241:
				row241 = r
			
			dis242 = "SELECT passmannBB50_0745 FROM Psychrometer_Assmann0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis242)
			result242 = cursor.fetchone()
			
			for r in result242:
				row242 = r
			
			dis243 = "SELECT passmannBB100_0745 FROM Psychrometer_Assmann0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis243)
			result243 = cursor.fetchone()
			
			for r in result243:
				row243 = r
			
			dis244 = "SELECT passmannBB150_0745 FROM Psychrometer_Assmann0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis244)
			result244 = cursor.fetchone()
			
			for r in result244:
				row244 = r
			
			dis245 = "SELECT passmannBB200_0745 FROM Psychrometer_Assmann0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis245)
			result245 = cursor.fetchone()
			
			for r in result245:
				row245 = r
			
			dis246 = "SELECT passmannRH5_0745 FROM Psychrometer_Assmann0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis246)
			result246 = cursor.fetchone()
			
			for r in result246:
				row246 = r
			
			dis247 = "SELECT passmannRH10_0745 FROM Psychrometer_Assmann0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis247)
			result247 = cursor.fetchone()
			
			for r in result247:
				row247 = r
			
			dis248 = "SELECT passmannRH20_0745 FROM Psychrometer_Assmann0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis248)
			result248 = cursor.fetchone()
			
			for r in result248:
				row248 = r
			
			dis249 = "SELECT passmannRH50_0745 FROM Psychrometer_Assmann0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis249)
			result249 = cursor.fetchone()
			
			for r in result249:
				row249 = r
			
			dis250 = "SELECT passmannRH100_0745 FROM Psychrometer_Assmann0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis250)
			result250 = cursor.fetchone()
			
			for r in result250:
				row250 = r
			
			dis251 = "SELECT passmannRH150_0745 FROM Psychrometer_Assmann0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis251)
			result251 = cursor.fetchone()
			
			for r in result251:
				row251 = r
			
			dis252 = "SELECT passmannRH200_0745 FROM Psychrometer_Assmann0745_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis252)
			result252 = cursor.fetchone()
			
			for r in result252:
				row252 = r
			
			dis253 = "SELECT passmannBK5_1345 FROM Psychrometer_Assmann1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis253)
			result253 = cursor.fetchone()
			
			for r in result253:
				row253 = r
			
			dis254 = "SELECT passmannBK10_1345 FROM Psychrometer_Assmann1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis254)
			result254 = cursor.fetchone()
			
			for r in result254:
				row254 = r
			
			dis255 = "SELECT passmannBK20_1345 FROM Psychrometer_Assmann1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis255)
			result255 = cursor.fetchone()
			
			for r in result255:
				row255 = r
			
			dis256 = "SELECT passmannBK50_1345 FROM Psychrometer_Assmann1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis256)
			result256 = cursor.fetchone()
			
			for r in result256:
				row256 = r
			
			dis257 = "SELECT passmannBK100_1345 FROM Psychrometer_Assmann1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis257)
			result257 = cursor.fetchone()
			
			for r in result257:
				row257 = r
			
			dis258 = "SELECT passmannBK150_1345 FROM Psychrometer_Assmann1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis258)
			result258 = cursor.fetchone()
			
			for r in result258:
				row258 = r
			
			dis259 = "SELECT passmannBK200_1345 FROM Psychrometer_Assmann1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis259)
			result259 = cursor.fetchone()
			
			for r in result259:
				row259 = r
			
			dis260 = "SELECT passmannBB5_1345 FROM Psychrometer_Assmann1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis260)
			result260 = cursor.fetchone()
			
			for r in result260:
				row260 = r
			
			dis261 = "SELECT passmannBB10_1345 FROM Psychrometer_Assmann1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis261)
			result261 = cursor.fetchone()
			
			for r in result261:
				row261 = r
			
			dis262 = "SELECT passmannBB20_1345 FROM Psychrometer_Assmann1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis262)
			result262 = cursor.fetchone()
			
			for r in result262:
				row262 = r
			
			dis263 = "SELECT passmannBB50_1345 FROM Psychrometer_Assmann1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis263)
			result263 = cursor.fetchone()
			
			for r in result263:
				row263 = r
			
			dis264 = "SELECT passmannBB100_1345 FROM Psychrometer_Assmann1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis264)
			result264 = cursor.fetchone()
			
			for r in result264:
				row264 = r
			
			dis265 = "SELECT passmannBB150_1345 FROM Psychrometer_Assmann1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis265)
			result265 = cursor.fetchone()
			
			for r in result265:
				row265 = r
			
			dis266 = "SELECT passmannBB200_1345 FROM Psychrometer_Assmann1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis266)
			result266 = cursor.fetchone()
			
			for r in result266:
				row266 = r
			
			dis267 = "SELECT passmannRH5_1345 FROM Psychrometer_Assmann1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis267)
			result267 = cursor.fetchone()
			
			for r in result267:
				row267 = r
			
			dis268 = "SELECT passmannRH10_1345 FROM Psychrometer_Assmann1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis268)
			result268 = cursor.fetchone()
			
			for r in result268:
				row268 = r
			
			dis269 = "SELECT passmannRH20_1345 FROM Psychrometer_Assmann1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis269)
			result269 = cursor.fetchone()
			
			for r in result269:
				row269 = r
			
			dis270 = "SELECT passmannRH50_1345 FROM Psychrometer_Assmann1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis270)
			result270 = cursor.fetchone()
			
			for r in result270:
				row270 = r
			
			dis271 = "SELECT passmannRH100_1345 FROM Psychrometer_Assmann1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis271)
			result271 = cursor.fetchone()
			
			for r in result271:
				row271 = r
			
			dis272 = "SELECT passmannRH150_1345 FROM Psychrometer_Assmann1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis272)
			result272 = cursor.fetchone()
			
			for r in result272:
				row272 = r
			
			dis273 = "SELECT passmannRH200_1345 FROM Psychrometer_Assmann1345_1 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis273)
			result273 = cursor.fetchone()
			
			for r in result273:
				row273 = r
			
			dis274 = "SELECT passmannBK5_1745 FROM Psychrometer_Assmann1745_2 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis274)
			result274 = cursor.fetchone()
			
			for r in result274:
				row274 = r
			
			dis275 = "SELECT passmannBK10_1745 FROM Psychrometer_Assmann1745_2 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis275)
			result275 = cursor.fetchone()
			
			for r in result275:
				row275 = r
			
			dis276 = "SELECT passmannBK20_1745 FROM Psychrometer_Assmann1745_2 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis276)
			result276 = cursor.fetchone()
			
			for r in result276:
				row276 = r
			
			dis277 = "SELECT passmannBK50_1745 FROM Psychrometer_Assmann1745_2 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis277)
			result277 = cursor.fetchone()
			
			for r in result277:
				row277 = r
			
			dis278 = "SELECT passmannBK100_1745 FROM Psychrometer_Assmann1745_2 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis278)
			result278 = cursor.fetchone()
			
			for r in result278:
				row278 = r
			
			dis279 = "SELECT passmannBK150_1745 FROM Psychrometer_Assmann1745_2 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis279)
			result279 = cursor.fetchone()
			
			for r in result279:
				row279 = r
			
			dis280 = "SELECT passmannBK200_1745 FROM Psychrometer_Assmann1745_2 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis280)
			result280 = cursor.fetchone()
			
			for r in result280:
				row280 = r
			
			dis281 = "SELECT passmannBB5_1745 FROM Psychrometer_Assmann1745_2 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis281)
			result281 = cursor.fetchone()
			
			for r in result281:
				row281 = r
			
			dis282 = "SELECT passmannBB10_1745 FROM Psychrometer_Assmann1745_2 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis282)
			result282 = cursor.fetchone()
			
			for r in result282:
				row282 = r
			
			dis283 = "SELECT passmannBB20_1745 FROM Psychrometer_Assmann1745_2 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis283)
			result283 = cursor.fetchone()
			
			for r in result283:
				row283 = r
			
			dis284 = "SELECT passmannBB50_1745 FROM Psychrometer_Assmann1745_2 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis284)
			result284 = cursor.fetchone()
			
			for r in result284:
				row284 = r
			
			dis285 = "SELECT passmannBB100_1745 FROM Psychrometer_Assmann1745_2 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis285)
			result285 = cursor.fetchone()
			
			for r in result285:
				row285 = r
			
			dis286 = "SELECT passmannBB150_1745 FROM Psychrometer_Assmann1745_2 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis286)
			result286 = cursor.fetchone()
			
			for r in result286:
				row286 = r
			
			dis287 = "SELECT passmannBB200_1745 FROM Psychrometer_Assmann1745_2 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis287)
			result287 = cursor.fetchone()
			
			for r in result287:
				row287 = r
			
			dis288 = "SELECT passmannRH5_1745 FROM Psychrometer_Assmann1745_2 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis288)
			result288 = cursor.fetchone()
			
			for r in result288:
				row288 = r
			
			dis289 = "SELECT passmannRH10_1745 FROM Psychrometer_Assmann1745_2 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis289)
			result289 = cursor.fetchone()
			
			for r in result289:
				row289 = r
			
			dis290 = "SELECT passmannRH20_1745 FROM Psychrometer_Assmann1745_2 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis290)
			result290 = cursor.fetchone()
			
			for r in result290:
				row290 = r
			
			dis291 = "SELECT passmannRH50_1745 FROM Psychrometer_Assmann1745_2 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis291)
			result291 = cursor.fetchone()
			
			for r in result291:
				row291 = r
				
			dis292 = "SELECT passmannRH100_1745 FROM Psychrometer_Assmann1745_2 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis292)
			result292 = cursor.fetchone()
			
			for r in result292:
				row292 = r
			
			dis293 = "SELECT passmannRH150_1745 FROM Psychrometer_Assmann1745_2 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis293)
			result293 = cursor.fetchone()
			
			for r in result293:
				row293 = r
			
			dis294 = "SELECT passmannRH200_1745 FROM Psychrometer_Assmann1745_2 WHERE Waktu = '%s'" % input_tahun_bulan_tanggal.get()
			cursor.execute(dis294)
			result294 = cursor.fetchone()
			
			for r in result294:
				row294 = r
			
		#PMG on Duty
		with con.cursor() as cursor:
			dis298 = "SELECT hari FROM PMGonDuty_Catatan_4 WHERE Waktu = '%s' " % input_tahun_bulan_tanggal.get()
			cursor.execute(dis298)
			result298 = cursor.fetchone()
			
			for r in result298:
				row298 = r
			
			dis299 = "SELECT tanggal FROM PMGonDuty_Catatan_4 WHERE Waktu = '%s' " % input_tahun_bulan_tanggal.get()
			cursor.execute(dis299)
			result299 = cursor.fetchone()
			
			for r in result299:
				row299 = r
			
			dis300 = "SELECT pmg_pagi FROM PMGonDuty_Catatan_4 WHERE Waktu = '%s' " % input_tahun_bulan_tanggal.get()
			cursor.execute(dis300)
			result300 = cursor.fetchone()
			
			for r in result300:
				row300 = r
				
			dis301 = "SELECT pmg_siang FROM PMGonDuty_Catatan_4 WHERE Waktu = '%s' " % input_tahun_bulan_tanggal.get()
			cursor.execute(dis301)
			result301 = cursor.fetchone()
			
			for r in result301:
				row301 = r
			
		"""===================================================== MYSQL ENDS HERE ========================================================"""
		
		'''++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ TABEL AREA PERTAMA ++++++++++++++++++++++++++++++++++++++++++++++++'''
		data = [
			['PSYCHROMETER SANGKAR METEOROLOGI', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47'],
			['Atribut\nPsychrometer', '', '', '', '', '07.15', '', '', '', '', '', '', '', '07.45', '', '', '', '', '', '', '', '13.15', '', '', '', '', '', '', '', '13.45', '', '', '', '', '', '', '', '14.15', '', '', '', '', '', '', '', '', '', '47'],
			['', '', '', '', '', '1.2 m', '', '4 m', '', '7 m', '', '10 m', '', '1.2 m', '', '4 m', '', '7 m', '', '10 m', '', '1.2 m', '', '4 m', '', '7 m', '', '10 m', '', '1.2 m', '', '4 m', '', '7 m', '', '10 m', '', '1.2 m', '', '4 m', '', '7 m', '', '10 m', '', '', '', ''],
			['', '', '', '', '', '1', '', '2', '', '3', '', '4', '', '5', '', '6', '', '7', '', '8', '', '9', '', '10', '', '11', '', '12', '', '13', '', '14', '', '15', '', '16', '', '17', '', '18', '', '19', '', '20', '', '', '', ''],
			['Tbk', '', '', '', '', row1, '', row4, '', row7, '', row10, '', row13, '', row16, '', row19, '', row22, '', row25, '', row28, '', row31, '', row34, '', row37, '', row40, '', row43, '', row46, '', row49, '', row52, '', row55, '', row58, '', '', '', '47'],
			['Tbb', '', '', '', '', row2, '', row5, '', row8, '', row11, '', row14, '', row17, '', row20, '', row23, '', row26, '', row29, '', row32, '', row35, '', row38, '', row41, '', row44, '', row47, '', row50, '', row53, '', row56, '', row59, '', '', '', '47'],
			['RH', '', '', '', '', row3, '', row6, '', row9, '', row12, '', row15, '', row18, '', row21, '', row24, '', row27, '', row30, '', row33, '', row36, '', row39, '', row42, '', row45, '', row48, '', row51, '', row54, '', row57, '', row60, '', '', '', '47'],	
			]

		t=Table(data,48*[0.555*cm], 7*[0.5*cm])
		t.setStyle(TableStyle([('GRID', (0,0), (-1,-1), 0.5, colors.black),
								('BOX', (5,0), (12,6), 1.5, colors.black),
								('BOX', (21,1), (28,6), 1.5, colors.black),
								('BOX', (37,1), (47,6), 1.5, colors.black),
								#garis double
								('LINEABOVE', (0,4), (47,4), 2, colors.black),
								('LINEABOVE', (0,4), (47,4), 1, colors.white),
								('BOX', (0,0), (-1,-1), 1.5, colors.black),
								
								('ALIGN', (0,0), (-1,-1), 'CENTER'),
								('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
								('FONTSIZE', (0,0), (-1,-1), 9),
								('FONTNAME', (0,0), (-1,-1), 'Calibri'),
								
								
								
								#JUDUL
								('SPAN', (0,0), (47,0)),
								('BACKGROUND', (0,0), (47,0), colors.black),
								('TEXTCOLOR', (0,0), (47,0), colors.white),
								
								('BACKGROUND', (5,3), (47,3), colors.gray),
								('FONTSIZE', (5,3), (47,3), 8),
								
								#kolom1
								('SPAN', (0,1), (4,3)), #Atribut Psychro
								('SPAN', (0,4), (4,4)),
								('SPAN', (0,5), (4,5)),
								('SPAN', (0,6), (4,6)),
								
								#kolom2
								('SPAN', (5,1), (12,1)),
								#kolom2 bagian1
								('SPAN', (5,2), (6,2)), #1.2m
								('SPAN', (5,3), (6,3)), #1
								('SPAN', (5,4), (6,4)), #entry mulai dari baris ini
								('SPAN', (5,5), (6,5)),
								('SPAN', (5,6), (6,6)),
								#kolom2 bagian2
								('SPAN', (7,2), (8,2)), #4m
								('SPAN', (7,3), (8,3)), #2
								('SPAN', (7,4), (8,4)), #entry mulai dari baris ini
								('SPAN', (7,5), (8,5)),
								('SPAN', (7,6), (8,6)),
								('SPAN', (9,2), (10,2)), #7m
								('SPAN', (9,3), (10,3)), #3
								('SPAN', (9,4), (10,4)), #entry mulai dari baris ini
								('SPAN', (9,5), (10,5)),
								('SPAN', (9,6), (10,6)),
								('SPAN', (11,2), (12,2)), #10m
								('SPAN', (11,3), (12,3)), #4
								('SPAN', (11,4), (12,4)), #entry mulai dari baris ini
								('SPAN', (11,5), (12,5)),
								('SPAN', (11,6), (12,6)),
								
								#kolom3
								('SPAN', (13,1), (20,1)),
								#kolom3 bagian1
								('SPAN', (13,2), (14,2)), #1.2m
								('SPAN', (13,3), (14,3)), #5
								('SPAN', (13,4), (14,4)), #entry mulai dari baris ini
								('SPAN', (13,5), (14,5)),
								('SPAN', (13,6), (14,6)),
								#kolom3 bagian2
								('SPAN', (15,2), (16,2)), #4m
								('SPAN', (15,3), (16,3)), #6
								('SPAN', (15,4), (16,4)), #entry mulai dari baris ini
								('SPAN', (15,5), (16,5)),
								('SPAN', (15,6), (16,6)),
								#kolom3 bagian3
								('SPAN', (17,2), (18,2)), #7m
								('SPAN', (17,3), (18,3)), #7
								('SPAN', (17,4), (18,4)), #entry mulai dari baris ini
								('SPAN', (17,5), (18,5)),
								('SPAN', (17,6), (18,6)),
								#kolom3 bagian4
								('SPAN', (19,2), (20,2)), #10m
								('SPAN', (19,3), (20,3)), #8
								('SPAN', (19,4), (20,4)), #entry mulai dari baris ini
								('SPAN', (19,5), (20,5)),
								('SPAN', (19,6), (20,6)),
								
								#kolom4
								('SPAN', (21,1), (28,1)),
								#kolom4 bagian1
								('SPAN', (21,2), (22,2)), #1.2m
								('SPAN', (21,3), (22,3)), #9
								('SPAN', (21,4), (22,4)), #entry mulai dari baris ini
								('SPAN', (21,5), (22,5)),
								('SPAN', (21,6), (22,6)),
								#kolom4 bagian2
								('SPAN', (23,2), (24,2)), #4m
								('SPAN', (23,3), (24,3)), #10
								('SPAN', (23,4), (24,4)), #entry mulai dari baris ini
								('SPAN', (23,5), (24,5)),
								('SPAN', (23,6), (24,6)),
								#kolom4 bagian3
								('SPAN', (25,2), (26,2)), #7m
								('SPAN', (25,3), (26,3)), #11
								('SPAN', (25,4), (26,4)), #entry mulai dari baris ini
								('SPAN', (25,5), (26,5)),
								('SPAN', (25,6), (26,6)),
								#kolom4 bagian4
								('SPAN', (27,2), (28,2)), #10m
								('SPAN', (27,3), (28,3)), #12
								('SPAN', (27,4), (28,4)), #entry mulai dari baris ini
								('SPAN', (27,5), (28,5)),
								('SPAN', (27,6), (28,6)),
								
								#kolom5
								('SPAN', (29,1), (36,1)),
								#kolom5 bagian1
								('SPAN', (29,2), (30,2)), #1.2m
								('SPAN', (29,3), (30,3)), #13
								('SPAN', (29,4), (30,4)), #entry mulai dari baris ini
								('SPAN', (29,5), (30,5)),
								('SPAN', (29,6), (30,6)),
								#kolom5 bagian2
								('SPAN', (31,2), (32,2)), #4m
								('SPAN', (31,3), (32,3)), #14
								('SPAN', (31,4), (32,4)), #entry mulai dari baris ini
								('SPAN', (31,5), (32,5)),
								('SPAN', (31,6), (32,6)),
								#kolom5 bagian3
								('SPAN', (33,2), (34,2)), #7m
								('SPAN', (33,3), (34,3)), #15
								('SPAN', (33,4), (34,4)), #entry mulai dari baris ini
								('SPAN', (33,5), (34,5)),
								('SPAN', (33,6), (34,6)),
								#kolom5 bagian4
								('SPAN', (35,2), (36,2)), #10m
								('SPAN', (35,3), (36,3)), #16
								('SPAN', (35,4), (36,4)), #entry mulai dari baris ini
								('SPAN', (35,5), (36,5)),
								('SPAN', (35,6), (36,6)),
								
								#kolom6
								('SPAN', (37,1), (47,1)),
								#kolom6 bagian1
								('SPAN', (37,2), (38,2)), #1.2m
								('SPAN', (37,3), (38,3)), #17
								('SPAN', (37,4), (38,4)), #entry mulai dari baris ini
								('SPAN', (37,5), (38,5)),
								('SPAN', (37,6), (38,6)),
								#kolom6 bagian2
								('SPAN', (39,2), (40,2)), #4m
								('SPAN', (39,3), (40,3)), #18
								('SPAN', (39,4), (40,4)), #entry mulai dari baris ini
								('SPAN', (39,5), (40,5)),
								('SPAN', (39,6), (40,6)),
								#kolom6 bagian3
								('SPAN', (41,2), (42,2)), #7m
								('SPAN', (41,3), (42,3)), #19
								('SPAN', (41,4), (42,4)), #entry mulai dari baris ini
								('SPAN', (41,5), (42,5)),
								('SPAN', (41,6), (42,6)),
								#kolom6 bagian4
								('SPAN', (43,2), (47,2)), #10m
								('SPAN', (43,3), (47,3)), #20
								('SPAN', (43,4), (47,4)), #entry mulai dari baris ini
								('SPAN', (43,5), (47,5)),
								('SPAN', (43,6), (47,6)),
								]))

		t.wrap(width, height)
		elements.append(t)

		'''==================================================================== CELAH ==========================================================='''
		data = [['1', '2', '3']]
		t=Table(data, 3*[1.1*cm], 1*[0.3*cm])
		t.setStyle(TableStyle([('FONTSIZE', (0,0), (-1,-1),  5),
							('TEXTCOLOR', (0,0), (-1,-1), colors.white),
							('ALIGN', (0,0), (-1,-1), 'CENTER'),
							('VALIGN', (0,0), (-1,-1), 'BOTTOM')]))

		t.wrap(width, height)
		elements.append(t)
		'''==================================================================== AKHIR CELAH ====================================================='''

		'''++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ TABEL AREA KEDUA ++++++++++++++++++++++++++++++++++++++++++++++++'''
		data = [
			['PSYCHROMETER SANGKAR METEOROLOGI', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'LAMA PENYINARAN', '', '', '', '', '', '', '', 'TERMOMETER MAKSIMUM DAN MINIMUM', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '47'],
			['Atribut\nPsychrometer', '', '', '', '', '17.45', '', '', '', '', '', '', '', '18.15', '', '', '', '', '', '', '', '', '', 'Waktu', '', 'Jam', '', '%', '', '', '', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47'],
			['', '', '', '', '', '1.2 m', '', '4 m', '', '7 m', '', '10 m', '', '1.2 m', '', '4 m', '', '7 m', '', '10 m', '', '', '', '', '', '29', '', '30', '', '', '', 'Ketinggian', '', '', '', '', '', '', '', '18.15', '', '', '', '14.15', '44', '45', '46', '47'],
			['', '', '', '', '', '21', '', '22', '', '23', '', '24', '', '25', '', '26', '', '27', '', '28', '', '', '', '12 Jam', '', row85, '', row87, '', '', '', '', '', '', '', '', '', '', '', 'Max', '', 'Reset', '', 'Min', '', 'Reset', '', ''],
			['Tbk', '', '', '', '', row61, '', row64, '', row67, '', row70, '', row73, '', row76, '', row79, '', row82, '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '31', '', '32', '', '33', '', '34', '', ''],
			['Tbb', '', '', '', '', row62, '', row65, '', row68, '', row71, '', row74, '', row77, '', row80, '', row83, '', '', '', '8 Jam', '', row86, '', row88, '', '', '', '1.2 meter', '', '', '', '', '', '', '', row89, '', row90, '', row91, '', row92, '', ''],
			['RH', '', '', '', '', row63, '', row66, '', row69, '', row72, '', row75, '', row78, '', row81, '', row84, '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],	
			]
		t=Table(data,48*[0.555*cm], 7*[0.55*cm])
		t.setStyle(TableStyle([	('ALIGN', (0,0), (-1,-1), 'CENTER'),
								('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
								('FONTSIZE', (0,0), (-1,-1), 9),
								('FONTNAME', (0,0), (-1,-1), 'Calibri'),
								
								#'''JUDUL PSYCHROMETER SANGKAR METEOROLOGI'''
								('GRID', (0,0), (20,6), 0.5, colors.black),
								('BOX', (5,1), (12,6), 1.5, colors.black),
								#garis double
								('LINEABOVE', (0,4), (20,4), 2, colors.black),
								('LINEABOVE', (0,4), (20,4), 1, colors.white),
								('BOX', (0,0), (20,6), 1.5, colors.black),
								('SPAN', (0,0), (20,0)),
								('BACKGROUND', (0,0), (20,0), colors.black),
								('TEXTCOLOR', (0,0), (20,0), colors.white),
								('BACKGROUND', (5,3), (20,3), colors.gray),
								('FONTSIZE', (5,3), (20,3), 8),
								
								#kolom1
								('SPAN', (0,1), (4,3)), #Atribut Psychro
								('SPAN', (0,4), (4,4)),
								('SPAN', (0,5), (4,5)),
								('SPAN', (0,6), (4,6)),
								
								#kolom2
								('SPAN', (5,1), (12,1)),
								#kolom2 bagian1
								('SPAN', (5,2), (6,2)), #1.2m
								('SPAN', (5,3), (6,3)), #21
								('SPAN', (5,4), (6,4)), #entry mulai dari baris ini
								('SPAN', (5,5), (6,5)),
								('SPAN', (5,6), (6,6)),
								#kolom2 bagian2
								('SPAN', (7,2), (8,2)), #4m
								('SPAN', (7,3), (8,3)), #22
								('SPAN', (7,4), (8,4)), #entry mulai dari baris ini
								('SPAN', (7,5), (8,5)),
								('SPAN', (7,6), (8,6)),
								('SPAN', (9,2), (10,2)), #7m
								('SPAN', (9,3), (10,3)), #23
								('SPAN', (9,4), (10,4)), #entry mulai dari baris ini
								('SPAN', (9,5), (10,5)),
								('SPAN', (9,6), (10,6)),
								('SPAN', (11,2), (12,2)), #10m
								('SPAN', (11,3), (12,3)), #24
								('SPAN', (11,4), (12,4)), #entry mulai dari baris ini
								('SPAN', (11,5), (12,5)),
								('SPAN', (11,6), (12,6)),
								
								#kolom3
								('SPAN', (13,1), (20,1)),
								#kolom3 bagian1
								('SPAN', (13,2), (14,2)), #1.2m
								('SPAN', (13,3), (14,3)), #25
								('SPAN', (13,4), (14,4)), #entry mulai dari baris ini
								('SPAN', (13,5), (14,5)),
								('SPAN', (13,6), (14,6)),
								#kolom3 bagian2
								('SPAN', (15,2), (16,2)), #4m
								('SPAN', (15,3), (16,3)), #26
								('SPAN', (15,4), (16,4)), #entry mulai dari baris ini
								('SPAN', (15,5), (16,5)),
								('SPAN', (15,6), (16,6)),
								#kolom3 bagian3
								('SPAN', (17,2), (18,2)), #7m
								('SPAN', (17,3), (18,3)), #27
								('SPAN', (17,4), (18,4)), #entry mulai dari baris ini
								('SPAN', (17,5), (18,5)),
								('SPAN', (17,6), (18,6)),
								#kolom3 bagian4
								('SPAN', (19,2), (20,2)), #10m
								('SPAN', (19,3), (20,3)), #28
								('SPAN', (19,4), (20,4)), #entry mulai dari baris ini
								('SPAN', (19,5), (20,5)),
								('SPAN', (19,6), (20,6)),
								
								#'''JUDUL LAMA PENYINARAN'''
								('GRID', (23,0), (28,6), 0.5, colors.black),
								#garis double
								('LINEABOVE', (23,3), (28,3), 2, colors.black),
								('LINEABOVE', (23,3), (28,3), 1, colors.white),
								('BOX', (23,0), (28,6), 1.5, colors.black),
								('SPAN', (23,0), (28,0)),
								('BACKGROUND', (23,0), (28,0), colors.black),
								('TEXTCOLOR', (23,0), (28,0), colors.white),
								('BACKGROUND', (25,2), (28,2), colors.gray),
								('FONTSIZE', (25,2), (28,2), 8),
								#kolom1
								('SPAN', (23,1), (24,2)),
								('SPAN', (23,3), (24,4)),
								('SPAN', (23,5), (24,6)),
								#kolom2
								('SPAN', (25,1), (26,1)),
								('SPAN', (25,2), (26,2)),
								('SPAN', (25,3), (26,4)),
								('SPAN', (25,5), (26,6)),
								#kolom3
								('SPAN', (27,1), (28,1)),
								('SPAN', (27,2), (28,2)),
								('SPAN', (27,3), (28,4)),
								('SPAN', (27,5), (28,6)),
								
								#'''JUDUL TERMOMETER MAKSIMUM DAN MINIMUM'''
								('GRID', (31,0), (47,6), 0.5, colors.black),
								('BOX', (39,2), (42,6), 1.5, colors.black),
								#garis double
								('LINEABOVE', (31,5), (47,5), 2, colors.black),
								('LINEABOVE', (31,5), (47,5), 1, colors.white),
								('BOX', (31,0), (47,6), 1.5, colors.black),
								('SPAN', (31,0), (47,1)),
								('BACKGROUND', (31,0), (47,1), colors.black),
								('TEXTCOLOR', (31,0), (47,1), colors.white),
								('BACKGROUND', (39,4), (47,4), colors.gray),
								('FONTSIZE', (39,4), (47,4), 8),
								#kolom1
								('SPAN', (31,2), (38,4)),
								('SPAN', (31,5), (38,6)),
								#kolom2
								('SPAN', (39,2), (42,2)), #waktu 18.15
								('SPAN', (39,3), (40,3)), #max
								('SPAN', (39,4), (40,4)),
								('SPAN', (39,5), (40,6)), #entry
								('SPAN', (41,3), (42,3)), #reset
								('SPAN', (41,4), (42,4)),
								('SPAN', (41,5), (42,6)),
								#kolom3
								('SPAN', (43,2), (47,2)), #waktu 14.15
								('SPAN', (43,3), (44,3)), #min
								('SPAN', (43,4), (44,4)),
								('SPAN', (43,5), (44,6)), #entry
								('SPAN', (45,3), (47,3)), #reset
								('SPAN', (45,4), (47,4)),
								('SPAN', (45,5), (47,6)),
								]))

		t.wrap(width, height)
		elements.append(t)

		'''==================================================================== CELAH ==========================================================='''
		data = [['1', '2', '3']]
		t=Table(data, 3*[1.1*cm], 1*[0.3*cm])
		t.setStyle(TableStyle([('FONTSIZE', (0,0), (-1,-1),  5),
							('TEXTCOLOR', (0,0), (-1,-1), colors.white),
							('ALIGN', (0,0), (-1,-1), 'CENTER'),
							('VALIGN', (0,0), (-1,-1), 'BOTTOM')]))

		t.wrap(width, height)
		elements.append(t)
		'''==================================================================== AKHIR CELAH ====================================================='''

		'''++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ TABEL AREA KETIGA ++++++++++++++++++++++++++++++++++++++++++++++++'''
		hitung3 = row299[3]
		hitung4 = row299[4]
		if (hitung3==str(0)):
			if(hitung4=="1"):
				Tanggal_pmg_on_duty_pdf = row299[0] + row299[1] + " JANUARI " + row299[6] + row299[7] + row299[8] + row299[9]
			elif(hitung4=="2"):
				Tanggal_pmg_on_duty_pdf = row299[0] + row299[1] + " FEBRUARI " + row299[6] + row299[7] + row299[8] + row299[9]
			elif(hitung4=="3"):
				Tanggal_pmg_on_duty_pdf = row299[0] + row299[1] + " MARET " + row299[6] + row299[7] + row299[8] + row299[9]
			elif(hitung4=="4"):
				Tanggal_pmg_on_duty_pdf = row299[0] + row299[1] + " APRIL " + row299[6] + row299[7] + row299[8] + row299[9]
			elif(hitung4=="5"):
				Tanggal_pmg_on_duty_pdf = row299[0] + row299[1] + " MEI " + row299[6] + row299[7] + row299[8] + row299[9]
			elif(hitung4=="6"):
				Tanggal_pmg_on_duty_pdf = row299[0] + row299[1] + " JUNI " + row299[6] + row299[7] + row299[8] + row299[9]
			elif(hitung4=="7"):
				Tanggal_pmg_on_duty_pdf = row299[0] + row299[1] + " JULI " + row299[6] + row299[7] + row299[8] + row299[9]
			elif(hitung4=="8"):
				Tanggal_pmg_on_duty_pdf = row299[0] + row299[1] + " AGUSTUS " + row299[6] + row299[7] + row299[8] + row299[9]
			elif(hitung4=="9"):
				Tanggal_pmg_on_duty_pdf = row299[0] + row299[1] + " SEPTEMBER " + row299[6] + row299[7] + row299[8] + row299[9]
		elif(hitung3=="1"):
			if(hitung4==str(0)):
				Tanggal_pmg_on_duty_pdf = row299[0] + row299[1] + " OKTOBER " + row299[6] + row299[7] + row299[8] + row299[9]
			elif(hitung4=="1"):
				Tanggal_pmg_on_duty_pdf = row299[0] + row299[1] + " NOVEMBER " + row299[6] + row299[7] + row299[8] + row299[9]
			elif(hitung4=="2"):
				Tanggal_pmg_on_duty_pdf = row299[0] + row299[1] + " DESEMBER " + row299[6] + row299[7] + row299[8] + row299[9]
		else:
			Tanggal_pmg_on_duty_pdf = "Tanggal Salah"
		
		data = [
			['PICHE EVAPORIMETER', '', '', '', '', '', '', '', '', '', '', '', '', 'RADIASI', '', '', '', '', '', '', '', '', '', 'SUHU MIN RUMPUT', '', '', '', '', '', '', '', 'OPEN PAN', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
			['Waktu', '', '', '', '', 'Ketinggian Air di Piche\n1.2 m', '', '', '', '', '', '', '', 'Waktu', '', '', '', 'I', '', '', '', '', '', 'Waktu', '', 'Pembacaan', '', 'Reseting', '', '', '', 'Waktu', '', 'Ketinggian Air\ndi Panci', '', '', '', 'Suhu Air', '', '', '', 'Hujan', '', '', '', 'Penguapan', '', ''],
			['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '36', '', '', '', '', '', '', '', '37', '', '38', '', '', '', '', '', '', '', '', '', 'Max', '', 'Min', '', '', '', '', '', '', '', ''],
			['', '', '', '', '', '35', '', '', '', '', '', '', '', '07.15', '', '', '', row99, '', '', '', '', '', '07.15', '', row100, '', row101, '', '', '', '', '', '39', '', '', '', '40', '', '41', '', '42', '', '', '', '46', '', ''],
			['07.45', '', '', '', '', row93, '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '07.15', '', row106, '', '', '', row110, '', row114, '', '13.5 J', '', '24 J', '', '24 J', '', ''],
			['', '', '', '', '', row94, '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '-', '', '', '', '', '', '', '', row118, '', row119, '', row123, '', ''],
			['13.45', '', '', '', '', row95, '', '', '', '', '', '', '', 'KONDISI CUACA TANAH', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '07.45', '', row107, '', '', '', row111, '', row115, '', '30 Menit', '', '', '', '13.5 Jam', '', ''],
			['', '', '', '', '', row96, '', '', '', '', '', '', '', 'Waktu', '', '', '', 'Kode Tanah', '', '', '', 'Kode Cuaca', '', '', '', '', '', '', '', '', '', '', '', '-', '', '', '', '', '', '', '', row120, '', '', '', row124, '', ''],
			['17.45', '', '', '', '', row97, '', '', '', '', '', '', '', '', '', '', '', '44', '', '', '', '45', '', '', '', '', '', '', '', '', '', '13.45', '', row108, '', '', '', row112, '', row116, '', '6 Jam', '', '', '', '6 Jam', '', ''],
			['', '', '', '', '', row98, '', '', '', '', '', '', '', '07.15', '', '', '', row102, '', '', '', row104, '', '', '', '', '', '', '', '', '', '', '', '-', '', '', '', '', '', '', '', row121, '', '', '', row125, '', ''],
			['', '', '', '', '', '', '', '', '', '', '', '', '', '14.15', '', '', '', row103, '', '', '', row105, '', '', '', '', '', '', '', '', '', '17.45', '', row109, '', '', '', row113, '', row117, '', '4 Jam', '', '', '', '4 Jam', '', ''],
			['BAROMETER', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '-', '', '', '', '', '', '', '', row122, '', '', '', row126, '', ''],
			['', '', '', '', '', '00.00 UTC', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
			['', '', '', '', '', '43', '', '', '', '', '', '', '', 'CATATAN:', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'TANGGAL', '', '', '', '', '', ''],
			['Suhu', '', '', '', '', row127, '', '', '', '', '', '', '', row302, '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
			['Barometer', '', '', '', '', row128, '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', Tanggal_pmg_on_duty_pdf, '', '', '', '', '', ''],
			['QFF', '', '', '', '', row129, '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
			['QFE', '', '', '', '', row130, '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],	
			['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'Halaman 1']
			]

		t=Table(data,48*[0.555*cm], 19*[0.55*cm])
		t.setStyle(TableStyle([('ALIGN', (0,0), (-1,-1), 'CENTER'),
								('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
								('FONTSIZE', (0,0), (-1,-1), 9),
								('FONTNAME', (0,0), (-1,-1), 'Calibri'),
								
								#JUDUL PICHE EVAPORIMETER
								('GRID', (0,0), (10,9), 0.5, colors.black),
								#garis double
								('LINEABOVE', (0,4), (10,4), 2, colors.black),
								('LINEABOVE', (0,4), (10,4), 1, colors.white),
								('BOX', (0,0), (10,9), 1.5, colors.black),
								('SPAN', (0,0), (10,0)),
								('BACKGROUND', (0,0), (10,0), colors.black),
								('TEXTCOLOR', (0,0), (10,0), colors.white),
								('BACKGROUND', (5,3), (10,3), colors.gray),
								('FONTSIZE', (5,3), (10,3), 8),
								#kolom1
								('SPAN', (0,1), (4,3)),
								('SPAN', (0,4), (4,5)),
								('SPAN', (0,6), (4,7)),
								('SPAN', (0,8), (4,9)),
								
								#kolom2
								('SPAN', (5,1), (10,2)),
								('SPAN', (5,3), (10,3)),
								('SPAN', (5,4), (10,4)),
								('SPAN', (5,5), (10,5)),
								('SPAN', (5,6), (10,6)),
								('SPAN', (5,7), (10,7)),
								('SPAN', (5,8), (10,8)),
								('SPAN', (5,9), (10,9)),
								
								#JUDUL BAROMETER
								('GRID', (0,11), (10,17), 0.5, colors.black),
								#garis double
								('LINEABOVE', (0,14), (10,14), 2, colors.black),
								('LINEABOVE', (0,14), (10,14), 1, colors.white),
								('BOX', (0,11), (10,17), 1.5, colors.black),
								('SPAN', (0,11), (10,11)),
								('BACKGROUND', (0,11), (10,11), colors.black),
								('TEXTCOLOR', (0,11), (10,11), colors.white),
								('BACKGROUND', (5,13), (10,13), colors.gray),
								('FONTSIZE', (5,13), (10,13), 8),
								#kolom1
								('SPAN', (0,12), (4,13)),
								('SPAN', (0,14), (4,14)),
								('SPAN', (0,15), (4,15)),
								('SPAN', (0,16), (4,16)),
								('SPAN', (0,17), (4,17)),
								#kolom2
								('SPAN', (5,12), (10,12)),
								('SPAN', (5,13), (10,13)),
								('SPAN', (5,14), (10,14)),
								('SPAN', (5,15), (10,15)),
								('SPAN', (5,16), (10,16)),
								('SPAN', (5,17), (10,17)),
								
								#JUDUL RADIASI
								('GRID', (13,0), (20,4), 0.5, colors.black),
								#garis double
								('LINEABOVE', (13,3), (20,3), 2, colors.black),
								('LINEABOVE', (13,3), (20,3), 1, colors.white),
								('BOX', (13,0), (20,4), 1.5, colors.black),
								('SPAN', (13,0), (20,0)),
								('BACKGROUND', (13,0), (20,0), colors.black),
								('TEXTCOLOR', (13,0), (20,0), colors.white),
								('BACKGROUND', (17,2), (20,2), colors.gray),
								('FONTSIZE', (17,2), (20,2), 8),
								#kolom1
								('SPAN', (13,1), (16,2)),
								('SPAN', (13,3), (16,4)),
								#kolom2
								('SPAN', (17,1), (20,1)),
								('SPAN', (17,2), (20,2)),
								('SPAN', (17,3), (20,4)),
								
								#JUDUL KONDISI CUACA DAN TANAH
								('GRID', (13,6), (24,10), 0.5, colors.black),
								#garis double
								('LINEABOVE', (13,9), (24,9), 2, colors.black),
								('LINEABOVE', (13,9), (24,9), 1, colors.white),
								('BOX', (13,6), (24,10), 1.5, colors.black),
								('SPAN', (13,6), (24,6)),
								('BACKGROUND', (13,6), (24,6), colors.black),
								('TEXTCOLOR', (13,6), (24,6), colors.white),
								('BACKGROUND', (17,8), (24,8), colors.gray),
								('FONTSIZE', (17,8), (24,8), 8),
								#kolom1
								('SPAN', (13,7), (16,8)),
								('SPAN', (13,9), (16,9)),
								('SPAN', (13,10), (16,10)),
								#kolom2
								('SPAN', (17,7), (20,7)),
								('SPAN', (17,8), (20,8)),
								('SPAN', (17,9), (20,9)),
								('SPAN', (17,10), (20,10)),
								#kolom3
								('SPAN', (21,7), (24,7)),
								('SPAN', (21,8), (24,8)),
								('SPAN', (21,9), (24,9)),
								('SPAN', (21,10), (24,10)),
								
								#JUDUL CATATAN
								('GRID', (41,13), (47,17), 1.5, colors.black),
								('BOX', (13,13), (47,17), 1.5, colors.black),
								('SPAN', (13,13), (40,13)),						#catatan:
								('ALIGN', (13,13), (40,13), 'LEFT'),
								('SPAN', (13,14), (40,17)),						#tulis disini
								('ALIGN', (13,14), (40,17), 'LEFT'),
								('VALIGN', (13,14), (40,17), 'TOP'),
								('SPAN', (41,13), (47,14)),						#Tanggal
								('BACKGROUND', (41,13), (47,14), colors.black),
								('TEXTCOLOR', (41,13), (47,14), colors.white),
								('SPAN', (41,15), (47,17)),						#03 oktober 2019
								('FONTSIZE', (41,15), (47,17), 12),
								
								#JUDUL SUHU MIN RUMPUT
								('GRID', (23,0), (28,4), 0.5, colors.black),
								#garis double
								('LINEABOVE', (23,3), (28,3), 2, colors.black),
								('LINEABOVE', (23,3), (28,3), 1, colors.white),
								('BOX', (23,0), (28,4), 1.5, colors.black),
								('SPAN', (23,0), (28,0)),
								('BACKGROUND', (23,0), (28,0), colors.black),
								('TEXTCOLOR', (23,0), (28,0), colors.white),
								('BACKGROUND', (25,2), (28,2), colors.gray),
								('FONTSIZE', (25,2), (28,2), 8),
								#kolom1
								('SPAN', (23,1), (24,2)),
								('SPAN', (23,3), (24,4)),
								#kolom2
								('SPAN', (25,1), (26,1)), #Pembacaan
								('SPAN', (25,2), (26,2)),
								('SPAN', (25,3), (26,4)),
								#kolom3
								('SPAN', (27,1), (28,1)), #Reseting
								('SPAN', (27,2), (28,2)),
								('SPAN', (27,3), (28,4)),
								
								('FONTSIZE', (25,1), (28,1), 6),
								
								#JUDUL OPEN PAN
								('GRID', (31,0), (47,11), 0.5, colors.black),
								#garis double
								('LINEABOVE', (31,4), (47,4), 2, colors.black),
								('LINEABOVE', (31,4), (47,4), 1, colors.white),
								('BOX', (31,0), (47,11), 1.5, colors.black),
								('SPAN', (31,0), (47,0)),
								('BACKGROUND', (31,0), (47,0), colors.black),
								('TEXTCOLOR', (31,0), (47,0), colors.white),
								('BACKGROUND', (33,3), (47,3), colors.gray),
								('FONTSIZE', (33,3), (47,3), 8),
								#kolom1
								('SPAN', (31,1), (32,3)),
								('SPAN', (31,4), (32,5)),
								('SPAN', (31,6), (32,7)),
								('SPAN', (31,8), (32,9)),
								('SPAN', (31,10), (32,11)),
								#kolom2
								('SPAN', (33,1), (36,2)),
								('SPAN', (33,3), (36,3)),
								('SPAN', (33,4), (36,4)),
								('SPAN', (33,5), (36,5)),
								('SPAN', (33,6), (36,6)),
								('SPAN', (33,7), (36,7)),
								('SPAN', (33,8), (36,8)),
								('SPAN', (33,9), (36,9)),
								('SPAN', (33,10), (36,10)),
								('SPAN', (33,11), (36,11)),
								#kolom3
								('SPAN', (37,1), (40,1)),
								#kolom3 bagian1
								('SPAN', (37,2), (38,2)),
								('SPAN', (37,3), (38,3)),
								('SPAN', (37,4), (38,5)),
								('SPAN', (37,6), (38,7)),
								('SPAN', (37,8), (38,9)),
								('SPAN', (37,10), (38,11)),
								#kolom3 bagian2
								('SPAN', (39,2), (40,2)),
								('SPAN', (39,3), (40,3)),
								('SPAN', (39,4), (40,5)),
								('SPAN', (39,6), (40,7)),
								('SPAN', (39,8), (40,9)),
								('SPAN', (39,10), (40,11)),
								#kolom4
								('SPAN', (41,1), (44,2)),
								('SPAN', (41,3), (44,3)),
								('SPAN', (41,4), (42,4)), #13.5 J
								('SPAN', (41,5), (42,5)),
								('SPAN', (43,4), (44,4)), #24 J
								('SPAN', (43,5), (44,5)),
								('SPAN', (41,6), (44,6)), #30 menit
								('SPAN', (41,7), (44,7)),
								('SPAN', (41,8), (44,8)), #6 jam
								('SPAN', (41,9), (44,9)),
								('SPAN', (41,10), (44,10)), #4 jam
								('SPAN', (41,11), (44,11)),
								#kolom5
								('SPAN', (45,1), (47,2)),
								('SPAN', (45,3), (47,3)),
								('SPAN', (45,4), (47,4)), #24 J
								('SPAN', (45,5), (47,5)),
								('SPAN', (45,6), (47,6)), #13.5 Jam
								('SPAN', (45,7), (47,7)),
								('SPAN', (45,8), (47,8)), #6 jam
								('SPAN', (45,9), (47,9)),
								('SPAN', (45,10), (47,10)), #4 jam
								('SPAN', (45,11), (47,11)),
								
								#HALAMAN1
								('ALIGN', (47,18), (47,18), 'RIGHT'),
								]))

		t.wrap(width, height)
		elements.append(t)
		'''==================================================================== CELAH KETIGA HALAMAN 1 ==========================================================='''
		data = [['1', '2', '3']]
		t=Table(data, 3*[1.1*cm], 1*[0.3*cm])
		t.setStyle(TableStyle([('FONTSIZE', (0,0), (-1,-1),  5),
							('TEXTCOLOR', (0,0), (-1,-1), colors.white),
							('ALIGN', (0,0), (-1,-1), 'CENTER'),
							('VALIGN', (0,0), (-1,-1), 'BOTTOM'),
							]))
							

		t.wrap(width, height)
		elements.append(t)
		'''==================================================================== AKHIR CELAH KETIGA HALAMAN 1 ====================================================='''

		'''++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ TABEL AREA PERTAMA HALAMAN 2 ++++++++++++++++++++++++++++++++++++++++++++++++'''
		data = [
			['ANGIN', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
			['Waktu', '', '', '', '', 'Ketinggian Anemometer', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
			['', '', '', '', '', '0.5 m', '', '', '', '', '', '2 m', '', '', '', '', '', '4 m', '', '', '', '', '', '', '', '', '', '7 m', '', '', '', '', '', '', '', '', '', '10 m', '', '', '', '', '', '', '', '', '', ''],
			['', '', '', '', '', 'Cup Counter', '', '', '', '', '', 'Cup Counter', '', '', '', '', '', 'Arah', '', '', '', 'Kecepatan', '', '', '', '', '', 'Arah', '', '', '', 'Kecepatan', '', '', '', '', '', 'Arah', '', '', '', 'Kecepatan', '', '', '', '', '', ''],
			['', '', '', '', '', '1', '', '', '', '', '', '2', '', '', '', '', '', '3', '', '', '', '4', '', '', '', '', '', '5', '', '', '', '6', '', '', '', '', '', '7', '', '', '', '8', '', '', '', '', '', ''],
			['07.15', '', '', '', '', row131, '', '', '', '', '', row137, '', '', '', '', '', row143, '', '', '', row149, '', '', '', '', '', row155, '', '', '', row161, '', '', '', '', '', row167, '', '', '', row173, '', '', '', '', '', ''],
			['07.45', '', '', '', '', row132, '', '', '', '', '', row138, '', '', '', '', '', row144, '', '', '', row150, '', '', '', '', '', row156, '', '', '', row162, '', '', '', '', '', row168, '', '', '', row174, '', '', '', '', '', ''],
			['13.45', '', '', '', '', row133, '', '', '', '', '', row139, '', '', '', '', '', row145, '', '', '', row151, '', '', '', '', '', row157, '', '', '', row163, '', '', '', '', '', row169, '', '', '', row175, '', '', '', '', '', ''],
			['14.15', '', '', '', '', row134, '', '', '', '', '', row140, '', '', '', '', '', row146, '', '', '', row152, '', '', '', '', '', row158, '', '', '', row164, '', '', '', '', '', row170, '', '', '', row176, '', '', '', '', '', ''],
			['17.45', '', '', '', '', row135, '', '', '', '', '', row141, '', '', '', '', '', row147, '', '', '', row153, '', '', '', '', '', row159, '', '', '', row165, '', '', '', '', '', row171, '', '', '', row177, '', '', '', '', '', ''],
			['18.15', '', '', '', '', row136, '', '', '', '', '', row142, '', '', '', '', '', row148, '', '', '', row154, '', '', '', '', '', row160, '', '', '', row166, '', '', '', '', '', row172, '', '', '', row178, '', '', '', '', '', ''],
			]

		t=Table(data,48*[0.555*cm], 11*[0.5*cm])
		t.setStyle(TableStyle([	('ALIGN', (0,0), (-1,-1), 'CENTER'),
								('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
								('FONTSIZE', (0,0), (-1,-1), 9),
								('FONTNAME', (0,0), (-1,-1), 'Calibri'),
								('BACKGROUND', (0,0), (47,0), colors.black),
								('TEXTCOLOR', (0,0), (47,0), colors.white),
								('BACKGROUND', (5,4), (47,4), colors.gray),
								('FONTSIZE', (5,4), (47,4), 8),
								
								('GRID', (0,0), (-1,-1), 0.5, colors.black),
								('BOX', (5,1), (47,1), 1.5, colors.black),
								('BOX', (5,2), (10,10), 1.5, colors.black),
								('BOX', (17,2), (26,10), 1.5, colors.black),
								('BOX', (37,2), (47,10), 1.5, colors.black),
								
								('LINEABOVE', (0,5), (47,5), 2, colors.black),
								('LINEABOVE', (0,5), (47,5), 1, colors.white),
								('BOX', (0,0), (-1,-1), 1.5, colors.black),
								
								#JUDUL
								('SPAN', (0,0), (47,0)), #Angin
								('SPAN', (5,1), (47,1)), #Ketinggian Anemometer
								#kolom1
								('SPAN', (0,1), (4,4)),
								('SPAN', (0,5), (4,5)),
								('SPAN', (0,6), (4,6)),
								('SPAN', (0,7), (4,7)),
								('SPAN', (0,8), (4,8)),
								('SPAN', (0,9), (4,9)),
								('SPAN', (0,10), (4,10)),
								
								#kolom2 cup counter 0.5 m
								('SPAN', (5,2), (10,2)), #0.5 m
								('SPAN', (5,3), (10,3)), #cup counter
								('SPAN', (5,4), (10,4)), # 1
								('SPAN', (5,5), (10,5)),
								('SPAN', (5,6), (10,6)),
								('SPAN', (5,7), (10,7)),
								('SPAN', (5,8), (10,8)),
								('SPAN', (5,9), (10,9)),
								('SPAN', (5,10), (10,10)),
								
								#kolom2 cup counter 2 m
								('SPAN', (11,2), (16,2)), #2 m
								('SPAN', (11,3), (16,3)), #cup counter
								('SPAN', (11,4), (16,4)), # 2
								('SPAN', (11,5), (16,5)),
								('SPAN', (11,6), (16,6)),
								('SPAN', (11,7), (16,7)),
								('SPAN', (11,8), (16,8)),
								('SPAN', (11,9), (16,9)),
								('SPAN', (11,10), (16,10)),
								
								#kolom3 ANGIN 4m
								('SPAN', (17,2), (26,2)), #4m
								#kolom3 arah
								('SPAN', (17,3), (20,3)), #arah
								('SPAN', (17,4), (20,4)), #3
								('SPAN', (17,5), (20,5)),
								('SPAN', (17,6), (20,6)),
								('SPAN', (17,7), (20,7)),
								('SPAN', (17,8), (20,8)),
								('SPAN', (17,9), (20,9)),
								('SPAN', (17,10), (20,10)),
								#kolom3 kecepatan
								('SPAN', (21,3), (26,3)), #kecepatan
								('SPAN', (21,4), (26,4)), #4
								('SPAN', (21,5), (26,5)),
								('SPAN', (21,6), (26,6)),
								('SPAN', (21,7), (26,7)),
								('SPAN', (21,8), (26,8)),
								('SPAN', (21,9), (26,9)),
								('SPAN', (21,10), (26,10)),
								
								#kolom4 ANGIN 7m
								('SPAN', (27,2), (36,2)), #7m
								#kolom4 arah
								('SPAN', (27,3), (30,3)), #arah
								('SPAN', (27,4), (30,4)), #5
								('SPAN', (27,5), (30,5)),
								('SPAN', (27,6), (30,6)),
								('SPAN', (27,7), (30,7)),
								('SPAN', (27,8), (30,8)),
								('SPAN', (27,9), (30,9)),
								('SPAN', (27,10), (30,10)),
								#kolom4 kecepatan
								('SPAN', (31,3), (36,3)), #kecepatan
								('SPAN', (31,4), (36,4)), #6
								('SPAN', (31,5), (36,5)),
								('SPAN', (31,6), (36,6)),
								('SPAN', (31,7), (36,7)),
								('SPAN', (31,8), (36,8)),
								('SPAN', (31,9), (36,9)),
								('SPAN', (31,10), (36,10)),
								
								#kolom5 ANGIN 10m
								('SPAN', (37,2), (47,2)), #10m
								#kolom5 arah
								('SPAN', (37,3), (40,3)), #arah
								('SPAN', (37,4), (40,4)), #7
								('SPAN', (37,5), (40,5)),
								('SPAN', (37,6), (40,6)),
								('SPAN', (37,7), (40,7)),
								('SPAN', (37,8), (40,8)),
								('SPAN', (37,9), (40,9)),
								('SPAN', (37,10), (40,10)),
								#kolom5 kecepatan
								('SPAN', (41,3), (47,3)), #kecepatan
								('SPAN', (41,4), (47,4)), #8
								('SPAN', (41,5), (47,5)),
								('SPAN', (41,6), (47,6)),
								('SPAN', (41,7), (47,7)),
								('SPAN', (41,8), (47,8)),
								('SPAN', (41,9), (47,9)),
								('SPAN', (41,10), (47,10)),
								]))

		t.wrap(width, height)
		elements.append(t)
		'''==================================================================== CELAH PERTAMA HALAMAN 2==========================================================='''
		data = [['1', '2', '3']]
		t=Table(data, 3*[1.1*cm], 1*[0.3*cm])
		t.setStyle(TableStyle([('FONTSIZE', (0,0), (-1,-1),  5),
							('TEXTCOLOR', (0,0), (-1,-1), colors.white),
							('ALIGN', (0,0), (-1,-1), 'CENTER'),
							('VALIGN', (0,0), (-1,-1), 'BOTTOM')]))

		t.wrap(width, height)
		elements.append(t)
		'''==================================================================== AKHIR CELAH PERTAMA HALAMAN 2 ====================================================='''
		'''++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ TABEL AREA KEDUA HALAMAN 2 ++++++++++++++++++++++++++++++++++++++++++++++++'''
		inputan_curah_17_15 = row229
		CURAH_PER_17_15 = 'Jumlah Curah Hujan per Jam 17.15 : ' + inputan_curah_17_15
		inputan_nama_tan_komo = row230
		NAMA_TAN_KOMO = 'Nama Tanaman Komoditi : ' + inputan_nama_tan_komo
		data = [
			['SUHU TANAH', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'LYSIMETER', '', '', '', '', '', '', '', '', '', '', '', ''],
			['Kedalaman', '', '', '', '', '07.45', '', '', '', '', '', '', '', '13.45', '', '', '', '', '', '', '', '14.15', '', '', '', '', '', '', '', '17.45', '', '', '', '', '', 'Tanah Gundul', '', '', '', 'Tanaman Komoditi', '', '', '', 'Tanah Berumput', '', '', '', ''],
			['', '', '', '', '', 'Berumput', '', '', '', 'Gundul', '', '', '', 'Berumput', '', '', '', 'Gundul', '', '', '', 'Berumput', '', '', '', 'Gundul', '', '', '', 'Berumput', '', 'Gundul', '', '', '', 'Siram', '', 'Keluar', '', 'Siram', '', 'Keluar', '', 'Siram', '', 'Keluar', '', ''],
			['', '', '', '', '', '9', '', '', '', '10', '', '', '', '11', '', '', '', '12', '', '', '', '13', '', '', '', '14', '', '', '', '15', '', '16', '', '', '', '17', '', '18', '', '19', '', '20', '', '21', '', '22', '', ''],
			['0 cm', '', '', '', '', row179, '', '', '', row184, '', '', '', row189, '', '', '', row194, '', '', '', row199, '', '', '', row204, '', '', '', row209, '', row216, '', '', '', row223, '', row224, '', row225, '', row226, '', row227, '', row228, '', ''],
			['2 cm', '', '', '', '', row180, '', '', '', row185, '', '', '', row190, '', '', '', row195, '', '', '', row200, '', '', '', row205, '', '', '', row210, '', row217, '', '', '', CURAH_PER_17_15, '', '', '', '', '', '', '', '', '', '', '', ''],
			['5 cm', '', '', '', '', row181, '', '', '', row186, '', '', '', row191, '', '', '', row196, '', '', '', row201, '', '', '', row206, '', '', '', row211, '', row218, '', '', '', NAMA_TAN_KOMO, '', '', '', '', '', '', '', '', '', '', '', ''],
			['10 cm', '', '', '', '', row182, '', '', '', row187, '', '', '', row192, '', '', '', row197, '', '', '', row202, '', '', '', row207, '', '', '', row212, '', row219, '', '', '', 'Keterangan Fase :', '', '', '', '', '', row231, '', '', '', '', '', ''],
			['20 cm', '', '', '', '', row183, '', '', '', row188, '', '', '', row193, '', '', '', row198, '', '', '', row203, '', '', '', row208, '', '', '', row213, '', row220, '', '', '', '', '', '', '', '', '', row295, '', '', '', '_', '', ''],
			['50 cm', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', row214, '', row221, '', '', '', 'Digital:', '', row297, '', '', '', '', '', row296, '', 'mm', '', ''],
			['100 cm', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', row215, '', row222, '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
			]

		t=Table(data,48*[0.555*cm], 11*[0.5*cm])
		t.setStyle(TableStyle([	('ALIGN', (0,0), (-1,-1), 'CENTER'),
								('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
								('FONTSIZE', (0,0), (-1,-1), 9),
								('FONTNAME', (0,0), (-1,-1), 'Calibri'),
								
								#DETAIL SUHU TANAH
								('BACKGROUND', (0,0), (32,0), colors.black),
								('TEXTCOLOR', (0,0), (32,0), colors.white),
								('BACKGROUND', (5,3), (32,3), colors.gray),
								('FONTSIZE', (5,3), (32,3), 8),
								
								('GRID', (0,0), (32,10), 0.5, colors.black),
								('BOX', (0,1), (4,10), 1.5, colors.black),
								('BOX', (13,1), (20,8), 1.5, colors.black),
								('BOX', (29,1), (32,10), 1.5, colors.black),
								
								('LINEABOVE', (5,9), (28,9), 1.5, colors.black),
								#garis2
								('LINEABOVE', (0,4), (32,4), 2, colors.black),
								('LINEABOVE', (0,4), (32,4), 1, colors.white),
								('BOX', (0,0), (32,10), 1.5, colors.black),
								
								#JUDUL SUHU TANAH
								('SPAN', (0,0), (32,0)), #Angin
								#kolom1 suhu tanah
								('SPAN', (0,1), (4,3)), #kedalaman
								('SPAN', (0,4), (4,4)),
								('SPAN', (0,5), (4,5)),
								('SPAN', (0,6), (4,6)),
								('SPAN', (0,7), (4,7)),
								('SPAN', (0,8), (4,8)),
								('SPAN', (0,9), (4,9)),
								('SPAN', (0,10), (4,10)),
								
								#kolom2 07.45
								('SPAN', (5,1), (12,1)), #07.45
								#kolom2 berumput
								('SPAN', (5,2), (8,2)), #berumput
								('SPAN', (5,3), (8,3)), #9
								('SPAN', (5,4), (8,4)),
								('SPAN', (5,5), (8,5)),
								('SPAN', (5,6), (8,6)),
								('SPAN', (5,7), (8,7)),
								('SPAN', (5,8), (8,8)),
								#kolom2 gundul
								('SPAN', (9,2), (12,2)), #gundul
								('SPAN', (9,3), (12,3)), #10
								('SPAN', (9,4), (12,4)),
								('SPAN', (9,5), (12,5)),
								('SPAN', (9,6), (12,6)),
								('SPAN', (9,7), (12,7)),
								('SPAN', (9,8), (12,8)),
								
								#kolom3 13.45
								('SPAN', (13,1), (20,1)), #13.45
								#kolom3 berumput
								('SPAN', (13,2), (16,2)), #berumput
								('SPAN', (13,3), (16,3)), #11
								('SPAN', (13,4), (16,4)),
								('SPAN', (13,5), (16,5)),
								('SPAN', (13,6), (16,6)),
								('SPAN', (13,7), (16,7)),
								('SPAN', (13,8), (16,8)),
								#kolom3 gundul
								('SPAN', (17,2), (20,2)), #gundul
								('SPAN', (17,3), (20,3)), #12
								('SPAN', (17,4), (20,4)),
								('SPAN', (17,5), (20,5)),
								('SPAN', (17,6), (20,6)),
								('SPAN', (17,7), (20,7)),
								('SPAN', (17,8), (20,8)),
								
								#kolom4 14.15
								('SPAN', (21,1), (28,1)), #14.15
								#kolom4 berumput
								('SPAN', (21,2), (24,2)), #berumput
								('SPAN', (21,3), (24,3)), #13
								('SPAN', (21,4), (24,4)),
								('SPAN', (21,5), (24,5)),
								('SPAN', (21,6), (24,6)),
								('SPAN', (21,7), (24,7)),
								('SPAN', (21,8), (24,8)),
								#kolom4 gundul
								('SPAN', (25,2), (28,2)), #gundul
								('SPAN', (25,3), (28,3)), #14
								('SPAN', (25,4), (28,4)),
								('SPAN', (25,5), (28,5)),
								('SPAN', (25,6), (28,6)),
								('SPAN', (25,7), (28,7)),
								('SPAN', (25,8), (28,8)),
								
								#kolom5 suhu tanah 17.45
								('SPAN', (29,1), (32,1)), #17.45
								#berumput
								('SPAN', (29,2), (30,2)), #berumput
								('SPAN', (29,3), (30,3)), #15
								('SPAN', (29,4), (30,4)),
								('SPAN', (29,5), (30,5)),
								('SPAN', (29,6), (30,6)),
								('SPAN', (29,7), (30,7)),
								('SPAN', (29,8), (30,8)),
								('SPAN', (29,9), (30,9)),
								('SPAN', (29,10), (30,10)),
								#gundul
								('SPAN', (31,2), (32,2)), #gundul
								('SPAN', (31,3), (32,3)), #16
								('SPAN', (31,4), (32,4)),
								('SPAN', (31,5), (32,5)),
								('SPAN', (31,6), (32,6)),
								('SPAN', (31,7), (32,7)),
								('SPAN', (31,8), (32,8)),
								('SPAN', (31,9), (32,9)),
								('SPAN', (31,10), (32,10)),
								
								('FONTSIZE', (29,2), (32,2), 7),
								
								#BLANK SPACE
								('SPAN', (5,9), (28,10)),
								('BACKGROUND', (5,9), (28,10), colors.lightgrey),
								
								#DETAIL LYSIMETER
								('BACKGROUND', (35,0), (47,0), colors.black),
								('TEXTCOLOR', (35,0), (47,0), colors.white),
								('BACKGROUND', (35,3), (47,3), colors.gray),
								('FONTSIZE', (35,3), (47,3), 8),
								('BACKGROUND', (35,4), (42,4), colors.lightgrey),
								
								('GRID', (35,1), (47,5), 0.5, colors.black),
								#garis2
								('LINEABOVE', (35,4), (47,4), 2, colors.black),
								('LINEABOVE', (35,4), (47,4), 1, colors.white),
								('BOX', (35,0), (47,10), 1.5, colors.black),
								
								#JUDUL LYSIMETER
								('SPAN', (35,0), (47,0)),
								#KOLOM1 TANAH GUNDUL
								('SPAN', (35,1), (38,1)),
								#kolom1 siram
								('SPAN', (35,2), (36,2)),
								('SPAN', (35,3), (36,3)),
								('SPAN', (35,4), (36,4)),
								#kolom1 keluar
								('SPAN', (37,2), (38,2)),
								('SPAN', (37,3), (38,3)),
								('SPAN', (37,4), (38,4)),
								#kKOLOM2 TANAMAN KOMODITI
								('SPAN', (39,1), (42,1)),
								#kolom2 siram
								('SPAN', (39,2), (40,2)),
								('SPAN', (39,3), (40,3)),
								('SPAN', (39,4), (40,4)),
								#kolom2 keluar
								('SPAN', (41,2), (42,2)),
								('SPAN', (41,3), (42,3)),
								('SPAN', (41,4), (42,4)),
								#kKOLOM3 TANAH BERUMPUT
								('SPAN', (43,1), (47,1)),
								#kolom3 siram
								('SPAN', (43,2), (44,2)),
								('SPAN', (43,3), (44,3)),
								('SPAN', (43,4), (44,4)),
								#kolom3 keluar
								('SPAN', (45,2), (47,2)),
								('SPAN', (45,3), (47,3)),
								('SPAN', (45,4), (47,4)),
								
								('FONTSIZE', (35,1), (47,1), 7),
								
								#Jumlah curah Hujan per Jam 17.15
								('SPAN', (35,5), (47,5)),
								('ALIGN', (35,5), (47,6), 'LEFT'),
								#Nama Tanaman Komoditi
								('SPAN', (35,6), (47,6)),
								#Keterangan Fase
								('SPAN', (35,7), (40,7)),
								('ALIGN', (35,7), (40,7), 'LEFT'),
								#Keterangan Fase isian bagian atas
								('SPAN', (41,7), (44,7)),
								('ALIGN', (41,7), (44,9), 'RIGHT'),
								#Keterangan Fase isian bagian bawah
								('SPAN', (41,8), (44,8)),
								#Keterangan Fase isian bagian hasil
								('SPAN', (43,9), (44,9)),
								('LINEABOVE', (41,9), (44,9), 1.5, colors.black),
								
								('SPAN', (45,9), (46,9)), #mm
								('ALIGN', (45,8), (46,9), 'LEFT'),
								
								#BOX DIGITAL
								('BOX', (35,8), (38,10), 0.5, colors.black),
								('SPAN', (35,9), (36,9)), #Digital:
								('SPAN', (37,9), (38,9)), #isian atas
								('SPAN', (37,10), (38,10)), #isian bawah
								('ALIGN', (37,9), (38,10), 'RIGHT'),
								('LINEABOVE', (37,10), (38,10), 1.5, colors.black),
								]))

		t.wrap(width, height)
		elements.append(t)
		'''==================================================================== CELAH KEDUA HALAMAN 2 ==========================================================='''
		data = [['', '', '']]
		t=Table(data, 3*[1.1*cm], 1*[0.3*cm])
		t.setStyle(TableStyle([('FONTSIZE', (0,0), (-1,-1),  5),
							('TEXTCOLOR', (0,0), (-1,-1), colors.white),
							('ALIGN', (0,0), (-1,-1), 'CENTER'),
							('VALIGN', (0,0), (-1,-1), 'BOTTOM')]))

		t.wrap(width, height)
		elements.append(t)
		'''==================================================================== AKHIR CELAH KEDUA HALAMAN 2 ====================================================='''
		'''++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ TABEL AREA KETIGA HALAMAN 2 ++++++++++++++++++++++++++++++++++++++++++++++++'''
		inputan_hari = row298
		HARI = 'Hari : ' + inputan_hari
		inputan_tanggal = row299
		TANGGAL = 'Tanggal : ' + inputan_tanggal
		data = [
			['PSYCHROMETER ASSMANN', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'PMG ON DUTY', '', '', '', '', '', '', '', '', '', '', '', ''],
			['Tinggi', '', '', '', '', '07.45', '', '', '', '', '', '', '', '13.45', '', '', '', '', '', '', '', '', '', '17.45', '', '', '', '', '', '', '', '', '', '', '', HARI, '', '', '', '', '', TANGGAL, '', '', '', '', '', ''],
			['', '', '', '', '', 'BK', '', 'BB', '', 'RH', '', '', '', 'BK', '', 'BB', '', 'RH', '', '', '', '', '', 'BK', '', 'BB', '', 'RH', '', '', '', '', '', '', '', 'DUTY ON', '', '', '', 'NAMA', '', '', '', 'PARAF', '', '', '', ''],
			['', '', '', '', '', '23', '', '24', '', '25', '', '', '', '26', '', '27', '', '28', '', '', '', '', '', '29', '', '30', '', '31', '', '', '', '', '', '', '', '32', '', '', '', '33', '', '', '', '34', '', '', '', ''],
			['5 cm', '', '', '', '', row232, '', row239, '', row246, '', '', '', row253, '', row260, '', row267, '', '', '', '', '', row274, '', row281, '', row288, '', '', '', '', '', '', '', 'Pagi', '', '', '', row300, '', '', '', '', '', '', '', ''],
			['10 cm', '', '', '', '', row233, '', row240, '', row247, '', '', '', row254, '', row261, '', row268, '', '', '', '', '', row275, '', row282, '', row289, '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
			['20 cm', '', '', '', '', row234, '', row241, '', row248, '', '', '', row255, '', row262, '', row269, '', '', '', '', '', row276, '', row283, '', row290, '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
			['50 cm', '', '', '', '', row235, '', row242, '', row249, '', '', '', row256, '', row263, '', row270, '', '', '', '', '', row277, '', row284, '', row291, '', '', '', '', '', '', '', 'Siang', '', '', '', row301, '', '', '', '', '', '', '', ''],
			['100 cm', '', '', '', '', row236, '', row243, '', row250, '', '', '', row257, '', row264, '', row271, '', '', '', '', '', row278, '', row285, '', row292, '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
			['150 cm', '', '', '', '', row237, '', row244, '', row251, '', '', '', row258, '', row265, '', row272, '', '', '', '', '', row279, '', row286, '', row293, '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
			['200 cm', '', '', '', '', row238, '', row245, '', row252, '', '', '', row259, '', row266, '', row273, '', '', '', '', '', row280, '', row287, '', row294, '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
			['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'Halaman 2', '', '', '', '']
			]

		t=Table(data,48*[0.555*cm], 12*[0.5*cm])
		t.setStyle(TableStyle([	('ALIGN', (0,0), (-1,-1), 'CENTER'),
								('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
								('FONTSIZE', (0,0), (-1,-1), 9),
								('FONTNAME', (0,0), (-1,-1), 'Calibri'),
								
								#PSYCHROMETER ASSMANN DETAIL
								('BACKGROUND', (0,0), (32,0), colors.black),
								('TEXTCOLOR', (0,0), (32,0), colors.white),
								('BACKGROUND', (5,3), (32,3), colors.gray),
								('FONTSIZE', (5,3), (32,3), 8),
								
								('GRID', (0,0), (32,10), 0.5, colors.black),
								('BOX', (5,1), (12,10), 1.5, colors.black),
								('BOX', (23,1), (32,10), 1.5, colors.black),

								#garis2
								('LINEABOVE', (0,4), (32,4), 2, colors.black),
								('LINEABOVE', (0,4), (32,4), 1, colors.white),
								('BOX', (0,0), (32,10), 1.5, colors.black),
								
								#JUDUL PSYCHROMETER ASSMANN
								('SPAN', (0,0), (32,0)),
								#kolom1
								('SPAN', (0,1), (4,3)), #tinggi
								('SPAN', (0,4), (4,4)),
								('SPAN', (0,5), (4,5)),
								('SPAN', (0,6), (4,6)),
								('SPAN', (0,7), (4,7)),
								('SPAN', (0,8), (4,8)),
								('SPAN', (0,9), (4,9)),
								('SPAN', (0,10), (4,10)),
								
								#kolom2 psychro assmann 07.45
								('SPAN', (5,1), (12,1)), #07.45
								#kolom2 bagian1 BK assmann
								('SPAN', (5,2), (6,2)), #BK
								('SPAN', (5,3), (6,3)), #23
								('SPAN', (5,4), (6,4)),
								('SPAN', (5,5), (6,5)),
								('SPAN', (5,6), (6,6)),
								('SPAN', (5,7), (6,7)),
								('SPAN', (5,8), (6,8)),
								('SPAN', (5,9), (6,9)),
								('SPAN', (5,10), (6,10)),
								#kolom2 bagian2 BB assmann
								('SPAN', (7,2), (8,2)), #BB
								('SPAN', (7,3), (8,3)), #24
								('SPAN', (7,4), (8,4)),
								('SPAN', (7,5), (8,5)),
								('SPAN', (7,6), (8,6)),
								('SPAN', (7,7), (8,7)),
								('SPAN', (7,8), (8,8)),
								('SPAN', (7,9), (8,9)),
								('SPAN', (7,10), (8,10)),
								#kolom2 bagian3 RH assmann
								('SPAN', (9,2), (12,2)), #RH
								('SPAN', (9,3), (12,3)), #25
								('SPAN', (9,4), (12,4)),
								('SPAN', (9,5), (12,5)),
								('SPAN', (9,6), (12,6)),
								('SPAN', (9,7), (12,7)),
								('SPAN', (9,8), (12,8)),
								('SPAN', (9,9), (12,9)),
								('SPAN', (9,10), (12,10)),
								
								#kolom3 psychro assmann 13.45
								('SPAN', (13,1), (22,1)), #13.45
								#kolom3 bagian1 BK assmann
								('SPAN', (13,2), (14,2)), #BK
								('SPAN', (13,3), (14,3)), #26
								('SPAN', (13,4), (14,4)),
								('SPAN', (13,5), (14,5)),
								('SPAN', (13,6), (14,6)),
								('SPAN', (13,7), (14,7)),
								('SPAN', (13,8), (14,8)),
								('SPAN', (13,9), (14,9)),
								('SPAN', (13,10), (14,10)),
								#kolom3 bagian2 BB assmann
								('SPAN', (15,2), (16,2)), #BB
								('SPAN', (15,3), (16,3)), #27
								('SPAN', (15,4), (16,4)),
								('SPAN', (15,5), (16,5)),
								('SPAN', (15,6), (16,6)),
								('SPAN', (15,7), (16,7)),
								('SPAN', (15,8), (16,8)),
								('SPAN', (15,9), (16,9)),
								('SPAN', (15,10), (16,10)),
								#kolom3 bagian3 RH assmann
								('SPAN', (17,2), (22,2)), #RH
								('SPAN', (17,3), (22,3)), #28
								('SPAN', (17,4), (22,4)),
								('SPAN', (17,5), (22,5)),
								('SPAN', (17,6), (22,6)),
								('SPAN', (17,7), (22,7)),
								('SPAN', (17,8), (22,8)),
								('SPAN', (17,9), (22,9)),
								('SPAN', (17,10), (22,10)),
								
								#kolom4 psychro assmann 17.45
								('SPAN', (23,1), (32,1)), #17.45
								#kolom4 bagian1 BK assmann
								('SPAN', (23,2), (24,2)), #BK
								('SPAN', (23,3), (24,3)), #29
								('SPAN', (23,4), (24,4)),
								('SPAN', (23,5), (24,5)),
								('SPAN', (23,6), (24,6)),
								('SPAN', (23,7), (24,7)),
								('SPAN', (23,8), (24,8)),
								('SPAN', (23,9), (24,9)),
								('SPAN', (23,10), (24,10)),
								#kolom4 bagian2 BB assmann
								('SPAN', (25,2), (26,2)), #BB
								('SPAN', (25,3), (26,3)), #30
								('SPAN', (25,4), (26,4)),
								('SPAN', (25,5), (26,5)),
								('SPAN', (25,6), (26,6)),
								('SPAN', (25,7), (26,7)),
								('SPAN', (25,8), (26,8)),
								('SPAN', (25,9), (26,9)),
								('SPAN', (25,10), (26,10)),
								#kolom4 bagian3 RH assmann
								('SPAN', (27,2), (32,2)), #RH
								('SPAN', (27,3), (32,3)), #31
								('SPAN', (27,4), (32,4)),
								('SPAN', (27,5), (32,5)),
								('SPAN', (27,6), (32,6)),
								('SPAN', (27,7), (32,7)),
								('SPAN', (27,8), (32,8)),
								('SPAN', (27,9), (32,9)),
								('SPAN', (27,10), (32,10)),
								
								#PMG ON DUTY DETAIL
								('BACKGROUND', (35,0), (47,0), colors.black),
								('TEXTCOLOR', (35,0), (47,0), colors.white),
								('BACKGROUND', (35,3), (47,3), colors.gray),
								('FONTSIZE', (35,3), (47,3), 8),
								
								('GRID', (35,0), (47,10), 0.5, colors.black),
								('BOX', (35,0), (47,10), 1.5, colors.black),
								
								#JUDUL PMG ON DUTY
								('SPAN', (35,0), (47,0)),
								('SPAN', (35,1), (40,1)), #Hari
								('ALIGN', (35,1), (40,1), 'LEFT'),
								('SPAN', (41,1), (47,1)), #Tanggal
								('ALIGN', (41,1), (47,1), 'LEFT'),
								#kolom1 duty on
								('SPAN', (35,2), (38,2)),
								('SPAN', (35,3), (38,3)),
								('SPAN', (35,4), (38,6)),
								('SPAN', (35,7), (38,10)),
								#kolom2 NAMA
								('SPAN', (39,2), (42,2)),
								('SPAN', (39,3), (42,3)),
								('SPAN', (39,4), (42,6)),
								('SPAN', (39,7), (42,10)),
								#kolom3 PARAF
								('SPAN', (43,2), (47,2)),
								('SPAN', (43,3), (47,3)),
								('SPAN', (43,4), (47,6)),
								('SPAN', (43,7), (47,10)),
								
								#HALAMAN 2
								('SPAN', (43,11), (47,11)),
								('ALIGN', (43,11), (47,11), 'RIGHT')
								]))

		t.wrap(width, height)
		elements.append(t)
		'''+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'''
		#write the document to disk
		doc.build(elements)
		tkinter.messagebox.showinfo("Informasi", "File PDF sudah dibuat.")
	#"""################################################ EXPORT FILE INTO PDF END ######################################"""

	def tampilkan():
		global InputTahunBulanTanggal
		InputTahunBulanTanggal = input_tahun_bulan_tanggal.get()
		#ingar pengambilan nilai tahun_bulan_tanggal sudah d bagian SELECT MYSQL
		
		Button(win, text="Halaman 1", bg="grey", fg="white", width=10, font="callibri 10", command=halaman1).place(x=890, y=290)
		Button(win, text="Halaman 2", bg="grey", fg="white", width=10, font="callibri 10", command=halaman2).place(x=890, y=320)
		
		Button(win, text="Export", bg="grey", fg="white", width=10, font="callibri 10", command=export_file).place(x=890, y=370)
		
		
		#Label(win, text=InputTahunBulanTanggal, bg="cadet blue").place(x=882, y=400)
		
	Button(win, text="Tampilkan", bg="grey", fg="white", width=10, font="callibri 10", command=tampilkan).place(x=889, y=240)

"""=============================================== AKHIR MENAMPILKAN LAPORAN ================================================="""

menu_utama = Menu()
data_iklim = Menu(menu_utama, tearoff=0)

#ISIAN DARI MENU DATA IKLIM
data_iklim.add_command(label='Buat Laporan', command=membuat_laporan)
data_iklim.add_command(label='Lihat Laporan', command=tampilkan_laporan)

#CASCADE MENU UTAMA
menu_utama.add_cascade(label='Menu', menu=data_iklim)

win.configure(menu = menu_utama, background='white')
win.mainloop()
