from app import create_app

app = create_app()
app.logger.info("shopping is running")