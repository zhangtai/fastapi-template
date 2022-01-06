# fastapi-template

## db init

```shell
aerich init -t api.TORTOISE_ORM
aerich init-db
aerich upgrade

# after new changes
aerich migrate --name added_new_tables
```
