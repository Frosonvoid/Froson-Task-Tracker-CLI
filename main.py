from Tasktracker import create_table, insert_task, show_task, close_connection, delete_task, update_task

def main():
    print('\t\t\t Task Tracker')

    create_table()
    

    while True:

        print('1. Show Task')
        print('2. Insert Task')
        print('3. Delete Task')
        print('4. Update Task')
        print('5. Close program')
        choice = input('Enter Choice: ')

        match choice:
            case '1':
             show_task()

            case '2':
               insert_task()
               show_task()

            case '3':
                delete_task()
                show_task()

            case '4':
                update_task()
                show_task()

                
            case '5':
                close_connection()
                print('Program Closed')
                break

            case _:
                print('Invalid Choice')


if __name__ == "__main__":
    main()