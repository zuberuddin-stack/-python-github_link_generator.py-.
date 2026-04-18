username = input("Enter GitHub username: ")
repo = input("Enter repository name: ")
branch = input("Enter branch name (default: main): ") or "main"
file_path = input("Enter file path (optional, press Enter to skip): ")

repo_link = f"https://github.com/{username}/{repo}"
clone_https = f"https://github.com/{username}/{repo}.git"
clone_ssh = f"git@github.com:{username}/{repo}.git"
branch_link = f"https://github.com/{username}/{repo}/tree/{branch}"

print("\n--- Your GitHub Links ---")
print(f"Repo      : {repo_link}")
print(f"Clone HTTPS: {clone_https}")
print(f"Clone SSH  : {clone_ssh}")
print(f"Branch     : {branch_link}")

if file_path:
    file_link = f"https://github.com/{username}/{repo}/blob/{branch}/{file_path}"
    raw_link = f"https://raw.githubusercontent.com/{username}/{repo}/{branch}/{file_path}"
    print(f"File       : {file_link}")
    print(f"Raw File   : {raw_link}")
