
# Testing

The testing.md file provides a comprehensive overview of the testing process conducted for the project, ensuring that all features and functionalities are thoroughly evaluated for performance, usability, and compliance with best practices.

---

## HTML

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

## CSS

<details>
<summary>Click to expand.</summary>

- I have included only one screenshot as all the pages are linked to the same CSS and all pages load the styles consistently as can be seen in the features.

<img src="READMEmedia/css-checker.png" width="250px">

</details>

## JAVASCRIPT

<details>
<summary>Click to expand.</summary>

- JShint
- Here I included all my javascript in one jshint validator image for testing. 

<img src="READMEmedia/jshint.png" width="250px">

</details>

--- 

## PEP8

https://pep8ci.herokuapp.com

<img src="READMEmedia/pep8contact.png" width="250px">
<img src="READMEmedia/pep8order.png" width="250px">
<img src="READMEmedia/pep8product.png" width="250px">
<img src="READMEmedia/pep8profiles.png" width="250px">

---

## Responsiveness 

**Media Query Testing:**
- Below you will see the use of CSS media queries to ensure the layout adjusts based on different screen widths. For example:

<details>
<summary>Click to expand.</summary>

```
          /* -------------------------------- Media Queries */

          /* Slightly larger container on xl screens */
          @media (min-width: 1200px) {
              .container {
                max-width: 80%;
              }
            }

          @media (max-width: 992px) {
              .form-control {
                  width: 80%;
                  font-size: 0.9rem;
                  padding: 0.5rem;
              }
          }

            /* fixed top navbar only on medium and up */
            @media (min-width: 992px) {
                .fixed-top-desktop-only {
                    position: fixed;
                    top: 0;
                    right: 0;
                    left: 0;
                    z-index: 1030;
                }
            
                .header-container {
                    padding-top: 164px;
                }
            }
            
            /* pad the top a bit when navbar is collapsed on mobile */
            @media (max-width: 991px) {
                .header-container {
                    padding-top: 116px;
                }
            
                body {
                    height: calc(100vh - 116px);
                }
            }

            @media (max-width: 576px) {
              footer .row {
                text-align: center;
              }
              #mc_embed_signup {
                margin: 0 auto;
              }
            }
            @media (max-width: 992px) {
              .newsletter-field {
                  left: -1000px;
                  font-size: 0.8rem;
                  width: 70%;
              }
          }

          @media (max-width: 992px) {
              .content-box {
                  margin-top: 60px;
              }
          }
```

</details>

---

## Compatibilty 

The project has been tested for compatibility with the following browsers using this site. You will be able to see there are no issues with the compatability across these browsers:


<details>
<summary>Click to expand.</summary>

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

</details>

---

## Accessibility

By utilising the Wave Accessibility tool for ongoing development and final testing, used for the below:

1. Ensure all forms have associated labels or appropriate aria-labels.
2. Validate that color contrasts meet the minimum ratios outlined in WCAG 2.1 Contrast Guidelines.
3. Verify correct heading levels to accurately convey content importance.
4. Confirm content is organized within landmarks for ease of use with assistive technology.
5. Provide alternative text or titles for non-textual content.
6. Set the HTML page lang attribute.
7. Implement Aria properties in adherence to best practices outlined in WCAG 2.1.
8. Follow established coding best practices for WCAG 2.1.

---

## Manual Testing 


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
| **Submit Consultation Request**| On the consultation detail page, select a service and submit the form       | A success message is shown after submitting the consultation request.                                 | Pass   |
| **Forgot Password**           | On the login page, click "Forgot Password"                                   | The password reset page loads, allowing the user to input their email for a password reset.         | Pass   |
| **Login with Correct Credentials**| On the login page, enter correct username and password                  | The user is logged in successfully and redirected to the homepage or their account dashboard.         | Pass   |
| **Logout**                    | After logging in, click the "Logout" link in the navigation                  | The user is logged out and redirected to the login page.                                              | Pass   |
| **View Product in Bag**       | After adding a product to the bag, click on the bag icon                     | The bag icon updates with the product details and total price.                                        | Pass   |
| **View Account Profile**      | After logging in, click on the "Account" link in the navigation              | The user's profile page loads with their personal details, order history, and account settings.      | Pass   |
| **Update Account Details**    | On the profile page, update personal details and save                       | The updated details are saved successfully and displayed on the profile page.                        | Pass   |
| **View Order History**        | On the account profile page, click on "Order History"                        | The order history page loads, showing past orders with their details and statuses.                   | Pass   |


---

## Testing User Story

### Authentication and User Profiles

| User Story | Requirement Met | Image |
| ---------- | ---------------- | ----- |
| As a user, I want to create an account so that I can save my favorite tattoos and view my order history. | Yes | ![Signup Page](READMEmedia/signup.png) |
| As a user, I want to log in using my email or social media account so that I can easily access my saved items. | Yes | ![Login Page](READMEmedia/signin.png) |
| As a user, I want to update my profile details (name, email, password) so that my account information is accurate. | Yes | ![Profile Update](READMEmedia/my%20profile.png) |
| As an admin, I want to view a list of registered users so that I can manage accounts and view their activities. | Yes | ![Admin User List](READMEmedia/admin-user.png) |

### Shopping & Filtering

| User Story | Requirement Met | Image |
| ---------- | ---------------- | ----- |
| As a customer, I want to filter tattoos by size and style so that I can quickly find designs that match my preferences. | Yes | ![Filter Tattoos](READMEmedia/filter.png) |
| As a customer, I want to sort tattoos by price or rating so that I can find options within my budget or the highest-rated designs. | Yes | ![Sort Tattoos](READMEmedia/sort.png) |
| As a user, I want to view detailed product information, including pricing and design descriptions so that I can make an informed purchase. | Yes | ![Product Details](READMEmedia/product_detail.png) |

### Payment and Booking

| User Story | Requirement Met | Image |
| ---------- | ---------------- | ----- |
| As a customer, I want to add products to my cart so that I can purchase multiple items at once. | Yes | ![Add to Cart](READMEmedia/quickadd.png) ![Add to cart 2](READMEmedia/addtobag.png) |
| As a customer, I want to securely pay for my tattoo consultation via Stripe so that I can complete my booking without any worries. | Yes | ![Stripe Payment](READMEmedia/stripe-payment.png) |
| As a user, I want to book a tattoo appointment based on available slots so that I can reserve a convenient time with an artist. | Yes | Please see the [error](#errors) explained for this. |
| As a user, I want to receive a confirmation email with my appointment details after payment so that I know my booking is confirmed. | Yes | Please see the [error](#errors) explained for this. |

### Consultation Booking

| User Story | Requirement Met | Image |
| ---------- | ---------------- | ----- |
| As a customer, I want to see available dates and times for consultations so that I can select a slot that works for me. | Yes | Please see the [error](#errors) explained for this. |
| As a customer, I want to cancel or reschedule my consultation if my plans change, with an easy-to-use interface. | Yes | Please see the [error](#errors) explained for this. |
| As a user, I want to view my past consultations, including dates, artist details, and feedback, so that I can keep track of my sessions. | Yes | Please see the [error](#errors) explained for this. |

### Wishlist and Likes

| User Story | Requirement Met | Image |
| ---------- | ---------------- | ----- |
| As a user, I want to save my favorite tattoos to a wishlist so that I can easily return to them later. | Yes | ![Add to Wishlist](READMEmedia/like1.png) |
| As a user, I want to "like" products in the store so that I can quickly access them from my profile. | Yes | ![Like Product](READMEmedia/like2.png) |
| As a user, I want to view all the products I've liked on a dedicated page so that I can easily browse my favorites. | Yes | ![Liked Products](READMEmedia/viewlikes.png) |

### Order History and Tracking

| User Story | Requirement Met | Image |
| ---------- | ---------------- | ----- |
| As a user, I want to view my order history so that I can track my previous purchases and consultations. | Yes | ![Order History](READMEmedia/previousorders.png) |

### Admin Management

| User Story | Requirement Met | Image |
| ---------- | ---------------- | ----- |
| As an admin, I want to manage products and consultations in the system so that I can keep the catalog up to date. | Yes | ![Manage Products](READMEmedia/adminproducts.png) |
| As an admin, I want to track customer purchases and consultations so that I can offer tailored services and recommendations. | Yes | ![Track Purchases](READMEmedia/adminorders.png) |
| As an admin, I want to manage user accounts (approve, deactivate) so that I maintain the security of the platform. | Yes | ![Manage Accounts](READMEmedia/admin1.png) |

### SEO & Marketing

| User Story | Requirement Met | Image |
| ---------- | ---------------- | ----- |
| As a user, I want to share tattoo designs and consultations on social media platforms like Instagram so that I can show my choices to friends. | Yes | ![Social Sharing](READMEmedia/fbfeed.png) |
| As a marketer, I want to optimize the website's SEO using meta tags, sitemaps, and descriptions to ensure it ranks higher on search engines. | Yes | ![SEO Optimisation](READMEmedia/sitemap.png) |
| As a user, I want to subscribe to a newsletter so that I can receive updates about new tattoo designs and promotions. | Yes | ![Newsletter Subscription](READMEmedia/footer-subscribe.png) |

### Accessibility

| User Story | Requirement Met | Image |
| ---------- | ---------------- | ----- |
| As a user, I want to have sufficient contrast in visuals so that the website is easy to read under various lighting conditions. | Yes | ![High Contrast](READMEmedia/flower-bug.png) |
| As a user, I want the forms to have clear labels and instructions so that I can easily fill them out without confusion. | Yes | ![Clear Labels](READMEmedia/labels.png) |
| As a user, I want to receive clear error messages when I make mistakes while filling out forms. |	Yes	| Error messages are displayed near the relevant field with sufficient information on how to resolve the error. |
| As a user with visual impairments, I want to have all images described with alternative text, so I can understand their content. |	Yes	| All images have descriptive alt attributes, following the WCAG 2.1 guidelines for text alternatives.

### 404 Error and Custom Pages

| User Story | Requirement Met | Image |
| ---------- | ---------------- | ----- |
| As a user, I want to be shown a custom 404 error page if I navigate to a non-existing page so that my experience isn't disrupted with an unfriendly error. | Yes | ![404 Error Page](READMEmedia) |
| As an admin, I want to update the content on the 404 error page to reflect the website's branding, offering users helpful links to explore other parts of the site. | Yes | ![Custom 404 Page](READMEmedia) |

---

## Errors

1. **Google Calendar API Verification**

I have set up the Google Cloud Calendar API; however, an error occurs after logging in to Google and clicking the "Book a Consultation" link. The error states that the site has not been verified. 

The verification process for Google Cloud is lengthy, as outlined in [Google's Help Documentation](https://support.google.com/cloud/answer/7454865?hl=en). Unfortunately, due to time constraints during the course, I was unable to complete the verification process.

Despite this, I have tested the functionality by proceeding through the "unsafe" option. While I was able to successfully log in:
<img src="READMEmedia/googlelogin.png" width="300px">
I was ultimately unable to proceed further because the site is not verified and cannot be fully trusted by Google. This remains a known issue in the current project implementation.

2. **Toast Dissmissal**

**Error:**
The toast dismissal function is not working as expected. When clicking the dismiss button inside the toast:
```html
<button type="button" class="ml-2 mb-1 close text-dark" data-dismiss="toast" aria-label="Close">
    <span aria-hidden="true">&times;</span>
</button>
```
Nothing happens. The toast does not close as it should.

**Debugging Steps Taken:**
- Verified Bootstrap JavaScript is Loaded:
Checked that Bootstrap JavaScript was properly included and loaded in the project.

- Ensured jQuery is Loaded (for Bootstrap 4):
Confirmed that jQuery was loaded as Bootstrap 4 requires it for components like toast to function properly.

- Checked data-dismiss Attribute:
Ensured that the dismiss button contained the correct data-dismiss="toast" attribute.

- Checked JavaScript Console for Errors:
Inspected the browser’s developer tools console for any JavaScript errors that may be causing the issue, but found no significant errors.

- Manually Triggered Dismissal:

Attempted to manually hide the toast using:

```
    $('.toast').toast('hide');
```

This worked, which indicates the issue lies with the button interaction.

- Checked for JavaScript Conflicts:
Disabled other scripts and libraries temporarily to check for conflicts with Bootstrap's toast functionality.

- Verified Bootstrap Toast Initialization:
Ensured that the toast was properly initialised with:
```
$('.toast').toast('show');
```

- Added Custom Event Listener for Dismissal:

Tried adding a custom event listener to trigger the toast dismissal:
```
    $('.toast .close').click(function() {
        $(this).closest('.toast').toast('hide');
    });
```

- Tested Across Different Browsers:
Tried the functionality on different browsers, but the issue persists.
Despite following all of the above debugging steps, the toast dismissal function still doesn’t work as expected.

Both of these issues have been thoroughly tested and debugged, but unfortunately, no changes have been achieved. I have discussed them with the community on Slack and have gone through the course walkthrough again, but the errors remain unresolved.

---

## Lighthouse Report
LightHouse is a web performance testing tool that can be used to evaluate the performance of a website. The report is generated by Google Chrome.

[Lighthouse Report](READMEmedia/lighthouse.png)

---

## Project assessment criteria CHECKLIST. Portfolio 5: Project Submission

Below I have included the criteria needed in order to Pass this Project submission. I have completed each step by putting a **'X'** in each box.

### **1. Design and Build the Application**
- [ **X** ] **Front-End Design**: Ensure the front-end is easy to navigate and allows users to find information intuitively.
- [ **X** ] **Full CRUD Implementation**: Create, read, update, and delete functionalities are fully implemented and visible in the user interface.
- [ **X** ] **Responsive Design**: Ensure the site is fully responsive and follows UX design and accessibility guidelines.

### **2. Robust Codebase**
- [ **X** ] **Code Quality**: Produce a robust codebase with no logic errors. If errors are presented then document this.
- [ **X** ] **Data Validation**: Validate all input data effectively.
- [ **X** ] **User Feedback**: Provide users with clear progress indicators and feedback on actions.
- [ **X** ] **API Handling**: Handle APIs effectively with clear error handling.

### **3. Thorough Testing**
- [ **X** ] **Testing Approach**: Demonstrate manual and/or automated testing in the git commits (e.g., JavaScript and Python tests).
- [ **X** ] **Bug-Free Code**: Ensure there are no runtime errors or unexpected behaviours.

### **4. Efficient Configuration**
- [ **X** ] **Procfile**: Maintain an organised and effective `Procfile` for deployment.
- [ **X** ] **Requirements.txt**: Include all necessary dependencies in the `requirements.txt` file.
- [ **X** ] **Settings Files**: Keep configuration and settings files well-organised, with different versions for different branches.
- [ **X** ] **Data Store Configuration**: Centralise data store configuration to a single location for easy changes.

### **5. Documentation**
- [ **X** ] **Data Schema**: Fully describe the data schema in the README file.
- [ **X** ] **Deployment**: Document the deployment process (e.g., Heroku).
- [ **X** ] **Version Control**: Use version control software effectively, providing a detailed record of the development process.

### **6. User Experience**
- [ **X** ] **User Control**: Allow users full control of their interaction with the application.
- [ **X** ] **Purpose Visibility**: Ensure the site’s purpose is immediately evident to a new user without needing supporting documentation.
- [ **X** ] **Meeting Expectations**: Address user demands and expectations effectively.
- [ **X** ] **Large Data Sets**: Provide progress indicators for loading large data sets.

### **7. SEO and Sitemap**
- [ **X** ] **Robots.txt**: Control access to your sitemap using a `robots.txt` file.
- [ **X** ] **Canonical Links**: Ensure all sitemap links are canonical.
- [ **X** ] **Descriptive Metadata**: Use descriptive metadata for SEO, accurately reflecting the site’s purpose.

### **8. Security and Access Control**
- [ **X** ] **Access Control**: Restrict users to intended views and functionalities only.

### **9. Marketing**
- [ **X** ] **Marketing Strategy**: Document the primary marketing strategy behind the application.
- [ **X** ] **Marketing Tools**: Employ relevant marketing strategies and tools.

### **10. Clear Purpose**
- [ **X** ] **Target Audience**: Define and address the needs of a specific target audience (or multiple related audiences).
- [ **X** ] **Clarity of Purpose**: Ensure the solution’s purpose is well-defined and immediately evident.
