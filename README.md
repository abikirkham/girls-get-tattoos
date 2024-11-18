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
- [Deployment](#deployment)
- [Testing](#testing)
- [Issues](#issues)
- [Credits](#credits)

---

## Project Overview
This is an e-commerce website focused on providing tattoo design services. Customers can:
1. Purchase pre-designed tattoos.
2. Request custom tattoo designs.
3. Book consultations to discuss tattoo ideas.
4. View their purchases bookings through an interactive calendar.
5. Pay securely via Stripe.
6. If a store owner, have the control over product and consultation management.

## Features
- **Authentication**: User registration and login via email or social media.
- **User Profiles**: Save favorite tattoo designs, view order history, and bookings.
- **Stripe Payment Integration**: Secure payments for tattoos and consultations.
- **Consultation Booking**: Users can select dates from a calendar and manage appointments.
- **Admin Interface**: Manage orders, consultations, and calendar events.
- **SEO & Marketing**: SEO implementation, including robots.txt, sitemap, and meta tags.

## User Stories
1. **Authentication and User Profiles**:
   - “As a user, I want to create an account so that I can save my favorite tattoos and view my order history.”
   - “As a user, I want to log in using my email or social media account so that I can easily access my saved items.”
   
2. **Shopping & Filtering**:
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

... process to shopping and management.

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
  - A mockup Instagram business page is created for social media marketing which can be accessed in the header.

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

## Deployment

### Making a Local Clone to create project

- Find the GitHub Repository.
- Click the Code button
- Copy the link shown.
- In Gitpod, change the directory to the location you would like the cloned directory to be located.
- Type git clone, and paste the link you copied in step 3.
- Press Enter to have the local clone created.

### Updating my changes

git add <file> - This command was used to add the file(s) to the staging area before they are committed.

git commit -m “commit message” - This command was used to commit changes to the local repository queue ready for the final step.

git push - This command was used to update all committed code to the remote repository on github.

### Heroku


#### 1. Prepare Your Project

Ensure your project has the necessary files for deployment:

- **Procfile**: Specifies the commands that are executed by the app on startup.
    ```makefile
  python app.py 
  ```
- **requirements.txt**: Lists all the dependencies your app needs.
    ```makefile
  Flask==1.1.2
  gunicorn==20.0.4
  ```

#### 2. Create a New Heroku App
Open your terminal and log in to Heroku:

```
bash:
heroku login
Create a new app:

bash:
heroku create girls-get-tattoos
```

Alternatively, create an app directly from the Heroku dashboard by clicking "New" and then "Create new app".

#### 3. Connect Heroku App to GitHub
- Go to Heroku Dashboard: Navigate to the Heroku dashboard.
- Select Your App: Click on the app you created.
- Deploy Tab: Go to the "Deploy" tab.
- Deployment Method: Under "Deployment method", select "GitHub".
- Connect to GitHub: Authorise Heroku to access your - GitHub account if it's your first time. Search for the repository you want to connect and click "Connect".

#### 4. Configure Environment Variables
Set any necessary environment variables for your app:

Go to the "Settings" tab.
Click "Reveal Config Vars".
Add your key-value pairs.

#### 5. Manual Deployment
In the "Deploy" tab:

Go to the "Manual deploy" section.
Select the branch you want to deploy.
Click "Deploy Branch".



## Testing

#### HTML

<details>
<summary>Click to expand.</summary>

- About.html
<img src="READMEmedia/home-validate.png">

- Explain here

- Dashboard.html
<img src="READMEmedia/">

- 

- Login.html
<img src="READMEmedia/">

- Logout.html
<img src="READMEmedia/">

- Messages.html
<img src="READMEmedia/">

- Profile.html
<img src="READMEmedia/">

- Register.html
<img src="READMEmedia/">

- As you can see here on the register page, these errors are coming from the django modal. This does not cause any issues with the sign up however I was unable to do this with the time limits.

</details>

#### CSS

<details>
<summary>Click to expand.</summary>

- I have included only one screenshot as all the pages are linked to the same CSS and all pages load the styles consistently as can be seen in the features.

<img src="READMEmedia/css-checker.png" width="250px">

</details>

#### JAVASCRIPT

<details>
<summary>Click to expand.</summary>

- JShint

<img src="READMEmedia/jshint.png" width="250px">

</details>


### Responsiveness 

<details>
<summary>Click to expand.</summary>

- .html

<img src="READMEmedia/signin.png">

- .html

<img src="READMEmedia/signin.png">

</details>

### Compatibilty 

The project has been tested for compatibility with the following browsers using this site. You will be able to see there are no issues with the compatability across these browsers:

- Google Chrome (Version 124)
- Edge (Version 124)
- Firefox (Version 124)
- Opera (Version 109)
- macOS Sonoma (17)
- Chrome (124)
- iOS (<= 16 17)

<img src="">

### Accessibility

By utilising the Wave Accessibility tool for ongoing development and final testing, used for the below:

1. Ensure all forms have associated labels or appropriate aria-labels.
2. Validate that color contrasts meet the minimum ratios outlined in WCAG 2.1 Contrast Guidelines.
3. Verify correct heading levels to accurately convey content importance.
4. Confirm content is organized within landmarks for ease of use with assistive technology.
5. Provide alternative text or titles for non-textual content.
6. Set the HTML page lang attribute.
7. Implement Aria properties in adherence to best practices outlined in WCAG 2.1.
8. Follow established coding best practices for WCAG 2.1.


### Manual Testing 



## Issues

- 


## Credits
- **Django Documentation**: For framework setup and understanding models.
- **Stripe API**: For payment gateway integration.
- **Bootstrap**: For responsive design elements.
- **MailChimp**: For integrating newsletter functionality.
- **Boutique Abdo**: Code institute guide.