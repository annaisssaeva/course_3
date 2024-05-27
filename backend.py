import pyttsx3
def text_to_speech(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 115)
    engine.say(text)
    engine.runAndWait()


#создание списка стимулов-слов
stringg = '''выбор — 3+1=4
пират — 3+2+1=6
ждать — 3+2+0=5
пролил — 4+1+1=6
шов — 1+1+1= 3
заря — 2+2+1=5
кэб — 1+2+1=4
выдра — 3+0+1=4
храпят — 4+3+1=8
привет — 4+3+1=8
цена — 2+3+0=5
продукт — 5+3+0=8
купец — 3+4+1=8
голова — 4+1+0=5
запрет — 4+3+1=8
поворот — 5+1+1=7
хорёк — 3+2+1=6
поэт — 2+1+0=3
ёлка — 2+1+1=4
щука — 2+3+1=6
ель — 1+2+1=4
зараза — 4+2+1=7
фонарь — 4+2+1=7
цокот — 3+3+1=7
подъезд — 5+3+1=9
съезд — 3+4+1=8
пух — 1+2+1=4
хлопоты — 5+2+1=8
язык — 2+3+0=5
чечётка — 5+5+1=11
курица — 4+4+1=9
часы — 2+2+1=5
жюри — 2+2+1=5
жук — 1+2+1=4
жизнь — 3+4+0=7
японец — 4+4+1=9
цирк — 2+3+1=6
якорь — 3+3+1=7
цыплята — 5+3+1=9
сыграть — 5+4+1=10
глыба — 3+2+1=6
гамак — 3+3+1=7
игра — 2+2+0=4
бабушка — 5+5+0=10
бублик — 4+5+1=10
яхонт — 3+4+1=8
люк — 1+2+1=4
ключ — 2+3+1=6
ёжик — 2+2+1=5
закат — 3+3+1=7
попугай — 5+3+1=9
край — 2+2+0=4
рай — 1+1+1=3
кроха — 3+2+1=6
шить — 2+4+1=7
щавель — 4+3+1=8
щипок — 3+3+1=7
съёмка — 4+4+1=9
кофта — 3+2+1=6
фига — 2+2+1=5
сэр — 1+1+1=3
миля — 2+3+1=6'''

words = {}
ind = 0
for line in stringg.split("\n"):
    ind+=1
    word=line.split(' — ')[0]
    num = line.split('=')[1]
    words[word] = int(num)
word_compl=dict(sorted(words.items(), key=lambda item: item[1]))
words_sorted = list(word_compl.keys())


#создание списка предложений
stringg = '''Класс зашумел.
Птицы живут в лесах.
Рыболов поймал в реке щуку.
От учтивых слов язык не отсохнет.
Море глухо роптало и билось о берег.
Сад тихонько зашумел листвой и замер.
Маша прочитает книгу о путешествиях.
Ночью ударил мороз и заморозил цветы.
Школьники путешествуют по родному краю.
Старшеклассники участвуют в лыжных соревнованиях.
Ему было 76 лет.
Мне 12 лет, а тебе?
У него было 3 кошки.
Это произошло в 1496 году.
Война длилась с 1398 по 1425.
Я хожу в бассейн 5 раз в неделю.
Она была в этом городе раз 7 или 8.
Моя работа вышла в 10 раз больше.
Это фильм для зрителей старше 20 лет.
Запишите мой номер: 49 (351) 082 60 73.
Звёзды меркнут, гаснут.
Вы у меня в гостях, ребята.
Зацвели одуванчики, шиповник.
Тракторы пашут, разрыхляют почву.
В болоте урчали, квакали лягушки.
На столе лежали книги, тетради, карандаши.
В лесу росли ландыши, фиалки, колокольчики.
Мы показали на выставке, что мы умеем делать.
Осенние листья летят, кружатся, падают на землю.
В лесном озере водились караси, плотва, щуки, лещи.
Серебряные паутинки опускались на деревья, на кусты.
Славная осень!
Ах ты, обжора!
Привет, Кирилл!
Дорогие ребята!
Стой, братцы, стой!
Граждане пассажиры!
Увы, я разбито, разбито!
Дайте два больших пенала!
Ступайте, ребята, за мной!
Я у самого Юлия Цезаря в почёте был!
Далеко?
А куда ты идёшь?
Куда же они летят?
Что же было на выставке?
Какие части есть у растения?
А ты что ж, кумушка, в дорогу?
Ты опять завтракаешь на уроке?
Что с вами приключилось, друзья?
Какие птицы улетают на юг осенью?
Почему же происходит извержение вулкана?
«Абсолютно верно!» - сказал учитель.
«Стой, братцы, стой!» - кричит Мартышка.
Мы попросили лесника: «Проводи нас, дедушка».
«Кто ты? Что делаешь?» - спросил сердито Лев.
«Ешьте, ребята, яблоки», - предложил нам лесник.
Этот поезд останавливается на станции «Аэропорт»?
«Что это?» - спросил вдруг Костя, приподняв голову.
«Куда так, кумушка, бежишь ты без оглядки?» - Лисицу спрашивал Сурок.
«Кумушка, мне странно это: да работала ль ты в лето?» - говорит ей Муравей.
Максим Горький писал: «Обогащайте себя знанием русского языка, читайте больше».'''

sents = []
ind = 0
for line in stringg.split("\n"):
    ind+=1
    sents.append(line)

