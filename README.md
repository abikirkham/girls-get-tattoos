# Tattoo Design E-commerce Project

This is my e-commerce platform built using Django where customers can purchase custom or pre-designed tattoos and consultations. It integrates Stripe for secure payments, provides user authentication, and enables booking consultation appointments through a calendar system. Users can view previous orders, save favorite tattoo designs, and manage their bookings. 

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [User Stories](#user-stories)
- [Installation](#installation)
- [Technologies Used](#technologies-used)
- [Stripe Payment Integration](#stripe-payment-integration)
- [SEO and Web Marketing](#seo-and-web-marketing)
- [Agile Methodology](#agile-methodology)
- [Custom Models](#custom-models)
- [Custom 404 Page](#custom-404-page)
- [Testing and Debugging](#testing-and-debugging)
- [Credits](#credits)

---

## Project Overview
This is an e-commerce website focused on providing tattoo design services. Customers can:
1. Purchase pre-designed tattoos.
2. Request custom tattoo designs.
3. Book consultations to discuss tattoo ideas.
4. Manage their bookings through an interactive calendar.
5. Pay securely via Stripe.

## Features
- **Authentication**: User registration and login via email or social media.
- **User Profiles**: Save favorite tattoo designs, view order history, and manage bookings.
- **Gallery**: Browse and filter tattoos by size and style.
- **Stripe Payment Integration**: Secure payments for tattoos and consultations.
- **Consultation Booking**: Users can select dates from a calendar and manage appointments.
- **Custom Calendar**: Real-time calendar system to show my availability.
- **Admin Interface**: Manage orders, consultations, and calendar events.
- **SEO & Marketing**: SEO implementation, including robots.txt, sitemap, and meta tags.

## User Stories
1. **Authentication and User Profiles**:
   - “As a user, I want to create an account so that I can save my favorite tattoos and view my order history.”
   - “As a user, I want to log in using my email or social media account so that I can easily access my saved items.”
   
2. **Gallery & Filtering**:
   - “As a customer, I want to filter tattoos by size and style so that I can quickly find designs that match my preferences.”
   - “As a user, I want to view a gallery of custom designs so that I can get inspired for my own tattoo.”
   
3. **Payment and Booking**:
   - “As a user, I want to book a tattoo appointment based on available slots so that I can reserve a convenient time.”
   - “As a customer, I want to pay for my tattoo consultation via Stripe so that I can secure my booking easily.”
   
4. **Checkout and Calendar**:
   - “As a customer, I want to select a date and time from an available calendar when purchasing a tattoo service so that I can schedule my session efficiently.”
   - “As a customer, I want to receive a confirmation email with my appointment details after payment so that I know my booking is confirmed.”

## Installation
To set up the project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/tattoo-ecommerce.git
   ```

2. **Navigate to the project directory**:
   ```bash
   cd tattoo-ecommerce
   ```

3. **Set up a virtual environment**:
   ```bash
   python -m venv env
   source env/bin/activate  # For Windows: env\Scripts\activate
   ```

4. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up the database**:
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser for accessing the admin interface**:
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

... process to gallery y management.

## Technologies Used
- **Django**: Web framework.
- **PostgreSQL**: Database.
- **Stripe API**: Payment gateway.
- **JavaScript**: For calendar and interactive elements.
- **HTML/CSS**: Front-end structure and design.
- **Bootstrap**: Responsive design.
- **Celery/Redis**: For handling background tasks (e.g., confirmation emails).

## Stripe Payment Integration
I have integrated Stripe to process payments for:
- Custom tattoo designs.
- Pre-designed tattoos.
- Consultation bookings.

I will set up my Stripe API keys in my Django settings:

```python
STRIPE_PUBLIC_KEY = 'your_public_key_here'
STRIPE_SECRET_KEY = 'your_secret_key_here'
```

## SEO and Web Marketing
- **SEO**: 
  - A `robots.txt` file will be added to the project to guide web crawlers.
  - A `sitemap.xml` file will be created to help with indexing.
  - Descriptive meta tags are included on all key pages.
  
- **Marketing**:
  - A mockup Instagram business page is created for social media marketing.
  - A newsletter sign-up form integrated with MailChimp for lead generation.

## Agile Methodology
I followed Agile methodologies throughout the project:
- **User Stories**: Clearly defined user stories were created and tracked using GitHub Projects.
- **Tasks**: Each feature was broken down into individual tasks, which were tracked in GitHub issues.
- **Iterative Development**: The project was built in iterative cycles with regular updates to features and testing.


## Custom Models
1. **TattooDesign**: Stores information about tattoo designs (custom or pre-made).
2. **Consultation**: Handles booking of consultation appointments and stores relevant info.
3. **Order**: Stores user order history, including tattoo designs and consultations.

## Custom 404 Page
A custom 404 error page has been implemented to improve user experience. The template is located in the `templates` directory as `404.html`.

## Testing and Debugging
- **Unit Testing**: I used Django's testing framework for unit testing models and views.
- **Error Logging**: Errors are logged using Django's in-built logging system for easy debugging.

## Credits
- **Django Documentation**: For framework setup and understanding models.
- **Stripe API**: For payment gateway integration.
- **Bootstrap**: For responsive design elements.
- **MailChimp**: For integrating newsletter functionality.
- **Boutique Abdo**: Code institute guide.