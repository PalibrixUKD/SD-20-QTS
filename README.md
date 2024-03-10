# Практична робота 3
## Завдання - написати автоматичні тести, використовуючи модулі PyTest та requests

### Спершу необхідно інсталювати бібліотеки. Введіть ці команди у терміналі вашої IDE:
``
pip install pytest
``
``
pip install requests
``

### Склонуйте даний репозиторій або скопіюйте файли для роботи з ними:
``
git clone https://github.com/PalibrixUKD/SD-20-QTS.git
``
# Завдання 1
### На даній гілці є 2 файли із завданнями: 
### 1. math_operations.py
### 2. string_operations.py
### Необхідно створити файл test.py, у якому будуть написані тести для даних функцій.
### У кожній функції написано скільки має бути тестів та які умови перевірятись

# Завдання 2
### Окрім наперед написаних функцій, необхідно протестувати відкрите АПІ
### ``https://github.com/15Dkatz/official_joke_api``
### Дане посилання містить інструкцію щодо використання API
### Тести, які необхідно написати:
1. Вибір існуючого об'єкту за ID
2. Вибір неіснуючого об'єкту за ID
3. Вибір об'єкту за типом
4. Довжину при виборі десяти жартів

## Приклад написання тесту для функції
```python
def test_subtraction():
    assert function_name(2, 3) == -1

def test_is_rabbit():
    with pytest.raises(TypeError):
        function_name('Cow')
```

## Приклад написання тесту для API
```python
import requests

def test_api_status():
    response = requests.get("https://official-joke-api.appspot.com/jokes/370")
    assert response.status_code == 200
    data = response.json()
    assert data['type'] == 'programming'
```