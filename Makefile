run:
	py src/main.py
	
test:
	py src/test.py

save:
	git add . && git commit

show:
	pip show customtkinter

exe:
	poetry run pyinstaller --noconfirm --collect-data customtkinter --clean --noconsole  --onedir --name "Turing Machine" src/main.py
