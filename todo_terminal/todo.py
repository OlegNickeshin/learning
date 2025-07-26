import argparse, json

class ToDoList:
    def __init__(self):

        try:
            with open('todo.json') as reader:
                self.todojson = json.load(reader)
        except (FileNotFoundError, json.JSONDecodeError):
            self.todojson = []


    def adding_task(self, x):
            if x:
                self.todojson.append(" ".join(x))
                self.save()

    def list_show(self):
        for i, task in enumerate(self.todojson, start=1):
            print(f"{i}. {task}")

    def done_marker(self, x):
        index = x - 1
        if 0 <= index < len(self.todojson) and '✅' not in self.todojson[index]:
            self.todojson[index] = '✅' + self.todojson[index]
            self.save()
            print("Here is the updated list:")
            self.list_show()
        else:
            print ("Task either completed or doesn't exist")

    def save(self):
        with open('todo.json', 'w') as writer:
            json.dump(self.todojson, writer)

    def remove(self, x):
        if 0 <= x - 1 < len(self.todojson):
            self.todojson.pop(x-1)
            self.save()
        else:
            print ('Please insert a real number')

    def clear(self):
        self.todojson = []
        self.save()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'ToDoList Tool\nManage your tasks via Terminal',
        formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('--add', type = str, nargs ='+', help = 'adds task to the list', required=False)
    parser.add_argument('--list', action='store_true', help = 'shows tasks list')
    parser.add_argument('--done', type = int, help = 'marks a task as finished by the number', required = False)
    parser.add_argument('--remove', type = int, help = 'removes a specific task by the number')
    parser.add_argument('--clear', action='store_true', help = 'clears tasks list')
    args = parser.parse_args()
    todolist = ToDoList()
    if args.add:
        todolist.adding_task(args.add)
    if args.list:
        todolist.list_show()
    if args.done:
        todolist.done_marker(args.done)
    if args.remove:
        todolist.remove(args.remove)
    if args.clear:
        todolist.clear()
