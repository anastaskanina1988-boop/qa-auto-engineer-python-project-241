test:
	uv run pytest

lint:
	uv run ruff check .

test-coverage:
	uv run pytest --cov=hexlet_code --cov-report=xml	