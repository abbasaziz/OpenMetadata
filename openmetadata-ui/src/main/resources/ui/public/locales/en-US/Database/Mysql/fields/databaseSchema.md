In OpenMetadata, the Database Service hierarchy works as follows:

```
Database Service > Database > Schema > Table
```

In the case of MySQL, we won't have a DatabaseSchema as such. If you'd like to see your data in a databaseSchema named something other than `default`, you can specify the name in this field.