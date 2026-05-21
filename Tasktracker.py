import sqlite3

conn = sqlite3.connect('task.db')

cursor = conn.cursor()

def create_table():
    cursor.execute("""
    Create table IF NOT EXISTS taskTBL(
        taskID INTEGER PRIMARY KEY AUTOINCREMENT,
        taskname TEXT NOT NULL,
     taskstatus TEXT NOT NULL 
        ) 
        """)

    print('TABLE IS CREATED')

def getStatus():

    while True:

        try:

            taskstatus = int(input(
                'Task Status [1.To Do 2.In Progress 3.Done 4.Dropped]: '
            ))

            if taskstatus == 1:
                return 'To Do'

            elif taskstatus == 2:
                return 'In Progress'

            elif taskstatus == 3:
                return 'Done'

            elif taskstatus == 4:
                return 'Dropped'

            else:
                print('Status does not exist')

        except ValueError:
            print('Invalid input. Enter numbers only.')
    

def insert_task():
    show_task()

    taskname = input('Task Name: ').strip()

    if not taskname:
        print("Task name cannot be empty.")
        return

    # Check for duplicate task name
    cursor.execute("SELECT * FROM taskTBL WHERE taskname = ?", (taskname,))
    if cursor.fetchone():
        print(f"Task '{taskname}' already exists.")
        return

    taskstatus = getStatus()

    cursor.execute("""
        INSERT INTO taskTBL (taskname, taskstatus)
        VALUES (?, ?)
        """, (taskname, taskstatus))

    conn.commit()
    print(f"Task '{taskname}' inserted successfully.")


def show_task():
    cursor.execute("""
    SELECT * FROM taskTBL
    """)

    taskTBL = cursor.fetchall()
    print('='*50)
    print('List of Task')
    for taskID, taskname, taskstatus in taskTBL:
        print(f'Task ID [{taskID}] | Task: {taskname} | Status: {taskstatus}')
    print('='*50)


def delete_task():

    show_task()

    taskID = input("Enter ID of the task to delete: ")

    # Checks if task exists
    cursor.execute("""
        SELECT * FROM taskTBL
        WHERE taskID = ?
    """, (taskID,))

    task = cursor.fetchone()

    # If task exists
    if task:

        confirm = input("Are you sure? (y/n): ")

        if confirm.lower() == 'y':

            cursor.execute("""
                DELETE FROM taskTBL
                WHERE taskID = ?
            """, (taskID,))

            conn.commit()

            print("Task deleted successfully")

        else:
            print("Deletion cancelled")

    # If task does not exist
    else:
        print("ID does not exist.")

def update_task():
    show_task()

    print('Updating Task requires TASK ID')
    taskID = input('Task ID: ')
    cursor.execute("""
        SELECT * FROM taskTBL
        WHERE taskID = ?
        """, (taskID,))

    task = cursor.fetchone()

    if task:

        print('what to update')
        taskname = input("New task name: ")
        taskstatus = getStatus()  # getStatus handles its own input

        cursor.execute("""
            UPDATE taskTBL
            SET taskname = ?, taskstatus = ?
            WHERE taskID = ?
            """, (taskname, taskstatus, taskID))

        conn.commit()

        print("Task updated successfully")

    else:
        print("ID does not exist.")



def close_connection():
    conn.close()