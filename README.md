Nama : Aiko
NPM : 2506617140
Kelas : PBP C

### Tugas 1
1. Ya, saya menggunakan <section> dan <article>. Elemen tsb membantu saya membagi halaman berdasarkan fungsi dan informasi, seperti profile, education, dan experience, sehingga struktur HTML lebih teratur dan mudah dipahami. Menurut saya, hal ini juga memudahkan saat mengatur CSS karena setiap bagian memiliki struktur yang jelas.

2. Tantangan terbesar saya sebagai pengguna HTML dan CSS pertama kali adalah mengendalikan beberapa elemen terutama untuk PNG yang tidak jadi saya masukkan mengingat kendala pemahaman saya dan posisinya tidak konsisten pada ukuran layar yang berbeda. Oleh karena itu, saya memutuskan untuk tidak menggunakannya agar tampilan website tetap rapi dan responsif untuk sementara

3. Karena website masih berupa static web, data seperti education, experience, dan project masih ditulis langsung di kode. Pada iterasi selanjutnya, saya ingin menambahkan fitur dinamis seperti form untuk menambah atau mengubah data.

Generative AI digunakan untuk tools pembantu saya dalam mengerjakan ini seperti penjelasan HTML dan CSS, memperbaiki kode yang error, dsb. Ada keterbatasan dalam AI yang saya gunakan yaitu ketika tools tsb tidak bisa membantu saya dalam tampilan png tersebut

### Tugas 2
1. User membuka halaman skill, lalu browser mengirim request ke URL "/skill". Request tersebut pertama kali diproses oleh "portofolio/urls.py", yang meneruskan request ke "main/urls.py". Di dalam "main/urls.py", URL "/skill/"  diarahkan ke view "show_skill".

View "show_skill" mengambil data dari model "Skill" menggunakan "Skill.objects.all()" yang datanya dimasukkan ke "skill_list" dan diteruskan ke "skill.html". Template kemudian menggunakan Django Template Language untuk 
melakukan perulangan terhadap "skill_list" dan menampilkan setiap skill sebagai card.

Alurnya adalah:
user -> browser -> portofolio/urls.py -> main/urls.py -> show_skill -> Skill model -> skill.html -> browser

2. Data sebaiknya disimpan di model karena model memungkinkan data dikelola secara terstruktur 
dan terpisah dari tampilan. Dengan itu, data dapat dikelola dengan mudah. Selain itu, dengan menggunakan model, data dapat ditambah, diubah, atau dihapus tanpa perlu mengubah template. Template cukup mengambil data dari context dan menampilkannya menggunakan Django Template Language

3. "makemigrations" digunakan untuk membuat file migration setelah ada perubahan pada model. 
Sedangkan 'migrate" digunakan untuk menerapkan migration tersebut ke database sehingga struktur database sesuai dengan model yang dibuat.

Contohnya pada tugas ini, ketika model "Skill" pertama kali ditambahkan dengan field 
"name", "category", dan "level", kita menjalankan python manage.py makemigrations

### Tugas 3
1. Seperti di Tutorial 03, ModelForm adalah boilerplate bawaan Django: cukup menulis class Meta berisi model dan fields, lalu field, tipe input, dan validasinya diturunkan dari model. Jika membuat form HTML manual, harus ditulis ulang di HTML dan view serta akan sulit. {% csrf_token %} wajib karena Django menolak request POST tanpa token yang valid. Sesuai penjelasan tutorial, tujuannya mencegah request diubah atau diarahkan ke pihak lain yang berbahaya. Itu juga alasan CSRF_TRUSTED_ORIGINS

2. Keduanya self-descriptive dan sama-sama bisa dibaca manusia, tetapi JSON lebih ringkas karena tidak butuh tag pembuka dan penutup untuk setiap elemen

3. a. Browser mengirim request GET -> urls.py -> get_skills_json
b. view mengambil semua objek dengan Skill.objects.all() (QuerySet)
c. serializers.serialize("json", skills) mengubah QuerySet menjadi string JSON
d. string dikirim kembali lewat HttpResponse(..., content_type="application/json")

Serialization diperlukan karena objek model Django adalah objek Python di memori server, sedangkan HTTP hanya bisa membawa teks atau bytes.

AI DISCLOSURE
Tools : Claude
a. Bagian yang dibantu AI: Debugging form update yang bermasalah (jadi terlihat membuat data baru)
b. Penjelasan alur create vs update (instance=), alur JSON serialize/deserialize

### Tugas 4
AI DISCLOSURE
Tools : ChatGPT, Claude
Saya menggunakan bantuan generative AI seperti Claude dan ChatGPT untuk membantu saya memahami alur dari tutorial dan menjelaskan step-by-step dari Tugas 4. Selain itu AI membantu saya dalam traceback dan mengatasi ValueError

### Tugas 5
1. Debouncing adalah teknik untuk menunda sebuah fungsi hingga suatu jeda waktu berlalu tanpa event baru. Pada fitur pencarian berbasis AJAX, setiap ketikan di kotak pencarian berpotensi memicu satu request ke server. Tanpa debouncing, tiap huruf mengirim satu request ke server sehingga membebani server

2. await digunakan untuk menunggu sebuah Promise, seperti hasil dari fetch(), selesai sebelum melanjutkan ke baris kode berikutnya, di dalam fungsi async. Tanpa await, fetch() akan langsung mengembalikan objek Promise yang masih pending, bukan data atau response sebenarnya

3. XSS atau Cross-Site Scripting adalah serangan di mana penyerang menyisipkan skrip berbahaya, biasanya JavaScript, ke dalam halaman web, yang kemudian dieksekusi oleh browser pengguna lain yang membuka halaman tersebut. Data yang ditampilkan melalui AJAX/JavaScript lebih rentan terhadap serangan keamanan karena Django secara otomatis mematikan (escape) karakter berbahaya pada sistem templatenya, sementara JavaScript secara bawaan mempercayai data tersebut jika dimasukkan langsung ke dalam struktur HTML

AI DISCLOSURE
Tools : ChatGPT, Claude
Saya menggunakan bantuan generative AI seperti Claude dan ChatGPT untuk debugging error seperti migrasi model, format tanggal di form, dan masalah fungsi di views.py, menjelaskan pola dari Tutorial 5 yang dari model Project ke model Experience, serta menjelaskan konsep AJAX, debouncing, dan proteksi XSS.