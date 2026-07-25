# venv folder remove করো GitHub থেকে
echo "venv/" >> .gitignore
git rm -r --cached venv/
git add .
git commit -m "remove venv from tracking"
git push