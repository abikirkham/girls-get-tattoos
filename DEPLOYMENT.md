# Deployment

## Payment Setup

1. Register for a Stripe account at [Stripe Registration](https://dashboard.stripe.com/register).

2. Navigate to the Developers page in your Stripe dashboard:

3. Select **API Keys** from the sidebar:

4. Copy the `public key` and `secret key` and add them to your `env.py` file.

5. Update your `settings.py` file with the following:

   ```python
   STRIPE_PUBLIC_KEY = os.environ.get("STRIPE_PUBLIC_KEY")
   STRIPE_SECRET_KEY = os.environ.get("STRIPE_SECRET_KEY")

6. Install the Stripe package:

```
pip3 install stripe
```

7. Create an order model with the required fields in the orders app.

8. Set up a payment app and its associated structure.

9. Add a payment form to the payment app's template.

10. Include a <div> to hold the Stripe element:

```
<div id="stripe-element"></div>
```

11. Create a view to handle the payment setup:

Retrieve the public key: stripe_public_key = settings.STRIPE_PUBLIC_KEY.
Retrieve the secret key: stripe_secret_key = settings.STRIPE_SECRET_KEY.
Create a payment intent: intent = stripe.PaymentIntent.create(**kwargs).
Include in **kwargs:
amount: Payment amount.
currency: Payment currency.
metadata: Include additional data, such as user_id.
Example context for the view:

```
context = {
    'my_profile': my_profile,
    'total_sum': total_sum,
    'client_secret': intent.client_secret,
    'stripe_public_key': stripe_public_key,
}
```

12. Add an extra JavaScript block in your payment template, including CSRF token and Stripe public key:

```
{% block postloadjs_extra %}
  <script>
      let CSRF_TOKEN = '{{ csrf_token }}';
      let stripe_public_key = '{{ stripe_public_key }}';
  </script>
  <script src="https://js.stripe.com/v3/"></script>
  <script src="{% static 'js/payment.js' %}" data-rel-js></script>
{% endblock %}
```

13. In payment.js, define variables for Stripe, the payment element, and the client_secret. Use a data-secret attribute in the confirmation button for the client secret:

```
<button data-secret="{{ client_secret }}">Confirm</button>

```
14. Set up Stripe elements for card input:

```
let elements = stripe.elements();
let style = {
    base: {
        color: "#000",
        lineHeight: '2.4',
        fontSize: '16px'
    }
};
let card = elements.create("card", { style: style });
card.mount("#card-element");
```

14. Gather form data using new FormData() and send it via AJAX to a URL like window.location.origin + '/orders/add/'.

15. In the orders app views, create a view to handle order creation.

15. Test the payment process using Stripe-provided test cards:

No auth: 4242424242424242
Requires auth: 4000002500003155
Error: 4000000000009995

17. Create a success page to redirect users after a successful payment. Use JavaScript to handle redirection:

```
if (result.paymentIntent.status === 'succeeded') {
    window.location.replace(window.location.origin + "/payment/order_placed/");
}
```

18. Install and configure the Stripe CLI:

Follow the Stripe CLI Documentation to download the correct version for your OS.

```
./stripe login
```
Follow the prompts to log in and connect to your Stripe dashboard.

19. Create a function in the orders app views to handle payment confirmation and send email notifications.

---

## Making a Local Clone to create project

- Find the GitHub Repository.
- Click the Code button
- Copy the link shown.
- In Gitpod, change the directory to the location you would like the cloned directory to be located.
- Type git clone, and paste the link you copied in step 3.
- Press Enter to have the local clone created.

## Installation
To set up the project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/abikirkham/girls-get-tattoos.git
   ```

2. **Navigate to the project directory**:
   ```bash
   cd girls-get-tattoos
   ```

3. **Set up a virtual environment**:
   ```bash
   python -m venv env
   source env/bin/activate  
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


## Updating my changes

git add <file> - This command was used to add the file(s) to the staging area before they are committed.

git commit -m “commit message” - This command was used to commit changes to the local repository queue ready for the final step.

git push - This command was used to update all committed code to the remote repository on github.


---

## Heroku


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

### 2. Create a New Heroku App
Open your terminal and log in to Heroku:

```
bash:
heroku login
Create a new app:

bash:
heroku create girls-get-tattoos
```

Alternatively, create an app directly from the Heroku dashboard by clicking "New" and then "Create new app".

### 3. Connect Heroku App to GitHub
- Go to Heroku Dashboard: Navigate to the Heroku dashboard.
- Select Your App: Click on the app you created.
- Deploy Tab: Go to the "Deploy" tab.
- Deployment Method: Under "Deployment method", select "GitHub".
- Connect to GitHub: Authorise Heroku to access your - GitHub account if it's your first time. Search for the repository you want to connect and click "Connect".

### 4. Configure Environment Variables
Set any necessary environment variables for your app:

Go to the "Settings" tab.
Click "Reveal Config Vars".
Add your key-value pairs.

### 5. Manual Deployment
In the "Deploy" tab:

Go to the "Manual deploy" section.
Select the branch you want to deploy.
Click "Deploy Branch".

---

## Important note


**NOTE !**

As the app requires assigning a role for each user, you will need to apply some changes Profile model for the role field.:

```python
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(
        max_length=20, null=True, blank=True)
    default_country = CountryField(
        blank_label='Country *',
        null=True,
        blank=True
    )
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_town_or_city = models.CharField(
        max_length=40, null=True, blank=True)
    default_street_address1 = models.CharField(
        max_length=80, null=True, blank=True
    )
    default_street_address2 = models.CharField(
        max_length=80, null=True, blank=True
    )
    default_county = models.CharField(max_length=80, null=True, blank=True)

    def __str__(self):
        """
        Returns a string representation of the user profile by username.
        """
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """Create or update the user profile when a User instance is saved."""
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()

```

- ```python manage.py makemigrations```
- ```python manage.py migrate```

- After migration, you will need to create a superuser.


8. Create the superuser.

    - ```python manage.py createsuperuser```


**After the following steps, you will ensure that the app is working correctly, and any other user registered in your app will only have access as a customer. The rest of the roles will be controlled by the admin.**


9. Run the server.

    - ```python manage.py runserver```

10. Access the website by the link provided in terminal. Add ```/admin/``` at the end of the link to access the admin panel.


---
