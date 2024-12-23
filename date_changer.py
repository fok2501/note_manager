created_date=input('Укажите дату создания заметки в формате: 21-12-2024 ')
issue_date=input('Укажие требуемый дедлайн этой заметки в формате: 22-12-2024 ')
# краткий вывод дат
tmp_created_date=created_date[0:5]
tmp_issue_date=issue_date[0:5]
print("Дата создания заметки:", tmp_created_date)
print("Дедлайн (срок истечения):", tmp_issue_date)