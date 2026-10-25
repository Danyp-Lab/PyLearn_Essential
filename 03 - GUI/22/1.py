import sqlite3

# اتصال به دیتابیس (یا ایجاد اگر وجود ندارد)
conn = sqlite3.connect("todo.db")
c = conn.cursor()

# ایجاد جدول tasks اگر وجود ندارد
c.execute("""CREATE TABLE IF NOT EXISTS tasks
             (id INTEGER PRIMARY KEY, task TEXT, priority INTEGER, done INTEGER, date TEXT)""")


# تابع برای افزودن تسک جدید
def add_task(task_text, priority, date):
    c.execute(
        "INSERT INTO tasks (task, priority, done, date) VALUES (?, ?, 0, ?)",
        (task_text, priority, date),
    )
    conn.commit()


# تابع برای تیک زدن تسک
def mark_task_done(task_id):
    c.execute("UPDATE tasks SET done = 1 WHERE id = ?", (task_id,))
    conn.commit()


# تابع برای حذف تسک
def delete_task(task_id):
    c.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()


# تابع برای نمایش تسک‌ها با ترتیب مشخص
def show_tasks():
    c.execute("SELECT * FROM tasks ORDER BY done ASC, priority DESC")
    return c.fetchall()


# تابع برای نمایش جزئیات تسک
def show_task_details(task_id):
    c.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
    return c.fetchone()


# نمونه استفاده از توابع
add_task("خرید نان", 1, "2024-05-08 10:00")
add_task("تمرین ورزشی", 2, "2024-05-08 08:00")
mark_task_done(1)
delete_task(2)

# نمایش تسک‌ها
tasks = show_tasks()
for task in tasks:
    print(task)

# نمایش جزئیات یک تسک
task_details = show_task_details(1)
print(task_details)

# بستن اتصال دیتابیس
conn.close()
