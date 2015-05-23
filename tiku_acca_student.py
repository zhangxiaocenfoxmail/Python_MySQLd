#!/usr/bin/env python
# -*- coding:utf-8 -*-

from StudentInfo import StudentInfo
import time, sys, os
import traceback

def dateConvertUnixTimestamp(date=None):
    """
        /* 无参数  -->  <type:int>  返回当前时间戳
        /* 有参数  -->  <type:int>  返回给定日期的时间戳
        /* 错误  -->  返回 0
    """
    if not date:
        return int(time.time()) # 没有参数，直接返回当前时间戳
    
    date_list = date.split('-')
    for i in range(9): # 方法：time.mktime() 需要9个参数
        if i >= len(date_list):
            date_list.append(0)
        else:
            try:
                date_list[i] = int(date_list[i])
            except(ValueError):
                print("%s ：参数错误，输入参数必须可被'-'分割，且可转化为正整数！" % (begin_time))
                return 0
    date_tuple = tuple(date_list) # 方法：time.mktime() 参数必须为元组
    convert_timestamp = int(time.mktime(date_tuple))
    return convert_timestamp

def unixTimestampConvertDate(timestamp=None):
    """
        /* 无参数  -->  <type:string>  返回当前日期格式
        /* 有参数  -->  <type:string>  返回给定时间戳的日期格式
        /* 错误  -->  返回 ''
    """
    if not timestamp:
        timestamp = int(time.time())
    try:
        timestamp = int(timestamp)
    except(ValueError):
        print("%s ：参数错误，输入参数必须可转化为正整数！")
        return ''
    date_list = time.localtime(timestamp)
    date = '-'.join([str(date_list.tm_year), str(date_list.tm_mon), str(date_list.tm_mday)])
    return date

def UnixTimestampConvertWeek(timestamp=None):
    """
        /* 无参数  -->  <type:string>  返回当前日期格式
        /* 有参数  -->  <type:string>  返回给定时间戳的日期格式
        /* 错误  -->  返回 ''
    """
    if not timestamp:
        timestamp = int(time.time())
    try:
        timestamp = int(timestamp)
    except(ValueError):
        print("%s ：参数错误，输入参数必须可转化为正整数！")
        return ''
    date_list = time.localtime(timestamp)
    date_week = str(date_list.tm_wday)
    return date_week

def selectRegStudent(table, s_table, b_time, e_time, db):
    select_sql = """select group_concat(`id`) from %s \
where `time` >= %s \
and `time` < %s order by `id`""" % (table, b_time, e_time)
    db.execute(select_sql)
    db_result = db.fetchall()
    if db_result:
        mid_str = db_result[0][0]
        select_sql = """select `id` from %s \
where `member_id` in (%s) order by `id`""" % (s_table, mid_str)
        db.execute(select_sql)
        sid_result = db.fetchall()
        return sid_result
    return ''

def selectCourseId(table, c_column, c_id, db):
    select_sql = """select group_concat(`id`) from %s \
where `%s` = %s""" % (table, c_column, c_id)
    print(select_sql)
    db.execute(select_sql)
    db_result = db.fetchall()
    return db_result

def selectOrderStudentIdByCourseAndDate(table, c_str, b_time, e_time, db):
    select_sql = """select `student_id` from %s \
where `course_id` in (%s)""" % (table, c_str)
    if b_time or e_time:
        select_sql = """select `student_id` from %s \
where `orderstatus` > 1 \
and `course_id` in (%s) \
and `paytime` >= %s \
and `paytime` < %s""" % (table, c_str, b_time ,e_time)
    print(select_sql)
    db.execute(select_sql)
    db_result = db.fetchall()
    return db_result

def selectBeginIdByTime(table, b_time, db):
    select_sql = """select min(`id`) from %s \
where `regdate` >= %s""" % (table, b_time)
    db.execute(select_sql)
    db_result = db.fetchall()
    return db_result

def selectTikuStudentIdByDate(table, c_column, c_id, b_id, e_id, b_time, e_time, db):
    select_sql = """select distinct(`student_id`) from %s \
where `%s` = %s \
and `id` >= %d \
and `id` < %d""" % (table, c_column, c_id, b_id, e_id)
    if e_id == 0:
        select_sql = """select distinct(`student_id`) from %s \
where `%s` = %s \
and `id` >= %d \
and `regdate` >= %s \
and `regdate` < %s""" % (table, c_column, c_id, b_id, b_time, e_time)
    elif b_time and e_time:
        select_sql = """select distinct(`student_id`) from %s \
where `%s` = %s \
and `id` >= %d \
and `id` < %d \
and `regdate` >= %s \
and `regdate` < %s""" % (table, c_column, c_id, b_id, e_id, b_time, e_time)
    print(select_sql)
    db.execute(select_sql)
    db_result = db.fetchall()
    return db_result

def selectOrderByStudentAndCourse(table, s_id, c_str, e_time, db):
    select_sql = """select `id` from %s \
where `student_id` = %s \
and `course_id` in (%s) \
and `invalid_time` >= %s \
and `isdel` = 0 \
and `isprobation` = 0""" % (table, s_id, c_str, e_time)
#     print(select_sql)
    db.execute(select_sql)
    db_result = db.fetchall()
    return db_result

def selectOrderByStudentAndCourseAndRegtime(table, c_str, r_time, db):
    select_sql = """select distinct(`student_id`) from %s \
where `course_id` in (%s) \
and `regdate` >= %s \
and `isdel` = 0 \
and `isprobation` = 0""" % (table, c_str, r_time)
    print(select_sql)
    db.execute(select_sql)
    db_result = db.fetchall()
    return db_result

def selectTikuCountByStudentTypeAndDate(table, s_id, c_column, c_id, s_type, b_time, e_time, db):
    select_sql = """select count(`id`) from %s \
where `student_id` = %s \
and `%s` = %s \
and `type` = %s""" % (table, s_id, c_column, c_id, s_type)
    if b_time or e_time:
        select_sql = """select count(`id`) from %s \
where `student_id` = %s \
and `%s` = %s \
and `type` = %s \
and `regdate` >= %s \
and `regdate` < %s""" % (table, s_id, c_column, c_id, s_type, b_time, e_time)
#     print(select_sql)
    db.execute(select_sql)
    db_result = db.fetchall()
    return db_result

def insertStudentInfo(i_table, i_list, p_name, db):
    i_str = ''
    for i in i_list:
        i_str = i_str + "'" + str(i).replace("'", "\\\'") + "',"
    i_str = i_str[:-1]
    insert_sql = "insert into %s(student_id,user_name,user_phone,user_email,user_laiyuan,time,beizhu,user_source) values (%s)" % (i_table, i_str)
    print(insert_sql)
    try:
        db.execute(insert_sql)
        db.execute("commit")
    except(Exception, e):
        print(p_name + "提交学员失败！错误如下：\n" + traceback.format_exc())

def selectTikuProjectStudentInfo(i_table, s_id, db):
    select_sql = "select item_count from %s where student_id = %s" % (i_table, s_id)
    db.execute(select_sql)
    db_result = db.fetchall()
    return db_result

def updateTikuStudentProject(i_table, s_id, p_name, item_count, db):
    update_sql = "update %s set user_laiyuan = '%s',item_count = %s where student_id = %s" % (i_table, p_name, item_count, s_id)
    print(update_sql)
    db.execute(update_sql)
    db.execute("commit")

if __name__ == "__main__":
    si = StudentInfo()
    tj_db, www_db, test_db, ucenter_db = si.tongji_db, si.www_db, si.test_db, si.ucenter_db
    today = unixTimestampConvertDate()
    today_timestamp = dateConvertUnixTimestamp(today)
    end_time = today_timestamp
    begin_time, end_time = dateConvertUnixTimestamp('2015-03-08'), dateConvertUnixTimestamp('2015-03-09')
    project_dict = {
                    "8":"project_id:CPA",
                    }
    course_table, order_table, tiku_table, member_table = 'gd_course', 'gd_order', 'gd_paper_wrong', 'gd_members'
    student_table, assign_table = 'gd_members_student', 'gd_members_student_assign'
    im_student_table = 'gd_student'
    reg_result = selectRegStudent(member_table, student_table, begin_time, end_time, www_db)
    reg_student = []
    for reg in reg_result:
        s_id = reg[0]
        if s_id:
            reg_student.append(s_id)
    for p_id in sorted(project_dict.keys()):
        im_db = si.im_db
        select_sql = "select max(`id`) from %s" % (tiku_table)
        print(select_sql)
        www_db.execute(select_sql)
        db_result = www_db.fetchall()
        max_id = int(db_result[0][0])
        p_list = project_dict[p_id].split(":")
        p_type, p_name = p_list[0], p_list[1]
        insert_table = p_name + '_no_course_tiku_student'
        print(p_type, p_name)
        if p_name == '中级职称':
            course_result = selectCourseId(course_table, 'project_id', '29', www_db) # 中级职称project_id为29
        else:
            course_result = selectCourseId(course_table, p_type, p_id, www_db)
        if not course_result:
            continue
        course_str = course_result[0][0]
        print(course_str)
        tiku_no_order_count, tiku_right_no_order_count, tiku_order_str = 0, 0, ''
        bid_result = selectBeginIdByTime(tiku_table, begin_time, www_db) # 取一下离开始时间最近的id，写一个方法
        begin_id, end_id = bid_result[0][0], 0 # end_id为空时，方法selectTikuStudentIdByDate只取大于begin_id的student_id
        student_dict, real_student = {}, {}
        student_result = selectTikuStudentIdByDate(tiku_table, p_type, p_id, begin_id, end_id, begin_time, end_time, www_db)
        for student in student_result:
            s_id = student[0]
            student_dict[s_id] = ''
        tiku_count = len(student_dict)
        for s_id in sorted(student_dict.keys()):
            print(s_id)
#             if s_id not in reg_student:
#                 continue
#             reg_student.remove(s_id)
            order_result = selectOrderByStudentAndCourse(assign_table, s_id, course_str, end_time, www_db)
            if not order_result:
                question_result = selectTikuCountByStudentTypeAndDate(tiku_table, s_id, p_type, p_id, '1', begin_time, end_time, www_db) # 用户做了该科目多少题
                question_count = int(question_result[0][0])
                wrong_result = selectTikuCountByStudentTypeAndDate(tiku_table, s_id, p_type, p_id, '2', begin_time, end_time, www_db) # 用户该科目做错了多少题
                wrong_count = int(wrong_result[0][0])
                if question_count == 0:
                    str_percentage = '0.0'
                else:
                    percentage = wrong_count / question_count
                    str_percentage = str(percentage * 100)
                    if len(str_percentage) > 5:
                        str_percentage = str_percentage[:5]
                str_percentage = str_percentage + '%'
                real_student[s_id] = ','.join(['做题数量：' + str(question_count), '做题正确率' + str_percentage])
                print(real_student[s_id])
        print(len(real_student))
        for r_id in real_student.keys():
            base_info = si.getStudentBaseInfoBySid(r_id, www_db)
            print(base_info)
            if not base_info:
                continue
            s_name, s_nickname, s_email, s_phone = base_info[0], base_info[1], base_info[2], base_info[3]
            if not s_phone and not s_email:
                continue
            submit_time = int(time.time())
            s_beizhu = real_student[r_id]
            i_list = [r_id, s_name, s_phone, s_email, p_name, submit_time, s_beizhu, begin_time]
            if not s_name:
                i_list = [r_id, s_nickname, s_phone, s_email, p_name, submit_time, s_beizhu, begin_time]
                print(i_list)
            insertStudentInfo(insert_table, i_list, p_name, test_db)
