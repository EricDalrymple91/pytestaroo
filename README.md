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
