
## Testing

#### HTML

<details>
<summary>Click to expand.</summary>


- [home.html](https://girls-get-tattoos-6ad59281377a.herokuapp.com/)
  ![HTML Validator](READMEmedia/home-validator.png)
  
- [signup.html](https://girls-get-tattoos-6ad59281377a.herokuapp.com/accounts/signup/)
  ![HTML Validator](READMEmedia/signup-validator.png)

- [login.html](https://girls-get-tattoos-6ad59281377a.herokuapp.com/accounts/login/)
  ![HTML Validator](READMEmedia/login-validator.png)

- [products.html](https://girls-get-tattoos-6ad59281377a.herokuapp.com/products/)
  ![HTML Validator](READMEmedia/products-validator.png)

- [consultations.html](https://girls-get-tattoos-6ad59281377a.herokuapp.com/consultations/)
  ![HTML Validator](READMEmedia/consultation-validator.png)

- [contact.html](https://girls-get-tattoos-6ad59281377a.herokuapp.com/contact/)
  ![HTML Validator](READMEmedia/contact-validator.png)

- [bag.html](https://girls-get-tattoos-6ad59281377a.herokuapp.com/bag/)
  ![HTML Validator](READMEmedia/bag-validator.png)

- [reset-password.html](https://girls-get-tattoos-6ad59281377a.herokuapp.com/accounts/password/reset/)
  ![HTML Validator](READMEmedia/reset-password-validator.png)

- [product_detail.html](https://girls-get-tattoos-6ad59281377a.herokuapp.com/products/1/)
  ![HTML Validator](READMEmedia/product-details-validator.png)

- [consultation1.html](https://girls-get-tattoos-6ad59281377a.herokuapp.com/consultations/1/)
  ![HTML Validator](READMEmedia/consultation-details-validator.png)


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
- Here I included all my javascript in one jshint validator image for testing. 

<img src="READMEmedia/jshint.png" width="250px">

</details>


### Responsiveness 

<details>
<summary>Click to expand.</summary>

- .html

<img src="READMEmedia/.png">


</details>

### Compatibilty 

The project has been tested for compatibility with the following browsers using this site. You will be able to see there are no issues with the compatability across these browsers:

- Google Chrome (Version 124)

<img src="READMEmedia/chrome.png">

- Edge (Version 124)

<img src="READMEmedia/edge.png">

- Firefox (Version 124)

<img src="READMEmedia/firefox.png">

- Safari (Version 17)

<img src="READMEmedia/safari.png">

- iE (11)

<img src="READMEmedia/explorer.png">


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


| Function                      | User Action                                                                 | Outcome                                                                                               | Result |
|------------------------------|-----------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|--------|
| **Load Home Page**            | Access the Girls Get Tattoos link                                            | The homepage loads with an active navigation system, site branding, and products display.            | Pass   |
| **Load Signup Page**          | From the home page, click on the "Sign Up" link                              | The signup page loads with fields for username, email, password, and a submit button.                | Pass   |
| **Load Login Page**           | From the home page, click on the "Login" link                                | The login page loads with username, password fields and a submit button.                             | Pass   |
| **Browse Products**           | From the navigation, select "Products"                                       | The products page loads with a list of available products, each with an image, name, and price.       | Pass   |
| **View Product Details**      | Click on a product from the "Products" page                                  | The product detail page loads with more information, including a description, price, and images.     | Pass   |
| **Add Product to Bag**        | On the product detail page, click "Add to Bag"                               | The item is added to the shopping bag, and the bag icon in the navigation updates with the count.     | Pass   |
| **View Shopping Bag**         | From the navigation, click on the "Bag" icon                                 | The shopping bag page loads, showing added items with quantity and price details.                    | Pass   |
| **Update Quantity in Bag**    | On the shopping bag page, update the quantity of a product                  | The page refreshes, updating the product quantity and recalculating the total price.                 | Pass   |
| **Remove Product from Bag**   | On the shopping bag page, click the "Remove" button on a product            | The product is removed from the shopping bag, and the page is updated to reflect the change.         | Pass   |
| **Proceed to Checkout**       | On the shopping bag page, click "Proceed to Checkout"                        | The checkout page loads with fields for shipping details, payment options, and a review of the order. | Pass   |
| **Submit Order**              | On the checkout page, fill in the necessary details and submit the order     | The order is placed successfully, and the user is shown a confirmation page with order details.      | Pass   |
| **Contact Us Page**           | From the navigation, click on "Contact"                                      | The contact page loads with a form for users to fill out their name, email, and message.             | Pass   |
| **Consultations Page**        | From the navigation, click on "Consultations"                                | The consultations page loads, displaying available options for users to book a tattoo consultation.  | Pass   |
| **View Consultation Details** | Click on a specific consultation service on the consultations page           | The consultation detail page loads with more information about the consultation process and pricing. | Pass   |
| **Submit Consultation Request**| On the consultation detail page, select a service and submit the form       | A success message is shown after submitting the consultation request.                                 | Pass   |
| **Forgot Password**           | On the login page, click "Forgot Password"                                   | The password reset page loads, allowing the user to input their email for a password reset.         | Pass   |
| **Login with Correct Credentials**| On the login page, enter correct username and password                  | The user is logged in successfully and redirected to the homepage or their account dashboard.         | Pass   |
| **Logout**                    | After logging in, click the "Logout" link in the navigation                  | The user is logged out and redirected to the login page.                                              | Pass   |
| **View Product in Bag**       | After adding a product to the bag, click on the bag icon                     | The bag icon updates with the product details and total price.                                        | Pass   |
| **View Account Profile**      | After logging in, click on the "Account" link in the navigation              | The user's profile page loads with their personal details, order history, and account settings.      | Pass   |
| **Update Account Details**    | On the profile page, update personal details and save                       | The updated details are saved successfully and displayed on the profile page.                        | Pass   |
| **View Order History**        | On the account profile page, click on "Order History"                        | The order history page loads, showing past orders with their details and statuses.                   | Pass   |



## Issues

<img src="READMEmedia/issue1.png">

- 

<img src="READMEmedia/issue2.png">

- 