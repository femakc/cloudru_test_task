# Описание тестового задания для поступления в DevOps Cloud.ru Camp

Тестовое задание состоит из двух задач.

## 1. Ansible playbook

 Ansible playbook, выполняет на хосте следующие действия:

- создает нового пользователя cloudru с паролем cloudpass
- разрешает на хосте авторизацию через ssh по ключу
- запрещает логин по ssh от пользователя root
- копирует предоставленный публичный ключ для пользователя cloudru

Плейбук проверен относительно ОС Ubuntu Server 22.04.3. 

Публичный ключ для публикации на хост:

```
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCfrfE0OluoNHb5dOpV4RpWmVXvMBWc17kaM7DDjCm7romNQMDX95i5Fc67Q3c47pvrm/qi/ZqsCeqNdLl5+VV41rVz701Pj/UUr2FZpIm80Ur0iM1DFy81GKo/lS1INopqdd4KvUnM2d8yqfJSm9m5Cq7AM9S0mqObuMayfqNR4YcOlm9fnEMqhrSWbBVvdghPNiBzs7T9RzEq/0w8rs743tCF7MICv72fdgYadrGlxFsFWSujwZXQLI4VUSxKirJBCUgfR0u84gZK/wUzJ4EPqMichniTf24AsvidozUHWMDmQ+pUaBTyxjD5egi8LcV0EHH4feHwzacA2gyGbOtFK3wpa/dgE1yvPTkPKnccIXKnbel0mfxfsBVkclc5/DnczmrdaGrX5DCrQbI+HO4lhr4KzAm/pw6qfLcw8KjCdVKsnCRXykdat8KUwNAeolknRWdKDqdsbyXBj+ePMTlMR8YmoBj9znYWwOnAAyu56utiteL0oq9YPkb7ZGF5ZOE=
```

#### Запуск Playbook

- В файле **playbook/hosts.txt** внести данные о серверах к которым подключаемся.
- В файл **playbook/group_vars/localhost_servers** внести данные о пользователе который имеет доступ к серверам (login и путь до публичного ключа).
- Создать в директории **playbook/ssh_key/** файл **id_rsa.pub** и поместить туда содержимое публичного ключа, указанного выше.
- В **useradd.yml** *25 строка* прописать путь к файлу с публичным путем созданным выше.
- ввести команду для запуска *playbook* , понадобиться root пароль от сервера.
```cmd
ansible-playbook useradd.yml --ask-become-pass
```

---

## 2. Web приложение на Python

### Приложение

Веб-приложение написано на фрейворке fastAPI, которое слушает входящие соединения на порту 8000 и предоставляет HTTP API, в котором реализовано 3 метода:

- GET /hostname - при запросе на этот метод приложение отдает имя хоста, на котором запущено приложение
- GET /author - возвращает значение переменной окружения $AUTHOR, в которой задано имя или никнейм человека, выполняющего это задание
- GET /id - возвращает значение переменной окружения $UUID, содержащее любую произвольную строку-идентификатор в формате uuid

### Kubernetes manifest

Манифест для запуска приложения в Kubernetes в отдельном неймспейсе в виде Deployment с 3 репликами и сервиса с типом ClusterIP. Реализовать readiness- и liveness- пробы. В переменную UUID подставляться уникальный идентификатор пода в кластере, в котором запущено приложение.

### Helm chart

Написать Helm чарт, в котором через переменные в файле values.yaml можно задать:

- имя образа, запускаемого в поде
- количество реплик приложения
- значение, подставляемое в переменную AUTHOR

Для запуска 2-й части задания, перейти в корневую директорию проекта и запустить команду 
```
helm install app helm
```

## Contacts

Maxim Fedorov   
[telegram](https://t.me/mishaviborniy)   
[email](femakc@yandex.ru)   
