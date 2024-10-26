## Syntetic Hand Dataset guide
# Функциональные компоненты решения: CServer, ConsoleClient, FRONT, PyBack (имена соответствуют папками в корне репозитория)
- Связка CServer, FRONT, PyBack является вариантом сборки приложения для онлайн-использования с выносом задачи генерации на отдельный IP локальной сети или без него. Следовательно реализуется в двух вариантах:
- 1. В рамках одного хоста: выполняем "compose up" файла docker-compose-pyneural-cserver-front.yml
- - 1. При сборке веб приложения на одном хосте дополнительная настройка не требуется
- - 2. Переходим по ссылке https://localhost:5173
- 2. Для отделения генерации от веб-части: 
- 2. 1. "compose up" docker-compose-pyneural-cserver-front.yml
- 2. 2. создаем image компонента PyBack с помощью файла docker-compose-pyneural.yml и запускаем его на другой машине
- Связка ConsoleClient и PyBack служит для прикладного использования в рамках корпоративной локальной сети. Реализация:
- 1. Создаем image компонента PyBack с помощью файла docker-compose-pyneural.yml и запускаем его
- 2. Помещать консольную клиентскую часть, принимающую поток генераций датасета в контейнер нерентабельно поэтому просто собираем как проект .NET и запускаем компонент ConsoleClient на машине, на которой будет производиться обучение новой нейросети.
# Мануал по настройке консольного варианта приложения для развертывания генерирующего микросервиса в WSL и потокового сохранения датасета в клиентской части (Windows) на двух ПК, находящихся в локальной сети
1. Сервис gRPC (PyBack) прослушивает порт 50051 на любом IP, проброс портов в рамках docker'а уже выполнен.
2. Организация канала windows-windows-wsl-docker
- 1. Запуск сервиса с нейросетью:
- - 1. docker run -d -p 50051:50051 имя_контейнера
- - 2. При первом запуске с google диска подгрузится последняя версия весов для нейросети
- 2. Настройка машины с сервисом
- - 1. Узнать IP-адрес WSL2 
``` bash
ip addr show eth0 | grep inet
```
- - 2. Проброс порта через PowerShell (<WSL_IP> меняем на свой)
``` PowerShell
netsh interface portproxy add v4tov4 listenaddress=0.0.0.0 listenport=50051 connectaddress=<WSL_IP> connectport=50051
```
- - 3. Разрешение доступа через брандмауэр Windows
``` PowerShell
netsh advfirewall firewall add rule name="Docker WSL2 Access" dir=in action=allow protocol=TCP localport=50051
```
3. Запускаем ConsoleClient на клиентской машине, указываем путь для сохранения датасета и его параметры
- - в коде ConsoleClient/Program.cs меняем адрес gRPC сервиса на адрес машины с WSL в локальной сети
``` C#
string grcpAdress = "http://192.168.1.100:50051"; // replace with your gRPC server address
```

