lint:
	poetry run flake8 gendiff
test:
	poetry run pytest

restart: install build publish package-reinstall 
install:
	poetry install
build:
	poetry build
publish:
	poetry publish --dry-run
package-reinstall:
	python3 -m pip install --force-reinstal --user dist/*.whl
package-install:
	python3 -m pip install --user dist/*.whl
test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml