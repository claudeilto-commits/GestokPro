# Overview

GestokPro is a Flask-based inventory management system designed for small to medium businesses. The application provides a web interface for managing product catalogs, tracking stock levels, and monitoring inventory metrics. Built with Python Flask, it offers user authentication, product CRUD operations, and a dashboard for inventory analytics. The system is localized in Portuguese (Brazilian) and focuses on simplicity and ease of use for inventory management tasks.

# User Preferences

Preferred communication style: Simple, everyday language.

# System Architecture

## Frontend Architecture
- **Template Engine**: Jinja2 with Flask's built-in templating system
- **UI Framework**: Tailwind CSS for responsive design and modern styling
- **Icons**: Font Awesome for consistent iconography
- **Architecture Pattern**: Server-side rendered templates with minimal JavaScript
- **Responsive Design**: Mobile-first approach with responsive grid layouts

## Backend Architecture
- **Web Framework**: Flask with Blueprint-style organization (though not explicitly using blueprints)
- **Application Structure**: Monolithic Flask application with separation of concerns
- **Forms**: WTForms with Flask-WTF for form handling and validation
- **Authentication**: Flask-Login for session management and user authentication
- **Password Security**: Werkzeug's security utilities for password hashing
- **Request Handling**: Standard Flask routing with decorators for authentication

## Data Storage
- **Database**: SQLite for development/local deployment
- **ORM**: SQLAlchemy with Flask-SQLAlchemy integration
- **Database Schema**: Two main entities - Users (usuarios) and Products (produtos)
- **Connection Management**: Connection pooling with automatic reconnection
- **Migration Strategy**: Manual database initialization script (init_db.py)

## Authentication & Authorization
- **User Management**: Email-based authentication with password hashing
- **Session Management**: Flask-Login handles user sessions
- **Role-Based Access**: Admin flag for user permissions
- **Security**: CSRF protection via Flask-WTF forms
- **Password Policy**: Basic password requirements with secure hashing

## Application Configuration
- **Environment Variables**: Session secrets and configuration via environment variables
- **Proxy Support**: ProxyFix middleware for deployment behind reverse proxies
- **Development Mode**: Debug mode enabled for development environment
- **Static Assets**: Standard Flask static file serving

## Data Models
- **Usuario Model**: User accounts with email, password hash, and admin privileges
- **Produto Model**: Product catalog with SKU, name, description, quantity, and pricing
- **Business Logic**: Built-in methods for stock calculations and status determination

# External Dependencies

## Core Framework Dependencies
- **Flask**: Web application framework and routing
- **Flask-SQLAlchemy**: Database ORM and connection management
- **Flask-Login**: User authentication and session management
- **Flask-WTF**: Form handling and CSRF protection
- **WTForms**: Form validation and rendering
- **Werkzeug**: WSGI utilities and security functions

## Frontend Dependencies
- **Tailwind CSS**: Utility-first CSS framework (CDN)
- **Font Awesome**: Icon library (CDN)

## Database Dependencies
- **SQLite**: Embedded database (no external service required)
- **SQLAlchemy**: Database abstraction layer

## Development Tools
- **Python Standard Library**: Logging, os, time modules for application functionality

## Deployment Considerations
- **WSGI Server**: Compatible with any WSGI server (Gunicorn, uWSGI)
- **Static File Serving**: Can be handled by web server or Flask in development
- **Database Migration**: Manual initialization script provided
- **Environment Configuration**: Supports environment-based configuration