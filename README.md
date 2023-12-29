MySQL Database via Docker
=========================

Use Docker [image](https://hub.docker.com/r/genschsa/mysql-employees) of the [MySQL Employee Sample database](https://dev.mysql.com/doc/employee/en/). Following [this](https://youtu.be/DiQ5Hni6oRI?si=dm8oqyvRsDATMxSC) guide.

It exposes port `3306` and supports a mountable volume at `/var/lib/mysql` for persistent data.

With the Docker image on-hand, start a container with the script `start_container.sh`. Execute this script by running `./start_container.sh` in a terminal

Following advise from [here](https://stackoverflow.com/questions/50608301/docker-mounted-volume-adds-c-to-end-of-windows-path-when-translating-from-linux), I was able to modify the Docker volume specification within `start_container.sh` to work on Windows using `git bash`. With the Docker volume working I can, for example, add files from within the repo `/data `directory and this change will be reflected within the volume directory `/var/lib/mysql`.
