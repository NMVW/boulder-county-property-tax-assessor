# Boulder County Property Tax Assessor (BCPTA)

Boulder County Tax Assessor machine learning algorithmic evaluation

## Tax-paying Resident Investigation

In a world increasingly influenced by machine learned systems, constituents have a right to transparency behind the algorithms that impact them and their families.

Just as policy amendments are voted on democratically in the public arena, so too should AI / ML policies be added to the ballot.

Hope to spur a public discussion around how to formulate a set of governance around how AI / ML systems can be used to affect the public.


🚀 Best ML Task Type: Regression

Since we aim to estimate residential property valuations, this is a supervised learning regression problem where:

	Input (Features): Property attributes (layout, location, square footage, age, quality, etc.).

	Output (Target): Sale Price or Time Adjusted Sale Price.



## 🔍 Key Considerations for an Explainable Model

### 1. Model Choice: Prioritizing Interpretability

Given that the county needs transparency in AI/ML assessments, we should use a model that is:

✅ **Explainable** (clear decision process)

✅ **Trustworthy** (consistent, interpretable)

✅ Performs well without being overly complex

#### Best Models for Explainability:

1. **Linear Regression (Baseline)**

    • Very easy to explain (coefficients show feature impact).

    • Good for understanding global trends in property valuation.

    • 📌 **Limitation**: Doesn’t capture non-linear interactions well.

2. **Decision Tree Regressor**

    • Easy to visualize & explain decisions step-by-step.

    • 📌 **Limitation**: Can be unstable if deep (prone to overfitting).

3. **Random Forest Regressor**

    • More robust & accurate than a single Decision Tree.

    • Feature Importance ranking explains which factors drive prices.

    • 📌 **Limitation**: Less interpretable than a single tree, but SHAP values help.

4. **XGBoost / LightGBM (With SHAP Explainability)**

    • Boosted trees = high accuracy, but interpretable via SHAP values.

    • 📌 **Limitation**: More complex to explain directly.

### 2. SHAP & Feature Importance for Transparency

To show constituents how the model makes decisions:

✅ Use Feature Importance to show which factors drive home prices.

✅ Use SHAP Values to provide local explanations for each prediction.

<details>
    <summary>Future feature considerations:</summary>

### Geospatial Features

1. **Neighborhood**: Use geocoding to determine the neighborhood of each property.

2. **City**: Extract the city from the geocoded location.

3. **Region**: Identify the region or county where the property is located (e.g., New York City, Los Angeles County).

4. **Latitude and Longitude**: Store these as separate features for spatial analysis. ✅

### Property Features

1. **Year Built**: Use a data source like PropertyShark or Zillow to extract this information.

2. **Number of Bedrooms**: Estimate the number of bedrooms based on the property's size (e.g., using a rule-based approach).

3. **Number of Bathrooms**: Similar to the above, estimate the number of bathrooms based on the property's size and layout.

4. **Property Type**: Determine if it's a single-family home, townhouse, condominium, or other type.

5. **Square Footage**: Estimate the square footage using various sources like public records or property tax data.

## Environmental Features

1. **School District**: Associate each property with its nearby school district and ratings (e.g., GreatSchools.org).

2. **Crime Rate**: Use crime data from local law enforcement agencies to assign a crime rate score for each property.

3. **Air Quality Index**: If available, use air quality monitoring data to assign an air quality index for each property.

## Economic Features

1. **Median Income**: Determine the median household income of nearby areas (e.g., zip codes or census tracts).

2. **Unemployment Rate**: Use economic data from local government sources or online resources like Bureau of Labor Statistics.

3. **Property Tax Rates**: Extract property tax rates for each jurisdiction and assign them to the properties.

## Demographic Features

1. **Population Density**: Calculate the population density based on nearby census tract data.

2. **Age Demographics**: Use American Community Survey (ACS) data or other sources to extract age demographics (e.g., proportion of households with children).

3. **Income Distribution**: Determine the income distribution for each property's vicinity using ACS data.

## Other Features

1. **Public Transportation Accessibility**: Calculate distances to public transportation hubs, airports, and other relevant points of interest.

2. **Local Amenities**: Identify nearby amenities like parks, schools, restaurants, and shops using data sources like Yelp or Foursquare.

3. **Zoning Regulations**: Extract zoning regulations for each property's location (e.g., commercial vs. residential).

Keep in mind that the quality and availability of these features will depend on the specific dataset you're working with and the region you're targeting.

Features may have varying time-dependencies and hence would require considering alternative model architectures in a more sophisticated ensemble composition.

---

__Ex: Seasonality of sale__

Is assumed to be captured in the currently extracted time features, however there are likely other correlated specific environmental features not included that would evoke inferential dependency on natural disasters, climate conditions, and social demographics. It is up to the independent contributor's discretion to explore these possibilities further.
</details>