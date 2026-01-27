import streamlit as st
import time
import pandas as pd
import random

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Neural HS Classifier | v2.1",
    page_icon="🧠",
    layout="wide"
)

# --- SESSION STATE ---
if "logs" not in st.session_state:
    st.session_state.logs = []

# --- SIDEBAR (System Control) ---
with st.sidebar:
    st.header("⚙️ Control Plane")
    st.code("Cluster: EU-WEST-4\nNode: #8821-Alpha", language="yaml")
    
    st.subheader("Model Config")
    model = st.selectbox("Active Model", ["WCO-BERT-Large (v4.2)", "GPT-4o (Fine-Tuned)"])
    threshold = st.slider("Confidence Gate", 0.0, 1.0, 0.88)
    
    st.divider()
    st.caption("Latency Status: 🟢 42ms")

# --- MOCK INFERENCE ENGINE ---
def run_inference(text):
    start_time = time.time()
    time.sleep(random.uniform(0.6, 1.2)) # Simulate processing
    text = text.lower()
    
    result = None
    keywords = []
    
    if "shoe" in text or "sneaker" in text:
        result = {"code": "6403.99.00", "rate": "19.0%", "cat": "Footwear", "conf": 0.9821}
        keywords = ["shoe", "sneaker"] if "sneaker" in text else ["shoe"]
    elif "shirt" in text or "cotton" in text:
        result = {"code": "6205.20.00", "rate": "12.0%", "cat": "Textiles", "conf": 0.9543}
        keywords = ["cotton", "shirt"]
    elif "laptop" in text:
        result = {"code": "8471.30.00", "rate": "0.0%", "cat": "Electronics", "conf": 0.9910}
        keywords = ["laptop"]
        
    duration = round(time.time() - start_time, 3)
    return result, keywords, duration

# --- MAIN LAYOUT (Split View) ---
st.title("🧠 Neural HS Classification Engine")
st.markdown("`REST API Gateway` > `POST /v1/classify`")

col1, col2 = st.columns([1, 1], gap="large")

# LEFT COLUMN: INPUT
with col1:
    st.subheader("📥 Data Ingestion")
    input_text = st.text_area("Manifest Description", height=150, placeholder="RAW_DATA: e.g. Women running shoe leather...")
    
    if st.button("▶ Execute Inference", type="primary", use_container_width=True):
        if not input_text:
            st.error("BUFFER_EMPTY: No data provided.")
        else:
            with st.spinner("Tokenizing & Vectorizing..."):
                prediction, keys, lat = run_inference(input_text)
                
            if prediction:
                # Store log
                st.session_state.logs.insert(0, {
                    "Time": pd.Timestamp.now().strftime("%H:%M:%S"),
                    "Input": input_text,
                    "Code": prediction['code'],
                    "Conf": f"{prediction['conf']:.2f}",
                    "Latency": f"{lat}s"
                })
                
                # --- RESULTS DISPLAY ---
                st.success("200 OK: Classification Successful")
                
                # Metrics Grid
                m1, m2 = st.columns(2)
                m1.metric("HS Code", prediction['code'], delta="Verified")
                m2.metric("Duty Rate", prediction['rate'])
                
                # Explainability Section (The Senior Feature)
                st.markdown("#### 🕵️ Explainability Report")
                st.write(f"**Detected Triggers:** `{keys}`")
                st.progress(prediction['conf'], text=f"Model Confidence: {prediction['conf']*100:.1f}%")
                st.caption(f"Processing Time: {lat}s")
                
            else:
                st.error("422 UNPROCESSABLE ENTITY: Confidence below threshold.")

# RIGHT COLUMN: SYSTEM LOGS
with col2:
    st.subheader("📟 Live System Logs")
    if st.session_state.logs:
        log_df = pd.DataFrame(st.session_state.logs)
        st.dataframe(
            log_df, 
            column_config={
                "Code": st.column_config.TextColumn("HS Code", help="Harmonized System Code"),
                "Conf": st.column_config.NumberColumn("Conf", format="%.2f"),
            },
            use_container_width=True,
            hide_index=True
        )
        
        # JSON Preview
        st.divider()
        st.markdown("#### 📄 Last Payload Response")
        if prediction:
            st.json({
                "meta": {"engine": "WCO-BERT", "latency": lat, "status": 200},
                "data": prediction
            })
    else:
        st.info("System Idle. Waiting for requests...")
        st.code("tail -f /var/log/hs-classifier.log", language="bash")