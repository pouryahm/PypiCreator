import os


def safe_package_name(name):
    # همه حروف کوچک، فاصله و خط تیره به آندرلاین
    s = name.strip().lower().replace(" ", "_").replace("-", "_")
    # فقط حروف، عدد و آندرلاین نگه می‌داریم
    s = "".join(ch for ch in s if (ch.isalnum() or ch == "_"))
    # اگر با عدد شروع شد، یک آندرلاین اولش بگذار
    if s and s[0].isdigit():
        s = "_" + s
    return s or "my_package"


project_name = 'pypifile'  # input('Enter project name: ').strip()
description = input('Enter your Description: ').strip()
# author = input('Author name: ').strip()
# email = input('Enter your Email address: ').strip()
License_name = input('Enter license type: ').strip() or "MIT"

package_name = safe_package_name(project_name)

# print project structure :
# print("------------  PLAN  ------------")
# print(f'Project Folder: {project_name}')
# print(f'Package Folder:/{project_name}/{package_name} ')
# print("----------File to Create ----------")
# print(f'{project_name}/setup.py')
# print(f'{project_name}/README.md')
# print(f'{project_name}/requirements.txt')
# print(f'{project_name}/LICENSE')
# print(f'{project_name}/.gitignore')
# print(f'{project_name}/{package_name}/__init__.py')
# print(f'{project_name}/{package_name}/main.py')
# print(f'{project_name}/tests/test_main.py')
#
# print("META DATA : ")
# print(f"Description:{description}")
# print(f'Auther Name/Email :{author} -- {email} ')
# print(f"console_script :{package_name} -> {package_name}.main:main ")
cwd = os.getcwd()
base_dir = os.path.join(cwd, project_name)
package_dir = os.path.join(base_dir, package_name)
tests_dir = os.path.join(base_dir, "tests")

os.makedirs(base_dir, exist_ok=True)
os.makedirs(package_dir, exist_ok=True)
os.makedirs(tests_dir, exist_ok=True)

file_list = {
    'setup.py': os.path.join(base_dir, 'setup.py'),
    'README.md': os.path.join(base_dir, 'README.md'),
    'requirements.txt': os.path.join(base_dir, 'requirements.txt'),
    'LICENSE': os.path.join(base_dir, 'LICENSE'),
    '.gitignore': os.path.join(base_dir, '.gitignore'),
    '__init__.py': os.path.join(package_dir, '__init__.py'),
    'main.py': os.path.join(package_dir, 'main.py'),
    'test_main.py': os.path.join(tests_dir, 'test_main.py'),
}

for key, value in file_list.items():
    file_name = value
    if os.path.exists(file_name) and key not in ["LICENSE", "main.py"]:
        print(f" Skipped  (already exists):{file_name}")
        # while True:
        #     decision=input('what is your decision? skip / overwrite / append ?').strip().lower()
        #     if decision=="skip":
        #         print(f"The file '{file_name}' already exists and")
        #         break
        #     elif decision=="overwrite":
        #         break
        #     elif decision=="append":
        #         break
        #     else:
        #         print('chose between skip overwite or append ')

    else:
        with open(file_name, 'w', encoding="utf-8") as f:
            if key=="main.py":
                f.write('def main():\n')
                f.write(f'    print("Hello from {project_name}")\n')
            elif key=="README.md":
                f.write(f"# {project_name}\n\n{description}\n")
            elif key==".gitignore":
                f.write(f'__pycache__/\n*.pyc\n*.egg-info/\ndist/\nbuild/\n')
            elif key=="test_main.py":
                f.write(f'assert 1 + 1 == 2\n')
            elif key=="LICENSE" and  License_name =="MIT":
                f.write(f' MIT License (placeholder)')
            elif key=="setup.py":
                f.write(f'import setuptools')
        print(f"Created: {file_name}")

def list_files_folders_os_walk(start_path):
    for root, dirs, files in os.walk(start_path):
        level = root.replace(start_path, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print(f'{indent}{os.path.basename(root)}/')
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print(f'{subindent}{f}')

print('---------------------summery---------------------')
print(f'Project: {project_name} ')
print(f'Package: {package_name} ')
print(f'Base dir: {base_dir} ')
print('---------Tree---------')
list_files_folders_os_walk(base_dir)