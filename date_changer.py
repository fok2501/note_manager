created_date=input('Укажите дату создания заметки в формате: DD-MM-YYYY ')
issue_date=input('Укажие требуемый дедлайн этой заметки в формате: DD-MM-YYYY ')
# краткий вывод дат
tmp_created_date=created_date[0:5]
tmp_issue_date=issue_date[0:5]
print("Дата создания заметки:", tmp_created_date)
print("Дедлайн (срок истечения):", tmp_issue_date)