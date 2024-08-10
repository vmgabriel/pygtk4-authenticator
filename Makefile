install:
	( \
		source venv/bin/activate; \
		pip install -r requirements.txt; \
	)


test: install
	. venv/bin/activate; pytest app/tests


clean:
	rm -rf venv
	find -iname "*.pyc" -delete


run: install
	( \
		source venv/bin/activate; \
		python main.py; \
	)