İBB Şehir Hatları Deniz Taksi Kar/Zarar ve CRM Analizi 






![Açıklama](https://pbs.twimg.com/profile_images/1670793732264796167/5x0JMUSN_400x400.jpg)                                    



![Açıklama](https://i.pinimg.com/originals/e6/6f/be/e66fbe79ce5ed5427f775fdf944d3c17.png)


Bu proje, İstanbul Büyükşehir Belediyesi (İBB) Şehir Hatları'na bağlı deniz taksilerin maliyet ve gelir yapısını analiz etmek amacıyla hazırlanmıştır. Proje kapsamında deniz taksilerin günlük operasyonel giderleri, gelirleri ve genel performansı detaylı bir şekilde incelenmiş ve kar/zarar hesaplamaları yapılmıştır.Proje Amacı
Deniz taksi hizmeti, şehir içi ulaşımda alternatif ve hızlı bir çözüm sunarken, işletme maliyetleri ve gelirlerin doğru bir şekilde yönetilmesi oldukça önemlidir. Bu projede:

*Deniz taksi hizmetinin sürdürülebilirliğini ve kârlılığını analiz etmek,
*Operasyonel giderler, bakım maliyetleri, yakıt giderleri gibi kalemleri inceleyerek deniz taksi başına ortalama günlük maliyetleri hesaplamak,
*Yolcu başına gelir ve sefer sayılarına göre gelir analizi yapmak,
*Kar/zarar dengesini optimize edebilmek için öneriler geliştirmek amaçlanmıştır.

CRM Entegrasyonu
*Müşteri İlişkileri Yönetimi (CRM) sistemi, deniz taksi hizmetinde müşteri memnuniyetini artırmak ve kullanıcı taleplerini optimize etmek amacıyla kullanılacaktır. Projenin CRM entegrasyonu aşağıdaki başlıklar altında değerlendirilebilir:

*Müşteri Geri Bildirimleri: CRM sistemi aracılığıyla deniz taksi hizmetini kullanan yolculardan alınan geri bildirimler analiz edilerek, yolcu memnuniyeti artırılacak. Geri bildirimlere dayalı olarak hizmet kalitesi ve müşteri talepleri doğrultusunda iyileştirmeler yapılabilir.

*Müşteri Segmentasyonu: CRM verileri, farklı müşteri segmentlerine göre talep analizini mümkün kılar. Böylece, belirli müşteri gruplarına yönelik özel promosyonlar veya indirim kampanyaları düzenlenebilir.

*Talep Tahminleri: CRM verileri, yolcuların talep ettiği sefer saatleri ve hat bilgileri doğrultusunda, ileride kullanılacak tahmin modellerinin geliştirilmesine temel oluşturacaktır.

*Sadakat Programları: Deniz taksi hizmetinden sıkça yararlanan yolcular için sadakat programları geliştirilip CRM verileriyle entegre edilerek müşteri bağlılığı artırılabilir.




******************************************************************************
Kullanılan Veri Seti
Bu projede kullanılan veri seti 2023 Temmuz-Ocak ayları baz alınarak oluşturulmuş olup ücretlendirme ilgili ayları baz alınarak kullanılmıştır, İBB Şehir Hatları deniz taksi seferleri, bilet satışları, yakıt  gibi operasyonel verilerden oluşmaktadır. Veri setinde yer alan ana değişkenler şunlardır:

toplamucret: Seferden elde edilen toplam gelir.
yolcusayisi: Seferde taşınan toplam yolcu sayısı.
talep_edilen_yolculuk_saati: Yolcuların talep ettiği sefer saati.
kalkis_saat_kategori: Seferin yapıldığı saat dilimi (örneğin sabah, öğlen, akşam).
hafta_gunu_isim: Seferin gerçekleştiği haftanın günü (örneğin Pazartesi, Salı).
ay: Seferin yapıldığı ay.
yolculuk_kategorisi: Seferin türü (örneğin kısa mesafe, uzun mesafe).
yolculuksuresi(dk): Seferin süresi (dakika cinsinden).
yolcu_hattı: Seferin yapıldığı hat.
dakikalık_sefer_ücreti(tl): Seferin her dakika başına maliyeti.
toplam_maliyet: Seferin toplam maliyeti (yakıt, bakım vb. giderler dahil).
kar_zarar_tutarı(günlük): Günlük kar ya da zarar tutarı.
karzarar_oranı%(günlük): Günlük kar/zarar oranı yüzdesi.
kar_mı_zarar_mı: Seferin kar mı zarar mı ettiğini belirten değişken.
gun_sefer_sayisi: Günlük toplam sefer sayısı.

CRM Analizi İçin Kullanılan Veriler
toplamucret: Seferden elde edilen toplam gelir.
olusturmazamani: Yolcuların deniztaksi talebini gerçekleştirdiği tarih
yolcu:Yolcunun adı ve soyadı
iademiktarı: Yolcuya iade edilen ücret
phoneNumber: Yolcunun telefon numarası

***************************************************************************************
Proje Adımları
Veri Toplama ve Temizleme:
Sefer, yolcu ve maliyet bilgilerini içeren veri seti düzenlenmiş ve eksik/veri hatalı olan kayıtlar temizlenmiştir.
Keşifsel Veri Analizi (EDA):
Veri setinde yer alan değişkenler incelenmiş, sefer başına ortalama gelir ve maliyet dağılımları analiz edilmiştir.
Kar/Zarar Analizi:
Deniz taksi başına günlük ortalama gelir ve maliyet hesaplanarak net kârlılık oranı bulunmuştur.
Öneriler:
Analiz sonuçlarına dayanarak, deniz taksilerin karlılığını artırmak için operasyonel süreçlerde iyileştirme önerileri geliştirilmiştir.
*******************************
Teknolojiler ve İstatistiki Yöntemler
Bu projede kullanılan ana teknolojiler ve İstatistiki araçlar araçlar:

Python: Veri analizi ve hesaplamalar için temel programlama dili.
Pandas: Veri manipülasyonu ve analiz.
Matplotlib & Seaborn: Veri görselleştirme için kullanıldı.
Jupyter Notebook: Proje geliştirimi ve analizlerin yürütülmesi için.
Power BI:Veri görselleştirme için Kullanıldı.
LightGbmRegressor:Makine tahmin modellemesi için kullanıldı.
Shapiro-Wilk Testi: Normalllik Testi
Kolmogorov-Smirnov (K-S) Testi:Bir örneklem ile belirli bir dağılımın (genellikle normal dağılım) veya iki örneklem arasındaki farkın istatistiksel olarak anlamlı olup olmadığını test etmek için kullanılan bir non-parametrik testtir.
Anderson-Darling Testi:Bir veri setinin belirli bir dağılıma (genellikle normal dağılım) ne kadar iyi uyduğunu test etmek için kullanılan bir güçlendirilmiş goodness-of-fit testidir.
Kruskal-Wallis H Testi:Bir veya daha fazla bağımsız gruptan gelen sıralı verilerin medyanlarının karşılaştırılmasını amaçlayan parametrik olmayan bir istatistiksel testtir.
Üç veya daha fazla bağımsız grubun medyanları arasında istatistiksel olarak anlamlı bir fark olup olmadığını test etmek için kullanılır.
Dunn's Testi:Kruskal-Wallis H Testi'nde bulunan anlamlı farklılıkları daha spesifik gruplar arasında incelemek için kullanılan post-hoc (sonrası) bir istatistiksel testtir. Bu test, farklı gruplar arasındaki medyanların karşılaştırılmasını sağlar ve hangi gruplar arasında anlamlı farklar olduğunu belirler.
Kruskal-Wallis H Testi sonucunda eğer anlamlı bir fark bulunursa, bu farkın hangi gruplar arasında olduğunu belirlemek için kullanılır.
Gamma Gamma Modeli:Müşterilerin ortalama işlem değerlerini (monetary value) tahmin etmeye odaklanır ve müşterilerin gelir seviyeleri arasındaki varyasyonu dikkate alarak çalışır.
BG/NBD Modeli:Bir müşterinin gelecekte kaç kez alışveriş yapacağını tahmin etmeye odaklanır.
*********************************************

Proje Sonuçları
Proje sonunda elde edilen bulgular şu şekildedir:

Deniz taksilerinin ortalama günlük maliyetleri ve gelirleri karşılaştırıldığında  seferlerin zarar ettiği görülmüştür.
Özellikle uzun mesafe yapılan seferlerin kârlılığı düşürmesi, bu tarz seferlerin optimize edilmesi gerektiğini ortaya koymuştur.
Ağustos ayı en karlı ay Ocak ayı ise kar oranı en düşük ay olmuştur.
Yakıt maliyetlerinin analiz edilmesi, bu alanlarda yapılabilecek maliyet düşürücü adımların tespit edilmesini sağlamıştır.


**************************************************************************
Gelecekteki Geliştirme Fırsatları
Bu proje, deniz taksilerin mali performansını analiz etmek için ilk adımdır. Gelecekte, daha kapsamlı bir tahmin modeli geliştirilebilir ve farklı sezonlara göre talep tahminleri yapılabilir. Ayrıca:

Talep Tahmini Modelleri: Mevsimsel ve saatlik yolcu talebi tahminleri için makine öğrenmesi modelleri geliştirilebilir.
Maliyet Optimizasyonu: Yakıt tüketimini giderlerini azaltacak optimizasyon yöntemleri araştırılabilir.



*************************************

NOT:Kodların tamamı PAYLAŞILMAMIŞTIR.
