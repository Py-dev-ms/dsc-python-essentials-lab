import json
with open("coffee_product_reviews.json") as f:
    reviews = json.load(f)
type(reviews)

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

selected_rating = 3

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
print('This is a {} review'.format(blank))
# print(f'This is a {blank} review.')