# Boulder County Property Tax Assessor (BCPTA)

Boulder County Tax Assessor machine learning algorithmic evaluation

## Tax-paying Resident Investigation

In a world increasingly influenced by machine learned systems, constituents have a right to transparency behind the algorithms that impact them and their families.

Just as policy amendments are voted on democratically in the public arena, so too should AI / ML policies be added to the ballot.

Hope to spur a public discussion around how to formulate a set of governance around how AI / ML systems can be used to affect the public.


🚀 Best ML Task Type: Regression

Since we aim to estimate residential property valuations, this is a supervised learning regression problem where:
	•	Input (Features): Property attributes (size, location, age, quality, etc.).
	•	Target (Output): Sale Price or Time Adjusted Sale Price.



🔍 Key Considerations for an Explainable Model

1️⃣ Model Choice: Prioritizing Interpretability

Given that the county needs transparency in AI/ML estimates, we should use a model that is:
✅ Explainable (clear decision process)
✅ Trustworthy (consistent, interpretable)
✅ Performs well without being overly complex

Best Models for Explainability:
	1.	Linear Regression (Baseline)
	•	Very easy to explain (coefficients show feature impact).
	•	Good for understanding global trends in property valuation.
	•	📌 Limitation: Doesn’t capture non-linear interactions well.
	2.	Decision Tree Regressor
	•	Easy to visualize & explain decisions step-by-step.
	•	📌 Limitation: Can be unstable if deep (prone to overfitting).
	3.	Random Forest Regressor
	•	More robust & accurate than a single Decision Tree.
	•	Feature Importance ranking explains which factors drive prices.
	•	📌 Limitation: Less interpretable than a single tree, but SHAP values help.
	4.	XGBoost / LightGBM (With SHAP Explainability)
	•	Boosted trees = high accuracy, but interpretable via SHAP values.
	•	📌 Limitation: More complex to explain directly.

2️⃣ SHAP & Feature Importance for Transparency

To show constituents how the model makes decisions:
✅ Use Feature Importance to show which factors drive home prices.
✅ Use SHAP Values to provide local explanations for each prediction.