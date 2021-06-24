# Courier
![](https://github.com/minkikim98/courier/blob/master/assets/images/courier-welcome.png)
[Courier](https://aa-courier.herokuapp.com/about) is a [Doordash](https://www.doordash.com/) clone, built using Flask and React-Redux. Users can browse restaurants near the App Academy headquarters and add food items to their cart for checkout and delivery! 

## Tech Stack
   - Javascript
   - React
   - React-Redux
   - Python
   - Flask
   - PostgresSQL
   - HTML
   - CSS

## Overview
The goal of this 2-week solo project was to implement some basic MVP features.
* Restaurants - Users can browse a selection of restaurants and their menu items.
* Cuisines - Users can filter restaurants by cuisine type and by various tags (Popular, Cultural, etc).
* Cart - Users can add restaurant items to their personal cart and remove any items that they don't want.

In addition to these core features, there were stretch goals and bonus features, including:
* Search bar functionality - Users can search for specific restaurants by name. - **Completed**.
* Checkout - Users can checkout the items in their cart, which takes them to a separate order page - *In progress*.
* Google Maps integration - Integrating Google Maps API to display geographical information - *TBA*.


## Features

### Login/Signup
Nothing too fancy here, just a standard UI for logging in to an existing account or signing up for a new one.
I added a demo button if someone just wants to see how the site works.  

![](https://github.com/minkikim98/courier/blob/master/assets/images/login.png)

### Restaurants
This is the main page of the application. As you can see, users can see a list of suggested restaurants initially. I tried to be faithful to Doordash's main page, but you'll notice some differences too!  
  
When you load the main page, a Redux thunk fetches *all* the restaurant data from the backend and stores it in a slice of state! On subsequent visits to this page, the data is fetched from state! This reduces strain on the backend server.  

![](https://github.com/minkikim98/courier/blob/master/assets/images/main.png)

### Cuisines
You can filter restaurants by what kind of food you're in the mood for. Each restaurant has a list of tags and cuisines that it's associated with in the database model. These aren't just hard-coded values! This approach makes it easier to add new restaurants and is good for scalability as well.  
  
By the way, I directly host the image URL's for the cuisine logos using Amazon's AWS technology!   

![](https://github.com/minkikim98/courier/blob/master/assets/images/cuisines.png)

### Cart
Users can add items to their personal cart from any restaurant. Carts are personalized for each user, and the contents of a cart are saved when a user logs out. Currently, the website allows users to add items from more than one restaurant, which Doordash doesn't allow. This functionality will most likely by changed as I continue to work on the checkout feature of this site.  

![](https://github.com/minkikim98/courier/blob/master/assets/images/cart.png)

### Search Bar
Users can search for a particular restaurant by name, and can click on the result to take them directly to that restaurant's page. This feature was probably one of my favorite ones to implement. I love figuring out how to filter and sort data, so this was a fun challenge for me.  

![](https://github.com/minkikim98/courier/blob/master/assets/images/search.png)

## That's it!
Thanks for taking the time to check out the site! I'm very proud of what I was able to do in such a short amount of time. Keep checking back for continuous updates and new features!  
  
If you want to see some of my other projects, you can do so 
[here](https://sites.google.com/view/minki-kim/home)!
