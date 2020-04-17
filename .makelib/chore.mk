clean-py-binary:
	find ./src -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete

auto-black:
	./.tox/lint/bin/black --config ./.black.toml --verbose src/

auto-isort:
	./.tox/lint/bin/isort --recursive src/

autoformat: auto-black auto-isort

autoformat-curent-env:
	black -l 79 --target-version py37 .
	isort src/**/*.py
