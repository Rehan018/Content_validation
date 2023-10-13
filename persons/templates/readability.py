import pandas as pd
import textstat

# Sample customer review dataset
data = {
    'ReviewID': [1, 2, 3, 4, 5],
    'ReviewText': [ 
        "Great as a device to read books. I like that it links with my borrowed library e-books. Switched from another popular tablet brand and I am happy with the choice I made. It took some time to get books from my previous non-Kindle reader, but finally figured out a way!",
        "I don't like this product. It's terrible.",
        "The product is so-so. Not bad, but not great either.",
        "I found the product easy to use and very helpful.",
        "This is the worst product ever. I regret buying it."
    ]
}
#csv_file = "persons/static/customer_review.csv"  
#df = pd.read_csv("persons/static/customer_review.csv" , encoding="ISO-8859-1",error_bad_lines=False)

df = pd.DataFrame(data)

# Function to calculate the Flesch-Kincaid score for a text
def calculate_flesch_kincaid(text):
    return textstat.flesch_kincaid_grade(text)

# Function to calculate the SMOG score for a text
def calculate_coleman_liau_index(text):
    return textstat.coleman_liau_index(text)

# Apply the functions to the review text
df['Flesch_Kincaid_Score'] = df['ReviewText'].apply(calculate_flesch_kincaid)
df['coleman_liau_index_Score'] = df['ReviewText'].apply(calculate_coleman_liau_index)

# Create an ensemble score (e.g., average)
df['Ensemble_Score'] = (df['Flesch_Kincaid_Score'] + df['coleman_liau_index_Score']) / 2

# Display the resulting DataFrame
print(df)
