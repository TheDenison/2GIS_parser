type_org_mapping = {
    'sport': 'Спорт товары',
    'salon': 'Салоны красоты',
    'studio': 'Ателье',
    'auto': 'Автосалоны',
    'showroom': 'Шоу-рум одежды',
    'shop_female': 'Магазин женской одежды',
    'shop_male': 'Магазин мужской одежды',
    'shop_kids': 'Магазин детской одежды',
    'hotel': 'Отель',
    'psychology': 'Психологическая консультация',
    'lawyer': 'Юридические услуги',
    'dancing': 'Школа танцов',
    'barber': 'Парикмахерская',
    'massage': 'Массажный салон',
    'accountant': 'Бухгалтерские услуги',
    'translator': 'Бюро переводов',
    'cleaning': 'Клининговые услуги',
    'phones': 'Ремонт телефонов',
    'nails': 'Ногтевая студия',
    'build': 'Cтроительная компания',
    'flowers': 'Цветочный Магазин',
    'candy': 'Кондитерская',
    'vish': 'Студия вышивки',
    'second': 'Секонд-хенд',
    'furniture': "мебель на заказ",
    'design': "дизайн интерьеров",
    'repair': "ремонт квартир",
    'RIP': "ритуальные услуги",

    'coffee': 'Кофейня',
    'coffee_to_go': 'Кофе с собой',
    'coffee_takeaway': 'Кофе на вынос',
    'flowers_delivery': 'доставка цветов',
    'optics': 'Салон оптики',
    'marry': 'свадебный салон',
    'vape': 'вейп-шоп',
    'intim': 'секс-шопы'

}

districts = [
    "Академический район", "Алексеевский район", "Бабушкинский район",
    "Басманный район",
    "Бескудниковский район", "Бутырский район",
    "Войковский район", "Гагаринский район", "Головинский район", "Даниловский район",
    "Донской район", "Красносельский район", "Мещанский район", "Можайский район",
    "Нагорный район",
    "Нижегородский район", "Обручевский район", "Останкинский район",
    "поселение Внуковское", "поселение Московский", "поселение Сосенское", "Пресненский район",
    "район Арбат", "район Аэропорт", "район Бибирево", "район Богородское", "район Братеево",
    "район Восточное Дегунино", "район Выхино-Жулебино", "район Гольяново",
    "район Дорогомилово", "район Замоскворечье", "район Зюзино",
    "район Зябликово", "район Измайлово", "район Коньково", "район Коптево",
    "район Косино-Ухтомский", "район Крылатское", "район Кузьминки", "район Кунцево",
    "район Левобережный", "район Лефортово", "район Люблино", "район Марфино",
    "район Марьина Роща", "район Марьино", "район Митино", "район Москворечье-Сабурово",
    "район Нагатино-Садовники", "район Нагатинский Затон", "район Некрасовка", "район Новогиреево",
    "район Новокосино", "район Ново-Переделкино", "район Орехово-Борисово Северное",
    "район Орехово-Борисово Южное", "район Отрадное", "район Очаково-Матвеевское",
    "район Перово", "район Печатники", "район Покровское-Стрешнево", "район Преображенское",
    "район Проспект Вернадского", "район Раменки", "район Ростокино", "район Свиблово",
    "район Северное Бутово", "район Северное Медведково", "район Северное Тушино",
    "район Сокол", "район Соколиная Гора", "район Сокольники", "район Солнцево", "район Строгино",
    "район Текстильщики", "район Тёплый Стан", "район Тропарёво-Никулино", "район Филёвский Парк",
    "район Фили-Давыдково", "район Хамовники", "район Ховрино", "район Хорошёво-Мнёвники", "район Царицыно",
    "район Черёмушки", "район Чертаново Северное", "район Чертаново Центральное", "район Чертаново Южное",
    "район Щукино", "район Южное Бутово", "район Южное Тушино", "район Якиманка", "район Ясенево",
    "Рязанский район", "Савёловский район", "Таганский район", "Тверской район", "Тимирязевский район",
    "Хорошёвский район", "Южнопортовый район"]

distr2 = [
    "Бескудниковский район", "Бутырский район",
    "Войковский район", "Гагаринский район", "Головинский район", "Даниловский район",
    "Донской район", "Красносельский район", "Мещанский район", "Можайский район",
    "Нагорный район",
    "Нижегородский район", "Обручевский район", "Останкинский район",
    "поселение Внуковское", "поселение Московский", "поселение Сосенское", "Пресненский район",
    "район Арбат", "район Аэропорт", "район Бибирево", "район Богородское", "район Братеево",
    "район Восточное Дегунино", "район Выхино-Жулебино", "район Гольяново",
    "район Дорогомилово", "район Замоскворечье", "район Зюзино",
    "район Зябликово", "район Измайлово", "район Коньково", "район Коптево",
    "район Косино-Ухтомский", "район Крылатское", "район Кузьминки", "район Кунцево",
    "район Левобережный", "район Лефортово", "район Люблино", "район Марфино",
    "район Марьина Роща", "район Марьино", "район Митино", "район Москворечье-Сабурово",
    "район Нагатино-Садовники", "район Нагатинский Затон", "район Некрасовка", "район Новогиреево",
    "район Новокосино", "район Ново-Переделкино", "район Орехово-Борисово Северное",
    "район Орехово-Борисово Южное", "район Отрадное", "район Очаково-Матвеевское",
    "район Перово", "район Печатники", "район Покровское-Стрешнево", "район Преображенское",
    "район Проспект Вернадского", "район Раменки", "район Ростокино", "район Свиблово",
    "район Северное Бутово", "район Северное Медведково", "район Северное Тушино",
    "район Сокол", "район Соколиная Гора", "район Сокольники", "район Солнцево", "район Строгино",
    "район Текстильщики", "район Тёплый Стан", "район Тропарёво-Никулино", "район Филёвский Парк",
    "район Фили-Давыдково", "район Хамовники", "район Ховрино", "район Хорошёво-Мнёвники", "район Царицыно",
    "район Черёмушки", "район Чертаново Северное", "район Чертаново Центральное", "район Чертаново Южное",
    "район Щукино", "район Южное Бутово", "район Южное Тушино", "район Якиманка", "район Ясенево",
    "Рязанский район", "Савёловский район", "Таганский район", "Тверской район", "Тимирязевский район",
    "Хорошёвский район", "Южнопортовый район"]

ACCEPT_BUTTON = '/ html / body / div[3] / div / div[1] / table / tbody / tr / td[2] / table / tbody / tr / td[2] / button'

# Agent
MY_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 '
                  'Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
    'Referer': 'https://www.google.com/'

}

# Список названий ссылок
LINK_NAMES = ['Контакты', 'О нас', 'О компании', 'Публичная оферта', 'Оферта', 'Реквизиты',
              'Политика конфидециальности', 'Политика в отношении обработки персональных данных',
              'Пользовательское соглашение', 'Политика конфиденциальности', 'Покупателям',
              'Политика конфиденциальности персональных данных', 'Наши реквизиты', 'Договор оферты',
              'Корп. клиентам', 'Корпоративным клиентам', 'Оплата', 'Реквизиты компании', 'Оплата и реквизиты',
              'О магазине'
              ]

STATIONS = [
    'Авиамоторная', 'Автозаводская', 'Академическая', 'Александровский сад', 'Алексеевская', 'Алма-Атинская',
    'Алтуфьево', 'Аминьевская', 'Андроновка', 'Аникеевка', 'Аннино', 'Арбатская', 'Аэропорт', 'Бабушкинская',
    'Багратионовская', 'Баковка', 'Балтийская', 'Баррикадная', 'Бауманская', 'Беговая', 'Белокаменная',
    'Беломорская', 'Белорусская', 'Беляево', 'Бескудниково', 'Бибирево', 'Библиотека имени Ленина', 'Битца',
    'Битцевский парк', 'Борисово', 'Боровицкая', 'Боровское шоссе', 'Ботанический сад', 'Братиславская',
    'Бульвар Дмитрия Донского', 'Бульвар Рокоссовского', 'Бульвар адмирала Ушакова', 'Бунинская аллея', 'Бутово',
    'Бутырская', 'Быково', 'ВДНХ', 'Варшавская', 'Верхние Котлы', 'Верхние Лихоборы', 'Вешняки', 'Владыкино',
    'Водники', 'Водный стадион', 'Войковская', 'Волгоградский проспект', 'Волжская', 'Волоколамская',
    'Воробьёвы горы', 'Воронцовская', 'Выставочная', 'Выставочный центр', 'Выхино', 'Говорово', 'Гражданская',
    'Грачёвская', 'Давыдково', 'Дегунино', 'Деловой центр', 'Депо', 'Динамо', 'Дмитровская', 'Добрынинская',
    'Долгопрудная', 'Домодедовская', 'Достоевская', 'Дубровка', 'Есенинская', 'Жулебино', 'ЗИЛ',
    'Зеленоград-Крюково', 'Зорге', 'Зюзино', 'Зябликово', 'Измайлово', 'Измайловская', 'Ильинская', 'Ипподром',
    'Калитники', 'Калужская', 'Кантемировская', 'Каховская', 'Каширская', 'Киевская', 'Китай-город',
    'Кленовый бульвар', 'Кожуховская', 'Коломенская', 'Коммунарка', 'Комсомольская', 'Коньково', 'Коптево', 'Косино',
    'Котельники', 'Красково', 'Красногвардейская', 'Красногорская', 'Краснопресненская', 'Красносельская',
    'Красные ворота', 'Красный Балтиец', 'Красный Строитель', 'Кратово', 'Крестьянская застава', 'Кропоткинская',
    'Крылатское', 'Крымская', 'Кузнецкий мост', 'Кузьминки', 'Кунцевская', 'КунцевскаяБелорусская', 'Курская',
    'Курьяново', 'Кутузовская', 'Левобережная', 'Ленинский проспект', 'Лермонтовский проспект', 'Лесопарковая',
    'Лефортово', 'Лианозово', 'Лихоборы', 'Лобня', 'Локомотив', 'Ломоносовский проспект', 'Лубянка', 'Лужники',
    'Лухмановская', 'Люберцы', 'Люблино', 'Малаховка', 'Марк', 'Марксистская', 'Марьина Роща', 'Марьино',
    'Маяковская', 'Медведково', 'Международная', 'Менделеевская', 'Минская', 'Митино', 'Мичуринский проспект',
    'Мнёвники', 'Молжаниново', 'Молодежная', 'Москва-Товарная', 'Москворечье', 'Моссельмаш', 'Мякинино',
    'Нагатинская', 'Нагатинский Затон', 'Нагорная', 'Народное Ополчение', 'Нахабино', 'Нахимовский проспект',
    'Некрасовка', 'Некрасовская', 'Немчиновка', 'Нижегородская', 'Новаторская', 'Новогиреево', 'Новодачная',
    'Новокосино', 'Новокузнецкая', 'Новопеределкино', 'Новоподрезково', 'Новослободская', 'Новохохловская',
    'Новоясеневская', 'Новые Черемушки', 'Новые Черёмушки', 'Одинцово', 'Озёрная', 'Окружная', 'Окская', 'Октябрьская',
    'Октябрьское поле', 'Ольховая', 'Опалиха', 'Орехово', 'Останкино', 'Остафьево', 'Отдых', 'Отрадное',
    'Охотный ряд', 'Павелецкая', 'Павшино', 'Панки', 'Панфиловская', 'Парк Победы', 'Парк культуры', 'Партизанская',
    'Пенягино', 'Первомайская', 'Перерва', 'Перово', 'Петровский парк', 'Петровско-Разумовская', 'Печатники',
    'Пионерская', 'Планерная', 'Площадь Гагарина', 'Площадь Ильича', 'Площадь Революции', 'Площадь трёх вокзалов',
    'Плющево', 'Подольск', 'Подрезково', 'Покровское', 'Полежаевская', 'Полянка', 'Пражская',
    'Преображенская площадь', 'Прокшино', 'Пролетарская', 'Проспект Вернадского', 'Проспект Мира', 'Профсоюзная',
    'Пушкинская', 'Пятницкое шоссе', 'Рабочий Посёлок', 'Раменки', 'Раменское', 'Рассказовка', 'Речной вокзал',
    'Рижская', 'Римская', 'Ростокино', 'Румянцево', 'Рязанский проспект', 'Савеловская', 'Савёловская', 'Саларьево',
    'Свиблово', 'Севастопольская', 'Селигерская', 'Семеновская', 'Серпуховская', 'Сетунь', 'Силикатная', 'Сколково',
    'Славянский бульвар', 'Смоленская', 'Сокол', 'Соколиная Гора', 'Сокольники', 'Солнцево', 'Сортировочная',
    'Спартак', 'Спортивная', 'Сретенский бульвар', 'Стахановская', 'Стрешнево', 'Строгино', 'Студенческая',
    'Сухаревская', 'Сходненская', 'Сходня', 'Таганская', 'Тверская', 'Театральная', 'Текстильщики', 'Телецентр',
    'Теплый Стан', 'Терехово', 'Тестовская', 'Технопарк', 'Тимирязевская', 'Томилино', 'Третьяковская',
    'Трикотажная', 'Тропарёво', 'Трубная', 'Тульская', 'Тургеневская', 'Тушинская', 'Угрешская', 'Удельная',
    'Улица 1905 года', 'Улица Академика Королёва', 'Улица Академика Янгеля', 'Улица Горчакова',
    'Улица Дмитриевского', 'Улица Милашенкова', 'Улица Сергея Эйзенштейна', 'Улица Скобелевская',
    'Улица Старокачаловская', 'Университет', 'Ухтомская', 'Фабричная', 'Филатов Луг', 'Филевский парк', 'Фили',
    'Фирсановская', 'Фонвизинская', 'Фрунзенская', 'Химки', 'Хлебниково', 'Ховрино', 'Хорошёво', 'Хорошёвская',
    'ЦСКА', 'Царицыно', 'Цветной бульвар', 'Черкизовская', 'Чертановская', 'Чеховская', 'Чистые пруды', 'Чкаловская',
    'Шаболовская', 'Шелепиха', 'Шереметьевская', 'Шипиловская', 'Шоссе Энтузиастов', 'Щелковская', 'Щербинка',
    'Щукинская', 'Электрозаводская', 'Юго-Восточная', 'Юго-Западная', 'Южная', 'Ясенево']

SITE_PATTERNS = [
    "http://", "https://", "www.", ".com", ".ru", ".org", ".рф", ".art", ".moscow", ".studio", ".pro",
    ".tilda", ".site", ".company", ".su", ".ltd", ".info", ".москва", ".net", ".shop", ".online", ".store", ".online",
    ".flowers"
]