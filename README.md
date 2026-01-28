# UEDemo

Tiny demo repo for standing up CI and unit tests.

## Usage

```bash
python -c "import uedemo; print(uedemo.greet('Bryant'))"
```

## Tests

```bash
python -m unittest discover -s tests -v
```

## CI

GitHub Actions runs on pushes and PRs to `main` and executes the unit tests.
