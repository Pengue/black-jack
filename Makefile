# Resolves the dependencies and installs them
install: 
	poetry install
# Play brain-games
brain-games:
	poetry run brain-games

# Make package
build: 
	poetry build

# Publish package 
publish:
	poetry publish --dry-run

# Install local package 
package-install: 
	python3 -m pip install --user dist/*.whl

# Reinstall local package
package-reinstall:
	python3 -m pip install --force-reinstall  --user dist/*.whl

# Run lint
lint: 
	poetry run flake8 brain_games
	