import json
with open("coffee_product_reviews.json") as f:
    reviews = json.load(f)
type(reviews)

num_reviews = len(reviews)
num_reviews
# print("The coffee product review dataset contains {} reviews".format(num_reviews))

# Ok, so now we know how many records we are working with! Let's investigate what each record looks like. In the cell below, replace `None` with appropriate code to select the first review

first_review = reviews[0]

for index in range(5):
    print(reviews[index])

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