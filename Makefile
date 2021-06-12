install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

lint:
	poetry run flake8 brain_games

brain-games:
	poetry run brain-games-py

even:
	poetry run brain-even-py

calc:
	poetry run brain-calc-py

gcd:
	poetry run brain-gcd-py

progression:
	poetry run brain-progression-py

prime:
	poetry run brain-prime-py
