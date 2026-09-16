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