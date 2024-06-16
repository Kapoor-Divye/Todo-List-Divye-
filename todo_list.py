class TodoList:
    def __init__(self):
        self.lists = {}

    def create_list(self, name):
        if name in self.lists:
            print(f"List '{name}' already exists.")
        else:
            self.lists[name] = []
            print(f"List '{name}' created.")

    def use_list(self, name):
        if name not in self.lists:
            print(f"List '{name}' does not exist.")
            return

        while True:
            print(f"\nUsing list '{name}':")
            for task in self.lists[name]:
                status = "✓" if task["completed"] else "✗"
                print(f"  {status} {task['name']}")

            print("\nOptions: add <item>, remove <item>, complete <item>, incomplete <item>, show, back")
            option = input("Choose an option: ").strip().lower()
            
            if option == "back":
                break
            elif option.startswith("add "):
                item = option[4:]
                self.lists[name].append({"name": item, "completed": False})
                print(f"Added '{item}' to list '{name}'.")
            elif option.startswith("remove "):
                item = option[7:]
                self.lists[name] = [task for task in self.lists[name] if task["name"] != item]
                print(f"Removed '{item}' from list '{name}'.")
            elif option.startswith("complete "):
                item = option[9:]
                for task in self.lists[name]:
                    if task["name"] == item:
                        task["completed"] = True
                        print(f"Marked '{item}' as completed.")
                        break
                else:
                    print(f"Item '{item}' not found in list '{name}'.")
            elif option.startswith("incomplete "):
                item = option[11:]
                for task in self.lists[name]:
                    if task["name"] == item:
                        task["completed"] = False
                        print(f"Marked '{item}' as incomplete.")
                        break
                else:
                    print(f"Item '{item}' not found in list '{name}'.")
            elif option == "show":
                for task in self.lists[name]:
                    status = "✓" if task["completed"] else "✗"
                    print(f"  {status} {task['name']}")
            else:
                print("Invalid option.")

    def remove_list(self, name):
        if name in self.lists:
            del self.lists[name]
            print(f"List '{name}' removed.")
        else:
            print(f"List '{name}' does not exist.")

    def show_all_lists(self):
        if not self.lists:
            print("No lists available.")
        else:
            print("\nAll Lists:")
            for list_name, tasks in self.lists.items():
                print(f"\nList '{list_name}':")
                for task in tasks:
                    status = "✓" if task["completed"] else "✗"
                    print(f"  {status} {task['name']}")

    def quit(self):
        print("Quitting program.")
        exit(0)

def main():
    todo_list = TodoList()

    while True:
        print("\nMain Menu")
        print("Options: create <list name>, use <list name>, remove <list name>, show all lists, quit")
        option = input("Choose an option: ").strip().lower()

        if option == "quit":
            todo_list.quit()
        elif option.startswith("create "):
            list_name = option[7:]
            todo_list.create_list(list_name)
        elif option.startswith("use "):
            list_name = option[4:]
            todo_list.use_list(list_name)
        elif option.startswith("remove "):
            list_name = option[7:]
            todo_list.remove_list(list_name)
        elif option == "show all lists":
            todo_list.show_all_lists()
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
