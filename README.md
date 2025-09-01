# Add-to-Cart Category Prediction (E-commerce Recommendation System)

This project builds a machine learning model to predict the **first product category a visitor will add to their cart** based on the categories they previously viewed.  
The goal is to improve recommendation quality, increase conversions, and personalize user experience for e-commerce platforms.

---

## Business Questions Addressed & Insights

### 1. What types of actions (views, add-to-cart, purchases) do users perform most frequently on the platform?  
- **Insight:** The majority of user interactions (96.7%) are product views, while only 2.5% progress to add-to-cart and just 0.8% result in transactions.  
- **Business Implication:** This sharp drop-off highlights potential lost sales opportunities. Personalized recommendations, retargeting campaigns, and streamlined checkout processes could help close the conversion gap.

---

### 2. How does overall user activity (all events) change over time?  
- **Insight:** Daily event volume was highly volatile between May–September 2015, peaking at 27,081 in mid-May but dropping as low as 1,528 in September.  
- **Business Implication:** Seasonal fluctuations or operational disruptions likely affected engagement. Retailers could stabilize activity with marketing pushes or promotions during low-demand periods.

---

### 3. Which products receive the highest number of views from users?  
- **Insight:** Item **187946** dominates with 3,381 views, followed by **item 2,030** views. Beyond the top two, views decline steadily (1,689–1,192).  
- **Business Implication:** A small set of items attracts disproportionate attention. Highlighting these in promotions could amplify engagement, while long-tail products may require targeted visibility campaigns.

---

### 4. Which products generate the most transactions?  
- **Insight:** Purchases concentrate on **item 461686 (98 sales)** and **item 119736 (73 sales)**, with the rest falling between 42–27.  
- **Business Implication:** Demand is skewed toward a few products. This suggests a need for inventory optimization and diversification strategies to avoid overdependence on a narrow set of products.

---

### 5. Which items have the highest conversion rates from view to purchase?  
- **Insight:** Outlier products such as **item 132633 (400%)**, **item 28789 (200%)**, and **item 192003 (200%)** far outperform the baseline conversion rates (~100%).  
- **Business Implication:** Understanding what drives these exceptional conversions (pricing, product type, marketing placement) can inform broader sales strategies.

---

### 6. At what times of the day are users most active on the platform?  
- **Insight:** Activity peaks at **20:00 (8 PM)** with ~150K events, and is lowest at **10:00 AM** (~12K events).  
- **Business Implication:** Retailers should time promotions, recommendations, and push notifications for the evening peak, while scheduling maintenance in low-activity windows.

---

### 7. How much abnormal traffic exists in the dataset, and what is its impact?  
- **Insight:** About **30.4% of visitors were flagged as abnormal** (likely bots or crawlers). After filtering, events dropped from ~2.0M → ~0.69M. Abnormal users generated unrealistic patterns:  
  - Hundreds of clicks per minute  
  - Short sessions with massive activity  
  - Many views but zero purchases  
- **Business Implication:** Without filtering, these distortions would inflate engagement metrics and mislead ML models. Cleaning improves data quality, speeds training, and ensures recommendations reflect genuine customer intent.

---

## Data Summary
- **Source:** E-commerce browsing event logs  
- **Scope:** Visitor-level data of views, add-to-carts, and purchases  
- **Key Columns:**  
  - `visitorid`, `event`, `itemid`, `categoryid`, `timestamp`  

---

## Key Insights (Model-Focused)
- **Prediction Feasibility:** Browsing history is a strong predictor of add-to-cart actions.  
- **Model Performance:** Logistic Regression achieved ~78% accuracy, outperforming Random Forest.  
- **Category Patterns:** Users often view multiple related categories before carting.  
- **Data Cleaning:** Filtering abnormal users removed noise, making downstream ML tasks more reliable.  

---

## Recommendations
| Focus Area             | Action                                                                 |
|-------------------------|------------------------------------------------------------------------|
| Recommendation System   | Use predicted add-to-cart categories to suggest products dynamically. |
| Cross-Selling           | Leverage related categories to recommend bundles.                     |
| Personalization         | Apply model predictions for targeted discounts and promotions.        |
| Real-Time Deployment    | Integrate model into online store to serve live recommendations.      |

---

## Tools Used
- **Python (Pandas, scikit-learn, NumPy)**  
- **Gradio (for interactive UI)**  
- **Joblib (model persistence)**  
- **Hugging Face Spaces (deployment)**  
- **GitHub (version control & collaboration)**  

---

## Conclusion
This project demonstrates that predicting a user’s first add-to-cart category from their viewed categories is not only feasible but also highly accurate with Logistic Regression.  
By deploying the model via Gradio on Hugging Face Spaces, businesses can integrate it into their platforms to deliver **real-time, personalized product recommendations**, improving customer engagement and conversion rates.

👉 [Live Demo on Hugging Face](https://huggingface.co/spaces/your-username/your-space-name)  
