# NumaratörGezinme Modu #

* Yazar: Luke Davis (Open Source Systems, Ltd.)
* [Kararlı sürüm][1]ü indir

Sayısal Tuş Takımı Gezinme Modu, klavyenizin sayısal tuş takımını NVDA'nın
gezinme kontrolleri ile ekran okuyucu olmayan Windows gezinme kontrolleri
arasında kolayca değiştirmenize olanak tanıyan bir
[NVDA](https://nvaccess.org/) eklentisidir. Bu özellikle Jaws'tan NVDA'ya
geçiş yapan kullanıcılar için yararlı olabilir. Bu eklenti aynı zamanda hem
NVDA başladığında hem de isteğe bağlı olarak profillerde numara kilidi tuşu
üzerinde ayrıntılı kontrol sağlar.

### Gezinme modları açıklama ve özellikleri

Numara kilidi kapalıyken PC numaratörünün normal işlevleri şunlardır: önceki
sayfa, sonraki sayfa, baş,, son, dört yönlü yön tuşları ve bir silme
tuşu. Ancak NVDA, bu tuşları inceleme imleci, fare tıklamaları ve nesne
sunucusu navigasyon tuşları olarak kullanır. Bu, numaratörü bulunmayan
klavyelerde, masaüstü düzeninde numaratörün kullanıldığı NVDA komutlarının
başka tuşlarla gerçekleştirilebilmesi için düzenlenmiş dizüstü klavye düzeni
için de geçerlidir. Yani klavye düzeni olarak belirlenen seçenek ne olursa
olsun NVDA numaratör tuşlarını kendi komutları için kullanmaya zorlar.

Bununla birlikte, bazı kullanıcıların dizüstü bilgisayarlarında bir sayısal
tuş takımı vardır ve özellikle bazı dizüstü bilgisayarlarda ev, bitiş veya
benzeri başka tuşlar bulunmadığından, bunu Windows gezinme amaçları için (en
azından bazı zamanlar) kullanmayı tercih ederler. Bu eklentinin yardımcı
olabileceği yer burasıdır. Ek olarak, bazı masaüstü kullanıcıları, örneğin
JAWS'ta sayısal tuş takımının çalışmasına alışık olanlar, bazen bu
eklentinin etkinleştirdiği normal NVDA tuşları yerine söz konusu klavye
işlevleri için sayısal tuş takımını kullanmayı uygun bulabilir. Bu, bu
eklentinin bazı eski kullanıcılarından özel bir özellik isteği olan, sonuna
kadar okuma için popüler JAWS komutu NumpadInsert+Numpad2'yi içerir.

### Nasıl çalışır

Numlock kapalıyken, hangi klavye düzenini kullandığınızdan bağımsız olarak,
bu eklenti, NVDA tuşları ve windows standart navigasyon tuşları arasında
Alt+NVDA+NumpadPlus'a (genellikle sağda ikinci uzun tuştur) basarak hızlı ve
kolay bir şekilde geçiş yapmanıza olanak tanır. Bu hareket, tercihler
menüsünden Girdi Hareketleri iletişim kutusunda yeniden atanabilir.

Eklenti numaratör insert tuşunun işlevine müdahale etmez. BU tuşu da NVDA
tuşu olarak belirlediyseniz, windows standart navigasyonu modunda da aynı
işlev için kullanmaya devam edebilirsiniz. Bu özelliği istiyorsanız, lütfen
bana bildirin, ancak numaratör insert tuşunu NVDA tuşu olarak kullanmak
istemiyorsanız halihazırda bunu NVDA ayarları klavye kategorisi altından
yapabilirsiniz.

NVDA'nın varsayılan olarak Windows navigasyon modu etkin başlamasını tercih
ederseniz, bunu NVDA ayarlarında yapılandırabilirsiniz. NVDA'nın tercihler
menüsü, ayarlar iletişim kutusunda  Numpad Nav Mode (numaratör navigasyon
modu) kategorisini bulun ve NVDA'yı başlattığınızda Windows navigasyon
Modunu varsayılan olarak etkinleştir onay kutusunu işaretleyin.

### Numara kilidi özellikleri

Varsayılan olarak, numara kilidi tuşuyla hiçbir şey yapılmaz.

Ancak, bilgisayarınızı numara kilidinin her zaman açık olmasını tercih eden
gören bir kullanıcıyla paylaşıyor ve sayısal tuş takımının NVDA ile
çalışması için kapalı olmasını istiyorsanız NVDA başladığında numara
kilidinin otomatik olarak kapatılmasını isteyebilirsiniz.  Alternatif
olarak, çok fazla veri girebilirsiniz ve bu nedenle NVDA'yı başlattığınızda
numara kilidinin her zaman açık olmasını tercih edebilirsiniz.

 NVDA menüsü, Tercihler, Ayarlar, Sayısal Tuş Takımı Moduna gidin ve "NVDA başladığında veya profil yüklendiğinde numara kilidiğ durumu" seçicisini kullanın. Bunun üç seçeneği vardır. İlki, "değiştirme", varsayılandır ve numara kilidine dokunmaz. NVDA başlamadan önce hangi durumdaysa o durumda kalacaktır.
İkinci seçenek, NVDA başladığında Numara kilidini her zaman kapatacak olan "Numara kilidini kapat" seçeneğidir. Üçüncü seçenek olan "Numara Kilidini Aç" NVDA başladığında numara kilidi kapalıysa açacaktır.
İkinci veya üçüncü seçeneklerden birini seçerseniz, NVDA'dan çıktığınızda numara kilidi daha önce hangi durumdaysa o duruma geri getirilecektir. Örneğin, "Numara kilidini kapat" seçeneğini seçip ve NVDA'yı başlattığınızda numara kilidi açıksa: NVDA'yı kullanırken kapatılacak, ancak NVDA'dan çıktığınızda tekrar açılacaktır.

#### Gelişmiş kullanım durumları

NVDA'nın güçlü yapılandırma profillerini kullanıyorsanız ve belirli
profillere girdiğinizde numara kilidinin otomatik olarak açılmasını
istiyorsanız, aşağıdakileri yapın:

* "Normal profil"deyken, yukarıda açıklanan Sayısal tuş takımı Gezinme Modu
  ayarları paneline gidin. "İlk numlock durumu yapılandırma profiline
  bağlıdır" kutusunu işaretleyin. Bu seçenek varsayılan olarak işaretli
  değildir.

* Tamam'ı seçin.

* Numara kilidinin her zaman kapalı veya açık olmasını istediğiniz profile
  geçin.

* Sayısal Tuş Takımı Gezinme Modu ayarları paneline geri dönün ve
  tercihinize göre numara kilidini kapatma veya açma seçeneğini seçin.

* Ardından Tamam'ı seçin. Şimdi, bu profile her girdiğinizde, numara kilidi
  otomatik olarak istenen duruma geçecektir.

Bunun yeni bir özellik olduğunu ve kimsenin bu özelliği kullanıp
kullanmadığını bilmiyorum. Bir tane bulursanız, onu kullanmayı nasıl
bulduğunuzu bana bildirmek için lütfen bir e-posta gönderin veya [bir
sorun](https://github.com/opensourcesys/numpadNavMode/issues/new) açın.

### Yeni özellikler

Bir [sorunu](https://github.com/openSourceSys/numpadNavMode/issues/new)
yayınlamanızı tavsiye ederim. Ayrıca, herhangi bir özellik önerisini, burada
listelemediğim diğer kullanım durumlarını e-posta ile gönderin veya yalnızca
eklentiyi yararlı bulduğunuzu bana bildirin!

### Geçmiş

Bu eklenti, yıllar boyunca kullanıcılardan gördüğüm isteklerin ve
[#9549](https://github.com/nvaccess/nvda/issues/9549) adresindeki GitHub
meselesinin sonucu oldu. @Qchristensen ve @feerrenrut'a teşekkürler.

### Değişiklik günlüğü

(Bu değişiklik günlüğü eksik. Tüm ayrıntılar için Git günlüğüne bakın.)

* 23.0: NVDA 2023.X uyumluluğu.

* 23.1.0: Numara kilidi yönetim özellikleri eklendi. Daha iyi günlük
  kaydı. Geliştirilmiş yapılandırma profili işleme (WIP).

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=numpadNavMode
