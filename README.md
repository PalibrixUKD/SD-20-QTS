# Практична робота 4

### Команда інсталяції
``
pip install selenium
``

## Завдання 1 - Автоматизувати логін на тестовий сайт та зміну даних користувача

### [Посилання на тестовий сайт](https://opensource-demo.orangehrmlive.com/web/index.php/auth/login)

## Дані, які потрібно автоматизувати:
1. Вхід на сайт
2. Перехід у розділ My Info
3. Зміна:
   * імені - вигадане ім'я, яке складатиметься з перших букв ПІБ, цифра групи та номер у журналі
     * Наприклад, SPM-3-13 
4. Підтвердження змін
5. Вихід з сайту


## Завдання 2 - Автоматизувати форму

### [Посилання на тестовий сайт](https://testpages.eviltester.com/styled/index.html)

## Дані, які потрібно автоматизувати:
1. Перехід на Input Validation форму
2. Автоматизувати заповнення усіх полів
   * використовувати справжні дані, на цьому сайті вони не зберігаються
3. Зберегти форму


## Усі завдання варто документувати на кожному етапі через print() або logging.info() у консоль
## У звіт обов'язково вставити код або посилання на репозиторій, знімки екранів під час виконання програми та консоль

### Для написання коду використовуйте контекстний мененджер:
```python
with closing(webdriver.Chrome()) as driver:
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    driver.implicitly_wait(30)
```
### Він автоматично закриває з'єднання з сайтом

### Деякі приклади використання пошуку за атрибутами чи типом:
```python
driver.find_element(by=By.NAME, value="username")
driver.find_element(by=By.ID, value="firstname")
driver.find_element(by=By.CSS_SELECTOR, value='button[type="submit"]')
driver.find_element(by=By.PARTIAL_LINK_TEXT, value="My Info")

```

# Корисні матеріали:
### [Відеоурок](https://www.youtube.com/watch?v=NB8OceGZGjA&t=3s)
### [Невеличкий туторіал по базових командах](https://www.selenium.dev/documentation/webdriver/getting_started/first_script/)