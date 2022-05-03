1. Перейти в папку с проектом и создать виртуальную среду:
cd <project_folder>
python3 -m venv venv


2. Активировать виртуальную среду и установить в нее необходимые библиотеки из файла requirements.txt:
source venv/bin/activate
pip install -r requirements.txt


3. Создать и запустить контейнер с БД:
sudo docker-compose up -d


4. Для запуска веб-сервера с приложением запустить скрипт start_app.sh,
 предварительно сделав его исполняемым с помощью команды: chmod a+x start_app.sh.
 База данных и таблица создадутся автоматически при первом запуске веб-сервера.


5. Для проверки использовать следующую команду:
curl -i -H "Content-Type: application/json" -X POST http://localhost:5000/api/questions -d '{"questions_num":1}'

