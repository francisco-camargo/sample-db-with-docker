MySQL Database via Docker
=========================

Use Docker [image](https://hub.docker.com/r/genschsa/mysql-employees) of the [MySQL Employee Sample database](https://dev.mysql.com/doc/employee/en/). Following [this](https://youtu.be/DiQ5Hni6oRI?si=dm8oqyvRsDATMxSC) guide.

It exposes port `3306` and supports a mountable volume at `/var/lib/mysql` for persistent data.

With the Docker image on-hand, start a container with the script `start_container.sh`. Execute this script by running `./start_container.sh` in a terminal

Following advise from [here](https://stackoverflow.com/questions/50608301/docker-mounted-volume-adds-c-to-end-of-windows-path-when-translating-from-linux), I was able to modify the Docker volume specification within `start_container.sh` to work on Windows using `git bash`. With the Docker volume working I can, for example, add files from within the repo `/data `directory and this change will be reflected within the volume directory `/var/lib/mysql`.

If when you run `docker run` you get complaints about port 3306 already being in use, try [this](https://stackoverflow.com/questions/68065284/specified-port-3306-is-already-in-use-when-installing-mysql)

If succesfully running the container, you get execute a SQL querry against the containarized database by running

```python
python main.py
```

which will print to the terminal five data entries.
