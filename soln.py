import json
with open("coffee_product_reviews.json") as f:
    reviews = json.load(f)
type(reviews)

from IPython.display import Image, display

num_reviews = len(reviews)
num_reviews
# print("The coffee product review dataset contains {} reviews".format(num_reviews))

# Ok, so now we know how many records we are working with! Let's investigate what each record looks like. In the cell below, replace `None` with appropriate code to select the first review

first_review = reviews[0]

# for index in range(5):
#     print(reviews[index])

# It looks like each review has the same structure as the first one.
# Edit the string below to describe what we've learned about the dataset so far:

# Replace <None> with an appropriate explanation
"""
For this analysis, we are using a dataset collected from Amazon by <None>

Each record represents a Review

There are a total of 86 records

Each record has 7 keys, all of which are type string

The values associated with these keys have mixed types: float, string, list, <None>, and dictionary
"""

## Review Selection
# Now that we have a general sense of what is contained in our dataset, let's implement a system for a user to be able to query for an individual record. For now, assume that the user can edit the value of a variable in this Jupyter Notebook.

# In the cell below, create a variable called `review_index` and set it to the value of `2`

# (Why are we bothering to use a variable, if we're just "hard-coding" it to 2? Because it's helpful to practice *parameterizing* our code, i.e. using variables that can have their values substituted rather than using the values directly.)

review_index = 2

# Now let's use that review index to create a variable `selected_review` that extracts the relevant review dictionary from the list of review dictionaries

selected_review = reviews[review_index]

## Review Summary
# Now it's time to practice two other key skills: **conditionals** and **string parsing** (and optionally, learn how to display images with Python code in a Jupyter Notebook).
# We'll do this by **writing code to summarize a given review dictionary** in a more user-friendly way than the original raw dictionary format, practicing some data cleaning along the way.

### Positive, Negative, or Neutral

# Using conditionals, let's display whether a given review is positive, negative, or neutral based on the value associated with the `rating` key. We'll use the following definitions:

#  - Positive: `rating` value of 4 or 5 (out of 5)
#  - Neutral: `rating` value of 3 (out of 5)
#  - Negative: `rating` value of 1 or 2 (out of 5)

# Once you've found that value, print out: `This is a <blank> review` where `<blank>` is replaced with either `positive`, `negative`, or `neutral`.

# selected_rating = 3
review_index = 47
selected_review = reviews[review_index]
selected_rating = selected_review["rating"]

# if selected_rating == 4 or selected_rating == 5:
#     print('This is a Positive review')
# elif selected_rating == 3:
#     print('This is a Neutral review')
# else:
#     print('This is a Negative review')

## ALTERNATIVE
blank = None
if selected_rating > 4 or selected_rating == 5:
    blank = 'positive'
elif selected_rating == 3:
    blank = 'neutral'
else:
    blank = "negative"
# print('This is a {} review'.format(blank))
# print(f'This is a {blank} review.')

### Review Year
# While it may be less exciting than building machine learning models, a significant part of data science is data cleaning. Lets start to practice some data cleaning skills with the `review_time` key-value pairs.

# For the rest of this lab, we'll go ahead and set up three variables to represent the positive, negative, and neutral examples above.

# (Don't worry too much about this syntax; it uses "unpacking" and "list comprehensions", which we haven't covered yet.)

selected_review_indices = (2, 4, 47)
positive_review, negative_review, neutral_review = [reviews[i] for i in selected_review_indices]

# Now let's extract the `review_time` value from the positive review:

positive_review_time = positive_review["review_time"]
negative_review_time = negative_review["review_time"]
neutral_review_time = neutral_review["review_time"]
# print(positive_review_time)


# Ok, it looks like this is is a string showing the month, the day, and then the year that the review was written. Write code to extract the last 4 characters of the string, then convert it into an integer

positive_review_year = int(positive_review_time[-4:])
negative_review_year = int(negative_review_time[-4:])
neutral_review_year = int(neutral_review_time[-4:])
# print(positive_review_year)


# display(Image(url='https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png'))

positive_review_image_url = positive_review['images'][0]
negative_review_image_url = negative_review['images'][0]
neutral_review_image_url = neutral_review['images'][0]
# print(positive_review_image_url)

# The complete summary for index `2` should look like this:

# "Bialetti is the Best!"
# This was a positive review written by Karen in 2017. 

# print(reviews[2])
# new line in python

print(f'{selected_review["images"][0]} \n')
print('{} \n'.format(selected_review["review_title"]))
print(f'This was a {blank} review written by {selected_review["reviewer_name"]} in {selected_review["review_time"][-4:]}.')
