# dev_pyCRUD
Basic Python CRUD Development

#### MAC OSX Notes

$brew update
$brew install pyenv

$pyenv install 3.6.3

$pyenv global 3.6.3


$brew install pipenv
$pip install --user pipenv

$pip install flask==1.0.2

$pipenv install marshmallow==2.16.3

#### Python REST API Persistence with MongoDB

$pipenv install pymongo==3.7.2

$pipenv install pyjwt==1.7.1

$export MONGO_URL=mongodb://mongo_user:mongo_secret@0.0.0.0:27017/

$pipenv install flask_cors==3.0.7

$FLASK_APP=$PWD/app/http/api/endpoints.py FLASK_ENV=development pipenv run python -m flask run --port 4433

#### Client-Side App
$yarn global add create-react-app

$create-react-app app

Inside the directory where you ran $create-react-app app, you can run several commands:

  yarn start
    Starts the development server.

  yarn build
    Bundles the app into static files for production.

  yarn test
    Starts the test runner.

  yarn eject
    Removes this tool and copies build dependencies, configuration files
    and scripts into the app directory. If you do this, you can’t go back!

We suggest that you begin by typing:

  cd app
  yarn start

$yarn add @material-ui/core
$yarn add @material-ui/icons


