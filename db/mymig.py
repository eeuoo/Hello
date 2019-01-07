import mig_util as mu

oraconn = mu.get_oracle_conn()
myconn = mu.get_mysql_conn('doodb')

with oraconn :

   cursor_j = oraconn.cursor()
   cursor_d = oraconn.cursor()
   cursor_jh = oraconn.cursor()
   cursor_e = oraconn.cursor()

   oracle_j = ''' select JOB_ID, JOB_TITLE, MIN_SALARY, MAX_SALARY from JOBS '''
   oracle_d = ''' select DEPARTMENT_ID, DEPARTMENT_NAME, MANAGER_ID from DEPARTMENTS '''
   oracle_jh = ''' select EMPLOYEE_ID, START_DATE, END_DATE, JOB_ID, DEPARTMENT_ID from JOB_HISTORY '''
   oracle_e = ''' select EMPLOYEE_ID, FIRST_NAME, LAST_NAME, EMAIL, PHONE_NUMBER, HIRE_DATE, JOB_ID, NVL(SALARY,0), NVL(COMMISSION_PCT, 0), MANAGER_ID, DEPARTMENT_ID from EMPLOYEES'''

   cursor_j.execute(oracle_j)
   cursor_d.execute(oracle_d)
   cursor_jh.execute(oracle_jh)
   cursor_e.execute(oracle_e)

   rows_j = cursor_j.fetchall()
   rows_d = cursor_d.fetchall()
   rows_jh = cursor_jh.fetchall()
   rows_e = cursor_e.fetchall()

''' 오라클 데이터 출력
for j in rows_j:
   print(j)

for d in rows_d:
   print(d)

for jh in rows_jh:
   print(jh)
'''


with myconn :

   cur_j = myconn.cursor()
   cur_d = myconn.cursor()
   cur_jh = myconn.cursor()
   cur_e = myconn.cursor()

   sql_j = ''' create table Jobs (
                   id varchar(10) not null primary key default '',
                   job_title varchar(35) not null default '',
                   min_salary int default 0,
                   max_salary int default 0
               )
         '''
         
   sql_d = ''' create table Departments (
                   id int unsigned not null primary key default 0,
                   department_name varchar(30) not null default '',
                   manager_id int unsigned default 0
               )
         '''

   sql_jh = ''' create table JobHistory (
                   employee_id int unsigned not null default 0,
                   start_date date not null,
                   end_date  date not null,
                   job_id varchar(10) not null default '',
                   department_id int unsigned not null default 0,
                   primary key (employee_id, start_date)
               )
         '''

   sql_e = ''' create table Employees (
                    id int unsigned not null primary key default '0',
                    first_name varchar(20),
                    last_name varchar(25) not null,
                    email varchar(25) not null unique,
                    phone_number varchar(20),
                    hire_date date not null,
                    job_id varchar(10) not null,
                    salary int(10) unsigned not null default '0',
                    commission_pct int(10) unsigned not null default '0',
                    manager_id int unsigned default 0,
                    department_id int(10) unsigned default 0
              )
        '''     

# Jobs 데이터 이관
   cur_j.execute("drop table if exists Jobs")
   cur_j.execute(sql_j)

   sql_insert_j = "insert into Jobs(id, job_title, min_salary, max_salary) values(%s, %s, %s, %s)"
   cur_j.executemany(sql_insert_j, rows_j)

# Departments 데이터 이관
   cur_d.execute("drop table if exists Departments")
   cur_d.execute(sql_d)

   sql_insert_d = "insert into Departments(id, department_name, manager_id) values(%s, %s, %s)"
   cur_d.executemany(sql_insert_d, rows_d)

# JobHistory 데이터 이관
   cur_jh.execute("drop table if exists JobHistory")
   cur_jh.execute(sql_jh)

   sql_insert_jh = "insert into JobHistory(employee_id, start_date, end_date, job_id, department_id) values(%s, %s, %s, %s, %s)"
   cur_jh.executemany(sql_insert_jh, rows_jh)


# Employees 데이터 이관
   cur_e.execute("drop table if exists Employees")
   cur_e.execute(sql_e)

   sql_insert_e = "insert into Employees(id, first_name, last_name, email, phone_number, hire_date, job_id, salary, commission_pct, manager_id, department_id) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
   cur_e.executemany(sql_insert_e, rows_e)


   print( "Jobs rowcount :", cur_j.rowcount)
   print( "Departments rowcount :", cur_d.rowcount)
   print( "JobHistory rowcount", cur_jh.rowcount)
   print( "Employees rowcount", cur_e.rowcount)