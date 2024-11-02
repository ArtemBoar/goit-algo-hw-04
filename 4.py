import sys
from pathlib import Path
from colorama import init, Fore, Style

# 1
def total_salary(path):
    try:
        with open(path, encoding='utf-8') as file:
            salaries = []
            for line in file:
                # Розділяємо рядок на ім'я та зарплату
                name, salary = line.strip().split(',')
                salaries.append(int(salary))

            total = sum(salaries)
            average = total / len(salaries) if salaries else 0

            return total, average

    except FileNotFoundError:
        print(f"Файл за шляхом {path} не знайдено.")
        return 0, 0
    except Exception as e:
        print(f"Сталася помилка при читанні файлу: {e}")
        return 0, 0

# 2
def get_cats_info(path):
    try:
        with open(path, encoding='utf-8') as file:
            cats_info = []
            for line in file:
                cat_id, name, age = line.strip().split(',')
                cat_info = {
                    "id": cat_id,
                    "name": name,
                    "age": int(age)
                }
                cats_info.append(cat_info)

            return cats_info

    except FileNotFoundError:
        print(f"Файл за шляхом {path} не знайдено.")
        return []
    except Exception as e:
        print(f"Сталася помилка при читанні файлу: {e}")
        return []

# 3

def print_directory_tree(path, indent=""):
    try:
        path = Path(path)
        if not path.exists():
            print(f"Директорія за шляхом {path} не знайдена.")
            return

        print(f"{Fore.BLUE}{indent}{path.name}/")

        for item in path.iterdir():
            if item.isdir():
                print_directory_tree(item, indent + "  ")
            else:
                print(f"{Fore.GREEN}{indent}  {item.name}")

    except Exception as e:
        print(f"Сталася помилка: {e}")

def main():

    init(autoreset=True)
    if len(sys.argv) == 2:
        directory_path = sys.argv[1]
        print_directory_tree(directory_path)
    else:
        total, average = total_salary("path/to/salary_file.txt")
        print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

        cats_info = get_cats_info("path/to/cats_file.txt")
        print(cats_info)

if __name__ == "__main__":
    main()