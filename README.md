# pydataq

## Pipenv virtual environments

This project makes use of [pipenv](https://pipenv.pypa.io/en/latest/) to manage all the needed packages for the project as well as a virtual environment. To install pipenv, follow [these steps](https://pipenv.pypa.io/en/latest/#install-pipenv-today).

After cloning the repository, under the project root execute the following command to install the needed pip packages:

`pipenv install`

Activate the enviromnent with:

`pipenv shell`

And happy coding!


## Postgres for env environment
In order to set up your first pydataq test, it is recommended to run two docker containers with postgres. You can easily do that as it follows:
1. `docker pull postgres`
2. `docker run -d --name pydataq01 -v pydataq01:/var/lib/postgresql/data -e POSTGRES_PASSWORD=<your_pass> -p <a_port>:5432 postgres`
3. `docker run -d --name pydataq02 -v pydataq02:/var/lib/postgresql/data -e POSTGRES_PASSWORD=<your_pass> -p <another_port>:5432 postgres`
4. Use the script provided in `sample dataset` folder to populate both databases

Now you're good to start writing tests!

In order to run these tests using the docker images just follow these instructions.

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
