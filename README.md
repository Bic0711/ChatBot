# Rut_moooovie



[Перейти к разделу "Как пользоваться"](#как-пользоваться)

[Перейти к разделу"Базовые команды"](#базовые-команды-действующие-в-любом-месте-диалога)

[Перейти к разделу"Контекстные команды"](#контекстные-командыработают-в-конкретных-случаях)


[Перейти к разделу" Цель создания проекта"](#цель-создания-проекта)


[Перейти к разделу"как Запустить"](#как-запустить)

# Цель создания проекта
- Создание личных списков фильмов, таких как:
    1. Список фильмов к просмотру.
    2. Список просмотренных фильмов.
    3. Список фильмов которые не планируются к просмотру.
    
    Посредством поиска фильмов с разными настройками(рандомный фильм какого либо года, жанра, страны, режиссера и т.д.)
- И сортировка и отображение этих списков по фильтрам
    - год
    - жанр
    - страна
    - рейтинг
    - возрастной рейтинг

Бот работает с API Kinopoisk

# Как пользоваться.
Предоставление ботом кнопок для выбора фильтров,списков, или параметров поиска.
В случаях, когда нужен ввод сообщения от пользователя бот запрашивает и объясняет что нужно.



# Типы команд
## Базовые команды (действующие в любом "месте" диалога).
`/start` - Начальная команда которая запускает бота, приветствует пользователя, объясняет что это за бот,для чего он нужен,что умеет,и дает подсказки к следующим шагам.

**Пример ответа:**

    Привет,я Rut_Moovie Bot.
    Я помогу тебе найти фильм.

    Вот доступные кнопки:
    случ. фильм - Показывает случайный фильм
    год - показывает случайный фильм выбранного года
    страна - показывает случайный фильм выбраной страны
    режиссер - показывает случайный фильм режиссера
    актер - показывает случайный фильм с выбранным актером
    поиск - поиск фильма по параметрам



`/help` - Команда которая выводит подсказку со всеми базовыми командами.

**Пример ответа:**

    Привет, вот все доступные команды(они работают в любом разделе и в любой момент диалога):

    /help - вывод всех доступных команд
    /clean - стереть весь диалог
    /about - показать описание, цель и функции бота
    /start_search_movie - начать поиск фильма
    /black_list_show - показать список режиссеров,актеров,жанров или конкретных фильмов которые исключены из поиска
    /black_list_add - добавить что или кого-либо в список исключений
    /to_see_list_show - Показать список непросмотренных фильмов которые ты хочешь посмотреть

`/clean` - очистить диалог

`/about` - Вывести информацию о боте.

**Пример ответа:**

    Привет, я Rut_moovie.
    Я сделан для того чтобы ты мог:  
    - составить собственный список фильмов к просмотру
    - составить список актеров, режиссеров, стран и тд которые ты хочешь исключить из поиска
    - найти конкретный фильм
    - найти случайный фильм
    - найти случайный фильм по какому либо параметру(год,режиссер,рейтинг кинопоиска и тд)

`/search_movie`

**Пример ответа**

    Хорошо,давай найдем фильмы, как ты хочешь искать?
    /id_movie - поиск по ID с кинопоиска
    /rand_movie - рандомный фильм
    /rand_movie_year - рандомный фильм конкретного года
    /rand_movie_country - рандомный фильм конкретной страны
    /rand_movie_genre - рандомный фильм конкретного жанра

`/black_list_show`

**Пример ответа:**

    Привет, вот твой "черный список":
    Режиссеры:
        - Стивен Спилберг
        - Мартин Скорсезе
        - Квентин Тарантино
    Актеры:
        -Мэрил Стрип
        -Марлон Брандо
        -Кэтрин Хепбёрн
    Годы:
        -1976
        -1994
        -2010
    Страны:
        -Сша
        -Франция
        -Индия
    Фильмы:
        -Крестный отец
        -Список Шиндлера
        -Касабланка

    *так же из глобального поиска исключаются фильмы находящиеся в ваших списках'к просмотру' и 'просмотрено'

`/black_list_add`

**Пример ответа**

    Давай добавим что-нибудь в "черный лист".
    Напиши через пробел категорию того что хочешь добавить и что ты хочешь добавить.
    Например:
        Режиссер Гай Ричи
    или:
        Актер Роберт Де Ниро

## Контекстные команды(Работают в конкретных случаях)

### /search_movie

`/id_movie`

    Показывает фильм с конкретным ID с кинопоиска

пример запроса к API:

    https://api.kinopoisk.dev/v1.4/movie/300

Пример ответ запроса:

``` {
  "fees": {
    "world": {
      "value": 55534455,
      "currency": "$"
    },
    "usa": {
      "value": 42734455,
      "currency": "$"
    }
  },
  "status": null,
  "externalId": {
    "imdb": "tt0306841",
    "tmdb": 18736,
    "kpHD": "4255a9dbf9244d6e8b6d49e49c76074e"
  },
  "rating": {
    "kp": 6.314,
    "imdb": 5.5,
    "filmCritics": 5.3,
    "russianFilmCritics": 0,
    "await": null
  },
  "votes": {
    "kp": 11420,
    "imdb": 42331,
    "filmCritics": 102,
    "russianFilmCritics": 0,
    "await": 0
  },
  "backdrop": {
    "url": "https://image.openmoviedb.com/kinopoisk-ott-images/374297/2a00000177fbf21f44f8c5101cfb16d448ed/orig",
    "previewUrl": "https://image.openmoviedb.com/kinopoisk-ott-images/374297/2a00000177fbf21f44f8c5101cfb16d448ed/x1000"
  },
  "movieLength": 94,
  "images": {
    "framesCount": 10
  },
  "productionCompanies": [
    {
      "name": "Teen Life Productions",
      "url": null,
      "previewUrl": null
    },
    {
      "name": "Walt Disney Pictures",
      "url": "https://www.themoviedb.org/t/p/original/wdrCwmRnLFJhEoH8GSfymY85KHT.png",
      "previewUrl": "https://www.themoviedb.org/t/p/w500/wdrCwmRnLFJhEoH8GSfymY85KHT.png"
    }
  ],
  "spokenLanguages": [
    {
      "name": "English",
      "nameEn": "English"
    }
  ],
  "id": 300,
  "type": "movie",
  "name": "Лиззи Магуайр",
  "description": "Тринадцатилетняя школьница Лиззи Магуайер и ее приятели Гордо, Кейт и Эсан собираются оттянуться по полной программе во время их поездки с классом в Италию.\n\nНо там случается весьма неожиданное происшествие: девочку ошибочно принимают за итальянскую поп-звезду Изабеллу, да к тому же девушка влюбляется в бывшего дружка Изабеллы Паоло. Когда родители Лизи обо всем узнают, они вместе с ее братом Мэттом срочно вылетают в Италию.\n\nНо Лиззи уже не та закомплексованная девочка-подросток, кем была раньше, она до такой степени вжилась в роль певицы, что и на самом деле стала самой настоящей звездой.",
  "distributors": {
    "distributor": null,
    "distributorRelease": "Уолт Дисней Компани СНГ"
  },
  "premiere": {
    "world": "2003-04-26T00:00:00.000Z",
    "dvd": "2011-06-14T00:00:00.000Z",
    "bluray": null,
    "cinema": null,
    "digital": null,
    "russia": null
  },
  "slogan": "Lizze McGuire goes to Rome.",
  "year": 2003,
  "budget": {
    "value": 17000000,
    "currency": "$"
  },
  "poster": {
    "url": "https://image.openmoviedb.com/kinopoisk-images/4303601/a60e881c-c989-4a26-bbaf-c8323ffbf600/orig",
    "previewUrl": "https://image.openmoviedb.com/kinopoisk-images/4303601/a60e881c-c989-4a26-bbaf-c8323ffbf600/x1000"
  },
  "facts": null,
  "genres": [
    {
      "name": "мелодрама"
    },
    {
      "name": "комедия"
    },
    {
      "name": "приключения"
    },
    {
      "name": "семейный"
    },
    {
      "name": "музыка"
    }
  ],
```

`/rand_movie`

    Показывает рандомный фильм

пример запроса к API:

    https://api.kinopoisk.dev/v1.4/movie/random

Пример ответ запроса:

```{


    
  "id": 2001001,
  "alternativeName": "The Hail Mary",
  "collections": [],
  "countries": [
    {
      "name": "США"
    }
  ],
  "createdAt": "2022-01-26T14:23:39.075Z",
  "description": null,
  "enName": null,
  "externalId": {
    "kpHD": null,
    "imdb": "tt13557860",
    "tmdb": null
  },
  "facts": [],
  "genres": [
    {
      "name": "драма"
    }
  ],
  "movieLength": 61,
  "name": null,
  "names": [
    {
      "name": "The Hail Mary"
    }
  ]
  ```

`/rand_movie_year`

    Показывает рандомный фильм какого-либо года

пример запроса к API:

    https://api.kinopoisk.dev/v1.4/movie/random?year=1993

Пример ответа запроса:

```{
  "status": null,
  "externalId": {
    "imdb": "tt0106184",
    "tmdb": 306556,
    "kpHD": null
  },
  "rating": {
    "kp": 0,
    "imdb": 5.4,
    "filmCritics": 0,
    "russianFilmCritics": 0,
    "await": 0
  },
  "votes": {
    "kp": 14,
    "imdb": 18,
    "filmCritics": 0,
    "russianFilmCritics": 0,
    "await": 0
  },
  "backdrop": {
    "url": null,
    "previewUrl": null
  },
  "movieLength": 94,
  "images": {
    "framesCount": 0
  },
  "productionCompanies": [],
  "spokenLanguages": [
    {
      "name": "普通话",
      "nameEn": "Mandarin"
    },
    {
      "name": "广州话 / 廣州話",
      "nameEn": "Cantonese"
    }
  ],
  "id": 221970,
  "type": "movie",
  "name": "Глотай мою пыль",
  "description": null,
  "distributors": {
    "distributor": null,
    "distributorRelease": null
  },
  "premiere": {
    "bluray": null,
    "cinema": null,
    "digital": null,
    "dvd": null,
    "russia": null,
    "world": null
  },
  "slogan": null,
  "year": 1993,
  "poster": {
    "url": "https://image.openmoviedb.com/kinopoisk-images/1599028/be662dde-24e7-4887-b543-e1fa938d7e3e/orig",
    "previewUrl": "https://image.openmoviedb.com/kinopoisk-images/1599028/be662dde-24e7-4887-b543-e1fa938d7e3e/x1000"
  },
  "facts": [],
  "genres": [],
  "countries": [
    {
      "name": "Тайвань"
    },
    {
      "name": "Гонконг"
    }
  ]
  ```


`/rand_movie_country`

пример запроса к API:

    https://api.kinopoisk.dev/v1.4/movie/random?countries.name=%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D1%8F

Пример ответ запроса:

```{
  "id": 977702,
  "type": "movie",
  "externalId": {
    "kpHD": null
  },
  "name": "Урок рисования для взрослых",
  "rating": {
    "kp": 0,
    "imdb": 0,
    "filmCritics": 0,
    "russianFilmCritics": 0,
    "await": 0
  },
  "description": "Любе — 26, Вере — 40 лет. Они встретились на уроках рисования. Для Веры их встреча — случайность, для Любы — необходимость. Любовь к одному и тому же мужчине положит начало их короткой дружбе.",
  "votes": {
    "kp": 152,
    "imdb": 0,
    "filmCritics": 0,
    "russianFilmCritics": 0,
    "await": 0
  },
  "distributors": {
    "distributor": null,
    "distributorRelease": null
  },
  "premiere": {
    "bluray": null,
    "cinema": null,
    "digital": null,
    "dvd": null,
    "russia": null,
    "world": null
  },
  "slogan": null,
  "year": 2016,
  "poster": {
    "url": "https://image.openmoviedb.com/kinopoisk-images/4774061/a799db52-fb57-4936-a802-9150c8e0dfa3/orig",
    "previewUrl": "https://image.openmoviedb.com/kinopoisk-images/4774061/a799db52-fb57-4936-a802-9150c8e0dfa3/x1000"
  },
  "facts": [],
  "genres": [
    {
      "name": "короткометражка"
    }
  ],
  "countries": [
    {
      "name": "Россия"
    }
  ]
  ```

`/rand_movie_genre`

пример запроса к API:

    https://api.kinopoisk.dev/v1.4/movie/random?genres.name=%D0%B4%D1%80%D0%B0%D0%BC%D0%B0

Пример ответ запроса:

```{
  "id": 41146,
  "type": "movie",
  "externalId": {
    "kpHD": null,
    "imdb": "tt0109653"
  },
  "name": "Дорога в рай",
  "rating": {
    "kp": 0,
    "imdb": 6.6,
    "filmCritics": 0,
    "russianFilmCritics": 0,
    "await": 0
  },
  "description": "Москва, 1957 год, Всемирный Фестиваль Молодежи и Студентов.  «Всеобщая дружба» осуществляется под бдительным надзором  всесильного КГБ. Игорь Синицкий, студент МГУ и талантливый  джазмен, живет у дяди, академика Лернера, в «режимном» доме. Работой  академика очень интересуется иностранная разведка.\n\nПохитить  секретные документы Лернера по разработке химического оружия  поручено очаровательной француженке Мишель. В свою очередь,  вездесущий КГБ вербует Игоря, используя для этого весьма грязные  методы. Разведки двух стран учли все, кроме одного - возможности  появления настоящего чувства между молодыми людьми. Но это  происходит, и события ускользают из-под контроля разведчиков,  развиваясь по новому сценарию, написанному любовью и звездами.",
  "votes": {
    "kp": 139,
    "imdb": 31,
    "filmCritics": 0,
    "russianFilmCritics": 0,
    "await": 0
  },
  "distributors": {
    "distributor": null,
    "distributorRelease": null
  },
  "premiere": {
    "russia": "1993-01-01T00:00:00.000Z",
    "bluray": null,
    "cinema": null,
    "digital": null,
    "dvd": null,
    "world": null
  },
  "slogan": null,
  "year": 1993,
  "poster": {
    "url": "https://image.openmoviedb.com/kinopoisk-images/1704946/f1d8707a-545b-406c-8144-9cc2c7acd4ea/orig",
    "previewUrl": "https://image.openmoviedb.com/kinopoisk-images/1704946/f1d8707a-545b-406c-8144-9cc2c7acd4ea/x1000"
  },
  "facts": [],
  "genres": [
    {
      "name": "драма"
    }
  ],
  "countries": [
    {
      "name": "Германия"
    },
    {
      "name": "Россия"
    }
  ]
  ```


# Как запустить.

1) Клонируйте репозиторий

    git clone https://gitlab.skillbox.ru/leonid_rutkovskii/movie_bot.git

2) Перейдите в папку с ботом
    
    cd movie_bot

3) установите зависимости

  pip install -r requirements.txt

4) запустите бота

  python main.py


[Перейти в начало](#rut_moooovie)