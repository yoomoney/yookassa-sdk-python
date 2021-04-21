## Работа с платежами

SDK позволяет создавать, подтверждать, отменять платежи, а также получать информацию о них.

Объект платежа `PaymentResponse` содержит всю информацию о платеже, актуальную на текущий момент времени. 
Он формируется при создании платежа и приходит в ответ на любой запрос, связанный с платежами.

* [Запрос на создание платежа](#Запрос-на-создание-платежа)
* [Запрос на создание платежа через билдер](#Запрос-на-создание-платежа-через-билдер)
* [Запрос на частичное подтверждение платежа](#Запрос-на-частичное-подтверждение-платежа)
* [Запрос на отмену незавершенного платежа](#Запрос-на-отмену-незавершенного-платежа)
* [Получить информацию о платеже](#Получить-информацию-о-платеже)
* [Получить список платежей с фильтрацией](#Получить-список-платежей-с-фильтрацией)

---

### Запрос на создание платежа

[Создание платежа в документации](https://yookassa.ru/developers/api?lang=python#create_payment)

Чтобы принять оплату, необходимо создать объект платежа — `PaymentRequest`. Он содержит всю необходимую информацию 
для проведения оплаты (сумму, валюту и статус). У платежа линейный жизненный цикл, 
он последовательно переходит из статуса в статус.

В ответ на запрос придет объект платежа - `PaymentResponse` в актуальном статусе.

```python
import var_dump as var_dump
from yookassa import Payment

res = Payment.create(
    {
        "amount": {
            "value": 1000,
            "currency": "RUB"
        },
        "confirmation": {
            "type": "redirect",
            "return_url": "https://merchant-site.ru/return_url"
        },
        "capture": True,
        "description": "Заказ №72",
        "metadata": {
            'orderNumber': '72'
        },
        "receipt": {
            "customer": {
                "full_name": "Ivanov Ivan Ivanovich",
                "email": "email@email.ru",
                "phone": "79211234567",
                "inn": "6321341814"
            },
            "items": [
                {
                    "description": "Переносное зарядное устройство Хувей",
                    "quantity": "1.00",
                    "amount": {
                        "value": 1000,
                        "currency": "RUB"
                    },
                    "vat_code": "2",
                    "payment_mode": "full_payment",
                    "payment_subject": "commodity",
                    "country_of_origin_code": "CN",
                    "product_code": "44 4D 01 00 21 FA 41 00 23 05 41 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 12 00 AB 00",
                    "customs_declaration_number": "10714040/140917/0090376",
                    "excise": "20.00",
                    "supplier": {
                        "name": "string",
                        "phone": "string",
                        "inn": "string"
                    }
                },
            ]
        }
    }
)

var_dump.var_dump(res)
```
---

### Запрос на создание платежа через билдер

[Создание платежа в документации](https://yookassa.ru/developers/api?lang=python#create_payment)

Билдер позволяет создать объект платежа — `PaymentRequest` программным способом, через объекты.

```python
import var_dump as var_dump
from yookassa import Payment
from yookassa.domain.models.currency import Currency
from yookassa.domain.models.receipt import Receipt
from yookassa.domain.models.receipt_item import ReceiptItem
from yookassa.domain.common.confirmation_type import ConfirmationType
from yookassa.domain.request.payment_request_builder import PaymentRequestBuilder

receipt = Receipt()
receipt.customer = {"phone": "79990000000", "email": "test@email.com"}
receipt.tax_system_code = 1
receipt.items = [
    ReceiptItem({
        "description": "Product 1",
        "quantity": 2.0,
        "amount": {
            "value": 250.0,
            "currency": Currency.RUB
        },
        "vat_code": 2
    }),
    {
        "description": "Product 2",
        "quantity": 1.0,
        "amount": {
            "value": 100.0,
            "currency": Currency.RUB
        },
        "vat_code": 2
    }
]

builder = PaymentRequestBuilder()
builder.set_amount({"value": 1000, "currency": Currency.RUB}) \
    .set_confirmation({"type": ConfirmationType.REDIRECT, "return_url": "https://merchant-site.ru/return_url"}) \
    .set_capture(False) \
    .set_description("Заказ №72") \
    .set_metadata({"orderNumber": "72"}) \
    .set_receipt(receipt)
    
request = builder.build()
# Можно что-то поменять, если нужно
request.client_ip = '1.2.3.4'
res = Payment.create(request)

var_dump.var_dump(res)
```
---

### Запрос на частичное подтверждение платежа

[Подтверждение платежа в документации](https://yookassa.ru/developers/api?lang=python#capture_payment)

Подтверждает вашу готовность принять платеж. После подтверждения платеж перейдет в статус succeeded. 
Это значит, что вы можете выдать товар или оказать услугу пользователю.

Подтвердить можно только платеж в статусе `waiting_for_capture` и только в течение определенного времени 
(зависит от способа оплаты). Если вы не подтвердите платеж в отведенное время, он автоматически перейдет 
в статус `canceled`, и деньги вернутся пользователю.

В ответ на запрос придет объект платежа в актуальном статусе.
```python
import var_dump as var_dump
from yookassa import Payment

payment_id = '21b23b5b-000f-5061-a000-0674e49a8c10'
res = Payment.capture(payment_id, {
    "amount": {
        "value": "1000.00",
        "currency": "RUB"
    },
    "transfers": [
        {
            "account_id": "123",
            "amount": {
                "value": "300.00",
                "currency": "RUB"
            }
        },
        {
            "account_id": "456",
            "amount": {
                "value": "700.00",
                "currency": "RUB"
            }
        }
    ]
})

var_dump.var_dump(res)
```
[Подробнее о подтверждении и отмене платежей](https://yookassa.ru/developers/payments/payment-process#capture-and-cancel)

---

### Запрос на отмену незавершенного платежа

[Отмена платежа в документации](https://yookassa.ru/developers/api?lang=python#cancel_payment)

Отменяет платеж, находящийся в статусе `waiting_for_capture`. Отмена платежа значит, что вы не готовы 
выдать пользователю товар или оказать услугу. Как только вы отменяете платеж, мы начинаем возвращать деньги на счет плательщика. Для платежей банковскими картами или из кошелька ЮMoney отмена происходит мгновенно. Для остальных способов оплаты возврат может занимать до нескольких дней.

В ответ на запрос придет объект платежа в актуальном статусе.
```python
import var_dump as var_dump
from yookassa import Payment

res = Payment.cancel('21b23b5b-000f-5061-a000-0674e49a8c10')

var_dump.var_dump(res)
```
[Подробнее о подтверждении и отмене платежей](https://yookassa.ru/developers/payments/payment-process#capture-and-cancel)

---

### Получить информацию о платеже

[Информация о платеже в документации](https://yookassa.ru/developers/api?lang=python#get_payment)

Запрос позволяет получить информацию о текущем состоянии платежа по его уникальному идентификатору.

В ответ на запрос придет объект платежа в актуальном статусе.

```python
import var_dump as var_dump
from yookassa import Payment

res = Payment.find_one('21b23b5b-000f-5061-a000-0674e49a8c10')

var_dump.var_dump(res)
```
---

### Получить список платежей с фильтрацией

[Список платежей в документации](https://yookassa.ru/developers/api?lang=python#get_payments_list)

Запрос позволяет получить список платежей, отфильтрованный по заданным критериям.

В ответ на запрос вернется список платежей с учетом переданных параметров. В списке будет информация о платежах, 
созданных за последние 3 года. Список будет отсортирован по времени создания платежей в порядке убывания.

Если результатов больше, чем задано в `limit`, список будет выводиться фрагментами. В этом случае в ответе на запрос 
вернется фрагмент списка и параметр `next_cursor` с указателем на следующий фрагмент.

```python
import var_dump as var_dump
from yookassa import Payment

cursor = None
data = {
    "limit": 2,                                    # Ограничиваем размер выборки
    "payment_method": "yoo_money",                 # Выбираем только оплату через кошелек
    "created_at.gte": "2020-08-08T00:00:00.000Z",  # Созданы начиная с 2020-08-08
    "created_at.lt": "2020-10-20T00:00:00.000Z"    # И до 2020-10-20
}

while True:
    params = data
    if cursor:
        params['cursor'] = cursor
    try:
        res = Payment.list(params)
        print(" items: " + str(len(res.items)))    # Количество платежей в выборке
        print("cursor: " + str(res.next_cursor))   # Указательна следующую страницу
        var_dump.var_dump(res)

        if not res.next_cursor:
            break
        else:
            cursor = res.next_cursor
    except Exception as e:
        print(" Error: " + str(e))
        break

```
[Подробнее о работе со списками](https://yookassa.ru/developers/using-api/lists)