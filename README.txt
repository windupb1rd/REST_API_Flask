Данная инструкция подготовлена для запуска приложения в ОС Linux

1. Перейти в папку с проектом и создать виртуальную среду:
cd <project_folder>
python3 -m venv venv
При возникновении ошибки, необходимо установить venv следующей командой:
sudo apt install python3-venv


2. Активировать виртуальную среду и установить в нее необходимые библиотеки из файла requirements.txt:
source venv/bin/activate
pip install -r requirements.txt


3. Создать и запустить контейнер с БД:
sudo docker-compose up -d
Если Docker и Docker-compose не установлены в системе, то установить, используя следующие ссылки:
https://docs.docker.com/engine/install/
https://docs.docker.com/compose/install/


4. Для запуска веб-сервера с приложением запустить скрипт start_app.sh,
 предварительно сделав его исполняемым с помощью команды: chmod a+x start_app.sh
 База данных и таблица создадутся автоматически при первом запуске веб-сервера


5. Для проверки использовать следующую команду:
curl -i -H "Content-Type: application/json" -X POST http://localhost:5000/api/questions -d '{"questions_num":1}'

