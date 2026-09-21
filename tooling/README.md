# Tooling

`oneshelf-core-ref.txt` is the OneShelf Core commit whose validators, packaged-test runtime, canonical
builder and Registry contract this repository is checked against. `./tools/bootstrap` installs exactly that
commit into `.venv`, and CI does the same. Moving the pin is its own reviewed Pull Request.
