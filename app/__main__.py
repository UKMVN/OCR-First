from app import create_application
from app.config import Config
from dotenv import load_dotenv

def main():
    app = create_application()
    app.run(
        host=Config.HOST,
        port=Config.PORT,
        debug=Config.DEBUG,
        threaded=Config.THREADED
    )

if __name__ == '__main__':
    load_dotenv()
    main()