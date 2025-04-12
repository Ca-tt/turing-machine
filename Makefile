run:
	py src/main.py
	
test:
	py src/test.py

save:
	git add . && git commit

exe:
	poetry run pyinstaller --clean --noconsole --onefile --name "Turing Machine" src/main.py

# --icon=img/mp4.ico