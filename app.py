import gradio as gr
import joblib
import numpy as np

# Load saved model and encoder
logreg = joblib.load("logreg_model.pkl")
mlb = joblib.load("mlb_encoder.pkl")

def predict_cart_category(viewed_str, top_n=3):
    # Parse input categories
    viewed_cats = [c.strip() for c in viewed_str.split(",") if c.strip()]
    if not viewed_cats:
        return "Please enter at least one category ID.", {}

    try:
        # Transform input
        X_new = mlb.transform([viewed_cats])

        # Predict best category
        pred = logreg.predict(X_new)[0]

        # Get probability distribution
        probs = logreg.predict_proba(X_new)[0]
        classes = logreg.classes_

        # Sort top-N predictions
        top_idx = np.argsort(probs)[::-1][:top_n]
        top_preds = {str(classes[i]): float(probs[i]) for i in top_idx}

        return str(pred), top_preds
    except Exception as e:
        return f"Error: {e}", {}

# Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("# 🛒 Add-to-Cart Category Prediction (Logistic Regression)")

    with gr.Row():
        viewed_input = gr.Textbox(
            label="Viewed categories (comma-separated)",
            placeholder="e.g., 1001, 1002, 1003"
        )
        top_n_input = gr.Slider(
            1, 10, value=3, step=1, label="Top-N Predictions"
        )

    predict_btn = gr.Button("Predict")

    pred_output = gr.Label(label="Predicted Category")
    top_output = gr.Label(label="Top-N Probabilities")

    predict_btn.click(
        fn=predict_cart_category,
        inputs=[viewed_input, top_n_input],
        outputs=[pred_output, top_output]
    )

if __name__ == "__main__":
    demo.launch()
