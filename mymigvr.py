import mig_util as mu

conn_hr = mu.get_oracle_conn()
# onn_dadb = mu.get_mysql_conn('doodb')
rand_row_count = 0

# read from source db
with conn_hr:
    cur = conn_hr.cursor()
    oracle_inner_count = "select count(*) from Employees e inner join Departments d on e.department_id = d.id"
    cur.execute(oracle_inner_count)
    ora_inner_count = cur.fetchone()[0]

    print(ora_inner_count)

    # cur = conn_hr.cursor()
    # sql = "select " + cols + " from " + table + " order by rand() limit %s"
    # rand_row_count = round(dooo_cnt / 3)
    # cur.execute(sql, (rand_row_count,))
    # dooo_list = cur.fetchall()

# lst = []
# for i in dooo_list:
#     l = list(i)
#     l.append(i[3])
#     lst.append(l)

# print("lst=", lst)

# with conn_dadb:
#     da_cnt = mu.get_count(conn_dadb, table)

#     print("dooodb =", dooo_cnt, ", dadb =", da_cnt)
#     if dooo_cnt != da_cnt:
#         print("Not Valid Count!! dooodb =", dooo_cnt, ", dadb =", da_cnt)
#         exit()

#     else:
#         print("Count is OK")
#         cur = conn_dadb.cursor()

#         sql = '''select id, name, prof, classroom
#                    from Subject
#                   where id = %s
#                     and name = %s
#                     and prof = %s
#                     and (case when %s is null 
#                               then classroom is null
#                               else classroom = %s end)
#                   '''
#         cur.executemany(sql, dooo_list)
#         # cur.executemany(sql, lst)
#         curcnt = cur.rowcount

#         if rand_row_count == curcnt:
#             print("Whole data is OK", "Verified count is", rand_row_count)

#         else:
#             print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Fail",
#                   rand_row_count, curcnt)

        # sql = "select " + cols + " from " + table + " where id = %s"
        # for row in dooo_list:
        #     cur.execute(sql, row[0])
        #     r = cur.fetchone()

        #     if row[0] == r[0] and row[1] == r[1] and row[2] == r[2] and row[3] == r[3]:
        #         print(r, "OK")
        #     else:
        #         print(row, r, "Fail!!")
        #         break

