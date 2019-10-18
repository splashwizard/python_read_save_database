import csv
import pymysql
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='humanresource')

with open('humanResources.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if not line_count == 0:
            line_count += 1
            sql = "INSERT INTO humanresource (satisfaction_level, last_evaluation, number_project, `average_montly_hours`, `time_spend_company`, `Work_accident`,`left`,`promotion_last_5years`,`sales`,`salary`) VALUES (" + row['satisfaction_level'] + ',' + row['last_evaluation'] + ',' + row['number_project']  + ',' + row['average_montly_hours']  + ',' + row['time_spend_company']   + ',' + row['Work_accident'] + ',' + row['left'] + ',' +row['promotion_last_5years'] + ',"' + row['sales']  + '","' + row['salary']+ '")'
            print(sql)
            cur = conn.cursor()
            cur.execute(sql)
            conn.commit()
            print(cur.lastrowid)
            
        line_count += 1
    # print(f'Processed {line_count} lines.')