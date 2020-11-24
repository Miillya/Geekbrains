# python-flask-docker
### Итоговый проект (пример) курса "Машинное обучение в бизнесе"

**Стек:**

ML: sklearn, pandas, numpy  
API: flask  
Данные: с kaggle - https://www.kaggle.com/c/catch-me-if-you-can-intruder-detection-through-webpage-session-tracking2   

**Description / Задание:**

(Russian version below)


Web-user identification is a hot research topic on the brink of sequential pattern mining and behavioral psychology.

Here we try to identify a user on the Internet tracking his/her sequence of attended Web pages. The algorithm to be built will take a webpage session (a sequence of webpages attended consequently by the same person) and predict whether it belongs to Alice or somebody else.

The data comes from Blaise Pascal University proxy servers. Paper "A Tool for Classification of Sequential Data" by Giacomo Kahn, Yannick Loiseau and Olivier Raynaud.


Будем решать задачу идентификации взломщика по его поведению в сети Интернет. Это сложная и интересная задача на стыке анализа данных и поведенческой психологии. В качестве примера, компания Яндекс решает задачу идентификации взломщика почтового ящика по его поведению. В двух словах, взломщик будет себя вести не так, как владелец ящика: он может не удалять сообщения сразу по прочтении, как это делал хозяин, он будет по-другому ставить флажки сообщениям и даже по-своему двигать мышкой. Тогда такого злоумышленника можно идентифицировать и "выкинуть" из почтового ящика, предложив хозяину войти по SMS-коду. Этот пилотный проект описан в статье на Хабрахабре. Похожие вещи делаются, например, в Google Analytics и описываются в научных статьях, найти можно многое по фразам "Traversal Pattern Mining" и "Sequential Pattern Mining".

В этом соревновании будем решать похожую задачу: алгоритм будет анализировать последовательность из нескольких веб-сайтов, посещенных подряд одним и тем же человеком, и определять, Элис это или взломщик (кто-то другой).

Данные собраны с прокси-серверов Университета Блеза Паскаля. "A Tool for Classification of Sequential Data", авторы Giacomo Kahn, Yannick Loiseau и Olivier Raynaud.

**Target / Целевая переменная:**

Target

**Evaluation / Метрика для оценки:**


The target metric is ROC AUC. / Целевая метрика – ROC AUC.

**Data Description**

(Russian version below)

The train set train_sessions.csv contains information on user browsing sessions where the features are:

site_i – are ids of sites in this session. The mapping is given with a pickled dictionary site_dic.pkl
time_j – are timestamps of attending the corresponding site
target – whether this session belongs to Alice
One can use the original data train.zip to form a train set differing from train_sessions.csv.


В обучающей выборке train_sessions.csv:

Признаки site_i – это индексы посещенных сайтов (расшифровка дана в pickle-файле со словарем site_dic.pkl)
Признаки time_j – время посещения сайтов site_j
Целевой признак target – факт того, что сессия принадлежит Элис (то есть что именно Элис ходила по всем этим сайтам)
Задача – сделать прогнозы для сессий в тестовой выборке (test_sessions.csv), определить, принадлежат ли они Элис. Не обязательно ограничиваться только предложенной выборкой train_sessions.csv – в train.zip даны исходные данные о посещенных пользователями веб-страницах, по которым можно сформировать свою обучающую выборку.

### Описание датасета:

* **site1** - индекс 1-го посещенного сайта в сессии
* **time1** - время посещения 1-го сайта в сессии
* **...**
* **site10** - индекс 10-го посещенного сайта в сессии
* **time10** - время посещения 10-го сайта в сессии
* **target** – целевая переменная, принимает значение 1 для сессий Элис и 0 для сессий других пользователей

### Клонируем репозиторий и создаем образ
```
$ git clone https://github.com/busiko7/Geekbrains/tree/master/%D0%9C%D0%B0%D1%88%D0%B8%D0%BD%D0%BD%D0%BE%D0%B5%20%D0%BE%D0%B1%D1%83%D1%87%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%B2%20%D0%B1%D0%B8%D0%B7%D0%BD%D0%B5%D1%81%D0%B5/Course_project
$ cd Course_project
$ docker build -t Course_project .
```

### Запускаем контейнер
```
$ docker run -d -p 8180:8180 -p 8181:8181 Course_project
```

### Переходим на localhost:8181
