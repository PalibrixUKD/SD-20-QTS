# Практична робота 3
## Завдання - написати автоматичні тести, використовуючи модулі PyTest

### Спершу необхідно інсталювати бібліотеку. Введіть цю команду у терміналі вашої IDE:
``
pip install pytest
``

### Склонуйте даний репозиторій або скопіюйте файли для роботи з ними:
``
git clone https://github.com/PalibrixUKD/SD-20-QTS.git
``
## На даній гілці є 2 файли із завданнями: 
### 1. math_operations.py
### 2. string_operations.py
## Необхідно створити файл test.py, у якому будуть написані тести для даних функцій.
## У кожній функції написано скільки має бути тестів та які умови перевірятись

## Приклад написання тесту для функції
```python
def test_subtraction():
    assert function_name(2, 3) == -1

def test_is_rabbit():
    with pytest.raises(TypeError):
        function_name('Cow')
```

