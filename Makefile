start-frontend:
	bash -c "cd ./math-buddy; yarn start"

start-backend:
	bash -c "cd ./math-buddy; export FLASK_ENV=development; python3 ./public/app.py"
