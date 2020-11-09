# pydataq

## Pipenv virtual environments

This project makes use of [pipenv](https://pipenv.pypa.io/en/latest/) to manage all the needed packages for the project as well as a virtual environment. To install pipenv, follow [these steps](https://pipenv.pypa.io/en/latest/#install-pipenv-today).

After cloning the repository, under the project root execute the following command to install the needed pip packages:

`pipenv install`

Activate the enviromnent with:

`pipenv shell`

And happy coding!


## Postgres for env environment

### Using docker run
In order to set up your first pydataq test, it is recommended to run two docker containers with postgres. You can easily do that as it follows:
1. `docker pull postgres`
2. `docker run -d --name pydataq01 -v pydataq01:/var/lib/postgresql/data -e POSTGRES_PASSWORD=<your_pass> -p <a_port>:5432 postgres`
3. `docker run -d --name pydataq02 -v pydataq02:/var/lib/postgresql/data -e POSTGRES_PASSWORD=<your_pass> -p <another_port>:5432 postgres`
4. Use the script provided in `sample_dataset` folder to populate both databases

Now you're good to start writing tests!

In order to run these tests using the docker images just follow these instructions.

### Using docker-compose

There is a docker-compose file that deploys the environment in a more automated way. It also deploys a pgAdmin service to be able to connect to the created servers. To do so:

1. Edit the file **variables.{environment}.env** and update the parameters accordingly. Right now, the parameters to update are:
    |Parameter name|Description|
    |--------------|-----------|
    |POSTGRES_PASSWORD|Password used for the Postgres servers and the pgAdmin service|

2. From the project root, execute: `docker-compose -f environment/docker-compose.yml --env-file environment/variables.dev.env up -d`

3. If everything was fine, you should be able to go to http://localhost:9999/ and the pgAdmin web interface will be accessible.

4. Login using pydataq@pydataq.com as user and the value you gave to POSTGRES_PASSWORD as password. 

5. Once in, add the Postgres servers. You will see some sample tables created in the databases used for testing purposes.

### If you are using vscode
1. Create a file named ".env" in the root of your project directory
2. Add the following two lines to this file:
    ```
    SOURCE_CONN=postgresql://<user>:<pass>@localhost:<port>/<dbname>
    TARGET_CONN=postgresql://<user>:<pass>@localhost:<port>/<dbname>
    ```
4. Open the file .vscode/settings.json and and this following line `"python.envFile": "${workspaceFolder}/.env"`
3. Run the tests using the vscode test runner

### If you are using bash
1. Exporting the environment variables should do the trick
2. The go to the project root directory and run "pytest"
