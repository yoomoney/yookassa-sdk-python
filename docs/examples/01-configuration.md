## Настройки SDK API ЮKassa

[Справочник API ЮKassa](https://yookassa.ru/developers/api)

С помощью этого SDK вы можете работать с онлайн-платежами: отправлять запросы на оплату, 
сохранять платежную информацию для повторных списаний, совершать возвраты и многое другое.

* [Аутентификация](#Аутентификация)
* [Статистические данные об используемом окружении](#Статистические-данные-об-используемом-окружении)
* [Получение информации о магазине](#Получение-информации-о-магазине)
* [Работа с Webhook](#Работа-с-Webhook)
* [Входящие уведомления](#Входящие-уведомления)

---

### Аутентификация

Для работы с API необходимо прописать в конфигурации данные аутентификации. Существует два способа аутентификации:
- shopId + секретный ключ
- OAuth-токен. [Подробнее в документации к API](https://yookassa.ru/developers/partners-api/basics)

```python
from yookassa import Configuration
# shopId + секретный ключ
Configuration.configure('XXXXXX', 'test_XXXXXXXX')
# или OAuth-токен
Configuration.configure_auth_token('token-XXXXXXXX')
```

---

### Статистические данные об используемом окружении

Для поддержки качества, а также быстром реагировании на ошибки, SDK передает статистику в запросах к API ЮKassa.

По молчанию, SDK передает в запросах версию операционной системы, версию Python, а также версию SDK. 
Но вы можете передать дополнительные данные об используемом фреймворке, CMS, а также модуле в CMS.

Например, это может выглядеть так:
```python
from yookassa import Configuration
from yookassa.domain.common.user_agent import Version

Configuration.configure_user_agent(
    framework=Version('Django', '2.2.3'),
    cms=Version('Wagtail', '2.6.2'),
    module=Version('Y.CMS', '0.0.1')
)
```

---

### Получение информации о магазине

После установки конфигурации можно проверить корректность данных, а также получить информацию о магазине.

```python
import var_dump as var_dump
from yookassa import Settings

me = Settings.get_account_settings()
var_dump.var_dump(me)
```
В результате мы увидим примерно следующее:
```
#0 dict(5) 
    ['account_id'] => str(6) "XXXXXX"
    ['test'] => bool(True) 
    ['fiscalization_enabled'] => bool(True) 
    ['payment_methods'] => list(2) 
        [0] => str(9) "yoo_money"
        [1] => str(9) "bank_card"
    ['status'] => str(7) "enabled"
```
[Подробнее в документации к API](https://yookassa.ru/developers/api?lang=python#me_object)

---

### Работа с Webhook

Если вы подключаетесь к API через Oauth-токен, то можете настроить получение уведомлений о смене статуса платежа или возврата.

Например, ЮKassa может сообщить, когда объект платежа, созданный в вашем приложении, перейдет в статус `waiting_for_capture`.

В данном примере мы устанавливаем вебхуки для succeeded и canceled уведомлений.
А так же проверяем, не установлены ли уже вебхуки. И если установлены на неверный адрес, удаляем.

```python
import var_dump as var_dump
from yookassa import Webhook
from yookassa.domain.notification import WebhookNotificationEventType

whUrl = 'https://merchant-site.ru/payment-notification'
needWebhookList = [
    WebhookNotificationEventType.PAYMENT_SUCCEEDED,
    WebhookNotificationEventType.PAYMENT_CANCELED
]

whList = Webhook.list()

for event in needWebhookList:
    hookIsSet = False
    for wh in whList.items:
        if wh.event != event:
            continue
        if wh.url != whUrl:
            Webhook.remove(wh.id)
        else:
            hookIsSet = True

    if not hookIsSet:
        Webhook.add({"event": event, "url": whUrl})
        
var_dump.var_dump(Webhook.list())
```

В результате мы увидим примерно следующее:
```
#0 object(WebhookList) (2)
    _WebhookList__items => list(2) 
        [0] => object(WebhookResponse) (3)
            _WebhookResponse__id => str(39) "wh-52e51c6e-29a2-4a0d-800b-01cf022b5613"
            _WebhookResponse__event => str(16) "payment.canceled"
            _WebhookResponse__url => str(66) "https://merchant-site.ru/payment-notification"
        [1] => object(WebhookResponse) (3)
            _WebhookResponse__id => str(39) "wh-c331b3ee-fb65-428d-b008-1b837d9c4d93"
            _WebhookResponse__event => str(17) "payment.succeeded"
            _WebhookResponse__url => str(66) "https://merchant-site.ru/payment-notification"
    _WebhookList__type => str(4) "list"
```
[Подробнее в документации к API](https://yookassa.ru/developers/api?lang=python#webhook)

### Входящие уведомления

Если вы хотите отслеживать состояние платежей и возвратов, вы можете подписаться на уведомления ([webhook](#Работа-с-Webhook), callback).

Уведомления пригодятся в тех случаях, когда объект API изменяется без вашего участия.
Например, если пользователю нужно подтвердить платеж, процесс оплаты может занять от нескольких минут до нескольких часов.
Вместо того чтобы всё это время периодически отправлять GET-запросы, чтобы узнать статус платежа, вы можете просто дожидаться уведомления от ЮKassa.

[Входящие уведомления в документации](https://yookassa.ru/developers/using-api/webhooks?lang=python)

#### Использование

Как только произойдет событие, на которое вы подписались, на URL, который вы указали при настройке, придет уведомление.
В нем будут все данные об объекте на момент, когда произошло событие.

Вам нужно подтвердить, что вы получили уведомление. Для этого ответьте HTTP-кодом 200. ЮKassa проигнорирует всё,
что будет находиться в теле или заголовках ответа. Ответы с любыми другими HTTP-кодами будут считаться невалидными,
и ЮKassa продолжит доставлять уведомление в течение 24 часов, начиная с момента, когда событие произошло.

#### Пример обработки уведомления с помощью SDK

```python
import json
from django.http import HttpResponse
from yookassa import Configuration, Payment
from yookassa.domain.notification import WebhookNotificationEventType, WebhookNotificationFactory

def my_webhook_handler(request):
    # Извлечение JSON объекта из тела запроса
    event_json = json.loads(request.body)
    try:
        # Создание объекта класса уведомлений в зависимости от события
        notification_object = WebhookNotificationFactory().create(event_json)
        response_object = notification_object.object
        if notification_object.event == WebhookNotificationEventType.PAYMENT_SUCCEEDED:
            some_data = {
                'paymentId': response_object.id,
                'paymentStatus': response_object.status,
            }
            # Специфичная логика
            # ...
        elif notification_object.event == WebhookNotificationEventType.PAYMENT_WAITING_FOR_CAPTURE:
            some_data = {
                'paymentId': response_object.id,
                'paymentStatus': response_object.status,
            }
            # Специфичная логика
            # ...
        elif notification_object.event == WebhookNotificationEventType.PAYMENT_CANCELED:
            some_data = {
                'paymentId': response_object.id,
                'paymentStatus': response_object.status,
            }
            # Специфичная логика
            # ...
        elif notification_object.event == WebhookNotificationEventType.REFUND_SUCCEEDED:
            some_data = {
                'refundId': response_object.id,
                'refundStatus': response_object.status,
                'paymentId': response_object.payment_id,
            }
            # Специфичная логика
            # ...
        elif notification_object.event == WebhookNotificationEventType.DEAL_CLOSED:
            some_data = {
                'dealId': response_object.id,
                'dealStatus': response_object.status,
            }
            # Специфичная логика
            # ...
        elif notification_object.event == WebhookNotificationEventType.PAYOUT_SUCCEEDED:
            some_data = {
                'payoutId': response_object.id,
                'payoutStatus': response_object.status,
                'dealId': response_object.deal.id,
            }
            # Специфичная логика
            # ...
        elif notification_object.event == WebhookNotificationEventType.PAYOUT_CANCELED:
            some_data = {
                'payoutId': response_object.id,
                'payoutStatus': response_object.status,
                'dealId': response_object.deal.id,
            }
            # Специфичная логика
            # ...
        else:
            # Обработка ошибок
            return HttpResponse(status=400)  # Сообщаем кассе об ошибке

        # Специфичная логика
        # ...
        Configuration.configure('XXXXXX', 'test_XXXXXXXX')
        # Получим актуальную информацию о платеже
        payment_info = Payment.find_one(some_data['paymentId'])
        if payment_info:
            payment_status = payment_info.status
            # Специфичная логика
            # ...
        else:
            # Обработка ошибок
            return HttpResponse(status=400)  # Сообщаем кассе об ошибке
        
    except Exception:
        # Обработка ошибок
        return HttpResponse(status=400)  # Сообщаем кассе об ошибке

    return HttpResponse(status=200)  # Сообщаем кассе, что все хорошо
```
