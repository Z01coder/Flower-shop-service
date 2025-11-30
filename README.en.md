<!-- Improved compatibility of Back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="readme-top"></a>



<!-- LANGUAGE SWITCHER -->
<div align="right">
  <strong>Language:</strong> <a href="README.en.md">English</a> | <a href="README.md">Русский</a>
</div>



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->




<!-- PROJECT LOGO -->
<br />
<div align="center">
  <h1 align="center">Flower Shop Service</h3>

  <p align="center">
    Django flower delivery service with Telegram bot integration
    <br />
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About the Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About the Project

![Preview](assets/book.webp)

![Preview](assets/fwsh_prev.gif)

Flower Shop Service is a Django web application for the "Color 25 of Spring" flower delivery service. The project provides a full-featured online flower shop with order placement, cart management, product catalog browsing, and Telegram bot integration for notifications and analytics.

<details>
  <summary><strong>Project Goals and Objectives</strong></summary>

**Goals:**
* Create a full-featured online flower shop with an order system
* Implement a user-friendly interface for selecting and placing orders
* Integrate a Telegram bot for notifications and analytics
* Provide efficient order and product management through the admin panel

**Key Tasks:**
* Develop data models for products, orders, users, and reviews
* Create a product catalog with detailed pages
* Implement a shopping cart and order placement system
* Deploy user authentication and personal account system
* Implement order history with reorder functionality
* Add a review and rating system for products
* Integrate a Telegram bot for order notifications and analytics
* Create an administrative panel for managing orders and products

</details>

<details>
  <summary><strong>Results</strong></summary>

**Implemented Features:**
* User registration and authentication with a custom user model
* Product catalog with detailed pages for each bouquet
* Shopping cart with the ability to add and remove products
* Order placement system with delivery date and time selection
* Order history with reorder functionality
* Review and rating system for products
* User personal account with profile editing
* Administrative panel for managing orders, products, and users
* Sales analytics for administrators
* Telegram bot with notifications for new orders and status changes
* `/analytics` command in the Telegram bot for daily statistics

**Created Components:**
* Django application `flower_shop` with models: CustomUser, Product, Order, OrderItem, Review, Report
* HTML templates for all application pages
* Signal system for automatic Telegram notifications
* Custom management commands for creating test users and products
* Integration with python-telegram-bot for Telegram bot functionality

</details>

<p align="right">(<a href="#readme-top">Back to top</a>)</p>



### Built With

Main technologies and libraries used in the project:

* [![Django][Django-badge]][Django-url]
* [![Python][Python-badge]][Python-url]

Additional dependencies:
* `python-telegram-bot==21.10` - for Telegram bot integration
* `pytest==8.3.4` and `pytest-django==4.10.0` - for testing
* `pillow==11.1.0` - for working with product images
* `python-dotenv==1.0.0` - for managing settings through environment variables
* `SQLite` - database (by default)
* `Bootstrap` - for modern responsive interface design

<p align="right">(<a href="#readme-top">Back to top</a>)</p>



<!-- GETTING STARTED -->
<details>
  <summary><strong>Getting Started</strong></summary>

Instructions for installing and running the project locally.

### Prerequisites

To work with the project, you need to install:

* Python 3.x
  ```sh
  # Check Python version
  python --version
  ```

### Installation

Below are instructions for installing and configuring the application.

1. Clone the repository
   ```sh
   git clone https://github.com/your_username/repo_name.git
   cd Flower-shop-service
   ```

2. Create a virtual environment (recommended)
   ```sh
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Linux/Mac
   source venv/bin/activate
   ```

3. Install dependencies
   ```sh
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root and add the necessary environment variables:
   ```sh
   SECRET_KEY=your-secret-key-here
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1
   TELEGRAM_BOT_TOKEN=your-telegram-bot-token
   TELEGRAM_ADMIN_CHAT_ID=your-telegram-chat-id
   ```

5. Apply migrations
   ```sh
   python manage.py migrate
   ```

6. Create test users
   ```sh
   python manage.py create_test_users
   ```
   
   By default, the following users are created:
   - **Admin:** `admin` / `admin123` (email: `admin@example.com`)
   - **User:** `testuser` / `test123` (email: `testuser@example.com`)

7. (Optional) Create test products
   ```sh
   python manage.py create_test_products
   ```

8. Run the development server
   ```sh
   python manage.py runserver
   ```

9. Open in browser:
   - Home page: http://127.0.0.1:8000/
   - Product catalog: http://127.0.0.1:8000/catalog/
   - Admin panel: http://127.0.0.1:8000/admin/

</details>

<p align="right">(<a href="#readme-top">Back to top</a>)</p>



<!-- USAGE EXAMPLES -->
<details>
  <summary><strong>Usage</strong></summary>

The application provides the following pages and functionality:

### Main Pages:

1. **Home Page** (`/`)
   - Welcome page with service description
   - Available to all users

2. **Product Catalog** (`/catalog/`)
   - Displays all available flower bouquets
   - Available to all users without authentication
   - Shows name, price, and image of each product

3. **Product Detail Page** (`/catalog/<product_id>/`)
   - Detailed information about the bouquet
   - Display of all reviews and ratings
   - Ability to leave a review (requires authentication)
   - Button to add product to cart

4. **Shopping Cart** (`/cart/`)
   - View products in cart
   - Change product quantities
   - Clear cart
   - Proceed to checkout

5. **Order Placement** (`/create_order/`)
   - Form for delivery placement
   - Selection of delivery date and time
   - Delivery address specification
   - Adding a comment to the order
   - Requires authentication

6. **Order History** (`/order_history/`)
   - View all user orders
   - Detailed information about each order
   - Ability to reorder
   - Requires authentication

7. **Personal Account** (`/profile/`)
   - View and edit profile
   - Manage personal data
   - Requires authentication

8. **Registration and Login** (`/register/`, `/login/`)
   - Registration of new users
   - Authentication of existing users
   - Password recovery

9. **Analytics** (`/analytics/`)
   - Sales statistics
   - Reports on orders and revenue
   - Available only to superusers

10. **Admin Panel** (`/admin/`)
    - Standard Django admin panel
    - Management of products, orders, users, and reviews
    - Order status changes
    - Available only to administrators

### Telegram Bot:

- **Order Notifications**: automatic sending of notifications to Telegram when a new order is created
- **Status Change Notifications**: sending messages when order status changes
- **`/analytics` Command**: getting daily statistics on orders and revenue
- The bot starts automatically when the Django application starts

</details>

<p align="right">(<a href="#readme-top">Back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

<details>
  <summary><strong>Show completed development stages</strong></summary>

### Completed Stages:

- [x] **Stage 1: Basic Project Structure**
  - [x] Creating Django project `flower_shop`
  - [x] Setting up basic URL structure and routing
  - [x] Configuring static files and media

- [x] **Stage 2: Data Models**
  - [x] Developing custom user model `CustomUser` with phone and address fields
  - [x] Creating `Product` model for products (bouquets)
  - [x] Developing `Order` model with delivery date and time selection
  - [x] Creating `OrderItem` model for linking orders with products
  - [x] Developing `Review` model with rating system
  - [x] Creating `Report` model for sales analytics
  - [x] Applying database migrations

- [x] **Stage 3: Authentication and Authorization System**
  - [x] Implementing registration of new users
  - [x] Implementing login and logout pages
  - [x] Setting up decorators to protect pages requiring authentication
  - [x] Implementing password recovery
  - [x] Configuring redirects after login/logout

- [x] **Stage 4: Product Catalog**
  - [x] Implementing view for displaying product list
  - [x] Creating product detail page with information display
  - [x] Creating HTML templates for catalog
  - [x] Integrating work with product images

- [x] **Stage 5: Shopping Cart**
  - [x] Implementing adding products to cart (session)
  - [x] Creating cart viewing page
  - [x] Implementing changing product quantities in cart
  - [x] Implementing cart clearing

- [x] **Stage 6: Order System**
  - [x] Creating `OrderForm` for order placement
  - [x] Implementing view for processing orders
  - [x] Creating HTML template for order form
  - [x] Implementing delivery date and time selection
  - [x] Saving order to database with products from cart

- [x] **Stage 7: Order History**
  - [x] Implementing viewing user order history
  - [x] Displaying detailed information about each order
  - [x] Implementing reorder functionality

- [x] **Stage 8: Review and Rating System**
  - [x] Creating `ReviewForm` for adding reviews
  - [x] Implementing ability to leave a review on a product
  - [x] Rating system from 1 to 5 stars
  - [x] Displaying all reviews on product page

- [x] **Stage 9: Personal Account**
  - [x] Creating personal account page
  - [x] Implementing user profile editing
  - [x] Creating `ProfileEditForm` for changing data

- [x] **Stage 10: Administrative Panel**
  - [x] Setting up Django admin panel for all models
  - [x] Adding filters and search in admin panel
  - [x] Configuring order display with inline editing of products
  - [x] Implementing order status changes

- [x] **Stage 11: Sales Analytics**
  - [x] Implementing analytics page for administrators
  - [x] Calculating total revenue and number of orders
  - [x] Creating sales reports
  - [x] Displaying statistics in a convenient format

- [x] **Stage 12: Telegram Bot Integration**
  - [x] Integrating `python-telegram-bot` library
  - [x] Setting up automatic bot startup when application starts
  - [x] Implementing sending notifications for new orders
  - [x] Implementing notifications for order status changes
  - [x] Creating `/analytics` command for getting statistics
  - [x] Setting up sending product photos in notifications

- [x] **Stage 13: Signal System**
  - [x] Implementing signals for automatic notification sending
  - [x] Setting up handling of order creation and update events
  - [x] Integrating signals with Telegram bot

- [x] **Stage 14: Custom Management Commands**
  - [x] Creating `create_test_users` command for creating test users
  - [x] Creating `create_test_products` command for creating test products
  - [x] Implementing image loading for products

- [x] **Stage 15: User Interface Improvements**
  - [x] Integrating Bootstrap for modern design
  - [x] Creating responsive navigation bar
  - [x] Improving forms with Bootstrap CSS classes
  - [x] Displaying user status in navigation
  - [x] Creating beautiful home page design

- [x] **Stage 16: Managing Settings Through Environment Variables**
  - [x] Integrating `python-dotenv` library
  - [x] Moving secret keys to environment variables
  - [x] Configuring `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS` through `.env`
  - [x] Configuring Telegram bot tokens through environment variables

</details>

### Planned Improvements:

- [ ] Adding pagination for product catalog
- [ ] Implementing full-text search for products
- [ ] Adding product filtering by categories and price
- [ ] Implementing discount and promo code system
- [ ] Adding ability to edit and delete reviews
- [ ] Implementing favorite products system
- [ ] Adding email notifications when order status changes
- [ ] Implementing integration with payment systems
- [ ] Adding notification system in personal account
- [ ] Implementing API endpoints (REST API) for mobile application
- [ ] Adding product category management system
- [ ] Implementing export of reports to Excel/PDF
- [ ] Writing unit tests and integration tests
- [ ] Setting up CI/CD pipeline
- [ ] Performance optimization and caching
- [ ] Adding interface multilingualism

<p align="right">(<a href="#readme-top">Back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement". Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">Back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">Back to top</a>)</p>



<!-- CONTACT -->
## Contact

* [![GitHub][GitHub-badge]][GitHub-url]
* [![Gmail][Gmail-badge]][Gmail-url]
* [![Telegram][Telegram-badge]][Telegram-url]

<p align="right">(<a href="#readme-top">Back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

I express sincere gratitude to the [Zerocoder](https://zerocoder.ru/) university and its entire team for creating an inspiring and professional educational environment. For preparing "IT-astronauts" at the Zerocoder "cosmodrome".

Special thanks to:

[Kirill Pshinnik](https://kpshinnik.ru/), the university director, for inspiring the feat;

Teachers [Nina Stefantsova](https://neural-courses.ru/teacher/nina-stefancova/), [Maxim Vershinin](https://neural-courses.ru/teacher/maksim-vershinin/), and [Darya Bobrovskaya](https://neural-courses.ru/teacher/darya-bobrovskaya/) — for deep knowledge, patience, and willingness to always help;

Nikita Murkin, the course curator, for clear organization and mentoring;

Elizaveta, the manager, for care, efficiency, and constant friendliness.

Thanks to you, this project became possible!

<p align="right">(<a href="#readme-top">Back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[Django-badge]: https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white
[Django-url]: https://www.djangoproject.com/
[Python-badge]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/
[GitHub-badge]: https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white
[GitHub-url]: https://github.com/Z01coder
[Gmail-badge]: https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white
[Gmail-url]: mailto:zolotuxin.alexey@gmail.com
[Telegram-badge]: https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white
[Telegram-url]: https://t.me/AZVXAN

