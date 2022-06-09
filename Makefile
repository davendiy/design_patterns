ve:
	test ! -d .ve && python3.8 -m virtualenv .ve; \
	. .ve/bin/activate; \
	python3.8 install -U pip; \
	python3.8 -m pip install -r requirements.txt; \
	python3.8 -m pip install -r requirements_ci.txt; \

clean:
	make -C docs/sphinx clean
	rm -rf `find . -name __pycache__`
	rm -f `find . -type f -name '*.py[co]' `
	rm -f `find . -type f -name '*~' `
	rm -f `find . -type f -name '.*~' `
	rm -f `find . -type f -name '@*' `
	rm -f `find . -type f -name '#*#' `
	rm -f `find . -type f -name '*.orig' `
	rm -f `find . -type f -name '*.rej' `
	rm -f `find . -type f -name '*.egg-info' `
	rm -f .coverage
	rm -rf coverage
	rm -rf cover
	rm -rf htmlcov
	rm -rf .cache
	rm -rf .eggs
	rm -rf *.egg-info
	rm -rf .env
	rm -rf .pytest_cache

doc:
	make -C docs clean html

lint:
	@echo "Checking code style and syntax convention..."
	@flake8 .
	@isort --check-only .
	@echo "... all good"
