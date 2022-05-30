install: # устанавливаем все зависимости
	poetry install

brain-games: # запуск основного кода
	poetry run brain-games

build: 
	poetry build

publish: # отладка публикации
	poetry publish --dry-run

package-install: 
	python3 -m pip install --user dist/*.whl

lint: # запуск flake8
	poetry run flake8 brain_games
