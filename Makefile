run:
	py src/main.py
	
save:
	git add . && git commit

ready:
	git add . && git commit && git push

show:
	pip show customtkinter

build:
	pyinstaller --noconfirm --collect-data customtkinter --clean --noconsole  --onefile --name "Turing Machine" src/main.py

builddir:
	pyinstaller --noconfirm --collect-data customtkinter --clean --noconsole  --onedir --name "Turing Machine" src/main.py

exe:
	rm dist build -r && pyinstaller --noconfirm --collect-data customtkinter --clean --noconsole  --onefile --name "Turing Machine" src/main.py
