# Access table 
table = instance.table('table_name')
row_filter = row_filters.CellsColumnLimitFilter(10)
partial_rows = table.read_rows(filter_=row_filter)

# Print rows
for row in partial_rows:\n",
    print('*********************')
    print('NEW ROW')
    print(row.row_key.decode('utf-8')

# Print column families
partial_rows = table.read_rows(filter_=row_filter)
for row in partial_rows:
	if row.row_key.decode('utf-8') == '191':
	  for column_family_id, columns in row.cells.items():
		print('-----------')
		print(column_family_id)

# Print value of the cell
for row in partial_rows:\n",
	if row.row_key.decode('utf-8') == '1010':
    print(row.cells['family_name']['variable'.encode()][0].value.decode('utf-8'))			
