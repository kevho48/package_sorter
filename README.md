Local Environment - 

python --version
Python 3.12.3

pip --version
pip 25.0.1

Run the following commands

```
pipenv sync --dev
pipenv shell
coverage run -m pytest .\test\test_technical_screen.py
coverage html
```

You can open the index.html file generated in the `htmlcov\index.html` locally to check code coverage
