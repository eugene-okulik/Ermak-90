insert into students (name, second_name) VALUES ('Ivan', 'Ivanov');
insert into books (title, taken_by_student_id) values ('War and world', 20075);
insert into books (title, taken_by_student_id) values ('Python for beginner', 20075);
insert into books (title, taken_by_student_id) values ('Python for professional', 20075);
insert into `groups` (title, start_date, end_date) values ('new course Python', 'oct 2023', 'feb 2024');
update students s set s.group_id = 4904 where s.id = 20075;
insert into subjets (title) values ('Наука о земле');
insert into subjets (title) values ('Наука о растениях');
insert into lessons (title, subject_id) values ('Урок №1', 10051);
insert into lessons (title, subject_id) values ('Урок №2', 10051);
insert into lessons (title, subject_id) values ('Урок №1', 10052);
insert into lessons (title, subject_id) values ('Урок №2', 10052);
insert into marks (value, lesson_id, student_id) values ('5', 9408, 20075);
insert into marks (value, lesson_id, student_id) values ('6', 9409, 20075);
insert into marks (value, lesson_id, student_id) values ('7', 9410, 20075);
insert into marks (value, lesson_id, student_id) values ('8', 9411, 20075);

-- 1. Все оценки студента
select m.value оценка from marks m
where m.student_id = 20075;

-- 2. Все книги, которые находятся у студента
select b.title Название_книги from books b
where b.taken_by_student_id  = 20075;

-- 3. Для вашего студента выведите всё, что о нем есть в базе: группа, книги, оценки с названиями занятий и предметов
-- (всё одним запросом с использованием Join)

select g.title Название_группы, b.title Название_книги, m.value Оценка, l.title Название_занятия, sub.title Название_предмета

from students s

join `groups` g
on s.group_id = g.id

join books b
on s.id = b.taken_by_student_id

join marks m
on s.id = m.student_id

join lessons l
on l.id = m.lesson_id

join subjets sub
on l.subject_id = sub.id

where s.id = 20075





