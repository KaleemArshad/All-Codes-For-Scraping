from selenium import webdriver

options = webdriver.ChromeOptions()

options.add_argument('headless')



browser = webdriver.Chrome(options=options)


url = "https://www.google.com/maps/place/Papa+John's+Pizza/@40.7936551,-74.0124687,17z/data=!3m1!4b1!4m5!3m4!1s0x" \
      "89c2580eaa74451b:0x15d743e4f841e5ed!8m2!3d40.7936551!4d-74.0124687"

# url = "https://www.google.com/maps/place/Lucky+Dhaba/@30.653792,76.8165233,17z/data=!3m1!4b1!4m5!3m4!1s0x390feb
# 3e3de1a031:0x862036ab85567f75!8m2!3d30.653792!4d76.818712"


browser.get(url)


# review titles / username / Person who reviews

review_titles = browser.find_elements_by_class_name("section-review-title")

print([a.text for a in review_titles])

# review text / what did they think

review_text = browser.find_elements_by_class_name("section-review-review-content")

print([a.text for a in review_text])

# get the number of stars

stars = browser.find_elements_by_class_name("section-review-stars")

first_review_stars = stars[0]

active_stars = first_review_stars.find_elements_by_class_name("section-review-star-active")

print(f"the stars the first review got was {len(active_stars)}")