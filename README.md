# PyTestaroo

Pytest example

# Usage

### Build Docker and run tests

```
cd pytestaroo
export DOCKER_BUILDKIT=1;
docker build --tag rocksteady:latest .
docker compose run test
```

# Contributing

```
git checkout -b my-branch
git add .
pre-commit run
git commit -m "Ish"
git push -u origin my-branch
```
