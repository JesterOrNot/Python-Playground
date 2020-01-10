build:
	pyinstaller --onefile Binary.py --distpath . --clean
clean:
	rm -rf __pycache__/* build/* build __pycache__ *.spec
deps:
	pip3 install -r requirements.txt
.PHONY: clean
.PHONY: build
.PHONY: deps
