lint:
	poetry run flake8 gendiff
test:
	poetry run pytest
test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml
restart: install build publish package-reinstall
install:
	poetry install
build:
	poetry build
publish:
	poetry publish --dry-run
package-reinstall:
	python3 -m pip install --force-reinstal dist/*.whl
package-install:
	python3 -m pip install --user dist/*.whl