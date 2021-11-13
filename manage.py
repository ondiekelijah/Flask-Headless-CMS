import os

def deploy():
	"""Run deployment tasks."""
	from cms import create_app,db

	app = create_app()
	app.app_context().push()

	from flask_migrate import upgrade,migrate,init,stamp
	db.create_all()

	# migrate database to latest revision
	if os.path.exists("./migrations"):
		stamp()
		migrate()
		upgrade()

	else:
		init()
		stamp()
		migrate()
		upgrade()
	
deploy()
	









