# Dockerized Python App

In the past I've struggled to make Python apps that are easy to share with collaboratrs because the development environment is hard to sync between each developer.

To completely get around this issue I've began a new approach. Do not base development on the  host of the user. Instead, define a docker container and use the `just` runner so developers can simply.

```bash
just build      # build the docker container
just run        # runs the code in app.py
```

As developemnt progresses and requirements change the files which build the
docker container can progress and you clone the repo, `just build` then `just
run` and we have a shared and reproducable app environment.
