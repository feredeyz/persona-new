<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://i.imgur.com/6wj0hh6.jpg" alt="Project logo"></a>
</p>

<h3 align="center">Образовательная платформа Persona</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-build-success.svg)]()

</div>

---

<p align="center">
<b><i>Persona</i></b> - образовательная платформа для размещения и продажи онлайн-курсов.
    <br> 
</p>

---

- [О проекте](#about)
- [Для начала](#getting_started)
- [Использование](#usage)
- [Сделано с использованием](#built_using)
- [Авторы](#authors)
- [Благодарности](#acknowledgement)

## 🧐 О проекте <a name = "about"></a>

***Persona*** создана, чтобы любой человек мог получить доступ к любым курсам и дать удобный интерфейс для создания собственных курсов и заработка на этом.

## 🏁 Для начала <a name = "getting_started"></a>

Эти инструкции позволят вам получить копию проекта, запущенную и работающую на локальной машине для целей разработки и тестирования. См. [deployment](#deployment) для заметок о том, как развернуть проект в работающей системе.

### Зависимости

Чтобы установить зависимости для API, выполните эти команды:

```
cd api
python3 -m venv .venv
source .venv/bin/activate
pip install -r pyproject.toml
```

Чтобы установить зависимости для Frontend, выполните эти команды:
```
cd frontend
npm i
```

## 🎈 Использование <a name="usage"></a>

Сначала запустите API:
```
cd api/persona
python manage.py runserver
```

Потом Frontend:
```
cd frontend
npm run dev # Для обычного запуска
npm run build # Для билда перед деплоем
```

## ⛏️ Сделано с использованием <a name = "built_using"></a>

- [PostgreSQL](https://www.postgresql.org/) - База данных
- [Django REST framework](https://www.django-rest-framework.org/) - Фреймворк API
- [ReactJS](https://react.dev/) - Фреймворк Frontend
- [Python](https://python.org/) - Серверное окружение

## ✍️ Авторы <a name = "authors"></a>

- [@feredeyz](https://github.com/feredeyz) - Идея и реализация

## 🎉 Благодарности <a name = "acknowledgement"></a>

- Всем, чей код был использован
- ChatGPT, DeepSeek
- Референсы