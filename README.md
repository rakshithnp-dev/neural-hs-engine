# 🧠 Neural HS Code Classifier

A Streamlit-based web application that uses AI to classify products into Harmonized System (HS) codes for international trade and customs purposes.

## 🌟 Features

- **Real-time Classification**: Instant HS code prediction from product descriptions
- **Explainability**: View confidence scores and detected keywords
- **Live Logs**: Track classification history in real-time
- **Professional UI**: Clean, modern interface with system monitoring

## 🚀 Live Demo

🔗 **Deployed on Azure**: https://hs-code-classifier-dsetahfee3gfh9cv.centralindia-01.azurewebsites.net

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## 🛠️ Local Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/hs-code-classifier.git
   cd hs-code-classifier
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

5. **Open in browser**
   - The app will automatically open at `http://localhost:8501`

## 🎯 Usage

1. Enter a product description in the "Manifest Description" field
2. Click "▶ Execute Inference" to classify
3. View the predicted HS code, duty rate, and confidence score
4. Check the explainability report for detected keywords
5. Monitor classification history in the live logs panel

### Example Inputs

- "Women's leather running shoes size 8"
- "Men's cotton shirt blue color"
- "Dell XPS 15 laptop with 16GB RAM"

## 🏗️ Project Structure

```
hs-code-classifier/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── startup.sh            # Azure App Service startup script
├── .deployment           # Azure deployment config
├── .gitignore           # Git ignore rules
└── README.md            # This file
```

## ☁️ Azure Deployment

This application is configured for easy deployment to Azure App Service.

### Deploy Steps

1. Create an Azure App Service (Python 3.11, Linux)
2. Connect your GitHub repository
3. Set the startup command: `bash startup.sh`
4. Deploy from the Azure Portal or GitHub Actions

For detailed deployment instructions, see [Azure Documentation](https://docs.microsoft.com/en-us/azure/app-service/).

## 🔧 Configuration

### Model Settings
Adjust in the sidebar:
- **Active Model**: Choose between WCO-BERT and GPT-4o
- **Confidence Gate**: Set minimum confidence threshold (0.0 - 1.0)

### Azure Settings
Environment variables (if needed):
- `PORT`: Application port (default: 8000)
- `STREAMLIT_SERVER_PORT`: Streamlit server port

## 📊 HS Code Coverage

Current mock classifier supports:
- **6403.99.00**: Footwear (19.0% duty)
- **6205.20.00**: Cotton shirts/textiles (12.0% duty)
- **8471.30.00**: Laptops/electronics (0.0% duty)

*Note: This is a demonstration version. Production deployment would require integration with a real ML model.*

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is open source and available under the MIT License.

## 📧 Contact

For questions or support, please open an issue on GitHub.

---

Built with ❤️ using Streamlit and deployed on Azure
