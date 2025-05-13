from flask import Flask
from flask_cors import CORS
from config import Config
from app.extensions import db
from app.models.user import User
from app.models.product import Product
from app.models.purchase import Purchase

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Enable CORS - Configure to allow all origins
    CORS(app, 
         origins=["*"],
         supports_credentials=True, 
         allow_headers=["Content-Type", "Authorization", "X-Requested-With", "Accept"],
         methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"])
    
    # Initialize extensions
    db.init_app(app)
    
    # Create database tables
    with app.app_context():
        db.create_all()
    
    # Register blueprints
    from app.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    # Initialize services
    with app.app_context():
        from app.services.user_service import UserService
        from app.services.product_service import ProductService
        from app.services.purchase_service import PurchaseService

        app.user_service = UserService(db)
        app.product_service = ProductService(db)
        app.purchase_service = PurchaseService(db, app.user_service, app.product_service)
    
    return app


