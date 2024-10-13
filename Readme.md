Алгоритм запуска проекта для выполнения задач в рабочей среде:
1. выполнить docker-compose up для файла docker-compose-pyback.yml
- - при старте контейнера с google диска подгружаются веса для нейросети
3. запустить c# проект ConsoleClient
## ЗАПУСК НА ДВУХ МАШИНАХ
- Изначально решение настроено для отладки на одном хосте, но изменив параметры подключения есть возможность запустить grcp клиент и сервис
на разных машинах.
- Адрес grcp сервиса указывается в PyBack/Main.py в функции serve(); 
```python
server.add_insecure_port("[::]:50051")
```
- Адрес, по которому подключается grcp клиент указывается в файле Program.cs проекта ConsoleClient.cs
```C#
string grcpAdress = "http://localhost:50051"; // replace with your gRPC server address
```